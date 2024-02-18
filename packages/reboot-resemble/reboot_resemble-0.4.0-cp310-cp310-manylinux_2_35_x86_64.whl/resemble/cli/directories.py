import git
# mypy fails with 'error: Trying to read deleted variable "exc"' if we use
# 'git.exc'
import git.exc as gitexc
import os
import resemble.cli.rc as rc
from contextlib import contextmanager
from resemble.cli.terminal import info


def is_on_path(file):
    """Helper to check if a file is on the PATH."""
    for directory in os.environ['PATH'].split(os.pathsep):
        if os.path.exists(os.path.join(directory, file)):
            return True
    return False


def dot_rsm_directory() -> str:
    """Helper for determining the '.rsm' directory."""
    try:
        repo = git.Repo(search_parent_directories=True)
    except gitexc.InvalidGitRepositoryError:
        return os.path.join(os.getcwd(), '.rsm')
    else:
        return os.path.join(repo.working_dir, '.rsm')


def dot_rsm_dev_directory() -> str:
    """Helper for determining the '.rsm/dev' directory."""
    return os.path.join(dot_rsm_directory(), 'dev')


@contextmanager
def chdir(directory):
    """Context manager that changes into a directory and then changes back
    into the original directory before control is returned."""
    cwd = os.getcwd()
    try:
        os.chdir(directory)
        yield
    finally:
        os.chdir(cwd)


@contextmanager
def use_working_directory(
    working_directory: str,
    parser: rc.ArgumentParser,
):
    """Context manager that changes into a working directory determined by
    how the parser expanded any flags."""
    for expanded_flag in parser.expanded_flags:
        if expanded_flag.startswith('--working-directory'):
            assert parser.dot_rc is not None
            # Change into the directory of the '.rc' file in order to
            # determine the relative working directory.
            with chdir(os.path.dirname(parser.dot_rc)):
                working_directory = os.path.abspath(working_directory)
                break

    # Always get the absolute directory because it might not have come
    # from an expanded flag.
    working_directory = os.path.abspath(working_directory)

    info(f"Using working directory {working_directory}\n")

    with chdir(working_directory):
        yield
