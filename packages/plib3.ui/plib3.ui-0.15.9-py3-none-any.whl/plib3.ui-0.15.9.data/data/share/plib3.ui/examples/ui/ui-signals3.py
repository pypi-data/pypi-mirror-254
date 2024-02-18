#!/usr/bin/env python3
"""
UI-SIGNALS.PY
Copyright (C) 2008-2022 by Peter A. Donis

Released under the GNU General Public License, Version 2
See the LICENSE and README files for more information

A demo app that tests all of the available UI signals.
It also demonstrates how to construct a user interface
dynamically based on information at run time, instead
of having everything pre-defined.
"""

import sys
import os
import functools

from plib.stdlib.builtins import first


# Must do this before any other plib.ui imports or action
# (Note that we don't set a specific toolkit here, but apps
# that want to do that must do it in this section)

from plib.ui import custom

custom.add_signals(
    SIGNAL_CUSTOM1=(('SIGNAL_FINISHED', 50), 'custom1'),
    SIGNAL_CUSTOM2=(('SIGNAL_FINISHED', 51), 'custom2'),
    SIGNAL_EMITTED=(('SIGNAL_FINISHED', 60), 'emitted', int),
)

custom.add_widget_prefixes(
    ClickableLabel='label',
    CustomWidget='widget',
)


from plib.ui import __version__
from plib.ui.defs import *
from plib.ui.app import PApplication, PTextLabel, PMouseMixin
from plib.ui.common import set_italic
from plib.ui.dialogs import StringSelectDialog
from plib.ui.manager import PWidgetManager
from plib.ui.output import PTextOutput
from plib.ui.widgets import *


class MouseMixin(PMouseMixin):
    
    @property
    def event_signal(self):
        return self.signals[0]
    
    msg_signames = (
        'SIGNAL_LEFTCLICK',
        'SIGNAL_RIGHTCLICK',
        'SIGNAL_MIDDLECLICK',
        'SIGNAL_LEFTDBLCLICK',
        'SIGNAL_RIGHTDBLCLICK',
        'SIGNAL_MIDDLEDBLCLICK',
    )
    
    def setup_signals(self):
        super(MouseMixin, self).setup_signals()
        for signame in self.msg_signames:
            sig = getattr(sys.modules[__name__], signame)
            self.setup_notify(sig, functools.partial(self.on_mouse_signal, signame))
        self.setup_notify(SIGNAL_LEFTCLICK, self.on_left_click)
    
    def on_mouse_signal(self, signame):
        self.manager.app.output_message("From Page {}: {}".format(self.__class__.__name__, signame))
    
    def on_left_click(self):
        self.do_notify(self.event_signal, *self.event_args)


class ClickableLabel(MouseMixin, PTextLabel):
    
    signals = (
        SIGNAL_CLICKED,
    )
    
    event_args = ()


class CustomWidget(MouseMixin, PTextLabel):
    
    signals = (
        SIGNAL_EMITTED,
    )
    
    @property
    def event_args(self,
                   sto=[0]):
        
        num = sto[0]
        sto[0] += 1
        return (num,)


def clickable_label(name, caption, geometry=None, font=None):
    args = (caption,)
    kwargs = dict(
        geometry=geometry,
        font=font,
    )
    return ('__main__', 'ClickableLabel', name, args, kwargs)


def custom_widget(name, caption, geometry=None, font=None):
    args = (caption,)
    kwargs = dict(
        geometry=geometry,
        font=font,
    )
    return ('__main__', 'CustomWidget', name, args, kwargs)


def display_sub_objects(mgr, mgr_name='app'):
    print("Showing sub-objects for {}".format(mgr_name))
    for widget in mgr.all_widgets:
        name = first(attr for attr in dir(mgr) if getattr(mgr, attr) is widget)
        print("Widget: {}".format(name))
        assert getattr(mgr, name) is widget
    for manager in mgr.sub_managers:
        name = manager.attrname
        print("Manager: {}".format(name))
        assert getattr(mgr, name) is manager


