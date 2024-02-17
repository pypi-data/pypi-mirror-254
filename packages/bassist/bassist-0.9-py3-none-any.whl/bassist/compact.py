from bassist.util import now, run


def compact(config, only=None):
    if only:
        with config["repositories"][only]:
            _compact_and_print(only)
    else:
        for reponame in config["repositories"]:
            with config["repositories"][reponame]:
                _compact_and_print(reponame)


def _compact_and_print(reponame):
    print(f"Compacting repository {reponame} at {now()}")
    run("borg compact")
