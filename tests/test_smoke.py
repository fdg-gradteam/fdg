"""Smoke test: proves the package installs and every module imports."""

import importlib

import pytest

import fdg

MODULES = ["capture", "compliance", "intelligence", "trust", "output", "common"]


def test_version_is_set():
    assert fdg.__version__


@pytest.mark.parametrize("name", MODULES)
def test_module_imports(name):
    importlib.import_module(f"fdg.{name}")
