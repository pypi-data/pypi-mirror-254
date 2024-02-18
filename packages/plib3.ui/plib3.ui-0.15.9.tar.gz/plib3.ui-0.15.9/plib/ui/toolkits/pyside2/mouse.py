#!/usr/bin/env python3
"""
Module MOUSE -- UI Mouse Widget Mixin
Sub-Package UI.TOOLKITS.PYSIDE2 of Package PLIB3 -- Python UI Toolkits
Copyright (C) 2008-2022 by Peter A. Donis

Released under the GNU General Public License, Version 2
See the LICENSE and README files for more information
"""

from PySide2.QtCore import Qt

from plib.ui.defs import *
from plib.ui.base.mouse import PMouseBase

from .app import PQtWidgetMeta


class PMouseMixin(PMouseBase, metaclass=PQtWidgetMeta):
    
    event_signals = (
        SIGNAL_LEFTCLICK,
        SIGNAL_RIGHTCLICK,
        SIGNAL_MIDDLECLICK,
        SIGNAL_LEFTDBLCLICK,
        SIGNAL_RIGHTDBLCLICK,
        SIGNAL_MIDDLEDBLCLICK,
    )
    
    button_events = {
        Qt.LeftButton: SIGNAL_LEFTCLICK,
        Qt.RightButton: SIGNAL_RIGHTCLICK,
        Qt.MiddleButton: SIGNAL_MIDDLECLICK,
    }
    
    double_events = {
        Qt.LeftButton: SIGNAL_LEFTDBLCLICK,
        Qt.RightButton: SIGNAL_RIGHTDBLCLICK,
        Qt.MiddleButton: SIGNAL_MIDDLEDBLCLICK,
    }
    
    def do_button_notify(self, event_map, event):
        sig = event_map.get(event.button())
        if sig:
            self.do_notify(sig)
    
    button_pressed = None
    
    def mousePressEvent(self, event):
        self.button_pressed = event.button()
    
    def mouseReleaseEvent(self, event):
        if (self.button_pressed is not None) and (event.button() == self.button_pressed):
            self.do_button_notify(self.button_events, event)
        self.button_pressed = None
    
    def mouseDoubleClickEvent(self, event):
        self.do_button_notify(self.double_events, event)
