import datetime
import subprocess
import sys


def run(command: str):
    try:
        return subprocess.run(command.split(" "), check=True)
    except subprocess.CalledProcessError as e:
        print(
            f"Command {command} failed with returncode {e.returncode}.", file=sys.stderr
        )
        raise


def now():
    return datetime.datetime.now().isoformat()
