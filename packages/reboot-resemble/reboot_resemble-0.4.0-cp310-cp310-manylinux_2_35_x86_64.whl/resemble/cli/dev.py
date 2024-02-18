import asyncio
import os
import random
import sys
from contextlib import asynccontextmanager
# We import the whole `terminal` module (as opposed to the methods it contains)
# to allow us to mock these methods out in tests.
from resemble.cli import terminal
from resemble.cli.directories import (
    dot_rsm_dev_directory,
    use_working_directory,
)
from resemble.cli.monkeys import monkeys, no_chaos_monkeys
# We won't mock the classes in `rc`, so it's safe to import those directly.
from resemble.cli.rc import ArgumentParser, BaseTransformer, TransformerError
from resemble.cli.subprocesses import Subprocesses
from resemble.cli.watch import watch
from resemble.settings import (
    DEFAULT_SECURE_PORT,
    ENVOY_PROXY_IMAGE,
    ENVVAR_RSM_DEV,
    ENVVAR_RSM_DEV_INSPECT_PORT,
    ENVVAR_RSM_DEV_LOCAL_ENVOY,
    ENVVAR_RSM_DEV_LOCAL_ENVOY_PORT,
    ENVVAR_RSM_DEV_NAME,
    ENVVAR_RSM_DOT_RSM_DEV_DIRECTORY,
)
from typing import Optional


class EnvTransformer(BaseTransformer):

    def transform(self, value: str):
        if '=' not in value:
            raise TransformerError(
                f"Invalid flag '--env={value}': must be in the form "
                "'--env=KEY=VALUE'"
            )
        return value.split('=', 1)


def register_dev(parser: ArgumentParser):
    parser.subcommand('dev').add_argument(
        '--working-directory',
        type=str,
        help="directory in which to execute",
        required=True,
    )

    parser.subcommand('dev').add_argument(
        '--name',
        type=str,
        help="name of instance; state will be persisted using this name in "
        f"'{dot_rsm_dev_directory()}'",
    )

    parser.subcommand('dev').add_argument(
        '--background-command',
        type=str,
        repeatable=True,
        help=
        'command(s) to execute in the background (multiple instances of this '
        'flag are supported)',
    )

    parser.subcommand('dev').add_argument(
        '--local-envoy',
        type=bool,
        default=True,
        help='whether or not to bring up a local Envoy'
    )

    parser.subcommand('dev').add_argument(
        '--local-envoy-port',
        type=int,
        help=f'port for local Envoy; defaults to {DEFAULT_LOCAL_ENVOY_PORT}',
    )

    parser.subcommand('dev').add_argument(
        '--inspect-port',
        type=int,
        help=f'port for inspecting state; defaults to {DEFAULT_INSPECT_PORT}',
    )

    parser.subcommand('dev').add_argument(
        '--python',
        type=bool,
        default=False,
        help="whether or not to launch the application by "
        "passing it as an argument to 'python'",
    )

    parser.subcommand('dev').add_argument(
        '--watch',
        type=str,
        repeatable=True,
        help=
        'path to watch; multiple instances are allowed; globbing is supported',
    )

    parser.subcommand('dev').add_argument(
        '--chaos',
        type=bool,
        default=True,
        help='whether or not to randomly induce failures',
    )

    parser.subcommand('dev').add_argument(
        "--env",
        type=str,
        repeatable=True,
        transformer=EnvTransformer(),
        help=
        "sets any specified environment variables before running the application; "
        "'ENV' should be of the form 'KEY=VALUE'",
    )

    parser.subcommand('dev').add_argument(
        "--protoc-watch",
        type=bool,
        default=False,
        help="also run `rsm protoc --watch` in the background if true, taking "
        "'protoc' arguments from the '.rsmrc' file, which must be present"
    )

    parser.subcommand('dev').add_argument(
        'application',
        type=str,  # TODO: consider argparse.FileType('e')
        help='path to application to execute',
    )


async def _run_background_command(
    background_command: str,
    *,
    verbose: bool,
    print_as: Optional[str] = None,
    subprocesses: Subprocesses,
):
    if verbose:
        terminal.info(
            f"Running background command '{print_as or background_command}'"
        )

    stdout: Optional[int] = None
    stderr: Optional[int] = None

    if not verbose:
        stdout = asyncio.subprocess.PIPE
        stderr = asyncio.subprocess.STDOUT

    async with subprocesses.shell(
        background_command,
        stdout=stdout,
        stderr=stderr,
    ) as process:
        await process.wait()

        if process.returncode != 0:
            terminal.fail(
                f"Failed to run background command '{background_command}', "
                f"exited with {process.returncode}"
            )
        else:
            terminal.warn(
                f"Background command '{background_command}' exited without errors"
            )


