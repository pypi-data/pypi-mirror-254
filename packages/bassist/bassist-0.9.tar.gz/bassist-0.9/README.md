# bassist

[![PyPI](https://img.shields.io/pypi/v/bassist.svg)](https://pypi.org/project/bassist/)
[![builds.sr.ht status](https://builds.sr.ht/~rensoliemans/bassist.svg)](https://builds.sr.ht/~rensoliemans/bassist?)

Create borg backups using a config file

## Installation

Install this tool using `pip`:

    pip install bassist

## Usage

For help, run:

    bassist --help

You can also use:

    python -m bassist --help

## Development

	git clone https://git.sr.ht/~rensoliemans/bassist
	cd bassist

If using [`direnv`](https://direnv.net/):

	echo "layout python" > .envrc
    direnv allow

Otherwise, create a [virtual
environment](https://docs.python.org/3/library/venv.html) and activate
it. Then, install the dependencies and dev dependencies:

    pip install -e '.[dev]'

To run the tests:

    pytest
