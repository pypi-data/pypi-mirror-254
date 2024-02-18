#!/usr/bin/env python3
"""
Module GROUP -- UI Button Group Widgets
Sub-Package UI.BASE of Package PLIB3 -- Python UI Framework
Copyright (C) 2008-2022 by Peter A. Donis

Released under the GNU General Public License, Version 2
See the LICENSE and README files for more information
"""

from plib.ui.defs import *
from plib.ui.coll import BaseStringListWidget
from plib.ui.common import font_args


class PButtonGroupMixin(BaseStringListWidget):
    # To be used as a mixin class for button groups in each toolkit,
    # subclassed from PPanel
    
    signals = (
        SIGNAL_BUTTONSELECTED,
    )
    
    def __init__(self, items=None, value=None, starting_index=None, font=None):
        self.item_font = font
        self.init_group()
        BaseStringListWidget.__init__(self, items, value, starting_index)
    
    def init_group(self):
        pass  # Toolkits may override to set up internal group object
    
    def create_button(self, item):
        """Derived classes must implement.
        """
        raise NotImplementedError
    
    def set_button_font(self, button, font_name=None, font_size=None, bold=None, italic=None):
        """Derived classes must implement.
        """
        raise NotImplementedError
    
    def add_button(self, item):
        widget = self.create_button(item)
        if self.item_font:
            self.set_button_font(widget, *self.item_font)
        self.add_widget(widget)
        self.contents.append(widget)
    
    def init_button(self, button):
        """Derived classes must implement.
        """
        raise NotImplementedError
    
    def add_widget(self, widget):
        self.init_button(widget)
        # This should call the toolkit's PPanel.add_widget
        super(PButtonGroupMixin, self).add_widget(widget)
    
    def group_buttons(self):
        """Derived classes must implement.
        """
        raise NotImplementedError
    
    @property
    def buttons(self):
        return self.group_buttons()
    
    def del_button(self, button):
        pass  # Subclasses may override
    
    def remove_button(self, button):
        self.contents.remove(button)
        self.remove_widget(button)
        self.del_button(button)
    
    def is_checked(self, button):
        """Derived classes must implement.
        """
        raise NotImplementedError
    
    def check_button(self, button, checked=True):
        """Derived classes must implement.
        """
        raise NotImplementedError
    
    def button_text(self, button):
        """Derived classes must implement.
        """
        raise NotImplementedError
    
    def set_button_text(self, button, value):
        """Derived classes must implement.
        """
        raise NotImplementedError
    
    def button_text_at(self, index):
        return self.button_text(self.buttons[index])
    
    def set_button_text_at(self, index, value):
        self.set_button_text(self.buttons[index], value)
    
    def selected_button(self):
        return first(button for button in self.buttons if self.is_checked(button))
    
    def current_text(self):
        button = self.selected_button()
        return self.button_text(button) if button else None
    
    def current_index(self):
        return first(i for i, button in enumerate(self.buttons) if self.is_checked(button))
    
    def set_current_index(self, index):
        self.check_button(self.buttons[index])
    
    def on_button_toggled(self, button, checked):
        if checked:
            index = self.buttons.index(button)
            self.do_notify(SIGNAL_BUTTONSELECTED, index)
    
    # Sequence emulator methods; note that the sequence interface does not support
    # inserting buttons at arbitrary indexes, only appending buttons and removing
    # them
    
    def _indexlen(self):
        return len(self.buttons)  # toolkits may override if a faster method exists
    
    def _get_data(self, index):
        return self.button_text_at(index)
    
    def _set_data(self, index, value):
        self.set_button_text_at(index, value)
    
    def _add_data(self, index, value):
        if index != len(self):
            raise ValueError("Cannot insert buttons in middle of button group")
        self.add_button(value)
    
    def _del_data(self, index):
        self.remove_button(self.contents[index])
