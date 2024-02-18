#!/usr/bin/env python3
"""
Module WX.HTML -- Python wxWidgets Html Display Widgets
Sub-Package UI.TOOLKITS.WX of Package PLIB3 -- Python GUI Toolkits
Copyright (C) 2008-2024 by Peter A. Donis

Released under the GNU General Public License, Version 2
See the LICENSE and README files for more information

This module contains the wxWidgets UI objects for text display widgets.
"""

import wx
import wx.html

from plib.ui.defs import *
from plib.ui.base.html import PHtmlDisplayBase

from .app import PWxWidget, ec_scroll_style


class PHtmlDisplay(PWxWidget, wx.html.HtmlWindow, PHtmlDisplayBase):
    
    _style = wx.html.HW_SCROLLBAR_AUTO
    
    _align = True  # used by panel to determine placement
    _expand = True
    
    def __init__(self, manager, parent, html=None,
                 scrolling=False, font=None):
        
        if scrolling:
            self._style = self._style | ec_scroll_style
        wx.html.HtmlWindow.__init__(self, parent, style=self._style)
        self._html = ""  # hack because wx gives no way of retrieving the html from the widget
        PHtmlDisplayBase.__init__(self, manager, parent, html,
                                  scrolling=scrolling, font=font)
    
    def setup_scrolling(self, scrolling):
        pass  # this must be done in the constructor in wxWidgets
    
    def get_html(self):
        return self._html
    
    def set_html(self, value):
        self._html = value
        self.SetPage(value)
