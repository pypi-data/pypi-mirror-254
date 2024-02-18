"""
Copyright (c) 2023 Gabriel Guerrer

Distributed under the MIT license - See LICENSE for details
"""

"""
The RAVA_APP is a Tk application designed to serve as a foundational framework
for various Graphical User Interface (GUI) sub-applications utilizing the RAVA
device.

The RAVA_APP instance denoted as the main application, lists the available
RAVA devices and handles the connection to the selected circuit, detecting and
responding to eventual disconnections.

The device's communication data and the program's state can be visualized in a
dedicated log window, a valuable resource for debugging the applications and
reporting any encountered errors.

Additionally, the main application features a status bar for vital information
display, and configuration file utilities for the permanent storage of user
preferences.

Sub-applications are tk.Toplevel windows that integrate into the main
application. Derived from the RAVA_SUBAPP class, they become part of the main
application when included in the subapp_dicts argument. Once integrated, these
sub-applications are easily accessible through the main application's menu and
central buttons.
"""

import sys
import os
import os.path
from functools import partial
import configparser
import logging

import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as tkm
import tkinter.filedialog as tkfd

from rng_rava.tk.rava_subapp import RAVA_SUBAPP
from rng_rava.rava_rng_led import RAVA_RNG_LED
from rng_rava.rava_rng import find_rava_sns


### VARS

PAD = 10
HOME_RAVA_PATH = os.path.join(os.path.expanduser('~'), '.rava/')
SUBAPP_DICT_KEYS = ['class', 'menu_title', 'show_button', 'use_rng']
LOG_LEVELS = ['DEBUG', 'INFO', 'WARNING', 'ERROR']

### RAVA_APP