number_strings = ("One", "Two", "Three", "Four", "Five", "Six")


class Page(PWidgetManager):
    
    name = 'manager'
    
    @property
    def main_widget(self):
        # We implement this as a property because we can't wait until before_create
        # to define the widget specs (as is done in the app below); the widget_from_spec
        # function gets called with this class and evaluates main_widget before any
        # widget creation starts. This will be true for any widget manager that is
        # used in the app's main_widget spec.
        return tab(ALIGN_JUST, LAYOUT_VERTICAL, [
            box(ALIGN_TOP, LAYOUT_VERTICAL, [
                clickable_label('labeltest', "Clickable Label Test"),
            ]),
            listbox('numbers', number_strings, font=self.app.font),
            box(ALIGN_BOTTOM, LAYOUT_HORIZONTAL, [
                button('custom1', "Custom Signal 1", font=self.app.font),
                button('custom2', "Custom Signal 2", font=self.app.font),
                padding(),
                button('input_str', "Input String", font=self.app.font),
                button('input_int', "Input Integer", font=self.app.font),
                padding(),
                custom_widget('custom3', "Custom Widget", font=self.app.font),
            ]),
        ])
    
    def setup_signals(self):
        # Normally should not need to override this method, we do it here only to show timing of method calls
        PWidgetManager.setup_signals(self)
        print("Page setup_signals")
        # TODO: can we automate this connection so the page knows when it is shown?
        self.app.panels.setup_notify(SIGNAL_TABSELECTED, self.on_page_selected)
        self.target_index = len(self.app.panels) - 1
    
    def after_create(self):
        display_sub_objects(self, self.attrname)
        print("Page after_create")
    
    showing = False  # since this page isn't displayed initially
    
    def on_page_selected(self, index):
        if index == self.target_index:
            self.populate_data()
    
    def populate_data(self):
        # Now the app's output_message function is set up
        self.app.output_message("Page populate_data")
    
    def on_numbers_selected(self, index):
        assert index == self.listbox_numbers.current_index()
        assert self.listbox_numbers[index] == self.listbox_numbers.current_text()
        self.app.output_message("From Page: SIGNAL_LISTBOXSELECTED {} {}".format(
            index, self.listbox_numbers.current_text()
        ))
    
    def on_labeltest_clicked(self):
        self.app.output_message("From Page ClickableLabel: SIGNAL_CLICKED")
    
    def on_custom1_clicked(self):
        print("custom1_clicked")
        self.app.do_notify(SIGNAL_CUSTOM1)
    
    def on_custom2_clicked(self):
        print("custom2_clicked")
        self.app.do_notify(SIGNAL_CUSTOM2)
    
    def on_input_str_clicked(self):
        value = self.app.message_box.enter_string("Enter String", "String value:")
        if value is not None:
            self.listbox_numbers.append(value)
    
    def on_input_int_clicked(self):
        value = self.app.message_box.enter_int("Enter Integer", "Integer value:")
        if value is not None:
            self.listbox_numbers.append(str(value))
    
    def on_custom3_emitted(self, num):
        self.app.output_message("From Page CustomWidget: SIGNAL_EMITTED {}".format(num))


PAGE_TABS = 0
PAGE_BUTTONS = 1
PAGE_COMBO = 2
PAGE_LIST = 3
PAGE_RADIO = 4
PAGE_DIALOG = 5


class PageSelectDialog(StringSelectDialog):
    
    @property
    def dialog_client(self):
        # This illustrates doing surgery on a widget spec (note that we can't do this in
        # before_create, even though this dialog is only constructed dynamically after the
        # app starts, because StringSelectDialog defines dialog_client as a property)
        client = super(PageSelectDialog, self).dialog_client
        client[4]['contents'][0][4]['contents'][0][4]['contents'].insert(0,
            label('message', "Current page: {}".format(self.manager.label_current_page.caption),
                  font=set_italic(self.app.font))
        )
        return client


