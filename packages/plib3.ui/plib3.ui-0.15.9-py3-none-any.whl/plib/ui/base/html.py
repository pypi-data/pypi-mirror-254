#!/usr/bin/env python3
"""
Module HTML -- UI Html Display Widgets
Sub-Package UI.BASE of Package PLIB3 -- Python UI Framework
Copyright (C) 2008-2022 by Peter A. Donis

Released under the GNU General Public License, Version 2
See the LICENSE and README files for more information
"""

from .app import PWidgetBase


class PHtmlDisplayBase(PWidgetBase):
    """Base class for widget that displays html.
    """
    
    def __init__(self, manager, parent, html="",
                 scrolling=False, font=None):
        
        PWidgetBase.__init__(self, manager, parent,
                             font=font)
        self.setup_scrolling(scrolling)
        self.set_html(html)
    
    def setup_scrolling(self, scrolling):
        """Placeholder for derived classes to implement.
        """
        raise NotImplementedError
    
    def get_html(self):
        """Placeholder for derived classes to implement.
        """
        raise NotImplementedError
    
    def set_html(self, value):
        """Placeholder for derived classes to implement.
        """
        raise NotImplementedError
    
    def clear_html(self):
        # This can be overridden in toolkits
        self.set_html("")
