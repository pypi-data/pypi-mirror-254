# SPDX-FileCopyrightText: Peter Pentchev <roam@ringlet.net>
# SPDX-License-Identifier: BSD-2-Clause
"""Helper functions for the vetox unit test suite."""

from __future__ import annotations

import contextlib
import pathlib
import tempfile
import typing

from vetox import __main__ as vmain


if typing.TYPE_CHECKING:
    from typing import Final, Iterator


@contextlib.contextmanager
def tempd_and_config() -> Iterator[tuple[pathlib.Path, vmain.Config]]:
    """Create a temporary directory tree, initialize a `Config` object."""
    with tempfile.TemporaryDirectory() as tempd_obj:
        tempd: Final = pathlib.Path(tempd_obj)

        package_dir: Final = tempd / "package"
        package_dir.mkdir(mode=0o755)

        cfg_tempd: Final = tempd / "tmp"
        cfg_tempd.mkdir(mode=0o755)

        cfg: Final = vmain.Config(
            conf=package_dir / "tox.ini",
            log=vmain.build_logger(),
            tempd=cfg_tempd,
        )
        yield (tempd, cfg)
