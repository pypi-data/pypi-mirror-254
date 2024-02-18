#!/usr/bin/env python3
"""
Module MOUSE -- UI Mouse Widget Mixin
Sub-Package UI.TOOLKITS.WX of Package PLIB3 -- Python GUI Toolkits
Copyright (C) 2008-2022 by Peter A. Donis

Released under the GNU General Public License, Version 2
See the LICENSE and README files for more information
"""

import wx

from plib.stdlib.builtins import first

from plib.ui.defs import *
from plib.ui.base.mouse import PMouseBase


class PMouseMixin(PMouseBase):
    
    button_signals = {
        wx.MOUSE_BTN_LEFT: SIGNAL_LEFTCLICK,
        wx.MOUSE_BTN_RIGHT: SIGNAL_RIGHTCLICK,
        wx.MOUSE_BTN_MIDDLE: SIGNAL_MIDDLECLICK,
    }
    
    button_pressed = None
    
    def setup_signals(self):
        self.wx_register_event(wx.EVT_LEFT_DOWN, self.OnButtonDown)
        self.wx_register_event(wx.EVT_RIGHT_DOWN, self.OnButtonDown)
        self.wx_register_event(wx.EVT_MIDDLE_DOWN, self.OnButtonDown)
        self.wx_register_event(wx.EVT_LEFT_UP, self.OnButtonUp)
        self.wx_register_event(wx.EVT_RIGHT_UP, self.OnButtonUp)
        self.wx_register_event(wx.EVT_MIDDLE_UP, self.OnButtonUp)
    
    def OnButtonDown(self, event):
        self.button_pressed = first(b for b in self.button_signals if event.Button(b))
        event.Skip()  # so default processing still occurs
    
    def OnButtonUp(self, event):
        button_released = first(b for b in self.button_signals if event.Button(b))
        if (button_released is not None) and (button_released == self.button_pressed):
            self.forward_event(self.button_signals[self.button_pressed], event)
        self.button_pressed = None
        event.Skip()  # so default processing still occurs
