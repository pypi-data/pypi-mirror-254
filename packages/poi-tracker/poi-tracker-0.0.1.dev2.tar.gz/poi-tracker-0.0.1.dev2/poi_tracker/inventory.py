# -*- coding: utf-8 -*-

# (c) Meta Platforms, Inc. and affiliates.
#
# SPDX-3.0-License-Identifier: GPL-2.0-or-later
#
# This program is free software.
# For more information on the license, see COPYING.md.
# For more information on free software, see
# <https://www.gnu.org/philosophy/free-sw.en.html>.

from __future__ import annotations  # for forward references

import io
import json
import sys

from collections.abc import Iterable
from pydantic import BaseModel, Field, EmailStr, NameEmail
from typing import Optional


class Inventory(BaseModel):
    name: str
    description: str
    maintainer: str
    labels: set[str]
    srpm_packages: set[SRPMPackage]

    class Config:
        frozen = True

    def get_rpm_packages(self: Inventory) -> set[RPMPackage]:
        return set(r for s in self.srpm_packages for r in s.rpm_packages)

    def get_rpm(self: Inventory, name: str) -> Optional[RPMPackage]:
        candidates = [rpm for rpm in self.get_rpm_packages() if rpm.name == name]
        if len(candidates) != 1:
            return None  # no unique match
        return candidates[0]

    def get_srpm(self: Inventory, name: str) -> Optional[SRPMPackage]:
        candidates = [srpm for srpm in self.srpm_packages if srpm.name == name]
        if len(candidates) != 1:
            return None  # no unique match
        return candidates[0]

    def has_rpm(self: Inventory, name: str) -> bool:
        return name in set(rpm.name for rpm in self.get_rpm_packages())

    def has_srpm(self: Inventory, name: str) -> bool:
        return name in set(srpm.name for srpm in self.srpm_packages)

    @staticmethod
    def load(inventory_file: str) -> Inventory:
        try:
            with io.open(inventory_file, "r", encoding="utf-8") as fp:
                inventory_dict = json.load(fp)
                inventory = Inventory.model_validate(inventory_dict)
        except json.decoder.JSONDecodeError as ex:
            print(f"{ex.strerror}: {inventory_file}", file=sys.stderr)
            raise (ex)
        except OSError as ex:
            print(f"{ex.strerror}: {inventory_file}", file=sys.stderr)
            raise (ex)
        return inventory

    def remove_rpm(self: Inventory, name: str):
        rpm = self.get_rpm(name)
        if rpm:
            for srpm in self.srpm_packages:
                if rpm in srpm.rpm_packages:
                    srpm.rpm_packages.remove(rpm)
                    return

    def remove_srpm(self: Inventory, name: str):
        srpm = self.get_srpm(name)
        if srpm:
            self.srpm_packages.remove(srpm)

    def save(self: Inventory, inventory_file: str):
        try:
            with io.open(inventory_file, "w", encoding="utf-8") as fp:
                print(self.model_dump_json(indent=2), file=fp)
        except OSError as ex:
            print(f"{ex.strerror}: {inventory_file}", file=sys.stderr)


class HashableNameEmail(NameEmail):
    def __hash__(self):
        return hash((self.name, self.email))


class Package(BaseModel):
    name: str
    poc: Optional[HashableNameEmail] = None
    reason: Optional[str] = None

    class Config:
        frozen = True

    def __hash__(self):
        # cheat and just hash the JSON representation
        return hash(self.model_dump_json())


class RPMPackage(Package):
    arches: Optional[set[str]] = None


class SRPMPackage(Package):
    rpm_packages: Optional[set[RPMPackage]] = None

    @staticmethod
    def new_with_rpms(
        name: str,
        rpm_names: Iterable[str],
        arches: Optional[set[str]] = None,
        poc: Optional[HashableNameEmail] = None,
        reason: Optional[str] = None,
    ) -> SRPMPackage:
        rpm_packages = set(
            RPMPackage(name=rpm_name, arches=arches) for rpm_name in rpm_names
        )
        return SRPMPackage(name=name, rpm_packages=rpm_packages, poc=poc, reason=reason)
