#!/usr/bin/env python3
"""
Module CUSTOM -- Support for Custom Signals and Widgets
Sub-Package UI of Package PLIB3 -- Python UI Framework
Copyright (C) 2008-2022 by Peter A. Donis

Released under the GNU General Public License, Version 2
See the LICENSE and README files for more information

Defines the API for adding custom signals and widgets.
"""

import sys


def set_toolkit(toolkit, err_msg=None, err_exit=True):
    from plib.ui import toolkits
    try:
        toolkits.set_toolkit(toolkit)
    except toolkits.ToolkitError:
        if err_msg:
            print(err_msg)
        if err_exit:
            sys.exit(1)
        raise


def add_signals(**kwargs):
    from plib.ui import defs
    from plib.ui import imp
    
    constants = {}
    handlers = {}
    custom_specs = []
    
    for name, specs in kwargs.items():
        signame = name.upper()
        assert signame.startswith("SIGNAL_")
        value, handler_name, *args = specs
        if isinstance(value, tuple):
            vname, offset = value
            value = getattr(defs, vname) + offset
        constants[signame] = value
        handlers[value] = handler_name
        custom_specs.append((signame,) + tuple(args))
    
    defs.add_constants(**constants)
    defs.add_handlers(handlers)
    
    # Have to do this after defs is updated above so custom signals get imported
    add_custom_signal = imp.get_toolkit_object('app', 'add_custom_signal')
    
    # Args are the types of arguments to be sent to the event handler
    # (Note: some toolkits ignore these)
    for args in custom_specs:
        add_custom_signal(*args)


def add_widget_prefixes(**kwargs):
    from plib.ui import defs
    
    defs.add_widget_prefixes(**kwargs)


def add_auto_prefixes(*args):
    from plib.ui import defs
    
    defs.add_auto_prefixes(args)


def add_action(key, name, caption, description, icon):
    from plib.ui import common
    if key in common.action_map:
        raise RuntimeError("Key {} is already in use".format(key))
    common.action_map[key] = [name, caption, description, icon]


def modify_action(key, name=None, caption=None, description=None, icon=None):
    from plib.ui import common
    entry = common.action_map.get(key)
    if not entry:
        raise RuntimeError("Invalid action key: {}".format(key))
    items = (name, caption, description, icon)
    add_index = len(entry)
    for index, item in enumerate(items[:add_index]):
        if item:
            entry[index] = item
    add_items = items[add_index:]
    if add_items:
        entry[add_index:] = add_items
