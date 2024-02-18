#!/usr/bin/env python3
"""
Sub-Package UI.WIDGETS of Package PLIB3 -- Python UI Framework
Copyright (C) 2008-2022 by Peter A. Donis

Released under the GNU General Public License, Version 2
See the LICENSE and README files for more information
"""

from plib.stdlib.classtools import recurselist

from plib.ui.defs import *
from plib.ui.imp import get_toolkit_object
from plib.ui.common import action_name


# Helper function to find and connect signals to handlers

def setup_signal_handlers(manager, obj, name,
                          event_map=WIDGET_EVENT_MAP):
    
    for signal in recurselist(type(obj), 'signals'):
        event = event_map[signal]
        method = "on_{}_{}".format(name, event) if event else "on_{}".format(name)
        target = getattr(manager, method, None)
        if target:
            obj.setup_notify(signal, target)


# Basic widget construction function; this will end up getting called
# for each widget spec with the obvious arguments. The widget will
# automagically find its event handlers on the manager when it is constructed

def widget_from_spec(manager, parent, spec,
                     attr_prefixes=WIDGET_ATTR_PREFIXES, auto_prefixes=WIDGET_AUTO_PREFIXES):
    
    # We do the test of the spec this way to avoid having to import
    # the module with PWidgetManager in it; this avoids circular imports
    # and also avoids having to import that code if it is not used
    if isinstance(spec, tuple):
        widget_manager_klass = None
        widget_manager = manager
    else:  # assume it's a subclass of PWidgetManager
        widget_manager_klass = spec
        widget_manager = widget_manager_klass(manager)
        setattr(manager, widget_manager.attrname, widget_manager)
        # This must be a tuple (no point in it being another PWidgetManager subclass)
        spec = widget_manager.main_widget
    
    modname, klassname, name, args, kwargs = spec
    klass = get_toolkit_object(modname, klassname)
    attrname = (
        name
        if any(name.startswith(prefix) for prefix in auto_prefixes) else
        "{}_{}".format(attr_prefixes.get(klassname, modname), name)
    )
    widget = klass(widget_manager, parent, *args, **kwargs)
    setattr(widget_manager, attrname, widget)
    setup_signal_handlers(widget_manager, widget, name)
    return widget


# Helper function for widgets that can have contents as list of specs

def widgets_from_contents(manager, parent, contents, callback=None):
    widgets = []
    for spec in contents:
        widget = widget_from_spec(manager, parent, spec)
        if callback:
            callback(widget)
        widgets.append(widget)
    return widgets


# Widget spec convenience functions

def auto_name(prefix, num):
    prefix = '{}_'.format(prefix)
    num[0] += 1
    return '{}{}'.format(prefix, num[0])


## Widget spec functions ##


# Buttons have a caption and optional icon
# Buttons fire SIGNAL_CLICKED

def button(name, caption, icon=None, font=None):
    args = (caption,)
    kwargs = dict(
        icon=icon,
        geometry=(None, None, BUTTON_WIDTH, None),
        font=font,
    )
    return ('button', 'PButton', name, args, kwargs)


# Action buttons take their caption and icon from a menu/toolbar action
# Action buttons fire SIGNAL_ACTIVATED when clicked

def action_button(action, font=None):
    name = action_name(action)
    args = (action,)
    kwargs = dict(
        geometry=(None, None, BUTTON_WIDTH, None),
        font=font,
    )
    return ('button', 'PActionButton', name, args, kwargs)


# Button groups are groups of toggle or radio buttons that are mutually exclusive
# Button groups fire SIGNAL_BUTTONSELECTED when the selected button is changed

def base_buttongroup(klassname, name, align, layout, items=None, value=None, starting_index=None, font=None):
    args = (align, layout, items)
    kwargs = dict(starting_index=starting_index, font=font)
    return ('group', klassname, name, args, kwargs)


def buttongroup(name, align, layout, items=None, value=None, starting_index=None, font=None):
    return base_buttongroup('PButtonGroup', name, align, layout, items, value, starting_index, font)


def radiogroup(name, align, layout, items=None, value=None, starting_index=None, font=None):
    return base_buttongroup('PRadioGroup', name, align, layout, items, value, starting_index, font)


# Check boxes have a label and checked state
# Check boxes fire SIGNAL_TOGGLED

def checkbox(name, label, checked=None, font=None):
    args = (label, checked)
    kwargs = dict(
        font=font,
    )
    return ('button', 'PCheckBox', name, args, kwargs)


def base_combo(klassname, name, items, value, **kwds):
    args = (items,)
    kwargs = dict(
        value=value,
    )
    kwargs.update(kwds)
    return ('combo', klassname, name, args, kwargs)


# Combo boxes have a string value and a drop-down list of choices
# Combo boxes fire SIGNAL_SELECTED

def combo(name, items=None, value=None, geometry=None, font=None):
    return base_combo('PComboBox', name, items, value, geometry=geometry, font=font)


# Numeric combo boxes present their values as ints instead of string

def num_combo(name, items=None, value=None, geometry=None, font=None):
    return base_combo('PNumComboBox', name, items, value, geometry=geometry, font=font)


