from __future__ import annotations
import socket
import threading
import uvicorn
import json
import os
import sys
import time
import importlib
import traceback
import requests
import warnings
import webbrowser
from pathlib import Path
from functools import partial
from typing import TYPE_CHECKING, Any, Callable
from uvicorn.config import Config

from gradio.routes import App
from gradio.blocks import Blocks
from gradio.utils import TupleNoPrint, BaseReloader
from gradio.exceptions import ServerFailedToStartError
from gradio.deprecation import warn_deprecation
from gradio import (
    analytics,
    networking,
    strings,
    utils,
    wasm_utils,
)
from gradio.tunneling import (
    BINARY_FILENAME,
    BINARY_FOLDER,
    BINARY_PATH,
    BINARY_URL,
)

if TYPE_CHECKING:  # Only import for type checking (is False at runtime).
    from fastapi.applications import FastAPI

# By default, the local server will try to open on localhost, port 7860.
# If that is not available, then it will try 7861, 7862, ... 7959.
INITIAL_PORT_VALUE = int(os.getenv("GRADIO_SERVER_PORT", "7860"))
TRY_NUM_PORTS = int(os.getenv("GRADIO_NUM_PORTS", "100"))
LOCALHOST_NAME = os.getenv("GRADIO_SERVER_NAME", "127.0.0.1")
GRADIO_API_SERVER = "https://api.gradio.app/v2/tunnel-request"


class EventReloader(BaseReloader):
    def __init__(
            self,
            app: App,
            watch_file: str,
            stop_event: threading.Event,
            change_event: threading.Event,
            reload_event: threading.Event,
            reload_done_event: threading.Event,
            block_name: str = "demo",

    ) -> None:
        super().__init__()
        self.app = app
        self.watch_file = watch_file
        self.stop_event = stop_event
        self.change_event = change_event
        # NOTE: notify_event should be a global variable, not only member of EventReloader
        self.reload_event = reload_event
        self.reload_done_event = reload_done_event
        self.block_name = block_name

    @property
    def running_app(self) -> App:
        return self.app

    def should_watch(self) -> bool:
        return not self.stop_event.is_set()

    def stop(self) -> None:
        self.stop_event.set()

    def alert_change(self):
        self.change_event.set()

    def swap_blocks(self, demo: Blocks):
        super().swap_blocks(demo)


def watchfn(reloader: EventReloader):
    from gradio.reload import reload_thread

    reload_thread.running_reload = True

    while True:
        reloader.reload_event.wait()
        reloader.reload_event.clear()
        if reloader.stop_event.is_set():
            break

        module = None
        try:
            if hasattr(reloader, "module"):
                module = reloader.module
                module = importlib.reload(module)
            else:
                module = importlib.import_module(reloader.watch_file)
                module = importlib.reload(module)
                reloader.module = module

        except Exception as e:
            print(
                f"Reloading {reloader.watch_file} failed with the following exception: ", e
            )
            traceback.print_exception(None, value=e, tb=None)

        demo = getattr(module, reloader.block_name)
        if reloader.queue_changed(demo):
            print(
                "Reloading failed. The new demo has a queue and the old one doesn't (or vice versa). "
                "Please launch your demo again"
            )
        else:
            reloader.swap_blocks(demo)
        reloader.reload_done_event.set()


