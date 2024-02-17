import builtins
import os
import sys
from unittest.mock import Mock

import pytest

from bassist.config import Config

CONFIGFILE = os.path.join(
    os.path.dirname(os.path.realpath(__file__)), "configs", "configtest.toml"
)


@pytest.fixture
def configfile() -> str:
    return CONFIGFILE


@pytest.fixture
def config() -> Config:
    return Config(CONFIGFILE)


def test_basic_config_sufficient(config: Config):
    assert isinstance(config, dict)
    assert "host" in config
    assert "BORG_RSH" in config
    assert "BORG_REMOTE_PATH" in config
    assert "docs" in config["repositories"]
    docs = config["repositories"]["docs"]
    assert docs["password"] == "password"
    assert len(docs["directories"]) == 2


def test_basic_config_sets_envvars_on_create(configfile: str, monkeypatch):
    putenv = Mock()
    monkeypatch.setattr("os.putenv", putenv)
    Config(configfile)

    putenv.assert_any_call("BORG_RSH", "ssh -i /home/user/.ssh/rsync")
    putenv.assert_any_call("BORG_REMOTE_PATH", "/usr/local/bin/borg1/borg1")


def test_repo_sets_envvars(config: Config, monkeypatch):
    putenv = Mock()
    monkeypatch.setattr("os.putenv", putenv)

    with config["repositories"]["docs"]:
        putenv.assert_any_call("BORG_REPO", "user@machine.rsync.net:borg/docs")
        putenv.assert_any_call("BORG_PASSPHRASE", "password")


def test_repo_removes_envvars(config: Config, monkeypatch):
    unsetenv = Mock()
    monkeypatch.setattr("os.unsetenv", unsetenv)

    with config["repositories"]["docs"]:
        unsetenv.assert_not_called()

    unsetenv.assert_any_call("BORG_REPO")
    unsetenv.assert_any_call("BORG_PASSPHRASE")


def test_prints_error_messages_keyerror(config: Config, monkeypatch):
    mock = Mock()
    builtins.print = mock

    with pytest.raises(KeyError):
        config["NotExisting"]

    mock.assert_called_with(
        "Could not find 'NotExisting' in the configuration file. "
        + "We expect this key in the root of the configuration file",
        file=sys.stderr,
    )


def test_prints_repospecific_error_messages(config: Config, monkeypatch):
    mock = Mock()
    builtins.print = mock
    with config["repositories"]["docs"] as repo, pytest.raises(KeyError):
        repo["NotExisting"]

    mock.assert_called_with(
        "'NotExisting' is missing from the configuration. "
        + "Check that it exists for the repository 'docs'.",
        file=sys.stderr,
    )
