#!/usr/bin/env python3
"""
Module FOCUS -- UI Focus Widget Mixin
Sub-Package UI.BASE of Package PLIB3 -- Python UI Framework
Copyright (C) 2008-2022 by Peter A. Donis

Released under the GNU General Public License, Version 2
See the LICENSE and README files for more information
"""

from plib.ui.defs import *


class PFocusBase:
    
    signals = (
        SIGNAL_FOCUS_IN,
        SIGNAL_FOCUS_OUT,
    )