class DialogButton(PWidgetManager):
    
    @property
    def font(self):
        f = self.app.font
        assert (not f) or (len(f) == 1)
        font_name = f[0] if f else None
        return (font_name, None, True)
    
    @property
    def main_widget(self):
        # We do this as a property for the same reason as the Page class above
        # (see comment there for further discussion)
        return panel(ALIGN_TOP, LAYOUT_HORIZONTAL, [
            label('current_page', "", font=self.font),
            button('change_page', "Change...", font=self.app.font),
        ])
    
    titles = None
    
    def setup_signals(self):
        # Normally should not need to override this method, we do it here only to show timing of method calls
        PWidgetManager.setup_signals(self)
        print("DialogButton setup_signals")
    
    def after_create(self):
        display_sub_objects(self, self.attrname)
        print("DialogButton after_create")
        self.label_current_page.caption = self.titles[0]
    
    def current_index(self):
        return self.titles.index(self.label_current_page.caption)
    
    def __getitem__(self, index):
        return self.titles[index]
    
    def page_change_callback(self, title):
        self.label_current_page.caption = title
        # TODO: can we make this signal connection automatic?
        self.manager.on_panels_selector_selected(self.current_index())
        self.manager.pagewidget_panels.set_current_index(self.current_index())
    
    def on_change_page_clicked(self):
        PageSelectDialog(self, "Select Page", self.titles, "Select the page to switch to:",
                         self.label_current_page.caption, self.page_change_callback,
                         font=self.app.font).run()


def dialogbutton(name, titles):
    DialogButton.name = name
    DialogButton.titles = titles
    return DialogButton


def horiz(group):
    def horiz_group(name, titles, font=None):
        return group(name, ALIGN_TOP, LAYOUT_HORIZONTAL, titles, starting_index=0, font=font)
    return horiz_group


def vert(group):
    def vert_group(name, titles, font=None):
        return group(name, ALIGN_LEFT, LAYOUT_VERTICAL, titles, starting_index=0, font=font)
    return vert_group


def listbox_panel(name, titles, font=None):
    return panel(ALIGN_JUST, LAYOUT_VERTICAL, [
        listbox(name, titles, font=font),
    ], name=name)


def panels(name, contents, app):
    sel = UISignalTester.page_select
    sel_layout = UISignalTester.select_layout
    if sel == PAGE_TABS:
        if sel_layout:
            print("Ignoring selector layout option, not usable with tab widget")
        return tabwidget(name, contents, font=app.font)
    
    selector_type, selector, default_panel_layout, selector_kwargs = (
        ('buttongroup', buttongroup, LAYOUT_VERTICAL, dict(font=app.font)) if sel == PAGE_BUTTONS else
        ('combo', combo, LAYOUT_VERTICAL, dict(font=app.font)) if sel == PAGE_COMBO else
        ('listbox', listbox_panel, LAYOUT_HORIZONTAL, dict(font=app.font)) if sel == PAGE_LIST else
        ('radiogroup', radiogroup, LAYOUT_VERTICAL, dict(font=app.font)) if sel == PAGE_RADIO else
        ('dialogbutton', dialogbutton, LAYOUT_VERTICAL, {}) if sel == PAGE_DIALOG else
        (None, None, None, None)
    )
    if (sel_layout == LAYOUT_VERTICAL) and (selector_type == 'combo'):
        raise RuntimeError("Cannot use combo box selector with vertical layout")
    if (sel_layout == LAYOUT_VERTICAL) and (selector_type == 'dialogbutton'):
        raise RuntimeError("Cannot use dialog button selector with vertical layout")
    if (sel_layout == LAYOUT_HORIZONTAL) and (selector_type == 'listbox'):
        raise RuntimeError("Cannot use list box selector with horizontal layout")
    assert selector is not None
    
    oriented, panel_layout = (
        (horiz, LAYOUT_VERTICAL) if sel_layout == LAYOUT_HORIZONTAL else
        (vert, LAYOUT_HORIZONTAL) if sel_layout == LAYOUT_VERTICAL else
        (None, None)
    )
    if panel_layout is None:
        panel_layout = default_panel_layout
    if selector_type in ('buttongroup', 'radiogroup'):
        if oriented is None:
            oriented = (
                horiz if panel_layout == LAYOUT_VERTICAL else
                vert if panel_layout == LAYOUT_HORIZONTAL else
                None
            )
            assert oriented is not None
        selector = oriented(selector)
    
    UISignalTester.selector_type = selector_type
    selector_name = '{}_selector'.format(name)
    frame_name = '{}_frame'.format(name)
    titles = [item[0] for item in contents]
    pages = [item[1] for item in contents]
    link_to = (
        '{}_{}'.format(selector_type, selector_name)
        if selector_type != 'dialogbutton' else
        None  # TODO: can we set up a selected signal for this case?
    )
    
    return panel(ALIGN_JUST, panel_layout, [
        selector(selector_name, titles, **selector_kwargs),
        pagewidget(name, pages, link_to=link_to),
    ], name=frame_name)


