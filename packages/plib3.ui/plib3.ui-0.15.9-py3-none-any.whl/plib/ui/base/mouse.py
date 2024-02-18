#!/usr/bin/env python3
"""
Module MOUSE -- UI Mouse Widget Mixin
Sub-Package UI.BASE of Package PLIB3 -- Python UI Framework
Copyright (C) 2008-2022 by Peter A. Donis

Released under the GNU General Public License, Version 2
See the LICENSE and README files for more information
"""

from plib.ui.defs import *


class PMouseBase:
    
    signals = (
        SIGNAL_LEFTCLICK,
        SIGNAL_RIGHTCLICK,
        SIGNAL_MIDDLECLICK,
        SIGNAL_LEFTDBLCLICK,
        SIGNAL_RIGHTDBLCLICK,
        SIGNAL_MIDDLEDBLCLICK,
    )
