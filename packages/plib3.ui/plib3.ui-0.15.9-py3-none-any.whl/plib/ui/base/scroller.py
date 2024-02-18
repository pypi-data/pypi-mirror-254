#!/usr/bin/env python3
"""
Module SCROLLER -- UI Scroller Widgets
Sub-Package UI.BASE of Package PLIB3 -- Python UI Framework
Copyright (C) 2008-2022 by Peter A. Donis

Released under the GNU General Public License, Version 2
See the LICENSE and README files for more information
"""

from plib.ui.widgets import widget_from_spec

from .app import PWidgetBase


class PScrollerBase(PWidgetBase):
    
    def __init__(self, manager, parent, child=None):
        PWidgetBase.__init__(self, manager, parent)
        if child:
            self.set_child(child)
    
    def set_child(self, child):
        """Derived classes must implement.
        """
        raise NotImplementedError


class PScrollingWrapperBase(PScrollerBase):
    
    def __init__(self, manager, parent, child_spec):
        PScrollerBase.__init__(self, manager, parent)
        child = widget_from_spec(manager, self.spec_parent, child_spec)
        layout = self.get_layout(child)
        if layout is not None:
            self.setup_layout(layout)
        self.set_child(child)
    
    @property
    def spec_parent(self):
        return self.parent
    
    def get_layout(self, child):
        return None  # Derived classes can override
    
    def setup_layout(self, layout):
        pass  # Derived classes can override