# Sorted combo boxes sort their strings in the drop-down list

def sorted_combo(name, items, value=None, key=None, geometry=None, font=None):
    return base_combo('PSortedComboBox', name, items, value, geometry=geometry, font=font, key=key)


def base_edit(klassname, name, value, geometry, font, expand=True):
    args = (value,)
    kwargs = dict(
        geometry=geometry,
        font=font,
        expand=expand,
    )
    return ('editctrl', klassname, name, args, kwargs)


# Edit boxes are single-line string editors and can be initialized with a value;
# they default to automatically expanding horizontally to fill available space
# Edit boxes fire: SIGNAL_EDITCHANGED when their content is changed
#                  SIGNAL_ENTER when Enter is pressed (normally used to trigger an action)

def edit(name, text="", geometry=None, font=None, expand=True):
    #geometry = geometry or (None, None, EDIT_WIDTH, None)
    return base_edit('PEditBox', name, text, geometry, font, expand=expand)


# Numeric edit boxes present their value as an int instead of a string

def num_edit(name, value=0, geometry=None, font=None, expand=True):
    #geometry = geometry or (None, None, NUM_EDIT_WIDTH, None)
    return base_edit('PNumEditBox', name, value, geometry, font, expand=expand)


# Group boxes organize child controls; they automatically expand to
# fill available space; contents must be an iterable of widget specs

def groupbox(caption, contents, name=None, font=None,
             num=[0]):
    
    name = name or auto_name('groupbox', num)
    args = (caption,)
    kwargs = dict(
        contents=contents,
        margin=TAB_MARGIN,
        spacing=PANEL_SPACING,
        font=font,
    )
    return ('groupbox', 'PGroupBox', name, args, kwargs)


# A label displays its caption string

def label(name, caption, geometry=None, font=None):
    #geometry = geometry or (None, None, LABEL_WIDTH, None)
    args = (caption,)
    kwargs = dict(
        geometry=geometry,
        font=font,
    )
    return ('label', 'PTextLabel', name, args, kwargs)


def base_listbox(klassname, name, items, value, **kwargs):
    args = (items, value)
    return ('listbox', klassname, name, args, kwargs)


# List boxes display a list of strings
# List boxes fire SIGNAL_LISTBOXSELECTED

def listbox(name, items=None, value=None, geometry=None, font=None):
    #geometry = geometry or (None, None, LIST_WIDTH, LIST_HEIGHT)
    return base_listbox('PListBox', name, items, value, geometry=geometry, font=font)


# Sorted list boxes sort their displayed list of strings

def sorted_listbox(name, items=None, value=None, key=None, geometry=None, font=None):
    #geometry = geometry or (None, None, LIST_WIDTH, LIST_HEIGHT)
    return base_listbox('PSortedListBox', name, items, value, key=key, geometry=geometry, font=font)


def base_listview(klassname, name, labels, **kwds):
    kwargs = dict(
        labels=labels,
    )
    kwargs.update(kwds)
    return ('listview', klassname, name, (), kwargs)


# List views display rows each with one or more columns of strings, plus a header;
# they automatically expand to fill available space
# List views appear in code as sequences of tuples of strings
# List views fire SIGNAL_LISTVIEWSELECTED

def listview(name, labels=None, data=None, font=None, header_font=None):
    return base_listview('PListView', name, labels=labels, data=data,
                         font=font, header_font=header_font)


# Sorted list views sort their displayed rows, treating each row as a tuple of strings

def sorted_listview(name, labels=None, data=None, key=None, font=None, header_font=None):
    return base_listview('PSortedListView', name, labels=labels, data=data, key=key,
                         font=font, header_font=header_font)


# Tree views display a tree of items, each with one or more columns of strings, plus a header;
# they automatically expand to fill available space
# Tree views appear in code as sequences of 2-tuples (cols, children), where cols is a tuple
# of strings and children is another sequence of 2-tuples (cols, children)
# Tree views fire SIGNAL_LISTVIEWSELECTED

def treeview(name, labels=None, data=None, auto_expand=False, font=None, header_font=None):
    return base_listview('PTreeView', name, labels=labels, data=data, auto_expand=auto_expand,
                         font=font, header_font=header_font)


# Edit controls (memos) are multi-line scrolling plain text editors;
# they automatically expand to fill available space
# Edit controls fire: SIGNAL_TEXTCHANGED when their text is changed
#                     SIGNAL_TEXTSTATECHANGED when their text selection state is changed

def memo(name, scrolling=True, font=None):
    kwargs = dict(
        scrolling=scrolling,
        font=font,
    )
    return ('editctrl', 'PEditControl', name, (), kwargs)


# Padding is a blank panel that automatically expands to fill available space;
# it can be used to help align other widgets in layouts

def padding(name=None,
            num=[0]):
    
    name = name or auto_name('padding', num)
    return ('form', 'PPanel', name, (), {})


# The contents for all panels must be an iterable of widget specs

