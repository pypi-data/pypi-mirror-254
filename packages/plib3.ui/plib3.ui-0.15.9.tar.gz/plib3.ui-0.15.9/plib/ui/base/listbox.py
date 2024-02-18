#!/usr/bin/env python3
"""
Module LISTBOX-- UI List Box Widget
Sub-Package UI.BASE of Package PLIB3 -- Python UI Framework
Copyright (C) 2008-2022 by Peter A. Donis

Released under the GNU General Public License, Version 2
See the LICENSE and README files for more information
"""

import functools

from plib.stdlib.coll import SortMixin

from plib.ui.defs import *
from plib.ui.coll import BaseStringListWidget

from .app import PWidgetBase


class PListBoxBase(PWidgetBase, BaseStringListWidget):
    """List box that looks like a list of strings.
    """
    
    signals = (
        SIGNAL_LISTBOXSELECTED,
    )
    
    default_itemheight = 30
    
    def __init__(self, manager, parent, items=None, value=None, starting_index=None,
                 geometry=None, font=None):
        
        PWidgetBase.__init__(self, manager, parent,
                             geometry=geometry, font=font)
        BaseStringListWidget.__init__(self, items, value, starting_index)
    
    def item_height(self, index):
        return self.default_itemheight
    
    def minheight(self):
        return sum(self.item_height(index) for index in range(len(self)))


class PSortedListBoxBase(SortMixin, PListBoxBase):
    """List box that automatically sorts its items.
    """
    
    def __init__(self, manager, parent, items=None, value=None, starting_index=None,
                 geometry=None, font=None, key=None):
        
        PListBoxBase.__init__(self, manager, parent, geometry=geometry, font=font)  # don't pass items here
        self._init_seq(items, key)  # sort items and add them here
        self.complete_init(items, value, starting_index)  # do this since the inherited constructor didn't see items or value
