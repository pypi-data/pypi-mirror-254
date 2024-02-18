#!/usr/bin/env python3
"""
Module PAGEWIDGET -- UI Page Widget
Sub-Package UI.BASE of Package PLIB3 -- Python UI Framework
Copyright (C) 2008-2022 by Peter A. Donis

Released under the GNU General Public License, Version 2
See the LICENSE and README files for more information
"""

from plib.ui.defs import *
from plib.ui.coll import BaseListWidget
from plib.ui.widgets import widget_from_spec

from .app import PWidgetBase


class PPageWidgetBase(PWidgetBase, BaseListWidget):
    """Page widget as a Python list of widgets.
    """
    
    signals = (
        SIGNAL_TABSELECTED,
    )
    
    def __init__(self, manager, parent, pages=None, link_to=None):
        PWidgetBase.__init__(self, manager, parent)
        BaseListWidget.__init__(self)
        if pages:
            self.create_pages(pages)
        self.link_to = link_to
    
    def link_to_widget(self, widget):
        signal = widget.signals[0]  # assume this is the selected signal that gives the new index
        widget.setup_notify(signal, self.on_link_selected)
    
    def setup_link_to(self):
        if not self.link_to:
            return
        widget = getattr(self.manager, self.link_to)
        self.link_to_widget(widget)
        self.link_to = None  # so repeated calls won't do anything
    
    def on_link_selected(self, index):
        # Need to filter signals here since it is possible for the selector
        # to send an out of range index if it is mutated; we don't raise an
        # exception because mutations should be due to other code, so the
        # code writer just needs to be aware of the consequences
        if (index < 0) or (index > (len(self) - 1)):
            return
        self.set_current_index(index)
    
    def setup_signals(self):
        self.setup_link_to()
    
    def create_pages(self, pages):
        """Create pages from sequence.
        
        Assumes that the sequence contains a widget spec for each page.
        """
        self.extend(widget_from_spec(self.manager, self, spec) for spec in pages)
    
    def append_and_focus(self, page):
        """Add new page and set focus to it.
        
        Assumes that page is a widget spec.
        """
        self.append(page)
        self.set_current_index(len(self) - 1)
    
    def __len__(self):
        return self.page_count()
    
    def _indexlen(self):
        return self.page_count()
    
    def page_count(self):
        """ Placeholder for derived classes to implement. """
        raise NotImplementedError
    
    def page_at(self, index):
        """ Placeholder for derived classes to implement. """
        raise NotImplementedError
    
    def add_page(self, index, widget):
        """Placeholder for derived classes to implement.
        """
        raise NotImplementedError
    
    def del_page(self, index):
        """Placeholder for derived classes to implement.
        """
        raise NotImplementedError
    
    def _get_data(self, index):
        return self.page_at(index)
    
    def _set_data(self, index, value):
        # This gets a little complicated because we have to delete the
        # old page at this index and insert a new one.
        self._del_data(index)
        self._add_data(index, value)
    
    def _add_data(self, index, value):
        self.add_page(index, value)
    
    def _del_data(self, index):
        self.del_page(index)
    
    def current_widget(self):
        return self[self.current_index()]