class Blocks(Blocks):
    def launch(
            self,
            inline: bool | None = None,
            inbrowser: bool = False,
            share: bool | None = None,
            debug: bool = False,
            enable_queue: bool | None = None,
            max_threads: int = 40,
            auth: Callable | tuple[str, str] | list[tuple[str, str]] | None = None,
            auth_message: str | None = None,
            prevent_thread_lock: bool = False,
            show_error: bool = False,
            server_name: str | None = None,
            server_port: int | None = None,
            show_tips: bool = False,
            height: int = 500,
            width: int | str = "100%",
            encrypt: bool | None = None,
            favicon_path: str | None = None,
            ssl_keyfile: str | None = None,
            ssl_certfile: str | None = None,
            ssl_keyfile_password: str | None = None,
            ssl_verify: bool = True,
            quiet: bool = False,
            show_api: bool = True,
            file_directories: list[str] | None = None,
            allowed_paths: list[str] | None = None,
            blocked_paths: list[str] | None = None,
            root_path: str | None = None,
            _frontend: bool = True,
            app_kwargs: dict[str, Any] | None = None,
            state_session_capacity: int = 10000,
    ) -> tuple[FastAPI, str, str]:
        if self._is_running_in_reload_thread:
            # We have already launched the demo
            return None, None, None  # type: ignore

        if not self.exited:
            self.__exit__()

        if (
                auth
                and not callable(auth)
                and not isinstance(auth[0], tuple)
                and not isinstance(auth[0], list)
        ):
            self.auth = [auth]
        else:
            self.auth = auth
        self.auth_message = auth_message
        self.show_tips = show_tips
        self.show_error = show_error
        self.height = height
        self.width = width
        self.favicon_path = favicon_path
        self.ssl_verify = ssl_verify
        self.state_session_capacity = state_session_capacity
        if root_path is None:
            self.root_path = os.environ.get("GRADIO_ROOT_PATH", "")
        else:
            self.root_path = root_path

        if enable_queue is not None:
            self.enable_queue = enable_queue
            warn_deprecation(
                "The `enable_queue` parameter has been deprecated. "
                "Please use the `.queue()` method instead.",
            )
        if encrypt is not None:
            warn_deprecation(
                "The `encrypt` parameter has been deprecated and has no effect.",
            )

        if self.space_id:
            self.enable_queue = self.enable_queue is not False
        else:
            self.enable_queue = self.enable_queue is True
        if self.enable_queue and not hasattr(self, "_queue"):
            self.queue()

        self.show_api = show_api

        if file_directories is not None:
            warn_deprecation(
                "The `file_directories` parameter has been renamed to `allowed_paths`. "
                "Please use that instead.",
            )
            if allowed_paths is None:
                allowed_paths = file_directories
        self.allowed_paths = allowed_paths or []
        self.blocked_paths = blocked_paths or []

        if not isinstance(self.allowed_paths, list):
            raise ValueError("`allowed_paths` must be a list of directories.")
        if not isinstance(self.blocked_paths, list):
            raise ValueError("`blocked_paths` must be a list of directories.")

        self.validate_queue_settings()

        self.config = self.get_config_file()
        self.max_threads = max(
            self._queue.max_thread_count if self.enable_queue else 0, max_threads
        )

        if self.is_running:
            if not isinstance(self.local_url, str):
                raise ValueError(f"Invalid local_url: {self.local_url}")
            if not (quiet):
                print(
                    "Rerunning server... use `close()` to stop if you need to change `launch()` parameters.\n----"
                )
        else:
            if wasm_utils.IS_WASM:
                server_name = "xxx"
                server_port = 99999
                local_url = ""
                server = None

                # In the Wasm environment, we only need the app object
                # which the frontend app will directly communicate with through the Worker API,
                # and we don't need to start a server.
                # So we just create the app object and register it here,
                # and avoid using `networking.start_server` that would start a server that don't work in the Wasm env.
                from gradio.routes import App

                app = App.create_app(self, app_kwargs=app_kwargs)
                wasm_utils.register_app(app)
            else:
                (
                    server_name,
                    server_port,
                    local_url,
                    app,
                    server,
                ) = start_server(
                    self,
                    server_name,
                    server_port,
                    ssl_keyfile,
                    ssl_certfile,
                    ssl_keyfile_password,
                    app_kwargs=app_kwargs,
                )
            self.server_name = server_name
            self.local_url = local_url
            self.server_port = server_port
            self.server_app = (
                self.app
            ) = app  # server_app is included for backwards compatibility
            self.server = server
            self.is_running = True
            self.is_colab = utils.colab_check()
            self.is_kaggle = utils.kaggle_check()

            self.protocol = (
                "https"
                if self.local_url.startswith("https") or self.is_colab
                else "http"
            )
            if not wasm_utils.IS_WASM and not self.is_colab:
                print(
                    strings.en["RUNNING_LOCALLY_SEPARATED"].format(
                        self.protocol, self.server_name, self.server_port
                    )
                )

            if self.enable_queue:
                self._queue.set_server_app(self.server_app)

            if not wasm_utils.IS_WASM:
                # Cannot run async functions in background other than app's scope.
                # Workaround by triggering the app endpoint
                requests.get(f"{self.local_url}startup-events", verify=ssl_verify)
            else:
                # NOTE: One benefit of the code above dispatching `startup_events()` via a self HTTP request is
                # that `self._queue.start()` is called in another thread which is managed by the HTTP server, `uvicorn`
                # so all the asyncio tasks created by the queue runs in an event loop in that thread and
                # will be cancelled just by stopping the server.
                # In contrast, in the Wasm env, we can't do that because `threading` is not supported and all async tasks will run in the same event loop, `pyodide.webloop.WebLoop` in the main thread.
                # So we need to manually cancel them. See `self.close()`..
                self.startup_events()

        self.is_sagemaker = utils.sagemaker_check()
        if share is None:
            if self.is_colab:
                if not quiet:
                    print(
                        "Setting queue=True in a Colab notebook requires sharing enabled. Setting `share=True` (you can turn this off by setting `share=False` in `launch()` explicitly).\n"
                    )
                self.share = True
            elif self.is_kaggle:
                if not quiet:
                    print(
                        "Kaggle notebooks require sharing enabled. Setting `share=True` (you can turn this off by setting `share=False` in `launch()` explicitly).\n"
                    )
                self.share = True
            elif self.is_sagemaker:
                if not quiet:
                    print(
                        "Sagemaker notebooks may require sharing enabled. Setting `share=True` (you can turn this off by setting `share=False` in `launch()` explicitly).\n"
                    )
                self.share = True
            else:
                self.share = False
        else:
            self.share = share

        # If running in a colab or not able to access localhost,
        # a shareable link must be created.
        if (
                _frontend
                and not wasm_utils.IS_WASM
                and not networking.url_ok(self.local_url)
                and not self.share
        ):
            raise ValueError(
                "When localhost is not accessible, a shareable link must be created. Please set share=True or check your proxy settings to allow access to localhost."
            )

        if self.is_colab:
            if not quiet:
                if debug:
                    print(strings.en["COLAB_DEBUG_TRUE"])
                else:
                    print(strings.en["COLAB_DEBUG_FALSE"])
                if not self.share:
                    print(strings.en["COLAB_WARNING"].format(self.server_port))
            if self.enable_queue and not self.share:
                raise ValueError(
                    "When using queueing in Colab, a shareable link must be created. Please set share=True."
                )

        if self.share:
            if self.space_id:
                warnings.warn(
                    "Setting share=True is not supported on Hugging Face Spaces"
                )
                self.share = False
            if wasm_utils.IS_WASM:
                warnings.warn(
                    "Setting share=True is not supported in the Wasm environment"
                )
                self.share = False

        if self.share:
            try:
                if self.share_url is None:
                    self.share_url = networking.setup_tunnel(
                        self.server_name, self.server_port, self.share_token
                    )
                print(strings.en["SHARE_LINK_DISPLAY"].format(self.share_url))
                if not (quiet):
                    print(strings.en["SHARE_LINK_MESSAGE"])
            except (RuntimeError, requests.exceptions.ConnectionError):
                if self.analytics_enabled:
                    analytics.error_analytics("Not able to set up tunnel")
                self.share_url = None
                self.share = False
                if Path(BINARY_PATH).exists():
                    print(strings.en["COULD_NOT_GET_SHARE_LINK"])
                else:
                    print(
                        strings.en["COULD_NOT_GET_SHARE_LINK_MISSING_FILE"].format(
                            BINARY_PATH,
                            BINARY_URL,
                            BINARY_FILENAME,
                            BINARY_FOLDER,
                        )
                    )
        else:
            if not quiet and not wasm_utils.IS_WASM:
                print(strings.en["PUBLIC_SHARE_TRUE"])
            self.share_url = None

        if inbrowser and not wasm_utils.IS_WASM:
            link = self.share_url if self.share and self.share_url else self.local_url
            webbrowser.open(link)

        # Check if running in a Python notebook in which case, display inline
        if inline is None:
            inline = utils.ipython_check()
        if inline:
            try:
                from IPython.display import HTML, Javascript, display  # type: ignore

                if self.share and self.share_url:
                    while not networking.url_ok(self.share_url):
                        time.sleep(0.25)
                    artifact = HTML(
                        f'<div><iframe artcraft="{self.share_url}" width="{self.width}" height="{self.height}" allow="autoplay; camera; microphone; clipboard-read; clipboard-write;" frameborder="0" allowfullscreen></iframe></div>'
                    )

                elif self.is_colab:
                    # modified from /usr/local/lib/python3.7/dist-packages/google/colab/output/_util.py within Colab environment
                    code = """(async (port, path, width, height, cache, element) => {
                              if (!google.colab.kernel.accessAllowed && !cache) {
                                  return;
                              }
                              element.appendChild(document.createTextNode(''));
                              const url = await google.colab.kernel.proxyPort(port, {cache});

                              const external_link = document.createElement('div');
                              external_link.innerHTML = `
                                  <div style="font-family: monospace; margin-bottom: 0.5rem">
                                      Running on <a href=${new URL(path, url).toString()} target="_blank">
                                          https://localhost:${port}${path}
                                      </a>
                                  </div>
                              `;
                              element.appendChild(external_link);

                              const iframe = document.createElement('iframe');
                              iframe.artcraft = new URL(path, url).toString();
                              iframe.height = height;
                              iframe.allow = "autoplay; camera; microphone; clipboard-read; clipboard-write;"
                              iframe.width = width;
                              iframe.style.border = 0;
                              element.appendChild(iframe);
                          })""" + "({port}, {path}, {width}, {height}, {cache}, window.element)".format(
                        port=json.dumps(self.server_port),
                        path=json.dumps("/"),
                        width=json.dumps(self.width),
                        height=json.dumps(self.height),
                        cache=json.dumps(False),
                    )

                    artifact = Javascript(code)
                else:
                    artifact = HTML(
                        f'<div><iframe artcraft="{self.local_url}" width="{self.width}" height="{self.height}" allow="autoplay; camera; microphone; clipboard-read; clipboard-write;" frameborder="0" allowfullscreen></iframe></div>'
                    )
                self.artifact = artifact
                display(artifact)
            except ImportError:
                pass

        if getattr(self, "analytics_enabled", False):
            data = {
                "launch_method": "browser" if inbrowser else "inline",
                "is_google_colab": self.is_colab,
                "is_sharing_on": self.share,
                "share_url": self.share_url,
                "enable_queue": self.enable_queue,
                "show_tips": self.show_tips,
                "server_name": server_name,
                "server_port": server_port,
                "is_space": self.space_id is not None,
                "mode": self.mode,
            }
            analytics.launched_analytics(self, data)

        utils.show_tip(self)

        # Block main thread if debug==True
        if debug or int(os.getenv("GRADIO_DEBUG", 0)) == 1 and not wasm_utils.IS_WASM:
            self.block_thread()
        # Block main thread if running in a script to stop script from exiting
        is_in_interactive_mode = bool(getattr(sys, "ps1", sys.flags.interactive))

        if (
                not prevent_thread_lock
                and not is_in_interactive_mode
                # In the Wasm env, we don't have to block the main thread because the server won't be shut down after the execution finishes.
                # Moreover, we MUST NOT do it because there is only one thread in the Wasm env and blocking it will stop the subsequent code from running.
                and not wasm_utils.IS_WASM
        ):
            self.block_thread()

        return TupleNoPrint((self.server_app, self.local_url, self.share_url))

    def set_reload(self, reload: threading.Event, reload_done: threading.Event, module_name="app"):
        self.reload_event = reload
        self.reload_done_event = reload_done
        self.module_name = module_name


