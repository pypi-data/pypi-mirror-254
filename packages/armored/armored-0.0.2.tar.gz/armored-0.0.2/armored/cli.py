# ------------------------------------------------------------------------------
# Copyright (c) 2022 Korawich Anuttra. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for
# license information.
# ------------------------------------------------------------------------------
import click


@click.group()
def cli() -> None:
    """A simple command line tool."""
    pass  # pragma: no cover.


def main() -> None:
    cli.main()


if __name__ == "__main__":
    main()
