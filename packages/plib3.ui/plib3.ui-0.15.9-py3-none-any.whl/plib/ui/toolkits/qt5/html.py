#!/usr/bin/env python3
"""
Module QT5.HTML -- Python Qt 5 Html Display Widgets
Sub-Package UI.TOOLKITS.QT5 of Package PLIB3 -- Python UI Toolkits
Copyright (C) 2008-2024 by Peter A. Donis

Released under the GNU General Public License, Version 2
See the LICENSE and README files for more information

This module contains the Qt 5 UI objects for text display widgets.
"""

from PyQt5 import QtWidgets as qt

from plib.ui.base.html import PHtmlDisplayBase

from .app import PQtWidgetMeta, PQtWidgetBase


class PHtmlDisplay(qt.QTextEdit, PQtWidgetBase, PHtmlDisplayBase,
                   metaclass=PQtWidgetMeta):
    
    fix_width_on_resize = True
    fix_height_on_resize = True
    
    widget_class = qt.QTextEdit
    
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
