import asyncio
import resemble.cli.terminal as terminal
import sys
from resemble.cli.dev import dev, register_dev
from resemble.cli.protoc import protoc, register_protoc
from resemble.cli.rc import ArgumentParser
from typing import Optional


def create_parser(
    *,
    rc_file: Optional[str] = None,
    argv: Optional[list[str]] = None,
) -> ArgumentParser:
    parser = ArgumentParser(
        program='rsm',
        filename='.rsmrc',
        subcommands=['dev', 'protoc'],
        rc_file=rc_file,
        argv=argv,
    )

    register_dev(parser)

    register_protoc(parser)

    return parser


async def rsm():
    terminal.init()  # Sets up the terminal for logging.

    parser = create_parser()

    args, argv_after_dash_dash = parser.parse_args()

    if args.subcommand == 'dev':
        return await dev(args, parser=parser)
    elif args.subcommand == 'protoc':
        return await protoc(args, argv_after_dash_dash, parser=parser)


# This is a separate function (rather than just being in `__main__`) so that we
# can refer to it as a `script` in our `pyproject.rsm.toml` file.
def main():
    try:
        returncode = asyncio.run(rsm())
        sys.exit(returncode)
    except KeyboardInterrupt:
        # Don't print an exception and stack trace if the user does a
        # Ctrl-C.
        pass


if __name__ == '__main__':
    main()
