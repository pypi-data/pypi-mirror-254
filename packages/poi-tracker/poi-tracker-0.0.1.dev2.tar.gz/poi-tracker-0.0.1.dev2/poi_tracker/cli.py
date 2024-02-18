# -*- coding: utf-8 -*-

# (c) Meta Platforms, Inc. and affiliates.
#
# Fedora-License-Identifier: GPLv2+
# SPDX-2.0-License-Identifier: GPL-2.0+
# SPDX-3.0-License-Identifier: GPL-2.0-or-later
#
# This program is free software.
# For more information on the license, see COPYING.md.
# For more information on free software, see
# <https://www.gnu.org/philosophy/free-sw.en.html>.

import click
import sys

from typing import Optional

from .exporters import ContentResolverInput
from .inventory import Inventory, RPMPackage, SRPMPackage

from . import (
    __version__,
)


@click.group("Main CLI")
def cli() -> None:
    """
    Tool for tracking packages of interest
    """


@cli.command(help="Track a binary RPM")
@click.argument("inventory-file", type=str)
@click.argument("srpm", type=str)
@click.argument("name", type=str)
@click.option(
    "--arch",
    default=None,
    multiple=True,
    type=str,
    help="The architecture for the binary RPM. Can be specified multiple times",
)
@click.option("--poc", default=None, type=str)
@click.option("--reason", default=None, type=str)
def add_rpm(
    inventory_file: str,
    srpm: str,
    name: str,
    poc: Optional[str],
    reason: Optional[str],
    arch: Optional[list[str]],
) -> None:
    """
    Track a binary RPM
    """
    inv = Inventory.load(inventory_file)
    if not inv.has_srpm(srpm):
        click.echo("Source RPM not tracked yet", err=True)
        sys.exit(1)
    inv.get_srpm(srpm).rpm_packages.add(
        RPMPackage(name=name, arches=arch, poc=poc, reason=reason)
    )
    inv.save(inventory_file)


@cli.command(help="Track a source RPM")
@click.argument("inventory-file", type=str)
@click.argument("name", type=str)
@click.option(
    "--arch",
    default=None,
    multiple=True,
    type=str,
    help="The architecture for the binary RPM. Can be specified multiple times",
)
@click.option("--poc", default=None, type=str)
@click.option("--reason", default=None, type=str)
@click.option(
    "--rpm",
    default=None,
    multiple=True,
    type=str,
    help="The binary RPM to track. Can be specified multiple times",
)
def add_srpm(
    inventory_file: str,
    name: str,
    poc: Optional[str],
    reason: Optional[str],
    arch: Optional[list[str]],
    rpm: Optional[list[str]],
) -> None:
    """
    Track a source RPM
    """
    inv = Inventory.load(inventory_file)
    inv.srpm_packages.add(
        SRPMPackage.new_with_rpms(
            name=name, rpm_names=rpm, arches=arch, poc=poc, reason=reason
        )
    )
    inv.save(inventory_file)


@cli.command(help="Export inventory for content resolver")
@click.argument("inventory-file", type=str)
@click.argument("content-resolver-input-file", type=str)
def export_as_content_resolver_input(
    inventory_file: str, content_resolver_input_file: str
):
    inv = Inventory.load(inventory_file)
    cri = ContentResolverInput(inv)
    cri.save(cri_file=content_resolver_input_file)


@cli.command(help="Create a new inventory")
@click.argument("inventory-file", type=str)
@click.argument("name", type=str)
@click.argument("description", type=str)
@click.argument("maintainer", type=str)
@click.option(
    "--label",
    default=["eln-extras"],
    multiple=True,
    show_default=True,
    type=str,
    help="Labels (tags) for this inventory",
)
def new_inventory(
    inventory_file: str, name: str, description: str, maintainer: str, label: list[str]
):
    inv = Inventory(
        name=name,
        description=description,
        maintainer=maintainer,
        labels=label,
        srpm_packages=set(),
    )
    inv.save(inventory_file)


@cli.command(help="Untrack an RPM")
@click.argument("inventory-file", type=str)
@click.argument("name", type=str)
def remove_rpm(inventory_file: str, name: str):
    inv = Inventory.load(inventory_file)
    inv.remove_rpm(name)
    inv.save(inventory_file)


@cli.command(help="Untrack a source RPM")
@click.argument("inventory-file", type=str)
@click.argument("name", type=str)
def remove_srpm(inventory_file: str, name: str):
    inv = Inventory.load(inventory_file)
    inv.remove_srpm(name)
    inv.save(inventory_file)


@cli.command(help="Show the inventory")
@click.argument("inventory-file", type=str)
def show(inventory_file: str):
    inv = Inventory.load(inventory_file)
    click.echo(inv.model_dump_json(indent=2))


@cli.command(help="Show inventory as content resolver input")
@click.argument("inventory-file", type=str)
def show_as_content_resolver_input(inventory_file: str):
    inv = Inventory.load(inventory_file)
    cri = ContentResolverInput(inv)
    click.echo(cri)


@cli.command(help="Display poi-tracker version information")
def version() -> None:
    """
    Display poi-tracker version information
    """
    click.echo(__version__)