class RAVA_APP(tk.Tk):

    cfg_default_str = '''
    [LOG]
    level_rava_driver = INFO
    level_rava_app = INFO
    show_on_startup = False
    update_interval_ms = 500

    [APP]
    connect_on_startup = True
    status_duration_ms = 3000
    '''

    def __init__(self, title, geometry='480x300', subapp_dicts=[], cfg_log_name='rava'):
        # Evaluate parameters
        if not self.subapp_evaluate(subapp_dicts):
            print('RAVA_APP Error: subapp_dicts must be suplied as a list of dictionaries containing the following keys: {}'
                  .format(SUBAPP_DICT_KEYS))
            exit()
        self.subapp_dicts = subapp_dicts
        self.subapp_buttons = {}

        ### Initialize RAVA_APP
        super().__init__()
        self.name = 'RAVA_APP'
        self.title(title)
        self.geometry(geometry)
        self.rowconfigure([0,1], weight=1)
        self.columnconfigure([0], weight=1)
        self.protocol('WM_DELETE_WINDOW', self.app_close)
        self.resizable(False, False) # No resize
        self.option_add('*tearOff', tk.FALSE) # Diable menu tear-off
        self.update() # Update geometry       
        
        # Files
        if not os.path.exists(HOME_RAVA_PATH):
            os.mkdir(HOME_RAVA_PATH)
    
        self.filename_logo = os.path.join(os.path.dirname(__file__), 'rava.png')
        self.filename_cfg = os.path.join(HOME_RAVA_PATH, '{}.cfg'.format(cfg_log_name))
        self.filename_log = os.path.join(HOME_RAVA_PATH, '{}.log'.format(cfg_log_name))

        # Logger setup        
        self.lgr, self.lg = self.log_setup()

        # Config setup
        self.cfg_setup()

        # Catch Tk exeptions
        self.report_callback_exception = self.app_handle_tk_exception

        # Debug
        self.lg.info('{}: Initializing'.format(self.name))

        ## Widgets

        # Log Window
        self.window_log = WIN_LOG(self)

        # Menu
        self.widgets_menu()

        # RAVA Connection
        self.frm_rava_conn = ttk.Frame(self, padding=(PAD, PAD))
        self.frm_rava_conn.grid(row=0, column=0, sticky='nsew')
        self.widgets_rava_connection()

        # Center
        self.frm_center =ttk.Frame(self, padding=(PAD, PAD))
        self.frm_center.grid(row=1, column=0, sticky='nsew')
        self.widgets_center()

        # Status Footer
        self.frm_status = ttk.Frame(self, padding=(4, 4))
        self.frm_status.grid(row=2, column=0, sticky='ew')
        self.widgets_status()
        
        self.task_status = None

        ## Key Binds
        self.bind('<Control-Key-l>', lambda event=None: self.window_log.show())
        self.bind('<Control-Key-s>', lambda event=None: self.rava_scan())
        self.bind('<Control-Key-q>', lambda event=None: self.app_close())

        ### Start

        # Update widgets enabled state
        self.widgets_state(rava_connected=False)

        # Initialize RAVA Device
        self.rng = RAVA_RNG_LED()

        # Register disconnect callback
        self.rng.cbkreg_device_close(self.rava_disconnect)

        # Scan for RAVA devices and connect if one found
        if self.cfg_read('APP', 'connect_on_startup', bool):
            self.rava_scan()


    ## LOGGING

    def log_setup(self):
        # Logger Formatter / Handler
        lg_fmt = logging.Formatter(fmt='%(asctime)s %(levelname)-7s %(message)s', datefmt='%H:%M:%S')
        lg_sh = logging.StreamHandler()
        lg_sh.setFormatter(lg_fmt)
        lg_fh = logging.FileHandler(self.filename_log, mode='w')
        lg_fh.setFormatter(lg_fmt)

        # Logger : RAVA Driver
        lgr = logging.getLogger('rava')
        if not lgr.hasHandlers():
            lgr.addHandler(lg_sh)
            lgr.addHandler(lg_fh)
            lgr.setLevel(logging.INFO)

        # Logger: RAVA APP
        lg = logging.getLogger('rava_app')
        if not lg.hasHandlers():
            lg.addHandler(lg_sh)
            lg.addHandler(lg_fh)
            lg.setLevel(logging.INFO)

        # Unhandled Exceptions 
        def log_unhandled_exception(exc_type, exc_value, exc_traceback):
            if issubclass(exc_type, KeyboardInterrupt):
                sys.__excepthook__(exc_type, exc_value, exc_traceback) # Call default excepthook
                return
            self.lg.critical('Unhandled Exception', exc_info=(exc_type, exc_value, exc_traceback))

        sys.excepthook = log_unhandled_exception

        return lgr, lg


    ## CONFIG

    def cfg_setup(self):
        # Default cfg
        cfg_extra_str = [subapp_dict['class'].cfg_default_str for subapp_dict in self.subapp_dicts]
        cfg_str = '\n'.join([self.cfg_default_str, *cfg_extra_str])
        cfg_default = configparser.ConfigParser()
        cfg_default.read_string(cfg_str)

        # Config file already exists?
        if os.path.isfile(self.filename_cfg):

            # Read cfg info
            self.cfg = configparser.ConfigParser()
            self.cfg.read(self.filename_cfg)

            # The read cfg contains all the expected entries?
            for key in cfg_default:
                if key not in self.cfg or set(self.cfg[key].keys()) != set(cfg_default[key].keys()):
                    os.remove(self.filename_cfg)
                    self.lg.error('{} Config: The provided config file is incomplete. Please restart the application.'
                             .format(self.name))
                    exit()

        # Config file inexists, create it with default values
        else:
            self.lg.info('{} Config: Creating file with default content'.format(self.name))
            self.cfg = cfg_default
            self.cfg_save()


    def cfg_read(self, section, option, type=str):
        # Return config option in the appropriate type
        if type is int:
            data = self.cfg.getint(section, option)
        elif type is float:
            data = self.cfg.getfloat(section, option)
        elif type is bool:
            data = self.cfg.getboolean(section, option)
        else:
            data = self.cfg.get(section, option)

        return data


    def cfg_write(self, section, option, value, save=True):
        # Write config option
        if type(value) is not str:
            value = str(value)
        self.cfg.set(section, option, value)
        
        if save:
            self.cfg_save()


    def cfg_save(self):
        # Write config file to disk
        with open(self.filename_cfg, 'w') as cfg_file:
            self.cfg.write(cfg_file)


    ## APP

    def app_handle_tk_exception(self, exc_type, exc_value, exc_traceback):
        self.lg.critical('{}: TK Exception'.format(self.name), exc_info=(exc_type, exc_value, exc_traceback))


    def app_close(self):
        # Debug
        self.lg.info('{}: Closing'.format(self.name))

        # Unregister RAVA close callback
        self.rng.cbkreg_device_close(None)

        # Close rava device
        self.rng.close()

        # Close Log Window
        self.window_log.close()

        # Close tkinter
        self.destroy()
        self.quit()


    def subapp_evaluate(self, subapp_dicts):
        # Test if subapp_dicts is a list of dictionaries containing SUBAPP_DICT_KEYS keys
        for subapp_dict in subapp_dicts:
            if not (isinstance(subapp_dict, dict) and set(subapp_dict.keys()) == set(SUBAPP_DICT_KEYS)):                
                return False
        
        # Test values
        for subapp_dict in subapp_dicts:

            # Class inherits from RAVA_SUBAPP
            if not issubclass(subapp_dict['class'], RAVA_SUBAPP):
                return False

            # Default values            
            if subapp_dict['show_button'] is None:
                subapp_dict['cfg_log_name'] = True
            if subapp_dict['use_rng'] is None:
                subapp_dict['cfg_log_name'] = True
            
        return True


    ## WIDGETS

    def widgets_menu(self):
        self.menu = tk.Menu(self)
        self['menu'] = self.menu

        ## File
        self.menu_file = tk.Menu(self.menu)
        self.menu.add_cascade(menu=self.menu_file, label='File')

        # Log
        self.menu_file.add_command(label='Show Log', command=self.window_log.show, underline=5)
        self.menu_file.add_separator()

        # Quit
        self.menu_file.add_command(label='Quit', command=self.app_close, underline=0)

        ## Sub-Apps
        self.menu_subapps = tk.Menu(self.menu)
        self.menu.add_cascade(menu=self.menu_subapps, label='Sub-Appps')

        # Create a menu entry for all subapps
        for subapp_dict in self.subapp_dicts:
            self.menu_subapps.add_command(label=subapp_dict['menu_title'], command=partial(subapp_dict['class'], self))


    def widgets_rava_connection(self):
        self.frm_rava_conn.columnconfigure([3], weight=1)
        self.frm_rava_conn.rowconfigure([0], weight=1)

        self.lb_rava_sn = ttk.Label(self.frm_rava_conn, text='SN')
        self.lb_rava_sn.grid(row=0, column=0, sticky='w', padx=(PAD, 0))

        self.cbb_rava_sns = ttk.Combobox(self.frm_rava_conn, width=12)
        self.cbb_rava_sns.grid(row=0, column=1, sticky='w', padx=(PAD,0))
        self.cbb_rava_sns.state(['readonly'])
        self.cbb_rava_sns.bind('<<ComboboxSelected>>', self.rava_connect)

        self.bt_rava_scan = ttk.Button(self.frm_rava_conn, text='Scan', width=7, command=self.rava_scan, underline=0)
        self.bt_rava_scan.grid(row=0, column=2, sticky='w', padx=(PAD,0))

        self.lb_rava_conn = ttk.Label(self.frm_rava_conn, anchor='c', text='Disconnected')
        self.lb_rava_conn.grid(row=0, column=3, sticky='we', padx=(2*PAD,0))


    def widgets_center(self):
        subapp_dicts_show = [subapp_dict for subapp_dict in self.subapp_dicts if subapp_dict['show_button']]
        n_apps = len(subapp_dicts_show)
        rows = list(range(n_apps)) if n_apps else [0]
        logo_rowspan = n_apps if n_apps else 1

        self.frm_center.columnconfigure([0,1], weight=1)
        self.frm_center.rowconfigure(rows, weight=1)

        # RAVA Logo
        self.img_rava = tk.PhotoImage(file=self.filename_logo)
        self.lb_img_rava = ttk.Label(self.frm_center, image=self.img_rava)
        self.lb_img_rava.grid(row=0, column=0, rowspan=logo_rowspan)

        # Buttons
        # Create buttons for all subapp_dicts with the option "show_button = True"
        for i, subapp_dict in enumerate(subapp_dicts_show):
            bt = ttk.Button(self.frm_center, width=20, text=subapp_dict['menu_title'], command=partial(subapp_dict['class'], self))
            bt.grid(row=i, column=1)
            self.subapp_buttons[subapp_dict['menu_title']] = bt


    def widgets_status(self):
        self.frm_status.columnconfigure([0], weight=1)
        self.frm_status.rowconfigure([0], weight=1)

        self.lb_status = ttk.Label(self.frm_status, text='', relief=tk.RIDGE, anchor='e')
        self.lb_status.grid(row=0, column=0, sticky='ew')


    def widgets_state(self, rava_connected):
        if rava_connected:
            menu_state = tk.NORMAL
            bt_state = ['!disabled']
        else:
            menu_state = tk.DISABLED
            bt_state = ['disabled']

        for subapp_dict in self.subapp_dicts:
            if subapp_dict['use_rng']:
                # Menu
                self.menu_subapps.entryconfigure(subapp_dict['menu_title'], state=menu_state)

                # Buttons
                if subapp_dict['show_button']:
                    self.subapp_buttons[subapp_dict['menu_title']].state(bt_state)


    def rava_scan(self):
        # Find serial numbers and actualize combobox values
        sns = find_rava_sns()
        self.cbb_rava_sns['values'] = sns

        # Status bar
        self.status_set('{} devices found'.format(len(sns)))

        # No one found
        if len(sns) == 0:
            self.cbb_rava_sns.set('')

        # If only one found, connect
        elif len(sns) == 1:
            self.cbb_rava_sns.set(sns[0])
            self.rava_connect()


    def rava_connect(self, tk_event=None):
        # Remove blue selection
        self.selection_clear()

        # Get serial number
        sn = self.cbb_rava_sns.get()
        if not sn:
            return

        # Previously connected ...
        if self.rng.connected():
            # ... to the same sn? Leave
            if self.rng.dev_serial_number == sn:
                return
            # ... to other sn? Disconnect
            else:
                self.rng.close()

        # Debug
        self.lg.info('{}: Connecting to RAVA device...'.format(self.name))

        # Connect
        if (self.rng.connect(sn)):
            # SN Combobox
            self.cbb_rava_sns.set(sn)

            # Connection label
            self.lb_rava_conn['text'] = 'Connected to {}'.format(self.rng.dev_usb_port)

            # Status bar
            self.status_set('Connected to RAVA device')

            # Update widgets state
            self.widgets_state(True)

        else:
            # SN Combobox
            self.cbb_rava_sns.set('')

            # Connection label
            self.lb_rava_conn['text'] = 'Disconnected'

            # Status bar
            self.status_set('Error connecting to RAVA device')

            # Update widgets state
            self.widgets_state(False)

            # Startup Health tests failed?
            if self.rng.health_startup_enabled and self.rng.health_startup_success == False:
                tkm.showerror(parent=self, message='Startup Health Tests Failed!')
                self.rng.close()


    def rava_disconnect(self):
        # Debug
        self.lg.info('{}: Lost connection to RAVA device'.format(self.name))

        # Update SN Combobox
        self.cbb_rava_sns['values'] = find_rava_sns()
        self.cbb_rava_sns.set('')

        # Connection label
        self.lb_rava_conn['text'] = 'Disconnected'

        # Status bar
        self.status_set('RAVA device disconnected')

        # Update widgets state
        self.widgets_state(False)

        # Close windows that use rng
        for subapp_dict in self.subapp_dicts:
            if subapp_dict['use_rng']:
                for inst in self.winfo_children():
                    if isinstance(inst, subapp_dict['class']):
                        inst.close()


    def status_set(self, str):
        # Cancel last task
        if self.task_status is not None:
            self.after_cancel(self.task_status)

        # Update
        self.lb_status['text'] = str + '  '

        # Erase after status_duration_ms
        if str:
            status_duration_ms = self.cfg_read('APP', 'status_duration_ms', int)
            self.task_status = self.after(status_duration_ms, self.status_set, '')