LONG_DESC = "List view item with long description to test horizontal scrolling behavior"


class UISignalTester(PApplication):
    
    signals = (
        SIGNAL_CUSTOM1,
        SIGNAL_CUSTOM2,
    )
    
    page_select = PAGE_TABS
    select_layout = None
    
    about_data = {
        'name': "UISignalTester",
        'version': "{} on Python {}".format(
            __version__,
            sys.version.split()[0]
        ),
        'description': "UI Signal Test Demo",
        'copyright': "Copyright (C) 2008-2022 by Peter A. Donis",
        'license': "GNU General Public License (GPL) Version 2",
        'developer': "Peter Donis",
        'website': "http://www.peterdonis.net"
    }
    
    about_format = "{name} {version}\n\n{description}\n\n{copyright}\n{license}\n\nDeveloped by {developer}\n{website}"
    
    main_title = "UI Signal Tester"
    
    main_size = SIZE_CLIENTWRAP
    main_placement = MOVE_CENTER
    
    font_name = None
    
    @property
    def font(self):
        return (self.font_name,) if self.font_name else None
    
    def before_create(self):
        # We can't call output_message here because widgets aren't available yet
        print("before_create")
        
        # We do this here so the panels function will see the options
        # filled in by option parsing. We could also do it as a property,
        # as is done in the Page and DialogButton classes above, but we
        # want to illustrate that it *can* be done in before_create for
        # the app. It could also be done in before_create for a widget
        # manager that is not referenced in the app's main_widget spec but
        # is only instantiated dynamically after the app starts.
        self.main_widget = frame(ALIGN_JUST, LAYOUT_HORIZONTAL, [
            panel(ALIGN_JUST, LAYOUT_VERTICAL, [
                panels('panels', [
                    ('Dialog', tab(ALIGN_JUST, LAYOUT_VERTICAL, [
                        button('action', "Test Clicked", font=self.font),
                        checkbox('option', "Test Toggled", font=self.font),
                        sorted_combo('selection', (numstr.lower() for numstr in number_strings), font=self.font),
                        edit('text', font=self.font),
                        num_edit('num', font=self.font),
                        sorted_listbox('list', ("Item {}".format(numstr) for numstr in number_strings), font=self.font),
                        buttongroup('colgrid', ALIGN_BOTTOM, (LAYOUT_COLGRID, 3),
                                    ("Button {}".format(numstr) for numstr in number_strings), font=self.font),
                        radiogroup('rowgrid', ALIGN_BOTTOM, (LAYOUT_ROWGRID, 3),
                                   ("Radio Button {}".format(numstr) for numstr in number_strings), font=self.font),
                    ])),
                    ('Memo', memo('notes', font=self.font)),
                    ('Tree', treeview('tree', [("Title", WIDTH_CONTENTS), ("Description", WIDTH_STRETCH)], (
                        (("Item {}".format(numstr), "Tree item {}".format(numstr.lower())), tuple(
                            (("Sub-item {} {}".format(numstr, substr), "Tree sub-item {} {}".format(numstr, substr)), ())
                            for substr in number_strings[:3]
                        ))
                        for numstr in number_strings
                    ), font=self.font, auto_expand=True)),
                    ('List', sorted_listview('items', [("Title", WIDTH_CONTENTS), ("Description", WIDTH_STRETCH)], (
                        ("Item {}".format(numstr), "List item {}".format(numstr.lower()))
                        for numstr in number_strings
                    ), font=self.font)),
                    ('Table', table('cells', [("Title", WIDTH_CONTENTS), ("Description", WIDTH_STRETCH)], (
                        ("Row {}".format(numstr), "Table row {}".format(numstr.lower()))
                        for numstr in number_strings
                    ), font=self.font)),
                    ('Scroller', scrolling(listbox('scroll_list', (
                        "{} {} {} - {}".format(a, b, c, LONG_DESC)
                        for a in number_strings for b in number_strings for c in number_strings
                    ), font=self.font))),
                    ('Page', Page),
                ], self),
                box(ALIGN_BOTTOM, LAYOUT_HORIZONTAL, [
                    padding(),
                    button('reset', "Reset Selector", font=self.font),
                ]),
            ]),
            text('output', font=self.font),
        ])
    
    def setup_signals(self):
        # Normally should not need to override this method, we do it here only to show timing of method calls
        PApplication.setup_signals(self)
        print("setup_signals")
    
    selector_type = None
    selector = None
    
    selector_sig_names = {
        'buttongroup': "BUTTON",
        'combo': "",
        'listbox': "LISTBOX",
        'radiogroup': "BUTTON",
        'dialogbutton': "",
    }
    
    selector_sig_name = None
    
    @property
    def panels(self):
        return getattr(self, '{}widget_panels'.format('tab' if self.page_select == PAGE_TABS else 'page'))
    
    def after_create(self):
        display_sub_objects(self)
        
        self.outputfile = PTextOutput(self.text_output)
        self.output_message("after_create")
        
        if self.page_select == PAGE_TABS:
            self.panel_title = (lambda index: self.tabwidget_panels[index][0])
        else:
            self.selector = selector = getattr(self, '{}_panels_selector'.format(self.selector_type))
            self.panel_title = (lambda index: selector[index])
            self.selector_sig_name = "SIGNAL_{}SELECTED".format(self.selector_sig_names[self.selector_type])
    
    def populate_data(self):
        self.output_message("populate_data")
    
    def output_message(self, message):
        print(message)
        self.outputfile.write("{}{}".format(message, os.linesep))
        self.outputfile.flush()
    
    def on_reset_clicked(self):
        self.output_message("SIGNAL_CLICKED")
        if self.selector is None:
            self.message_box.info("Information", "No reset available with tab widget.")
        elif isinstance(self.selector, DialogButton):
            self.message_box.info("Information", "No reset available with dialog button.")
        else:
            index = self.selector.current_index()
            titles = self.selector[:]
            self.selector.load_items(titles, starting_index=index)
    
    def focus_in(self, widget_name):
        self.output_message("SIGNAL_FOCUS_IN {}".format(widget_name))
    
    def focus_out(self, widget_name):
        self.output_message("SIGNAL_FOCUS_OUT {}".format(widget_name))
    
    def on_text_focus_in(self):
        self.focus_in('edit_text')
    
    def on_text_focus_out(self):
        self.focus_out('edit_text')
    
    def on_notes_focus_in(self):
        self.focus_in('memo_notes')
    
    def on_notes_focus_out(self):
        self.focus_out('memo_notes')
    
    def on_panels_selector_selected(self, index):
        assert self.selector.current_index() == index
        self.output_message("{} {}".format(self.selector_sig_name, index))
    
    def on_panels_selected(self, index):
        assert self.panels.current_index() == index
        self.output_message("SIGNAL_TABSELECTED {} {}".format(
            index, self.panel_title(index))
        )
    
    def on_action_clicked(self):
        self.output_message("SIGNAL_CLICKED")
    
    def on_option_toggled(self, checked):
        assert checked == self.checkbox_option.checked
        self.output_message("SIGNAL_TOGGLED {}".format(('off', 'on')[checked]))
    
    def on_selection_selected(self, index):
        assert self.combo_selection.current_index() == index
        assert self.combo_selection.current_text() == self.combo_selection[index]
        self.output_message("SIGNAL_SELECTED {} {}".format(
            index, self.combo_selection.current_text()
        ))
    
    def on_text_changed(self, text):
        assert text == self.edit_text.edit_text
        self.output_message("SIGNAL_EDITCHANGED {}".format(text))
    
    def on_text_enter(self):
        self.output_message("SIGNAL_ENTER")
    
    def on_num_changed(self, value):
        assert value == self.edit_num.edit_value
        self.output_message("SIGNAL_EDITCHANGED {}".format(value))
    
    def on_list_selected(self, index):
        assert index == self.listbox_list.current_index()
        assert self.listbox_list[index] == self.listbox_list.current_text()
        self.output_message("SIGNAL_LISTBOXSELECTED {} {}".format(
            index, self.listbox_list.current_text()
        ))
    
    def on_colgrid_selected(self, index):
        assert index == self.buttongroup_colgrid.current_index()
        assert self.buttongroup_colgrid[index] == self.buttongroup_colgrid.current_text()
        self.output_message("SIGNAL_SELECTED {} {}".format(
            index, self.buttongroup_colgrid.current_text()
        ))
    
    def on_rowgrid_selected(self, index):
        assert index == self.radiogroup_rowgrid.current_index()
        assert self.radiogroup_rowgrid[index] == self.radiogroup_rowgrid.current_text()
        self.output_message("SIGNAL_SELECTED {} {}".format(
            index, self.radiogroup_rowgrid.current_text()
        ))
    
    def on_notes_changed(self):
        self.output_message("SIGNAL_TEXTCHANGED {}".format(self.memo_notes.edit_text))
    
    def on_notes_mod_changed(self, changed):
        self.output_message("SIGNAL_TEXTMODCHANGED {} {}".format(self.memo_notes.edit_text, changed))
    
    def on_notes_state_changed(self):
        self.output_message("SIGNAL_TEXTSTATECHANGED memo_notes")
    
    def on_tree_selected(self, cols, children):
        assert (cols, children) == (self.treeview_tree.current_item().cols, self.treeview_tree.current_item().children)
        self.output_message("SIGNAL_LISTVIEWSELECTED {} ({}) {} {} {}".format(
            'treeview', " ".join(str(i) for i in self.treeview_tree.current_indexes()), len(children), *cols
        ))
    
    def on_items_selected(self, cols):
        assert cols == self.listview_items.current_item().cols
        assert cols == self.listview_items[self.listview_items.current_index()]
        self.output_message("SIGNAL_LISTVIEWSELECTED {} {} {} {}".format(
            'listview', self.listview_items.current_index(), *cols
        ))
    
    def on_cells_selected(self, curr_row, curr_col, prev_row, prev_col):
        assert self.table_cells.current_row() == curr_row
        assert self.table_cells.current_col() == curr_col
        assert self.table_cells.current_cell() == self.table_cells[curr_row][curr_col]
        self.output_message("SIGNAL_CELLSELECTED ({}, {}) -> ({}, {}) {}".format(
            str(prev_row), str(prev_col), str(curr_row), str(curr_col), self.table_cells.current_cell())
        )
    
    def on_cells_changed(self, row, col):
        assert self.table_cells.current_row() == row
        assert self.table_cells.current_col() == col
        assert self.table_cells.current_cell() == self.table_cells[row][col]
        self.output_message("SIGNAL_CELLCHANGED {} {} {}".format(
            str(row), str(col), self.table_cells.current_cell())
        )
    
    def on_scroll_list_selected(self, index):
        assert index == self.listbox_scroll_list.current_index()
        assert self.listbox_scroll_list[index] == self.listbox_scroll_list.current_text()
        self.output_message("SIGNAL_LISTBOXSELECTED {} {}".format(
            index, self.listbox_scroll_list.current_text()
        ))
    
    def on_app_custom1(self):
        self.output_message("SIGNAL_CUSTOM1")
    
    def on_app_custom2(self):
        self.output_message("SIGNAL_CUSTOM2")
    
    queryclose_handled = False
    
    def on_app_queryclose(self):
        self.queryclose_handled = True
        self.output_message("SIGNAL_QUERYCLOSE")
    
    def accept_close(self):
        print("SIGNAL_QUERYCLOSE handled:", self.queryclose_handled)
        return self.queryclose_handled
    
    def on_app_closing(self):
        self.output_message("SIGNAL_CLOSING")
    
    def on_app_shown(self):
        self.output_message("SIGNAL_SHOWN")
    
    def on_app_hidden(self):
        self.output_message("SIGNAL_HIDDEN")
    
    def before_quit(self):
        # We can't call output_message here because widgets might not be available
        # any more
        print("before_quit")


