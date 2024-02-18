#!/usr/bin/env python3
"""
Module PYSIDE2.PAGEWIDGET -- Python PySide 2 Page Widget
Sub-Package UI.TOOLKITS.PYSIDE2 of Package PLIB3 -- Python UI Toolkits
Copyright (C) 2008-2022 by Peter A. Donis

Released under the GNU General Public License, Version 2
See the LICENSE and README files for more information

This module contains the PySide 2 UI objects for the page widget.
"""

from PySide2 import QtWidgets as qt

from plib.ui.defs import *
from plib.ui.base.pagewidget import PPageWidgetBase

from .app import PQtSequenceWidget


class PPageWidget(PQtSequenceWidget, qt.QStackedWidget, PPageWidgetBase):
    
    def __init__(self, manager, parent, pages=None, link_to=None):
        qt.QStackedWidget.__init__(self, parent)
        PPageWidgetBase.__init__(self, manager, parent, pages=pages, link_to=link_to)
    
    def count(self, value):
        # Method name collision, we want it to be the Python sequence
        # count method here.
        return PPageWidgetBase.count(self, value)
    
    def page_count(self):
        # Let this method access the Qt page widget count method.
        return qt.QStackedWidget.count(self)
    
    def page_at(self, index):
        return self.widget(index)
    
    def add_page(self, index, widget):
        self.insertWidget(index, widget)
    
    def del_page(self, index):
        self.removeWidget(index)
    
    def current_index(self):
        return self.currentIndex()
    
    def set_current_index(self, index):
        self.setCurrentIndex(index)
