from collections.abc import Generator

import pytest

from sts import iscsi, lio
from sts.linux import log_kernel_version, log_package_version
from sts.utils.cmdline import run


@pytest.fixture()
def _log_check() -> Generator:
    """Checks if a new coredump entry was generated during the test."""
    last_dump = run('coredumpctl -1', msg='Checking dumps before test').stdout
    yield
    recent_dump = run('coredumpctl -1', msg='Checking dumps after test').stdout
    assert recent_dump == last_dump, 'New coredump appeared during the test'


@pytest.fixture()
def _iscsi_test(_log_check) -> Generator:  # noqa: ANN001
    """Installs userspace utilities and makes cleanup before and after the test."""
    assert iscsi.install()
    log_kernel_version()
    log_package_version('iscsi-initiator-utils')
    iscsi.cleanup()
    yield
    iscsi.cleanup()


@pytest.fixture()
def _iscsi_localhost_test(_iscsi_test) -> Generator:  # noqa: ANN001
    """Installs userspace utilities incl. targetcli and makes cleanup before and after the test."""
    assert lio.lio_install()
    lio.log_versions()
    lio.lio_clearconfig()
    yield
    lio.lio_clearconfig()
