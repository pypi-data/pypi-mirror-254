import asyncio
import glob
import os
from contextlib import asynccontextmanager
from resemble.cli.terminal import fail, warn
from typing import AsyncIterator, Optional
from watchdog.events import FileSystemEvent, FileSystemEventHandler
from watchdog.observers import Observer
from watchdog.observers.api import BaseObserver


@asynccontextmanager
async def watch(
    paths: list[str]
) -> AsyncIterator[asyncio.Task[FileSystemEvent]]:
    """Helper for watching the provided paths on file system. Implemented
    as a context manager to ensure proper cleanup of the watches."""
    loop = asyncio.get_running_loop()

    class EventHandler(FileSystemEventHandler):

        def __init__(self, events: asyncio.Queue[FileSystemEvent]):
            self._events = events

        def on_modified(self, event):
            loop.call_soon_threadsafe(lambda: self._events.put_nowait(event))

    events: asyncio.Queue[FileSystemEvent] = asyncio.Queue()

    handler = EventHandler(events)

    observer: Optional[BaseObserver] = None

    while True:
        # Construct a new observer every time to avoid re-adding the
        # same path and raising an error.
        observer = Observer()

        try:
            # We want to (re)determine the paths to watch _every_ time
            # to find any new subdirectories added by the developer
            # which they surely expect we will properly watch as well.
            for unglobed_path in paths:
                has_globbed_paths = False
                for path in glob.iglob(unglobed_path, recursive=True):
                    has_globbed_paths = True

                    if not os.access(path, os.R_OK):
                        fail('Expecting path passed to --watch to be readable')

                    observer.schedule(handler, path=path, recursive=False)

                if not has_globbed_paths:
                    warn(f"'{unglobed_path}' did not match any files")

            observer.start()
            break
        except:
            # NOTE: we capture all exceptions here because
            # 'observer.schedule()' may raise if a file that we had
            # globbed gets removed before calling it (e.g., by a build
            # system) and we just want to retry since the build system
            # should be completing and not removing files out from
            # underneath us all the time.
            await asyncio.sleep(0.5)
            continue

    # Ok, should have a valid observer now!
    assert observer is not None

    events_get = asyncio.create_task(events.get())

    try:
        yield events_get
    finally:
        events_get.cancel()
        observer.stop()
        observer.join()