if __name__ == "__main__":
    from plib.stdlib.options import parse_options
    optlist = (
        ("-b", "--panel-buttons", {
            'action': "store_const", 'const': PAGE_BUTTONS,
           'dest': "page_select", 'default': PAGE_TABS,
            'help': "Use toggle buttons to select panels"
        }),
        ("-c", "--panel-combo", {
            'action': "store_const", 'const': PAGE_COMBO,
            'dest': "page_select", 'default': PAGE_TABS,
            'help': "Use combo box to select panels"
        }),
        ("-d", "--panel-dialog", {
            'action': "store_const", 'const': PAGE_DIALOG,
            'dest': "page_select", 'default': PAGE_TABS,
            'help': "Use dialog box to select panels"
        }),
        ("-f", "--font_name", {
            'action': "store",
            'dest': "font_name",
            'help': "Font name for widgets"
        }),
        ("-l", "--panel-list", {
            'action': "store_const", 'const': PAGE_LIST,
            'dest': "page_select", 'default': PAGE_TABS,
            'help': "Use list box to select panels"
        }),
        ("-r", "--panel-radio", {
            'action': "store_const", 'const': PAGE_RADIO,
            'dest': "page_select", 'default': PAGE_TABS,
            'help': "Use radio buttons to select panels"
        }),
        ("-t", "--panel-tabs", {
            'action': "store_const", 'const': PAGE_TABS,
            'dest': "page_select", 'default': PAGE_TABS,
            'help': "Use tab widget to select panels"
        }),
        ("-v", "--selector-vertical", {
            'action': "store_const", 'const': LAYOUT_VERTICAL,
            'dest': "select_layout", 'default': None,
            'help': "Orient panel selector vertically"
        }),
        ("-z", "--selector-horizontal", {
            'action': "store_const", 'const': LAYOUT_HORIZONTAL,
            'dest': "select_layout", 'default': None,
            'help': "Orient panel selector horizontally"
        }),
    )
    opts, args = parse_options(optlist)
    # The options object supports a dictionary interface,
    # making it easy to update class fields from it
    for opt, value in opts.items():
        setattr(UISignalTester, opt, value)
    UISignalTester().run()
