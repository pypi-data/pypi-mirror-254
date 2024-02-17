import datetime
import socket
from typing import Optional

from bassist.config import Config
from bassist.util import now, run


def create_archive(
    config: Config, repository: str, prune: bool = False, name: Optional[str] = None
):
    hostname = socket.gethostname()
    date = datetime.date.today().isoformat()
    archive_name = name or f"{hostname}-{date}"

    with config["repositories"][repository] as repo:
        print(
            f"Creating archive {archive_name} at {now()} for repository"
            + f" {repo.full_name}",
            flush=True,
        )

        directories = repo["directories"]
        exclude_file = config["exclude_file"]
        run(
            f"borg create --exclude-from={exclude_file} --stats "
            + f"::{archive_name} "
            + " ".join(directories)
        )

        if prune:
            print(f"Pruning repository {repo.full_name} at {now()}", flush=True)
            prune_options = repo["prune_options"]
            prune_options_str = " ".join(prune_options)
            run(f"borg prune --prefix={hostname}- " + prune_options_str)
