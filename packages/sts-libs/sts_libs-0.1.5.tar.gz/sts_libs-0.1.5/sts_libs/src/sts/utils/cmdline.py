"""cmdline.py: Module to execute a command line."""
import logging

#  Copyright: Contributors to the sts project
#  GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
from typing import Optional, Union

from testinfra.backend.base import CommandResult

from sts import host_init

host = host_init()


def run(cmd: str, msg: Optional[str] = None) -> CommandResult:
    msg = msg if msg else 'Running'
    logging.info(f"{msg}: '{cmd}'")
    return host.run(cmd)


def log_fail(cr: CommandResult) -> None:
    logging.error(
        f'Unexpected command result\n'
        f'COMMAND: {cr.command}\n'
        f'RC: {cr.rc}\n'
        f'STDOUT: {cr.stdout}\n'
        f'STDERR: {cr.stderr}\n',
    )


def check_result(cr: CommandResult, succeed: bool = True) -> bool:
    if succeed and cr.succeeded:
        return True
    if not succeed and cr.failed:
        return True
    log_fail(cr)
    return False


def run_test(cmd: str, succeed: bool = True) -> bool:
    """Runs command and returns True or False based on expected output."""
    cr = host.run(cmd)
    return check_result(cr, succeed=succeed)


def run_ret_out(
    cmd: str,
    return_output: bool = False,
) -> Union[int, tuple[int, str]]:
    """Runs cmd and returns rc int or rc int, output str tuple.

    For legacy compatibility only. TODO: remove it an it's usages
    """
    completed_command = host.run(cmd)

    if return_output:
        output = completed_command.stdout if completed_command.stdout else completed_command.stderr
        return completed_command.rc, output.rstrip()  # type: ignore [return-value]

    return completed_command.rc


def exists(cmd: str) -> bool:
    return host.exists(cmd)
