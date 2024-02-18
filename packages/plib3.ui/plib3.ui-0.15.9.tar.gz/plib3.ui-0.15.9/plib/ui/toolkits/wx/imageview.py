#!/usr/bin/env python3
"""
Module WX.IMAGEVIEW -- Python wxWidgets Image View Widgets
Sub-Package UI.TOOLKITS.WX of Package PLIB3 -- Python GUI Toolkits
Copyright (C) 2008-2022 by Peter A. Donis

Released under the GNU General Public License, Version 2
See the LICENSE and README files for more information

This module contains the wxWidgets UI objects for image view widgets.
"""

import wx
from wx.lib import statbmp

from plib.ui.defs import *
from plib.ui.base.imageview import PImageViewBase

from .app import PWxWidget


WX_IMAGE_FORMATS = [
    "bmp",
    "png",
    "jpg",
    "jpeg",
    "gif",
    "pcx",
    "pnm",
    "tif",
    "tiff",
    "tga",
    "iff",
    "xpm",
    "ico",
    "cur",
    "ani",
]


class PImageView(PWxWidget, wx.ScrolledCanvas, PImageViewBase):
    
    _align = False  # used by panel to determine placement
    
    child = None
    
    def __init__(self, manager, parent, filename=None, geometry=None):
        wx.ScrolledCanvas.__init__(self, parent)
        PImageViewBase.__init__(self, manager, parent, filename=filename, geometry=geometry)
    
    @staticmethod
    def supported_formats():
        # TODO: is there a way to query wx for this?
        return sorted(WX_IMAGE_FORMATS)
    
    def load_from_file(self, filename):
        bitmap = wx.Bitmap(filename)
        self.child = statbmp.GenStaticBitmap(self, -1, bitmap)
        self.size_to_image()
    
    def get_image_and_size(self):
        bitmap = self.child.GetBitmap()
        return bitmap, bitmap.GetWidth(), bitmap.GetHeight()
    
    def get_image_size(self):
        return self.get_image_and_size()[1:]
    
    def size_to_image(self, width=None, height=None):
        if (width is None) or (height is None):
            w, h = self.get_image_size()
            width = w if width is None else width
            height = h if height is None else height
        self.SetScrollbars(20, 20, width // 20, height // 20)
    
    def zoom_to(self, width, height):
        bitmap, w, h = self.get_image_and_size()
        wfactor, hfactor = (width / w), (height / h)
        if wfactor < hfactor:
            height = round(h * wfactor)
        elif hfactor < wfactor:
            width = round(w * hfactor)
        image = bitmap.ConvertToImage()
        image.Rescale(width, height)
        self.child.SetBitmap(image.ConvertToBitmap())
        self.size_to_image(width, height)
    
    def rotate_90(self, clockwise):
        bitmap = self.child.GetBitmap()
        image = bitmap.ConvertToImage()
        self.child.SetBitmap(image.Rotate90(clockwise).ConvertToBitmap())
        self.size_to_image()
