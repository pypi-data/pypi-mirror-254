import datetime
import os
import socket
from unittest.mock import Mock

import pytest

from bassist.backup import create_archive
from bassist.config import Config

CONFIGFILE = os.path.join(
    os.path.dirname(os.path.realpath(__file__)), "configs", "backuptest.toml"
)


@pytest.fixture
def config() -> Config:
    return Config(CONFIGFILE)


@pytest.fixture
def run_mock(monkeypatch):
    run = Mock()
    monkeypatch.setattr("subprocess.run", run)
    return run


def test_create_archive_calls_borg_create(config: Config, run_mock):
    create_archive(config, "docs")

    expected_archive_name = (
        f"{socket.gethostname()}-{datetime.date.today().isoformat()}"
    )

    dirs = config["repositories"]["docs"]["directories"]
    _assert_run_call_once(
        run_mock,
        f"borg create --exclude-from={config['exclude_file']} "
        + f"--stats ::{expected_archive_name} {' '.join(dirs)}",
    )


def test_create_archive_custom_name(config: Config, run_mock):
    name = "custom-archive-name"
    create_archive(config, "docs", name=name)

    dirs = config["repositories"]["docs"]["directories"]
    _assert_run_call_once(
        run_mock,
        f"borg create --exclude-from={config['exclude_file']} "
        + f"--stats ::{name} {' '.join(dirs)}",
    )


def test_create_archive_calls_prune(config: Config, run_mock):
    create_archive(config, "docs", prune=True)
    prune_options = config["repositories"]["docs"]["prune_options"]
    _assert_run_call(
        run_mock,
        f"borg prune --prefix={socket.gethostname()}- " + " ".join(prune_options),
    )


def _assert_run_call_once(run_mock, command):
    run_mock.assert_called_once_with(command.split(), check=True)


def _assert_run_call(run_mock, command):
    run_mock.assert_called_with(command.split(), check=True)
