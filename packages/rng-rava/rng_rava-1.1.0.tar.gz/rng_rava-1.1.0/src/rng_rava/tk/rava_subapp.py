"""
Copyright (c) 2023 Gabriel Guerrer

Distributed under the MIT license - See LICENSE for details
"""

"""
The SUBAPP_RAVA serves as the base class that every RAVA sub-application should
inherit from. It incorporates code that guarantees a unique instance for each
sub-application.
"""

import tkinter as tk


### RAVA_SUBAPP

class RAVA_SUBAPP(tk.Toplevel):

    cfg_default_str = ''

    def __init__(self, parent, name, win_title, win_geometry, win_resizable=False):
        # Initialize tk.Toplevel
        super().__init__(parent)

        ## Initialize RAVA_SUBAPP
        self.name = name
        self.title(win_title)
        self.geometry('{}+{}+{}'.format(win_geometry, self.master.winfo_x() + self.master.winfo_width() + 10, self.master.winfo_y()))
        self.rowconfigure([0], weight=1)
        self.columnconfigure([0], weight=1)
        self.resizable(win_resizable, win_resizable)
        self.protocol('WM_DELETE_WINDOW', self.close)

        # Other instance already running? Destry this and keep the previous
        instances = [inst for inst in self.master.winfo_children() if isinstance(inst, type(self))]
        if len(instances) > 1:
            instances[-1].destroy()
            return False

        # Shortcuts
        self.lg = self.master.lg
        self.lgr = self.master.lgr
        self.rng = self.master.rng

        # Debug
        self.lg.info('{}: Initializing'.format(self.name))

        # Key binds
        self.bind('<Control-Key-q>', lambda event=None: self.master.app_close())

        return True


    def close(self):
        # Destroy
        self.destroy()

        # Debug
        self.lg.info('{}: Closing'.format(self.name))