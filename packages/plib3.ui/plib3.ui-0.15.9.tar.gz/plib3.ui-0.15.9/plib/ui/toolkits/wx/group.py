#!/usr/bin/env python3
"""
Module WX.GROUP -- Python wxWidgets Button Group Objects
Sub-Package UI.TOOLKITS.WX of Package PLIB3 -- Python GUI Toolkits
Copyright (C) 2008-2022 by Peter A. Donis

Released under the GNU General Public License, Version 2
See the LICENSE and README files for more information

This module contains the wxWidgets UI objects for the panel widgets.
"""

import wx

from plib.ui.defs import *
from plib.ui.base.group import PButtonGroupMixin

from .app import PWxSequenceWidget, eventManager, wx_font_object
from .form import PPanel


class PButtonGroupBase(PWxSequenceWidget, PButtonGroupMixin, PPanel):
    
    button_class = None
    
    def __init__(self, manager, parent, align, layout, items=None, value=None, starting_index=None, font=None,
                 style=PANEL_PLAIN, margin=None, spacing=None):
        
        self.clearing = False
        PPanel.__init__(self, manager, parent, align, layout,
                        style=style, margin=margin, spacing=spacing)
        PButtonGroupMixin.__init__(self, items, value, starting_index, font)
    
    def complete_init(self, items, value, starting_index):
        PButtonGroupMixin.complete_init(self, items, value, starting_index)
        self.SetSizerAndFit(self._sizer)
    
    def init_group(self):
        self._buttons = []
    
    def add_items(self, items, value=None, starting_index=None):
        PButtonGroupMixin.add_items(self, items, value, starting_index)
        self.SetSizerAndFit(self._sizer)
    
    button_style = 0
    
    def create_button(self, item):
        return self.button_class(self, label=item, style=self.button_style)
    
    def set_button_font(self, button, font_name=None, font_size=None, bold=None, italic=None):
        font = wx_font_object(font_name, font_size, bold, italic)
        button.SetFont(font)
    
    def init_button(self, button):
        self._buttons.append(button)
        eventManager.Register(self.buttonEvent, self.button_event, button)
    
    def group_buttons(self):
        return self._buttons  # TODO: can this just be self.contents?
    
    def del_button(self, button):
        self._buttons.remove(button)
    
    def remove_widget(self, widget):
        self._sizer.Detach(widget)
        if not self.clearing:
            self.SetSizerAndFit(self._sizer)
    
    def clear(self):
        if self._buttons:
            self.clearing = True
            PButtonGroupMixin.clear(self)
            self.SetSizerAndFit(self._sizer)
            self.clearing = False
    
    def is_checked(self, button):
        return button.GetValue()
    
    def check_button(self, button, checked=True):
        button.SetValue(checked)
        # This event doesn't get fired by wx when the button is checked in code,
        # so we have to emulate it manually
        self.on_button_toggled(button, checked)
    
    def button_text(self, button):
        return button.GetLabel()
    
    def set_button_text(self, button, value):
        button.SetLabel(value)


class PButtonGroup(PButtonGroupBase):
    
    button_class = wx.ToggleButton
    button_event = wx.EVT_TOGGLEBUTTON
    
    def buttonEvent(self, event):
        # Here we have to go around Robin Hood's barn because
        # wx has no built-in support for grouping toggle buttons (??)
        button = event.GetEventObject()
        checked = event.IsChecked()  # or button.GetValue()
        if checked:
            for other_button in self.buttons:
                if other_button is not button:
                    other_button.SetValue(False)
        self.on_button_toggled(button, checked)


class PRadioGroup(PButtonGroupBase):
    
    button_class = wx.RadioButton
    button_event = wx.EVT_RADIOBUTTON
    
    next_button_style = wx.RB_GROUP
    
    @property
    def button_style(self):
        style = self.next_button_style
        self.next_button_style = 0
        return style
    
    def buttonEvent(self, event):
        # Here this works simply because wx radio buttons can be grouped in the style
        button = event.GetEventObject()
        checked = event.IsChecked()  # or button.GetValue()
        self.on_button_toggled(button, checked)
