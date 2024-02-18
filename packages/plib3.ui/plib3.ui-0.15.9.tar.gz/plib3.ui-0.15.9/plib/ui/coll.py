#!/usr/bin/env python3
"""
Module COLL -- UI Collection Support
Sub-Package UI of Package PLIB3 -- Python UI Framework
Copyright (C) 2008-2022 by Peter A. Donis

Released under the GNU General Public License, Version 2
See the LICENSE and README files for more information
"""

from plib.stdlib.coll import baselist


class BaseListWidget(baselist):
    """Base class for widgets that support the list protocol.
    """
    
    def current_index(self):
        """Placeholder for derived classes to implement.
        """
        raise NotImplementedError
    
    def set_current_index(self, index):
        """Placeholder for derived classes to implement.
        """
        raise NotImplementedError


class BaseStringListWidget(BaseListWidget):
    """Base class for widgets that look like a list of strings.
    """
    
    def __init__(self, items=None, value=None, starting_index=None):
        BaseListWidget.__init__(self, items)
        self.complete_init(items, value, starting_index)
    
    def complete_init(self, items, value, starting_index):
        if starting_index:
            self.set_current_index(starting_index)
        elif value:
            self.set_current_text(value)
        elif items:
            self.set_current_index(0)
    
    def add_items(self, items, value=None, starting_index=None):
        self.extend(items)
        self.complete_init(items, value, starting_index)
    
    def load_items(self, items, value=None, starting_index=None):
        self.clear()
        self.add_items(items, value, starting_index)
    
    def current_text(self):
        return self[self.current_index()]
    
    get_current_text = current_text
    
    def set_current_text(self, text):
        self.set_current_index(self.index(text))
