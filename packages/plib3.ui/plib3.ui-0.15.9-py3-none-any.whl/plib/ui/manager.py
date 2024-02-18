#!/usr/bin/env python3
"""
Module MANAGER -- UI Widget Manager
Sub-Package UI of Package PLIB3 -- Python UI Framework
Copyright (C) 2008-2022 by Peter A. Donis

Released under the GNU General Public License, Version 2
See the LICENSE and README files for more information
"""

from plib.ui.base.app import PManagerBase


class PWidgetManager(PManagerBase):
    
    name = None
    
    main_widget = None
    
    def __init__(self, manager):
        PManagerBase.__init__(self)
        self.manager = manager
        manager.sub_managers.append(self)
    
    @property
    def manager_type(self):
        return type(self).__name__.lower()
    
    @property
    def attrname(self,
                 fmt="{}_{}".format):
        
        return fmt(self.manager_type, self.name)