### WIN_LOG

class WIN_LOG(tk.Toplevel):

    def __init__(self, parent):
        ## Initialize WIN_LOG
        super().__init__(parent)
        self.name = 'WIN_LOG'
        self.title('RAVA Log')
        self.geometry('750x500+{}+{}'.format(self.master.winfo_x(), self.master.winfo_y() + self.master.winfo_height() + 40))
        self.rowconfigure([0], weight=1)
        self.columnconfigure([0], weight=1)
        self.protocol('WM_DELETE_WINDOW', self.hide) # One instance

        # Logging
        self.lg = self.master.lg

        # Widgets
        self.widgets()

        # KEY BINDS
        self.bind('<Control-Key-q>', lambda event=None: self.master.app_close())

        ## Start
        show_on_startup = self.master.cfg_read('LOG', 'show_on_startup', bool)
        if not show_on_startup:
            self.hide()

        # Read cfg and update widgets
        self.cfg_read_update_widgets()

        # Set the log level according to the widgets values
        self.log_level_rava_driver(write=False)
        self.log_level_rava_app(write=False)

        # Open log file and keep updating it
        self.task_log_update = None
        self.log_file = open(self.master.filename_log, 'r')
        self.log_update()


    def widgets(self):
        self.frm_log = ttk.Frame(self, padding=(PAD, PAD))
        self.frm_log.grid(row=0, column=0, sticky='nsew')
        self.frm_log.columnconfigure([0], weight=1)
        self.frm_log.rowconfigure([0], weight=1)

        self.txt_log = tk.Text(self.frm_log, state='disabled')
        self.txt_log.grid(row=0, column=0, sticky='nsew')

        self.scroll_y = ttk.Scrollbar(self.frm_log, orient=tk.VERTICAL, command=self.txt_log.yview)
        self.scroll_y.grid(row=0, column=1, sticky='ns')
        self.txt_log['yscrollcommand'] = self.scroll_y.set

        self.frm_log_actions = ttk.Frame(self, padding=(PAD, 0, PAD, PAD))
        self.frm_log_actions.grid(row=1, column=0, columnspan=2, sticky='nsew')
        self.frm_log_actions.columnconfigure([0,1,2,3,4,5,6], weight=1)
        self.frm_log_actions.rowconfigure([0], weight=1)

        self.lb_rava_driver_level = ttk.Label(self.frm_log_actions, text='RAVA driver')
        self.lb_rava_driver_level.grid(row=0, column=0)

        self.cbb_rava_driver_level = ttk.Combobox(self.frm_log_actions, width=8)
        self.cbb_rava_driver_level.grid(row=0, column=1, sticky='w')
        self.cbb_rava_driver_level['values'] = LOG_LEVELS
        self.cbb_rava_driver_level.state(['readonly'])
        self.cbb_rava_driver_level.bind('<<ComboboxSelected>>', self.log_level_rava_driver)

        self.lb_rava_app_level = ttk.Label(self.frm_log_actions, text='RAVA app')
        self.lb_rava_app_level.grid(row=0, column=2)

        self.cbb_rava_app_level = ttk.Combobox(self.frm_log_actions, width=8)
        self.cbb_rava_app_level.grid(row=0, column=3, sticky='w')
        self.cbb_rava_app_level['values'] = LOG_LEVELS
        self.cbb_rava_app_level.state(['readonly'])
        self.cbb_rava_app_level.bind('<<ComboboxSelected>>', self.log_level_rava_app)

        self.var_show_startup = tk.BooleanVar(value=False)
        self.cb_show_startup = ttk.Checkbutton(self.frm_log_actions, text='Show on startup',
                                               variable=self.var_show_startup, command=self.log_win_show_startup)
        self.cb_show_startup.grid(row=0, column=4)

        self.bt_copy = ttk.Button(self.frm_log_actions, text='Copy to Clipboard', command=self.log_copy)
        self.bt_copy.grid(row=0, column=5)

        self.bt_save = ttk.Button(self.frm_log_actions, text='Save File', command=self.log_save)
        self.bt_save.grid(row=0, column=6)


    def show(self):
        self.geometry('750x500+{}+{}'.format(self.master.winfo_x(), self.master.winfo_y() + self.master.winfo_height() + 10))
        self.wm_deiconify()
        self.bt_save.focus()


    def hide(self):
        self.withdraw()


    def close(self):
        # Cancel scheduled log update
        self.after_cancel(self.task_log_update)
        self.destroy()


    def log_update(self):
        # Update log content
        new_data = self.log_file.read()
        if new_data:
            self.txt_log.configure(state='normal')
            self.txt_log.insert('end', new_data)
            self.txt_log.see('end')
            self.txt_log.configure(state='disabled')

        # Schedule new update
        update_interval_ms = self.master.cfg_read('LOG', 'update_interval_ms', int)
        self.task_log_update = self.after(update_interval_ms, self.log_update)


    def cfg_read_update_widgets(self):
        # level_rava_driver
        level_rava_driver_str = self.master.cfg_read('LOG', 'level_rava_driver')
        if level_rava_driver_str in LOG_LEVELS:
            self.cbb_rava_driver_level.set(level_rava_driver_str)
        else:
            self.lg.warning('{}: Unknown level_rava_driver={}. Provide one of those:{}'
                       .format(self.name, level_rava_driver_str, LOG_LEVELS))
            self.cbb_rava_driver_level.set('INFO')

        # level_rava_app
        level_rava_app_str = self.master.cfg_read('LOG', 'level_rava_app')
        if level_rava_app_str in LOG_LEVELS:
            self.cbb_rava_app_level.set(level_rava_app_str)
        else:
            self.lg.warning('{}: Unknown level_rava_app={}. Provide one of those:{}'
                       .format(self.name, level_rava_app_str, LOG_LEVELS))
            self.cbb_rava_app_level.set('INFO')

        # show_on_startup
        show_on_startup = self.master.cfg_read('LOG', 'show_on_startup', bool)
        self.var_show_startup.set(show_on_startup)


    def log_level_rava_driver(self, tk_event=None, write=True):
        # Update log level
        level_rava_driver_str = self.cbb_rava_driver_level.get()
        level_rava_driver = getattr(logging, level_rava_driver_str)
        self.master.lgr.setLevel(level_rava_driver)

        # Update cfg
        if write:
            self.master.cfg_write('LOG', 'level_rava_driver', level_rava_driver_str)


    def log_level_rava_app(self, tk_event=None, write=True):
        # Update log level
        level_rava_app_str = self.cbb_rava_app_level.get()
        level_rava_app = getattr(logging, level_rava_app_str)
        self.master.lg.setLevel(level_rava_app)

        # Update cfg
        if write:
            self.master.cfg_write('LOG', 'level_rava_app', level_rava_app_str)


    def log_win_show_startup(self, tk_event=None, write=True):
        # Update cfg
        if write:
            self.master.cfg_write('LOG', 'show_on_startup', self.var_show_startup.get())


    def log_copy(self):
        # Copy log content to clipboard
        self.master.clipboard_clear()
        self.master.clipboard_append(self.txt_log.get('1.0', 'end'))


    def log_save(self):
        # Get filename
        filename = tkfd.asksaveasfilename(filetypes=[('LOG','.log')])

        # Save
        if filename:
            with open(filename, 'w') as file:
                file.write(self.txt_log.get('1.0', 'end'))

            # Status
            self.master.status_set('Log saved')