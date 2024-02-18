"""Test Management Tool related things."""
#  Copyright: Contributors to the sts project
#  GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

import json
import logging
import tarfile
import time
from os import getenv
from pathlib import Path
from typing import Any, Literal, Optional, TypedDict, Union

test_data_path = getenv('TMT_TEST_DATA')
if not test_data_path:
    from uuid import uuid4

    dir_name = str(uuid4())
    logging.warning(f"TMT_TEST_DATA env var not detected. Using '/var/tmp/{dir_name}'")
    test_data_path = dir_name

TMT_TEST_DATA = Path(test_data_path)


def gather_logs_from_dir(logs_path: str, name: Optional[str]) -> Union[Path, None]:
    path = Path(logs_path)
    if not path.is_dir():
        return None
    if not name:
        name = str(path).replace('/', '_')
    if '.tar' not in name:
        name = f'{name}.tar'

    tarfile_path = f'{TMT_TEST_DATA}/{name}'
    with tarfile.open(tarfile_path, 'w') as tar:
        tar.add(path, recursive=True)
    return Path(tarfile_path)


def timestamp() -> float:
    return time.time()


def calculate_duration(start: float, end: float) -> str:
    """Returns hh:mm:ss duration."""
    secs = int(end - start)
    return f'{secs // 3600:02d}:{secs % 3600 // 60:02d}:{secs % 60:02d}'


class GuestType(TypedDict):
    name: Optional[str]
    role: Optional[str]


TmtResult = Literal['pass', 'fail', 'info', 'warn', 'error']


class CustomResults(TypedDict):
    name: str  # e.g. "/step-1" or "/setup/iscsi/target"
    result: TmtResult
    note: Optional[str]
    log: Optional[list[str]]  # path(s) to log file
    serialnumber: Optional[int]  # serial number of the test in the sequence of all tests of a plan.
    guest: Optional[GuestType]
    duration: Optional[str]
    ids: Optional[dict[str, str]]


def remove_nones(cr: CustomResults) -> dict[str, Any]:
    """Create generic dict to add to 'json dict'."""
    return {k: v for k, v in cr.items() if v is not None}


class Results:
    """Use to pass custom results to tmt run.

    https://tmt.readthedocs.io/en/stable/spec/tests.html#result
    https://tmt.readthedocs.io/en/stable/spec/plans.html#spec-plans-results
    """

    def __init__(self) -> None:
        self.results: list[dict[str, Any]] = []
        self.timestamp = timestamp()

    def add(
        self,
        name: str = '/',
        result: Literal['pass', 'fail', 'info', 'warn', 'error'] = 'pass',
        note: Optional[str] = None,
        log: Optional[list[str]] = None,
        errors: Optional[list[str]] = None,
    ) -> None:
        """Add result to custom results list.

        When tmt plan is set to 'result: custom', use this followed by submit() to create the necessary result.json.
        Use multiple times when test have distinctive steps (parts).

        Usage example:
            results = tmt.Results()
            results.add(name="setup", result="pass")
            results.add(name="test", errors=errors, log=["dmesg.log", "messages.log"])
            results.submit()

        Args:
            name: Optional path-like string. e.g. '/setup/something' or 'setup'.
            log: Paths in the custom results file are treated as relative to ${TMT_TEST_DATA} path.
            errors: Can be used with atomic_run. If errors are not None, result is overwritten to "false".
        """
        if not name.startswith('/'):
            name = f'/{name}'
        if errors:
            result = 'fail'
        new_timestamp = timestamp()
        duration = calculate_duration(self.timestamp, new_timestamp)
        self.timestamp = new_timestamp

        result_to_add = CustomResults(
            name=name,
            result=result,
            note=note,
            log=log,
            duration=duration,
            ids=None,
            serialnumber=None,
            guest=None,
        )

        self.results.append(remove_nones(result_to_add))

    def submit(self) -> None:
        file = Path(TMT_TEST_DATA / 'results.json')
        with file.open('w') as f:
            json.dump(self.results, f)
