#!/usr/bin/env python3
"""
Module PYSIDE2.SCROLLER -- Python PySide 2 Scroller Objects
Sub-Package UI.TOOLKITS.PYSIDE2 of Package PLIB3 -- Python UI Toolkits
Copyright (C) 2008-2022 by Peter A. Donis

Released under the GNU General Public License, Version 2
See the LICENSE and README files for more information

This module contains the PySide 2 UI objects for the panel widgets.
"""

from PySide2 import QtWidgets as qt

from plib.ui.base.scroller import PScrollerBase, PScrollingWrapperBase

from .app import PQtWidget


class PQtScrollerBase(PQtWidget, qt.QScrollArea):
    
    def __init__(self, parent):
        qt.QScrollArea.__init__(self, parent)
    
    def set_child(self, child):
        self.setWidget(child)


class PScroller(PQtScrollerBase, PScrollerBase):
    
    def __init__(self, manager, parent, child=None):
        PQtScrollerBase.__init__(self, parent)
        PScrollerBase.__init__(self, manager, parent, child)


class PScrollingWrapper(PQtScrollerBase, PScrollingWrapperBase):
    
    def __init__(self, manager, parent, child_spec):
        PQtScrollerBase.__init__(self, parent)
        self.setWidgetResizable(True)
        PScrollingWrapperBase.__init__(self, manager, parent, child_spec)
    
    def get_layout(self, child):
        # Intended for child to be a PPanel or subclass
        layout = getattr(child, '_playout', None)
        if layout is None:
            return None
        return layout
    
    def setup_layout(self, layout):
        layout.setSizeConstraint(layout.SetMinAndMaxSize)
