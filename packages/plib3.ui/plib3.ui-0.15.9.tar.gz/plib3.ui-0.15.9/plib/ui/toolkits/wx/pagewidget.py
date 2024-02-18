#!/usr/bin/env python3
"""
Module WX.TABWIDGET -- Python wxWidgets Tab Widget
Sub-Package UI.TOOLKITS.QT of Package PLIB3 -- Python GUI Toolkits
Copyright (C) 2008-2022 by Peter A. Donis

Released under the GNU General Public License, Version 2
See the LICENSE and README files for more information

This module contains the wxWidgets UI objects for the page widget.
"""

import wx

from plib.ui.defs import *
from plib.ui.base.pagewidget import PPageWidgetBase

from .app import PWxSequenceWidget


class PPageWidget(PWxSequenceWidget, wx.Simplebook, PPageWidgetBase):
    
    _align = True  # used by panel to determine placement
    _expand = True
    
    def __init__(self, manager, parent, pages=None, link_to=None):
        wx.Simplebook.__init__(self, parent)
        PPageWidgetBase.__init__(self, manager, parent, pages=pages, link_to=link_to)
    
    def page_count(self):
        return self.GetPageCount()
    
    def page_at(self, index):
        return self.GetPage(index)
    
    def add_page(self, index, widget):
        # Use empty labels since wx requires the label as a parameter
        if index == self.__len__():
            self.AddPage(widget, "")
        else:
            self.InsertPage(index, widget, "")
    
    def del_page(self, index):
        self.RemovePage(index)
    
    def current_index(self):
        return self.GetSelection()
    
    def set_current_index(self, index):
        self.SetSelection(index)
