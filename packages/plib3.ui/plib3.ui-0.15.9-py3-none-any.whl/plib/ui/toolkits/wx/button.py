#!/usr/bin/env python3
"""
Module WX.BUTTON -- Python wxWidgets Button Widgets
Sub-Package UI.TOOLKITS.WX of Package PLIB3 -- Python GUI Toolkits
Copyright (C) 2008-2022 by Peter A. Donis

Released under the GNU General Public License, Version 2
See the LICENSE and README files for more information

This module contains the wxWidgets UI objects for button widgets.
"""

import wx
#import wx.lib.buttons

from plib.ui.defs import *
from plib.ui.base.button import PButtonBase, PActionButtonBase, PCheckBoxBase

from .app import PWxWidget, PWxActionMixin, scaled_bitmap


class PWxButtonMixin(PWxWidget):
    
    fn_get_caption = 'GetLabel'
    fn_set_caption = 'SetLabel'
    
    _align = False  # used by panel to determine placement
    
    iconfactor = 0.5
    
    def set_icon_obj(self, icon):
        # FIXME: why the fsck*&^%$#@! doesn't this work???
        self.SetBitmap(scaled_bitmap(icon, self.iconfactor))


class PWxButtonBase(PWxActionMixin, PWxButtonMixin, wx.Button):
    
    def __init__(self, parent, _id):
        wx.Button.__init__(self, parent, _id)


class PButton(PWxButtonBase, PButtonBase):
    
    def __init__(self, manager, parent, caption, icon=None,
                 geometry=None, font=None):
        
        PWxButtonBase.__init__(self, parent, wx.ID_ANY)
        PButtonBase.__init__(self, manager, parent, caption, icon,
                             geometry=geometry, font=font)


class PActionButton(PWxButtonBase, PActionButtonBase):
    
    def __init__(self, manager, parent, action,
                 geometry=None, font=None):
        
        PWxButtonBase.__init__(self, parent, wx.ID_ANY)
        PActionButtonBase.__init__(self, manager, parent, action,
                                   geometry=geometry, font=font)


class PCheckBox(PWxButtonMixin, wx.CheckBox, PCheckBoxBase):
    
    fn_get_checked = 'GetValue'
    fn_set_checked = 'SetValue'
    
    def __init__(self, manager, parent, label, checked=None,
                 geometry=None, font=None, tristate=False):
        
        if tristate:
            style = wx.CHK_3STATE
        else:
            style = wx.CHK_2STATE
        wx.CheckBox.__init__(self, parent, style=style)
        PCheckBoxBase.__init__(self, manager, parent, label, checked=checked,
                               geometry=geometry, font=font, tristate=tristate)
    
    def make_tristate(self):
        # This is done in the constructor in wxWidgets
        pass
