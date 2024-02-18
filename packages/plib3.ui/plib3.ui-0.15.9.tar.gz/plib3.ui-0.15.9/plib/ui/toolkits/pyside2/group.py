#!/usr/bin/env python3
"""
Module PYSIDE2.GROUP -- Python PySide 2 Button Group Objects
Sub-Package UI.TOOLKITS.PYSIDE2 of Package PLIB3 -- Python UI Toolkits
Copyright (C) 2008-2022 by Peter A. Donis

Released under the GNU General Public License, Version 2
See the LICENSE and README files for more information

This module contains the PySide 2 UI objects for the panel widgets.
"""

from PySide2 import QtWidgets as qt

from plib.ui.defs import *
from plib.ui.base.group import PButtonGroupMixin

from .app import PQtSequenceWidget, qt_font_object
from .form import PPanel


class PButtonGroupBase(PButtonGroupMixin, PQtSequenceWidget, PPanel):
    
    event_signals = (
        SIGNAL_BUTTONSELECTED,
    )
    
    button_class = None
    group = None
    
    def __init__(self, manager, parent, align, layout, items=None, value=None, starting_index=None, font=None,
                 style=PANEL_PLAIN, margin=None, spacing=None):
        
        PPanel.__init__(self, manager, parent, align, layout,
                        style=style, margin=margin, spacing=spacing)
        PButtonGroupMixin.__init__(self, items, value, starting_index, font)
    
    def init_group(self):
        self.group = qt.QButtonGroup(self)
        self.group.buttonToggled.connect(self.on_button_toggled)
    
    def create_button(self, item):
        return self.button_class(item, self)
    
    def set_button_font(self, button, font_name=None, font_size=None, bold=None, italic=None):
        button.setFont(qt_font_object(font_name, font_size, bold, italic))
    
    def init_button(self, button):
        self.group.addButton(button)
    
    def group_buttons(self):
        return self.group.buttons()
    
    def del_button(self, button):
        self.group.removeButton(button)
    
    def is_checked(self, button):
        return button.isChecked()
    
    def check_button(self, button, checked=True):
        button.setChecked(checked)
    
    def button_text(self, button):
        return button.text()
    
    def set_button_text(self, button, value):
        button.setText(value)


class PButtonGroup(PButtonGroupBase):
    
    button_class = qt.QPushButton
    
    def init_button(self, button):
        PButtonGroupBase.init_button(self, button)
        button.setCheckable(True)


class PRadioGroup(PButtonGroupBase):
    
    button_class = qt.QRadioButton