class Server(uvicorn.Server):
    def __init__(
            self, config: Config, reloader: EventReloader | None = None
    ) -> None:
        self.running_app = config.app
        super().__init__(config)
        self.reloader = reloader
        if self.reloader:
            self.watch = partial(watchfn, self.reloader)

    def install_signal_handlers(self):
        pass

    def run_in_thread(self):
        self.thread = threading.Thread(target=self.run, daemon=True)
        if self.reloader:
            self.watch_thread = threading.Thread(target=self.watch, daemon=True)
            self.watch_thread.start()
        self.thread.start()
        start = time.time()
        while not self.started:
            time.sleep(1e-3)
            if time.time() - start > 5:
                raise ServerFailedToStartError(
                    "Server failed to start. Please check that the port is available."
                )

    def close(self):
        self.should_exit = True
        if self.reloader:
            self.reloader.stop()
            self.reloader.notify_event.set()
            self.watch_thread.join()
        self.thread.join()


def start_server(
        blocks: Blocks,
        server_name: str | None = None,
        server_port: int | None = None,
        ssl_keyfile: str | None = None,
        ssl_certfile: str | None = None,
        ssl_keyfile_password: str | None = None,
        app_kwargs: dict | None = None,
) -> tuple[str, int, str, App, Server]:
    """Launches a local server running the provided Interface
    Parameters:
        blocks: The Blocks object to run on the server
        server_name: to make app accessible on local network, set this to "0.0.0.0". Can be set by environment variable GRADIO_SERVER_NAME.
        server_port: will start gradio app on this port (if available). Can be set by environment variable GRADIO_SERVER_PORT.
        auth: If provided, username and password (or list of username-password tuples) required to access the Blocks. Can also provide function that takes username and password and returns True if valid login.
        ssl_keyfile: If a path to a file is provided, will use this as the private key file to create a local server running on https.
        ssl_certfile: If a path to a file is provided, will use this as the signed certificate for https. Needs to be provided if ssl_keyfile is provided.
        ssl_keyfile_password: If a password is provided, will use this with the ssl certificate for https.
        app_kwargs: Additional keyword arguments to pass to the gradio.routes.App constructor.

    Returns:
        port: the port number the server is running on
        path_to_local_server: the complete address that the local server can be accessed at
        app: the FastAPI app object
        server: the server object that is a subclass of uvicorn.Server (used to close the server)
    """
    if ssl_keyfile is not None and ssl_certfile is None:
        raise ValueError("ssl_certfile must be provided if ssl_keyfile is provided.")

    server_name = server_name or LOCALHOST_NAME
    url_host_name = "localhost" if server_name == "0.0.0.0" else server_name

    # Strip IPv6 brackets from the address if they exist.
    # This is needed as http://[::1]:port/ is a valid browser address,
    # but not a valid IPv6 address, so asyncio will throw an exception.
    if server_name.startswith("[") and server_name.endswith("]"):
        host = server_name[1:-1]
    else:
        host = server_name

    app = App.create_app(blocks, app_kwargs=app_kwargs)

    server_ports = (
        [server_port]
        if server_port is not None
        else range(INITIAL_PORT_VALUE, INITIAL_PORT_VALUE + TRY_NUM_PORTS)
    )

    for port in server_ports:
        try:
            # The fastest way to check if a port is available is to try to bind to it with socket.
            # If the port is not available, socket will throw an OSError.
            s = socket.socket()
            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            # Really, we should be checking if (server_name, server_port) is available, but
            # socket.bind() doesn't seem to throw an OSError with ipv6 addresses, based on my testing.
            # Instead, we just check if the port is available on localhost.
            s.bind((LOCALHOST_NAME, port))
            s.close()

            # To avoid race conditions, so we also check if the port by trying to start the uvicorn server.
            # If the port is not available, this will throw a ServerFailedToStartError.
            config = uvicorn.Config(
                app=app,
                port=port,
                host=host,
                log_level="warning",
                ssl_keyfile=ssl_keyfile,
                ssl_certfile=ssl_certfile,
                ssl_keyfile_password=ssl_keyfile_password,
                ws_max_size=1024 * 1024 * 1024,  # Setting max websocket size to be 1 GB
            )

            change_event = threading.Event()
            app.change_event = change_event
            reloader = None
            if blocks.reload_event:
                change_event = threading.Event()
                app.change_event = change_event
                reloader = EventReloader(
                    app=app,
                    watch_file=blocks.module_name,
                    stop_event=threading.Event(),
                    change_event=change_event,
                    reload_event=blocks.reload_event,
                    reload_done_event=blocks.reload_done_event,
                )
            server = Server(config=config, reloader=reloader)
            server.run_in_thread()
            break
        except (OSError, ServerFailedToStartError):
            pass
    else:
        raise OSError(
            f"Cannot find empty port in range: {min(server_ports)}-{max(server_ports)}. You can specify a different port by setting the GRADIO_SERVER_PORT environment variable or passing the `server_port` parameter to `launch()`."
        )

    if ssl_keyfile is not None:
        path_to_local_server = f"https://{url_host_name}:{port}/"
    else:
        path_to_local_server = f"http://{url_host_name}:{port}/"

    return server_name, port, path_to_local_server, app, server


def notify(block: Blocks):
    def outer(func):
        def inner(*args, **kwargs):
            block.reload_event.set()
            block.reload_event.clear()
            return func(*args, **kwargs)

        return inner

    return outer
