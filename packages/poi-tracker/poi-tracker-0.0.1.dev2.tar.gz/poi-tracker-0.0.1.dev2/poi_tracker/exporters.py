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
import sys
import yaml

from .inventory import Inventory


class ContentResolverInput:
    def __init__(self, inv: Inventory):
        self.doc = self.parse_inventory(inv)

    @staticmethod
    def parse_inventory(inv: Inventory):
        data = {
            "name": inv.name,
            "description": inv.description,
            "maintainer": inv.maintainer,
        }

        all_packages = inv.get_rpm_packages()
        package_names = set(p.name for p in all_packages if not p.arches)
        arch_packages = set(p for p in all_packages if p.arches)

        if package_names:
            data["packages"] = list(package_names)

        if arch_packages:
            arches = set(a for r in arch_packages for a in r.arches)
            data["arch_packages"] = {
                a: [r.name for r in arch_packages if a in r.arches] for a in arches
            }

        data["labels"] = list(inv.labels)

        doc = {
            "document": "feedback-pipeline-workload",
            "version": 1,
            "data": data,
        }
        return doc

    def save(self: ContentResolverInput, cri_file: str):
        try:
            with io.open(cri_file, "w", encoding="utf-8") as fp:
                yaml.dump(self.doc, fp, sort_keys=False)
        except OSError as ex:
            print(f"{ex.strerror}: {inventory_file}", file=sys.stderr)

    def __str__(self: ContentResolverInput):
        return yaml.dump(self.doc, sort_keys=False)
