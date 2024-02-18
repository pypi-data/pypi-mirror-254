#!/usr/bin/env python3
"""
Module DIALOGS -- UI Dialog Runner and Standard Dialogs
Sub-Package UI of Package PLIB3 -- Python UI Framework
Copyright (C) 2008-2022 by Peter A. Donis

Released under the GNU General Public License, Version 2
See the LICENSE and README files for more information
"""

from plib.ui.app import PDialog
from plib.ui.base.app import PControllerBase
from plib.ui.common import set_bold
from plib.ui.widgets import *


class DialogRunner(PControllerBase):
    
    dialog_class = PDialog
    
    dialog_client = None
    
    def __init__(self, manager, caption, callback=None):
        PControllerBase.__init__(self)
        self.manager = manager
        self.caption = caption
        self.callback = callback
        
        self.dialog = None
    
    def create_widgets(self):
        self.dialog = self.dialog_class(self, self.app.main_window, self.caption, self.dialog_client)
    
    def run(self):
        self.do_create()
        self.dialog.setup_notify(SIGNAL_FINISHED, self.dialog_done)
        self.dialog.display()
    
    show_dialog = run  # syntactic sugar
    
    def dialog_done(self, accepted):
        if accepted and self.callback:
            self.callback(self.get_result())
        self.dialog = None
    
    def get_result(self):
        return None


class DisplayDialog(DialogRunner):
    
    def __init__(self, manager, caption, client=None):
        DialogRunner.__init__(self, manager, caption)
        if client:
            self.dialog_client = client


class StringSelectDialog(DialogRunner):
    
    def __init__(self, manager, caption, values, prompt=None, starting_value=None, callback=None, font=None):
        DialogRunner.__init__(self, manager, caption, callback)
        self.values = values
        self.prompt = prompt
        self.starting_value = starting_value
        self.font = font
        self.label_font = set_bold(font)
    
    @property
    def dialog_client(self):
        return frame(ALIGN_JUST, LAYOUT_VERTICAL, [
            panel(ALIGN_JUST, LAYOUT_VERTICAL, ([
                box(ALIGN_TOP, LAYOUT_VERTICAL, [
                    label('current', self.prompt, font=self.label_font),
                ])] if self.prompt else []) + [
                listbox('values', [], font=self.font),
            ]),
            panel(ALIGN_BOTTOM, LAYOUT_HORIZONTAL, [
                action_button(ACTION_OK, font=self.font),
                action_button(ACTION_CANCEL, font=self.font),
            ]),
        ])
    
    def populate_data(self):
        self.listbox_values.extend(self.values)
        if self.starting_value:
            self.listbox_values.set_current_text(self.starting_value)
    
    def get_result(self):
        return self.listbox_values.current_text()
