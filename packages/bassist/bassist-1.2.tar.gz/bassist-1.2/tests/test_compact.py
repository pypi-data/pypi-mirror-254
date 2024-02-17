import os
from unittest.mock import Mock

import pytest

from bassist.compact import compact
from bassist.config import Config

CONFIGFILE = os.path.join(
    os.path.dirname(os.path.realpath(__file__)), "configs", "compacttest.toml"
)


@pytest.fixture
def config() -> Config:
    return Config(CONFIGFILE)


@pytest.fixture
def run_mock(monkeypatch):
    run = Mock()
    monkeypatch.setattr("subprocess.run", run)
    return run


def test_compact_calls_borg_compact_all_repos(config: Config, run_mock, monkeypatch):
    putenv = Mock()
    monkeypatch.setattr("os.putenv", putenv)

    compact(config)

    for reponame, repo in config["repositories"].items():
        full_reponame = f"{config['host']}:{config['remote_parent_dir']}/{reponame}"
        putenv.assert_any_call("BORG_REPO", full_reponame)
        putenv.assert_any_call("BORG_PASSPHRASE", repo["password"])

        run_mock.assert_any_call("borg compact".split(), check=True)


def test_compact_only(config: Config, run_mock, monkeypatch):
    putenv = Mock()
    monkeypatch.setattr("os.putenv", putenv)

    compact(config, "docs")

    full_reponame = f"{config['host']}:{config['remote_parent_dir']}/docs"
    putenv.assert_any_call("BORG_REPO", full_reponame)
    putenv.assert_any_call(
        "BORG_PASSPHRASE", config["repositories"]["docs"]["password"]
    )
    assert putenv.call_count == 2

    run_mock.assert_any_call("borg compact".split(), check=True)
    assert run_mock.call_count == 1
