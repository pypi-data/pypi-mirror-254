#!/usr/bin/env python3
"""
Module PYSIDE2.HTML -- Python PySide 2 Html Display Widgets
Sub-Package UI.TOOLKITS.PYSIDE2 of Package PLIB3 -- Python UI Toolkits
Copyright (C) 2008-2024 by Peter A. Donis

Released under the GNU General Public License, Version 2
See the LICENSE and README files for more information

This module contains the PySide 2 UI objects for text display widgets.
"""

from PySide2 import QtWidgets as qt

from plib.ui.base.html import PHtmlDisplayBase

from .app import PQtWidget


class PHtmlDisplay(PQtWidget, qt.QTextEdit, PHtmlDisplayBase):
    
    fix_width_on_resize = True
    fix_height_on_resize = True
    
    def __init__(self, manager, parent, html=None,
                 scrolling=False, font=None):
        
        qt.QTextEdit.__init__(self, parent)
        self.setReadOnly(True)
        self.setSizePolicy(qt.QSizePolicy.MinimumExpanding, qt.QSizePolicy.MinimumExpanding)
        PHtmlDisplayBase.__init__(self, manager, parent, html, scrolling=scrolling, font=font)
    
    def setup_scrolling(self, scrolling):
        if scrolling:
            self.setLineWrapMode(qt.QTextEdit.NoWrap)
    
    def get_html(self):
        return self.html()
    
    def set_html(self, html):
        self.setHtml(html)
