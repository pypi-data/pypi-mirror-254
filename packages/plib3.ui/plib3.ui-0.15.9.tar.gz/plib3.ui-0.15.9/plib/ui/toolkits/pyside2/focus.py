#!/usr/bin/env python3
"""
Module FOCUS -- UI Focus Widget Mixin
Sub-Package UI.TOOLKITS.PYSIDE2 of Package PLIB3 -- Python UI Toolkits
Copyright (C) 2008-2022 by Peter A. Donis

Released under the GNU General Public License, Version 2
See the LICENSE and README files for more information
"""

from plib.ui.defs import *
from plib.ui.base.focus import PFocusBase

from .app import PQtWidgetMeta


class PFocusMixin(PFocusBase, metaclass=PQtWidgetMeta):
    
    event_signals = (
        SIGNAL_FOCUS_IN,
        SIGNAL_FOCUS_OUT
    )
    
    def focusInEvent(self, event):
        super(PFocusMixin, self).focusInEvent(event)
        self.do_notify(SIGNAL_FOCUS_IN)
    
    def focusOutEvent(self, event):
        super(PFocusMixin, self).focusOutEvent(event)
        self.do_notify(SIGNAL_FOCUS_OUT)
