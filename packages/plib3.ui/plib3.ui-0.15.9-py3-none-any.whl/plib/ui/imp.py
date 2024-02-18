#!/usr/bin/env python3
"""
Module IMP -- Toolkit Import Support
Sub-Package UI of Package PLIB3 -- Python UI Framework
Copyright (C) 2008-2022 by Peter A. Donis

Released under the GNU General Public License, Version 2
See the LICENSE and README files for more information

Defines support functions for importing toolkit objects.
"""

from plib.stdlib.imp import import_from_module

from plib.ui.toolkits import get_toolkit


# Toolkit-aware object retrieval function

def get_toolkit_object(modname, name):
    if ("." not in modname) and (modname != '__main__'):
        toolkit = get_toolkit()
        modname = "plib.ui.toolkits.{}.{}".format(toolkit, modname)
    return import_from_module(modname, name)