@asynccontextmanager
async def _run(
    application,
    *,
    env: dict[str, str],
    launcher: Optional[str],
    subprocesses: Subprocesses,
):
    """Helper for running the application with an optional launcher."""
    args = [application] if launcher is None else [launcher, application]

    async with subprocesses.exec(*args, env=env) as process:
        yield process


async def _check_docker_status(subprocesses: Subprocesses):
    """Checks if Docker is running and can use the Envoy proxy image. Downloads
    that image if necessary."""
    async with subprocesses.exec(
        'docker',
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.STDOUT,
    ) as process:
        stdout, _ = await process.communicate()
        if process.returncode != 0:
            terminal.fail(
                f"Could not use Docker:\n"
                "\n"
                f"{stdout.decode() if stdout is not None else '<no output>'}"
            )

    # The '-q' flag returns only the image ID, so if stdout is empty
    # then the image is not downloaded.
    async with subprocesses.exec(
        'docker',
        'images',
        '-q',
        ENVOY_PROXY_IMAGE,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.STDOUT,
    ) as process:
        stdout, _ = await process.communicate()

        if process.returncode != 0:
            terminal.fail(
                f"Could not use Docker; 'docker images -q {ENVOY_PROXY_IMAGE}' failed with output:\n"
                "\n"
                f"{stdout.decode() if stdout is not None else '<no output>'}"
            )
        elif stdout is None or stdout == b'':
            # Empty output means the image is not downloaded because
            # 'docker' didn't find a match for the image name.
            terminal.info(
                f"Pulling Envoy proxy image '{ENVOY_PROXY_IMAGE}'..."
            )
            async with subprocesses.exec(
                'docker',
                'pull',
                ENVOY_PROXY_IMAGE,
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.STDOUT,
            ) as process:
                stdout, _ = await process.communicate()
                if process.returncode != 0:
                    terminal.fail(
                        f"Could not use Docker; 'docker pull {ENVOY_PROXY_IMAGE}' failed with output:\n"
                        "\n"
                        f"{stdout.decode() if stdout is not None else '<no output>'}"
                    )


def use_protoc_watch(args, parser: ArgumentParser) -> bool:
    """Check whether we can run `rsm protoc --watch` without further
    user-specified arguments. That depends on whether the user has
    specified the necessary arguments (notably `--output-directory`)
    in an `.rsmrc`."""
    if args.protoc_watch:
        if parser.dot_rc is None:
            terminal.fail(
                "The '--protoc-watch' flag was specified, but no '.rsmrc' file was found. "
                "Add an '.rsmrc' file containing the necessary arguments to run 'rsm protoc' "
                "to use 'rsm dev --protoc-watch'"
            )
        return True
    return False


DEFAULT_LOCAL_ENVOY_PORT: int = DEFAULT_SECURE_PORT
DEFAULT_INSPECT_PORT: int = 9992


