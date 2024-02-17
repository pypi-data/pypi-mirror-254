import os

import click

from bassist import backup, compact, quota, report
from bassist.config import Config

config = None
default_configfile = os.path.join("/", "etc", "bassist.toml")

CONTEXT_SETTINGS = dict(help_option_names=["-h", "--help"])


@click.group(context_settings=CONTEXT_SETTINGS)
@click.option(
    "-c",
    "--configfile",
    help=(
        "Location of the config.toml file to read. "
        + f"Defaults to `{default_configfile}`."
    ),
    default=default_configfile,
)
@click.version_option()
def cli(configfile):
    global config
    "Create borg backups using a config file"
    config = Config(configfile)


@cli.command(name="backup")
@click.argument("repository")
@click.option(
    "-p",
    "--prune",
    is_flag=True,
    help="Prunes the repository after creating an archive.",
)
@click.option(
    "-n",
    "--name",
    help=(
        "Name of the archive. If not given, the template {hostname}-{date} "
        + "will be used"
    ),
)
def backup_command(repository, prune, name):
    """Create a backup of a given repository. For example:

    \b
        bassist backup docs --prune --name before-upgrade

    """
    backup.create_archive(config, repository, prune, name)


@cli.command(name="compact")
@click.option(
    "-o", "--only", help="Compact only a given repository instead of every one"
)
def compact_command(only=None):
    """Compact all borg repositories found in the configfile. Use the
    option --only to limit compacting to a single repository. For
    example:

    \b
        bassist compact --only docs

    """
    compact.compact(config, only)


@cli.command(name="list")
def list_command():
    "List repositories known in the given configuration file"
    repositories = config["repositories"].keys()
    click.echo(f"Known repositories: {','.join(repositories)}")


@cli.command(name="report")
@click.argument("Logfile")
@click.option(
    "-e",
    "--empty-logfile",
    is_flag=True,
    help="Empty logfile after report",
)
def report_command(logfile, empty_logfile):
    "Report results found in logfile."
    report.report(config, logfile, empty_logfile)


@cli.command(name="quota")
def quota_command():
    "Show quota of the user that owns the borg server"
    quota.show(config)
