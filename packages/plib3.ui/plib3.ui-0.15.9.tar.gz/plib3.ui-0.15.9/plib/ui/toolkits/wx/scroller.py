#!/usr/bin/env python3
"""
Module WX.SCROLLER -- Python wxWidgets Scroller Objects
Sub-Package UI.TOOLKITS.WX of Package PLIB3 -- Python GUI Toolkits
Copyright (C) 2008-2022 by Peter A. Donis

Released under the GNU General Public License, Version 2
See the LICENSE and README files for more information

This module contains the wxWidgets UI objects for the panel widgets.
"""

import wx

from plib.ui.base.scroller import PScrollerBase, PScrollingWrapperBase

from .app import PWxWidget


class PWxScrollerBase(PWxWidget, wx.ScrolledWindow):
    
    def __init__(self, parent):
        wx.ScrolledWindow.__init__(self, parent)
        self._sizer = wx.BoxSizer(wx.VERTICAL)
        self.SetScrollRate(20, 20)
    
    def set_child(self, child):
        # Note: child widget must already have been constructed with self as parent,
        # so in wx we can never pass a child widget to the PScroller constructor
        # TODO: is there a way to fix this?
        self._sizer.Add(child, 1, wx.EXPAND, 0)
        self.SetSizer(self._sizer)


class PScroller(PWxScrollerBase, PScrollerBase):
    
    def __init__(self, manager, parent, child=None):
        PWxScrollerBase.__init__(self, parent)
        PScrollerBase.__init__(self, manager, parent, child)


class PScrollingWrapper(PWxScrollerBase, PScrollingWrapperBase):
    
    def __init__(self, manager, parent, child_spec):
        PWxScrollerBase.__init__(self, parent)
        PScrollingWrapperBase.__init__(self, manager, parent, child_spec)
    
    @property
    def spec_parent(self):
        return self  # since there's no other way to have us scroll the child window
    
    # get_layout and setup_layout are not used in wx