def base_panel(align, layout, contents, style=PANEL_PLAIN, margin=-1, spacing=-1, name=None,
               num=[0]):
    
    name = name or auto_name('panel', num)
    args = (align, layout)
    kwargs = dict(
        contents=contents,
        style=style,
        margin=margin,
        spacing=spacing,
    )
    return ('form', 'PPanel', name, args, kwargs)


# Frames are top-level layouts typically used as the main widget in an application to
# organize the layout of multiple sub-widgets; they automatically expand to fill
# available space

def frame(align, layout, contents, style=PANEL_PLAIN, name=None):
    return base_panel(align, layout, contents, style=style, margin=FRAME_MARGIN, spacing=PANEL_SPACING, name=name)


# Panels are layout widgets typically used as sub-widgets to frames in complex
# layouts; they automatically expand to fill available space

def panel(align, layout, contents, style=PANEL_PLAIN, name=None):
    return base_panel(align, layout, contents, style=style, margin=PANEL_MARGIN, spacing=PANEL_SPACING, name=name)


# Tabs are panels specialized to organize multiple widgets in a tab widget's tab;
# they automatically expand to fill available space

def tab(align, layout, contents, style=PANEL_PLAIN, name=None):
    return base_panel(align, layout, contents, style=style, margin=TAB_MARGIN, spacing=PANEL_SPACING, name=name)


# Boxes are simple containers typically used at the bottom level of layouts;
# they automatically expand to fill available space

def box(align, layout, contents, style=PANEL_PLAIN, name=None):
    return base_panel(align, layout, contents, style=style, margin=BOX_MARGIN, spacing=PANEL_SPACING, name=name)


# Tables are grid-style widgets with multiple rows and columns plus a header;
# they automatically expand to fill available space

def table(name, labels=None, data=None, font=None, header_font=None):
    kwargs = dict(
        labels=labels,
        data=data,
        font=font,
        header_font=header_font,
    )
    return ('table', 'PTable', name, (), kwargs)


# Tab widgets organize complex layouts in multiple tabs; they automatically expand
# to fill available space; tabs must be an iterable of widget specs

def tabwidget(name, tabs, font=None):
    kwargs = dict(
        tabs=tabs,
        font=font,
    )
    return ('tabwidget', 'PTabWidget', name, (), kwargs)


# Page widgets organize complex layouts in multiple pages; they automatically expand
# to fill available space; pages must be an iterable of widget specs; link_to gives
# the name of another widget that will be used to select the current page

def pagewidget(name, pages, link_to=None):
    kwargs = dict(
        pages=pages,
        link_to=link_to,
    )
    return ('pagewidget', 'PPageWidget', name, (), kwargs)


# Text displays are scrolling widgets that show multiple lines of plain text;
# they automatically expand to fill available space

def text(name, text="", scrolling=True, font=None):
    args = (text,)
    kwargs = dict(
        scrolling=scrolling,
        font=font,
    )
    return ('display', 'PTextDisplay', name, args, kwargs)


# Html displays are scrolling widgets that show html; they automatically
# expand to fill available space

def html(name, html="", scrolling=True, font=None):
    args = (html,)
    kwargs = dict(
        scrolling=scrolling,
        font=font,
    )
    return ('html', 'PHtmlDisplay', name, args, kwargs)


# The scrolling wrapper puts a scrolling window over a child widget
# specified by child_spec

def scrolling(child_spec):
    name = child_spec[2]
    args = (child_spec,)
    kwargs = dict()
    return ('scroller', 'PScrollingWrapper', name, args, kwargs)


# Containers are wrappers around widgets that are not directly supported
# by PLIB.UI; the add_child method is used to add the custom widget as
# a single child widget of the container

def container(name):
    return ('container', 'PContainer', name, (), {})


# Convenience function for labeled controls

def labeled(caption, control, layout=LAYOUT_VERTICAL, align=ALIGN_JUST, label_bold=True, label_font=None):
    name = control[2]  # control will be a widget spec tuple
    label_align = (ALIGN_TOP if layout == LAYOUT_VERTICAL else ALIGN_LEFT)
    label_name = '{}_label'.format(name)
    labelbox_name = '{}_labelbox'.format(name)
    box_name = '{}_box'.format(name)
    return box(align, layout, [
        box(label_align, LAYOUT_HORIZONTAL, [
            # Label name will be prefixed by 'label' in widget_from_spec
            label(label_name, caption, font=(label_font, None, label_bold)),
        ], name=labelbox_name),
        control
    ], name=box_name)

# Label boxes work like group boxes but allow a bold label without making
# every widget in the box bold also

def labelbox(caption, contents, layout=LAYOUT_VERTICAL, align=ALIGN_JUST, style=PANEL_PLAIN, label_bold=True, label_font=None, name=None,
             num=[0]):
    
    name = name or auto_name('labelbox', num)
    label_name = '{}_label'.format(name)
    box_name = '{}_box'.format(name)
    panel_name = '{}_panel'.format(name)
    contents = panel(ALIGN_JUST, layout, contents, style=style, name=panel_name)
    return box(align, LAYOUT_VERTICAL, [
        label(label_name, caption, font=(label_font, None, label_bold)),
        contents
    ], name=box_name)
