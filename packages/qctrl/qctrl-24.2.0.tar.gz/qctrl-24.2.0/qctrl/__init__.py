# Copyright 2024 Q-CTRL. All rights reserved.
#
# Licensed under the Q-CTRL Terms of service (the "License"). Unauthorized
# copying or use of this file, via any medium, is strictly prohibited.
# Proprietary and confidential. You may not use this file except in compliance
# with the License. You may obtain a copy of the License at
#
#    https://q-ctrl.com/terms
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS. See the
# License for the specific language.

"""The main qctrl namespace."""

__version__ = "24.2.0"

from rich.console import Console as _Console

from .qctrl import Qctrl  # pylint:disable=cyclic-import

_console = _Console()
_URL = "docs.q-ctrl.com/boulder-opal/get-started"
_console.print(
    "We've created a new dedicated and improved Boulder Opal client. "
    "Support for the legacy qctrl client ended on 2024-01-31. "
    f"For more information, read the get started guide: [link=https://{_URL}]{_URL}[/link]",
    style="bold",
)
