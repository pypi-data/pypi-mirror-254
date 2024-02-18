#!/usr/bin/env python3
"""
Module FOCUS -- UI Focus Widget Mixin
Sub-Package UI.TOOLKITS.WX of Package PLIB3 -- Python GUI Toolkits
Copyright (C) 2008-2022 by Peter A. Donis

Released under the GNU General Public License, Version 2
See the LICENSE and README files for more information
"""

from plib.ui.defs import *
from plib.ui.base.focus import PFocusBase


class PFocusMixin(PFocusBase):
    pass  # no special code required here since the focus events are built in to all wx widgets
