import os
import sys
import tomllib


class Config(dict):
    def __init__(self, configfile: str):
        super().__init__()

        with open(configfile, "rb") as f:
            config_dict = tomllib.load(f)

        self.update(config_dict)
        self._update_repositories()
        self._set_generic_borg_settings()

    def __missing__(self, key):
        print(
            f"Could not find '{key}' in the configuration file. We expect this "
            + "key in the root of the configuration file",
            file=sys.stderr,
        )
        raise KeyError(key)

    def _set_generic_borg_settings(self):
        """Sets borg settings generic to all repositories.
        See https://borgbackup.readthedocs.io/en/stable/man_intro.html#environment-variables"""
        os.putenv("BORG_RSH", self["BORG_RSH"])
        os.putenv("BORG_REMOTE_PATH", self["BORG_REMOTE_PATH"])

    def _update_repositories(self):
        """Replaces the 'repositories' key (list of dicts) with a list of list
        of RepositoryConfig items, which are context managers.
        """
        for reponame, contents in self["repositories"].items():
            customrepo = RepositoryConfig(self, reponame, contents)
            self["repositories"][reponame] = customrepo


class RepositoryConfig(dict):
    def __init__(self, parent, name, dictionary):
        super().__init__()
        self._parent = parent
        self._name = name
        self.update(dictionary)

    @property
    def full_name(self):
        """Returns the full name of the repository,
        including the hostname and directory."""
        host, remote_parent_dir = (
            self._parent["host"],
            self._parent["remote_parent_dir"],
        )
        path = os.path.join(remote_parent_dir, self._name)
        return f"{host}:{path}"

    def __missing__(self, key):
        print(
            f"'{key}' is missing from the configuration. "
            + f"Check that it exists for the repository '{self._name}'.",
            file=sys.stderr,
        )

        raise KeyError(key)

    def __enter__(self):
        """Sets the repository that borg should use.
        See https://borgbackup.readthedocs.io/en/stable/man_intro.html#environment-variables"""
        os.putenv("BORG_REPO", self.full_name)
        os.putenv("BORG_PASSPHRASE", self["password"])
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        os.unsetenv("BORG_REPO")
        os.unsetenv("BORG_PASSPHRASE")