async def dev(args, *, parser: ArgumentParser):
    """Implementation of the 'dev' subcommand."""
    # Determine the working directory and move into it.
    with use_working_directory(args.working_directory, parser):
        application = os.path.abspath(args.application)

        # Use `Subprocesses` to manage all of our subprocesses for us.
        subprocesses = Subprocesses()

        # If on Linux try and become a child subreaper so that we can
        # properly clean up all processes descendant from us!
        if sys.platform == 'linux':
            # The 'pyprctl' module is available on Linux only.
            import pyprctl
            try:
                pyprctl.set_child_subreaper(True)
            except:
                terminal.warn(
                    "Failed to become child subreaper, we'll do our "
                    "best to ensure all created processes are terminated"
                )
                pass

        # Run any background commands.
        background_command_tasks: list[asyncio.Task] = []

        for background_command in args.background_command or []:
            background_command_tasks.append(
                asyncio.create_task(
                    _run_background_command(
                        background_command,
                        verbose=True,
                        subprocesses=subprocesses,
                    )
                )
            )

        if use_protoc_watch(args, parser):
            # Run `rsm protoc` _once_, so that the application doesn't
            # exit because it can't find any of the generated files.
            #
            # Using `sys.argv[0]` in the event that `rsm` is
            # not on the path or someone renamed it.
            #
            # TODO(benh): aggregate all of the `--config=` and pass
            # them on to `rsm protoc`.
            rsm_protoc = f'{sys.executable} {sys.argv[0]} protoc'

            async with subprocesses.shell(
                rsm_protoc,
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.STDOUT,
            ) as process:
                stdout, _ = await process.communicate()

                if process.returncode != 0:
                    terminal.fail(
                        "Failed to run 'rsm protoc' (you can disable this with --no-protoc-watch):\n"
                        "\n"
                        f"{stdout.decode() if stdout is not None else '<no output>'}"
                    )

            background_command_tasks.append(
                asyncio.create_task(
                    _run_background_command(
                        f'{rsm_protoc} --watch --wait-for-changes',
                        verbose=False,
                        print_as='rsm protoc --watch --wait-for-changes',
                        subprocesses=subprocesses,
                    )
                )
            )

        # Set all the environment variables that
        # 'resemble.aio.Application' will be looking for.
        #
        # We make a copy of the environment so that we don't change
        # our environment variables which might cause an issue.
        env = os.environ.copy()

        env[ENVVAR_RSM_DEV] = 'true'

        if args.name is not None:
            env[ENVVAR_RSM_DEV_NAME] = args.name
            env[ENVVAR_RSM_DOT_RSM_DEV_DIRECTORY] = dot_rsm_dev_directory()

        if args.local_envoy:
            # Check if Docker is running and can access the Envoy proxy image.
            # Fail otherwise.
            await _check_docker_status(subprocesses)
            env[ENVVAR_RSM_DEV_LOCAL_ENVOY] = 'true'
        else:
            env[ENVVAR_RSM_DEV_LOCAL_ENVOY] = 'false'

        env[ENVVAR_RSM_DEV_LOCAL_ENVOY_PORT] = str(
            args.local_envoy_port or DEFAULT_LOCAL_ENVOY_PORT
        )

        env[ENVVAR_RSM_DEV_INSPECT_PORT] = str(
            args.inspect_port or DEFAULT_INSPECT_PORT
        )

        # Also include all environment variables from '--env='.
        for (key, value) in args.env or []:
            env[key] = value

        if not args.chaos:
            terminal.warn(
                '\n' + random.choice(no_chaos_monkeys) + '\n'
                'You Have Disabled Chaos Monkey! (see --chaos)\n'
                '\n'
                'Only You (And Chaos Monkey) Can Prevent Bugs!'
                '\n'
            )

        try:
            while True:
                if args.name is None:
                    terminal.warn(
                        '\n'
                        'Starting an ANONYMOUS application; to reuse state '
                        'across application restarts use --name'
                        '\n'
                    )

                # It's possible that the application may get deleted
                # and then (re)created by a build system so rather
                # than fail if we can't find it we'll retry but print
                # out a warning every ~10 seconds (which corresponds
                # to ~20 retries since we sleep for 0.5 seconds
                # between each retry).
                retries = 0
                while not os.path.isfile(application):
                    if retries != 0 and retries % 20 == 0:
                        terminal.warn(
                            f"Missing application at '{application}' "
                            "(is it being rebuilt?)"
                        )
                    retries += 1
                    await asyncio.sleep(0.5)

                # Expect an executable if we haven't been asked to use
                # `python`.
                if (
                    args.python is None and
                    not os.access(application, os.X_OK)
                ):
                    terminal.fail(
                        f"Expecting executable application at '{application}'. "
                        "Specify '--python' if you want to run a Python application."
                    )

                async with watch(
                    [application] + (args.watch or [])
                ) as file_system_event_task:
                    # TODO(benh): catch just failure to create the subprocess
                    # so that we can either try again or just listen for a
                    # modified event and then try again.
                    async with _run(
                        application,
                        env=env,
                        launcher=sys.executable
                        if args.python is not None else None,
                        subprocesses=subprocesses,
                    ) as process:
                        process_wait_task = asyncio.create_task(process.wait())

                        if args.chaos:
                            chaos_task = asyncio.create_task(
                                asyncio.sleep(random.randint(30, 60))
                            )

                        completed, pending = await asyncio.wait(
                            [file_system_event_task, process_wait_task] +
                            ([chaos_task] if args.chaos else []),
                            return_when=asyncio.FIRST_COMPLETED,
                        )

                        # Cancel chaos task regardless of what task
                        # completed first as we won't ever wait on it.
                        if args.chaos:
                            chaos_task.cancel()

                        task = completed.pop()

                        if task is process_wait_task:
                            terminal.warn(
                                '\n'
                                'Application exited unexpectedly '
                                f'(with code {process_wait_task.result()}) '
                                '... waiting for modification'
                                '\n'
                            )
                            # NOTE: we'll wait for a file system event
                            # below to signal a modification!
                        elif args.chaos and task is chaos_task:
                            terminal.warn(
                                '\n'
                                'Chaos Monkey Is Restarting Your Application'
                                '\n' + random.choice(monkeys) + '\n'
                                '... disable via --no-chaos if you must'
                                '\n'
                                '\n'
                            )
                            continue

                        await file_system_event_task

                        terminal.info(
                            '\n'
                            'Application modified; restarting ... '
                            '\n'
                        )
        except:
            if len(background_command_tasks) > 0:
                for background_command_task in background_command_tasks:
                    background_command_task.cancel()

                await asyncio.wait(
                    background_command_tasks,
                    return_when=asyncio.ALL_COMPLETED,
                )

            raise
