"""
Copyright (c) 2023 Gabriel Guerrer

Distributed under the MIT license - See LICENSE for details
"""

"""
The Control Panel sub-application provides an graphical user interface (GUI) for
testing the core features of the RAVA circuit, including EEPROM, PWM, RNG,
HEALTH, LED, and LAMP capabilities.
"""

import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as tkm

from rng_rava.rava_defs import *
from rng_rava.tk import RAVA_SUBAPP

### VARS

PAD = 10
CTRL_PANEL_N_MAX = 200


### RAVA_SUBAPP_CTRL_PANEL

class RAVA_SUBAPP_CTRL_PANEL(RAVA_SUBAPP):

    cfg_default_str = ''

    def __init__(self, parent):
        ## Initialize RAVA_SUBAPP
        name = 'RAVA_SUBAPP CTRL_PANEL'
        win_title = 'Control Panel'
        win_geometry = '620x350'
        win_resizable = False
        if not super().__init__(parent, name=name, win_title=win_title, win_geometry=win_geometry, win_resizable=win_resizable):
            return

        # Widgets
        self.nb = ttk.Notebook(self, padding=PAD)
        self.nb.grid(row=0, column=0, sticky='nsew')
        self.nb.bind('<<NotebookTabChanged>>', self.notebook_tab_change)

        self.frm_eeprom = ttk.Frame(self, name='eeprom')
        self.frm_eeprom.grid(row=0, column=0, sticky='nsew')
        self.widgets_eeprom()

        self.frm_rng = ttk.Frame(self, name='rng')
        self.frm_rng.grid(row=0, column=0, sticky='nsew')
        self.widgets_rng()

        self.frm_health = ttk.Frame(self, name='health')
        self.frm_health.grid(row=0, column=0, sticky='nsew')
        self.widgets_health()

        self.frm_periph = ttk.Frame(self, name='periph')
        self.frm_periph.grid(row=0, column=0, sticky='nsew')
        self.widgets_periph()

        self.frm_led = ttk.Frame(self, name='led')
        self.frm_led.grid(row=0, column=0, sticky='nsew')
        self.widgets_led()

        self.frm_lamp = ttk.Frame(self, name='lamp')
        self.frm_lamp.grid(row=0, column=0, sticky='nsew')
        self.widgets_lamp()

        self.nb.add(self.frm_eeprom, text=' EEPROM ')
        self.nb.add(self.frm_rng, text=' RNG ')
        self.nb.add(self.frm_health, text=' HEALTH ')
        self.nb.add(self.frm_periph, text=' PERIPH ')
        self.nb.add(self.frm_led, text=' LED ')
        self.nb.add(self.frm_lamp, text=' LAMP ')

        # Key Binds
        self.bind('<Control-Key-q>', lambda event=None: self.master.app_close())

        ## Start
        self.widgets_state()


    def close(self):
        if self.rng.connected():
            # Stop bytes stream
            if self.rng.rng_streaming:
                self.rng_gen_byte_stream_stop()

            # Turn LED off
            if self.rng.led_enabled and self.rng.led_intensity:
                self.rng.snd_led_intensity_fade(0, 1000)

            # LAMP mode off
            if self.rng.lamp_mode:
                self.rng.snd_lamp_mode(False)

        # Close RAVA_SUBAPP
        super().close()


    def widgets_eeprom(self):
        self.frm_eeprom.columnconfigure([0,1,2], weight=1)
        self.frm_eeprom.rowconfigure([0,1], weight=1)

        # firmware
        self.lbf_eeprom_firmware = ttk.Labelframe(self.frm_eeprom, text='Firmware', padding=(PAD, PAD))
        self.lbf_eeprom_firmware.grid(row=0, column=0, rowspan=2, sticky='nsew', padx=PAD, pady=PAD)
        self.lbf_eeprom_firmware.columnconfigure([0,1], weight=1)
        self.lbf_eeprom_firmware.rowconfigure([0,2], weight=1)

        self.lb_eeprom_firmw_version = ttk.Label(self.lbf_eeprom_firmware, text='Version')
        self.lb_eeprom_firmw_version.grid(row=0, column=0, sticky='w')

        self.var_eeprom_firmw_version = tk.StringVar()
        self.en_eeprom_firmw_version = ttk.Entry(self.lbf_eeprom_firmware, textvariable=self.var_eeprom_firmw_version, width=7)
        self.en_eeprom_firmw_version.state(['readonly'])
        self.en_eeprom_firmw_version.grid(row=0, column=1)

        self.lb_eeprom_firmw_modules = ttk.Label(self.lbf_eeprom_firmware, text='Enabled')
        self.lb_eeprom_firmw_modules.grid(row=1, column=0, columnspan=2, sticky='w')

        self.var_eeprom_firmw_modules = tk.StringVar(value=[''])
        self.lbox_eeprom_firmw_modules = tk.Listbox(self.lbf_eeprom_firmware, listvariable=self.var_eeprom_firmw_modules, selectmode='browse', width=16, height=7)
        self.lbox_eeprom_firmw_modules.bind("<<ListboxSelect>>", None)
        self.lbox_eeprom_firmw_modules.grid(row=2, column=0, columnspan=2)

        # pwm
        self.lbf_eeprom_pwm = ttk.Labelframe(self.frm_eeprom, text='PWM', padding=(PAD, PAD))
        self.lbf_eeprom_pwm.grid(row=0, column=1, sticky='nsew', padx=0, pady=PAD)
        self.lbf_eeprom_pwm.columnconfigure([0,1], weight=1)
        self.lbf_eeprom_pwm.rowconfigure([0,1], weight=1)

        self.lb_eeprom_pwm_freq = ttk.Label(self.lbf_eeprom_pwm, text='Frequency')
        self.lb_eeprom_pwm_freq.grid(row=0, column=0, sticky='w')

        self.cbb_eeprom_pwm_freq = ttk.Combobox(self.lbf_eeprom_pwm, width=7)
        self.cbb_eeprom_pwm_freq.grid(row=0, column=1)
        self.cbb_eeprom_pwm_freq.state(['readonly'])
        self.cbb_eeprom_pwm_freq['values'] = list(D_PWM_FREQ.keys())

        self.lb_eeprom_pwm_duty = ttk.Label(self.lbf_eeprom_pwm, text='Duty Cycle')
        self.lb_eeprom_pwm_duty.grid(row=1, column=0, sticky='w')

        self.var_eeprom_pwm_duty = tk.IntVar()
        self.spb_eeprom_pwm_duty = ttk.Spinbox(self.lbf_eeprom_pwm, from_=1, to=255, increment=1, textvariable=self.var_eeprom_pwm_duty, width=4)
        self.spb_eeprom_pwm_duty.grid(row=1, column=1)

        # rng
        self.lbf_eeprom_rng = ttk.Labelframe(self.frm_eeprom, text='RNG', padding=(PAD, PAD))
        self.lbf_eeprom_rng.grid(row=1, column=1, sticky='nswe', padx=0, pady=(0, PAD))
        self.lbf_eeprom_rng.columnconfigure([0,1], weight=1)
        self.lbf_eeprom_rng.rowconfigure([0], weight=1)

        self.lb_eeprom_rng_si = ttk.Label(self.lbf_eeprom_rng, text='Sampling \ninterval (us)')
        self.lb_eeprom_rng_si.grid(row=0, column=0, sticky='w')

        self.var_eeprom_rng_si = tk.IntVar()
        self.spb_eeprom_rng_si = ttk.Spinbox(self.lbf_eeprom_rng, from_=1, to=255, increment=1, textvariable=self.var_eeprom_rng_si, width=4)
        self.spb_eeprom_rng_si.grid(row=0, column=1)

        # led
        self.lbf_eeprom_led = ttk.Labelframe(self.frm_eeprom, text='LED', padding=(PAD, PAD))
        self.lbf_eeprom_led.grid(row=0, column=2, sticky='nsew', padx=PAD, pady=PAD)
        self.lbf_eeprom_led.columnconfigure([0,1], weight=1)
        self.lbf_eeprom_led.rowconfigure([0], weight=1)

        self.lb_eeprom_led_attached = ttk.Label(self.lbf_eeprom_led, text='Attached')
        self.lb_eeprom_led_attached.grid(row=0, column=0)

        self.cbb_eeprom_led_attached = ttk.Combobox(self.lbf_eeprom_led, width=7)
        self.cbb_eeprom_led_attached.grid(row=0, column=1)
        self.cbb_eeprom_led_attached['values'] = [True, False]
        self.cbb_eeprom_led_attached.state(['readonly'])

        # lamp
        self.lbf_eeprom_lamp = ttk.Labelframe(self.frm_eeprom, text='LAMP', padding=(PAD, PAD))
        self.lbf_eeprom_lamp.grid(row=1, column=2, sticky='nsew', padx=PAD, pady=(0, PAD))
        self.lbf_eeprom_lamp.columnconfigure([0,1], weight=1)
        self.lbf_eeprom_lamp.rowconfigure([0,1,2], weight=1)

        self.lb_eeprom_lamp_exp_dur = ttk.Label(self.lbf_eeprom_lamp, text='Exp. Duration (s)')
        self.lb_eeprom_lamp_exp_dur.grid(row=0, column=0, sticky='w')

        self.var_eeprom_lamp_exp_dur = tk.IntVar()
        self.spb_eeprom_lamp_exp_dur = ttk.Spinbox(self.lbf_eeprom_lamp, from_=60, to=6000, increment=1, textvariable=self.var_eeprom_lamp_exp_dur, width=5)
        self.spb_eeprom_lamp_exp_dur.grid(row=0, column=1)

        self.lb_eeprom_lamp_z_sig = ttk.Label(self.lbf_eeprom_lamp, text='Z-score sig.')
        self.lb_eeprom_lamp_z_sig.grid(row=1, column=0, sticky='w')

        self.var_eeprom_lamp_z_sig = tk.DoubleVar()
        self.spb_eeprom_lamp_z_sig = ttk.Spinbox(self.lbf_eeprom_lamp, from_=1, to=5, increment=0.05, textvariable=self.var_eeprom_lamp_z_sig, width=5)
        self.spb_eeprom_lamp_z_sig.grid(row=1, column=1)

        self.lb_eeprom_lamp_mag_smooth = ttk.Label(self.lbf_eeprom_lamp, text='Mag. smooth')
        self.lb_eeprom_lamp_mag_smooth.grid(row=2, column=0, sticky='w')

        self.var_eeprom_lamp_mag_smooth = tk.IntVar()
        self.spb_eeprom_lamp_mag_smooth = ttk.Spinbox(self.lbf_eeprom_lamp, from_=1, to=1000, increment=1, textvariable=self.var_eeprom_lamp_mag_smooth, width=5)
        self.spb_eeprom_lamp_mag_smooth.grid(row=2, column=1)

        # buttons
        self.frm_eeprom_buttons = ttk.Frame(self.frm_eeprom, padding=(PAD, 0, PAD, PAD))
        self.frm_eeprom_buttons.grid(row=2, column=0, columnspan=3, sticky='nsew')
        self.frm_eeprom_buttons.columnconfigure([0,1,2], weight=1)
        self.frm_eeprom_buttons.rowconfigure([0], weight=1)

        self.bt_eeprom_get = ttk.Button(self.frm_eeprom_buttons, text='Get', command=self.eeprom_get)
        self.bt_eeprom_get.grid(row=0, column=0)

        self.bt_eeprom_set = ttk.Button(self.frm_eeprom_buttons, text='Set', command=self.eeprom_set)
        self.bt_eeprom_set.grid(row=0, column=1)

        self.bt_eeprom_defaults = ttk.Button(self.frm_eeprom_buttons, text='Set Defaults', width=13, command=self.eeprom_set_defaults)
        self.bt_eeprom_defaults.grid(row=0, column=2)


    def widgets_rng(self):
        self.frm_rng.columnconfigure([0,1], weight=1)
        self.frm_rng.rowconfigure([0], weight=1)
        self.frm_rng.rowconfigure([1], weight=2)

        # Setup
        self.lbf_rng_setup = ttk.Labelframe(self.frm_rng, text='Setup', padding=(PAD, PAD))
        self.lbf_rng_setup.grid(row=0, column=0, sticky='nsew', padx=PAD, pady=PAD)
        self.lbf_rng_setup.columnconfigure([0,1,2,3], weight=1)
        self.lbf_rng_setup.rowconfigure([0,1], weight=1)

        self.lb_pwm_freq = ttk.Label(self.lbf_rng_setup, text='PWM Freq.')
        self.lb_pwm_freq.grid(row=0, column=0, sticky='w')

        self.cbb_pwm_freq = ttk.Combobox(self.lbf_rng_setup, width=7)
        self.cbb_pwm_freq.grid(row=0, column=1)
        self.cbb_pwm_freq.state(['readonly'])
        self.cbb_pwm_freq['values'] = list(D_PWM_FREQ.keys())

        self.lb_pwm_duty = ttk.Label(self.lbf_rng_setup, text='PWM Duty')
        self.lb_pwm_duty.grid(row=0, column=2)

        self.var_pwm_duty = tk.IntVar()
        self.spb_pwm_duty = ttk.Spinbox(self.lbf_rng_setup, from_=1, to=255, increment=1, textvariable=self.var_pwm_duty, width=4)
        self.spb_pwm_duty.grid(row=0, column=3)

        self.lb_rng_si = ttk.Label(self.lbf_rng_setup, text='Sampling \ninterval (us)')
        self.lb_rng_si.grid(row=1, column=0, sticky='w')

        self.var_rng_si = tk.IntVar()
        self.spb_rng_si = ttk.Spinbox(self.lbf_rng_setup, from_=1, to=255, increment=1, textvariable=self.var_rng_si, width=4)
        self.spb_rng_si.grid(row=1, column=1)

        self.bt_rng_setup_get = ttk.Button(self.lbf_rng_setup, text='Get', width=6, command=self.rng_setup_get)
        self.bt_rng_setup_get.grid(row=1, column=2)

        self.bt_rng_setup_set = ttk.Button(self.lbf_rng_setup, text='Set', width=6, command=self.rng_setup_set)
        self.bt_rng_setup_set.grid(row=1, column=3)

        # Output
        self.lbf_eeprom_rng_out = ttk.Labelframe(self.frm_rng, text='Output: RNG_A, RNG_B', padding=(PAD, PAD))
        self.lbf_eeprom_rng_out.grid(row=0, column=1, rowspan=2, sticky='nsew', padx=(0, PAD), pady=PAD)
        self.lbf_eeprom_rng_out.columnconfigure([0], weight=1)
        self.lbf_eeprom_rng_out.rowconfigure([0, 1], weight=1)

        self.txt_rng_a = tk.Text(self.lbf_eeprom_rng_out, width=18, state='disabled', wrap='word')
        self.txt_rng_a.grid(row=0, column=0, sticky='nsew')

        self.scroll_y_rng_a = ttk.Scrollbar(self.lbf_eeprom_rng_out, orient=tk.VERTICAL, command=self.txt_rng_a.yview)
        self.scroll_y_rng_a.grid(row=0, column=1, sticky='ns')
        self.txt_rng_a['yscrollcommand'] = self.scroll_y_rng_a.set

        self.txt_rng_b = tk.Text(self.lbf_eeprom_rng_out, width=18, state='disabled', wrap='word')
        self.txt_rng_b.grid(row=1, column=0, sticky='nsew', pady=(PAD, 0))

        self.scroll_y_rng_b = ttk.Scrollbar(self.lbf_eeprom_rng_out, orient=tk.VERTICAL, command=self.txt_rng_b.yview)
        self.scroll_y_rng_b.grid(row=1, column=1, sticky='ns', pady=(PAD, 0))
        self.txt_rng_b['yscrollcommand'] = self.scroll_y_rng_b.set

        ## Notebook
        self.nb_rng = ttk.Notebook(self.frm_rng)
        self.nb_rng.grid(row=1, column=0, sticky='nsew', padx=PAD, pady=(0, PAD))
        self.nb_rng.bind('<<NotebookTabChanged>>', self.rng_notebook_tab_change)

        # Data
        self.frm_rng_data = ttk.Frame(self.frm_rng, name='data', padding=PAD)
        self.frm_rng_data.grid(row=0, column=0, sticky='nsew')
        self.frm_rng_data.columnconfigure([0,1,2], weight=1)
        self.frm_rng_data.rowconfigure([0,1,2], weight=1)

        self.lb_rng_data_ammount = ttk.Label(self.frm_rng_data, text='Ammount N')
        self.lb_rng_data_ammount.grid(row=0, column=0, sticky='w')

        self.var_rng_data_ammount = tk.IntVar(value=10)
        self.spb_rng_data_ammount = ttk.Spinbox(self.frm_rng_data, from_=1, to=CTRL_PANEL_N_MAX, increment=5, textvariable=self.var_rng_data_ammount, width=5)
        self.spb_rng_data_ammount.grid(row=0, column=1)

        self.bt_rng_data_pulsecount = ttk.Button(self.frm_rng_data, text='N Pulse Counts', width=13, command=self.rng_gen_pulse_count)
        self.bt_rng_data_pulsecount.grid(row=0, column=2)

        self.lb_rng_data_bit_src = ttk.Label(self.frm_rng_data, text='Bit Source')
        self.lb_rng_data_bit_src.grid(row=1, column=0, sticky='w')

        self.cbb_rng_data_bit_src = ttk.Combobox(self.frm_rng_data, width=9)
        self.cbb_rng_data_bit_src.grid(row=1, column=1)
        self.cbb_rng_data_bit_src.state(['readonly'])
        self.cbb_rng_data_bit_src['values'] = list(D_RNG_BIT_SRC.keys())
        self.cbb_rng_data_bit_src.set(list(D_RNG_BIT_SRC.keys())[0])

        self.bt_rng_data_bit = ttk.Button(self.frm_rng_data, text='1 Bit', width=13, command=self.rng_gen_bit)
        self.bt_rng_data_bit.grid(row=1, column=2)

        self.lb_rng_data_byte_pp = ttk.Label(self.frm_rng_data, text='Post Processing')
        self.lb_rng_data_byte_pp.grid(row=2, column=0, sticky='w')

        self.cbb_rng_data_byte_pp = ttk.Combobox(self.frm_rng_data, width=9)
        self.cbb_rng_data_byte_pp.grid(row=2, column=1)
        self.cbb_rng_data_byte_pp.state(['readonly'])
        self.cbb_rng_data_byte_pp['values'] = list(D_RNG_POSTPROC.keys())
        self.cbb_rng_data_byte_pp.set(list(D_RNG_POSTPROC.keys())[0])

        self.bt_rng_data_byte = ttk.Button(self.frm_rng_data, text='N Bytes', width=13, command=self.rng_gen_byte)
        self.bt_rng_data_byte.grid(row=2, column=2)

        # Numbers
        self.frm_rng_num = ttk.Frame(self.frm_rng, name='num', padding=PAD)
        self.frm_rng_num.grid(row=0, column=0, sticky='nsew')
        self.frm_rng_num.columnconfigure([0,1,2,3,4], weight=1)
        self.frm_rng_num.rowconfigure([0,1,2], weight=1)

        self.lb_rng_num_ammount = ttk.Label(self.frm_rng_num, text='Ammount N')
        self.lb_rng_num_ammount.grid(row=0, column=0, columnspan=2, sticky='w')

        self.var_rng_num_ammount = tk.IntVar(value=10)
        self.spb_rng_num_ammount = ttk.Spinbox(self.frm_rng_num, from_=1, to=100, increment=5, textvariable=self.var_rng_num_ammount, width=5)
        self.spb_rng_num_ammount.grid(row=0, column=2)

        self.lb_rng_num_min_int = ttk.Label(self.frm_rng_num, text='Min')
        self.lb_rng_num_min_int.grid(row=1, column=0, sticky='w')

        self.var_rng_num_min_int = tk.IntVar(value=0)
        self.spb_rng_num_min_int = ttk.Spinbox(self.frm_rng_num, from_=0, to=65535, increment=5, textvariable=self.var_rng_num_min_int, width=4)
        self.spb_rng_num_min_int.grid(row=1, column=1)

        self.lb_rng_num_max_int = ttk.Label(self.frm_rng_num, text='Max')
        self.lb_rng_num_max_int.grid(row=1, column=2)

        self.var_rng_num_max_int = tk.IntVar(value=9)
        self.spb_rng_num_max_int = ttk.Spinbox(self.frm_rng_num, from_=1, to=65535, increment=5, textvariable=self.var_rng_num_max_int, width=4)
        self.spb_rng_num_max_int.grid(row=1, column=3)

        self.bt_rng_num_int = ttk.Button(self.frm_rng_num, text='N Integers', width=10, command=self.rng_gen_integer)
        self.bt_rng_num_int.grid(row=1, column=4)

        self.lb_rng_num_min_float = ttk.Label(self.frm_rng_num, text='Min')
        self.lb_rng_num_min_float.grid(row=2, column=0, sticky='w')

        self.var_rng_num_min_float = tk.DoubleVar(value=0.)
        self.spb_rng_num_min_float = ttk.Spinbox(self.frm_rng_num, from_=0, to=1000, increment=5, textvariable=self.var_rng_num_min_float, width=4)
        self.spb_rng_num_min_float.grid(row=2, column=1)

        self.lb_rng_num_max_float = ttk.Label(self.frm_rng_num, text='Max')
        self.lb_rng_num_max_float.grid(row=2, column=2)

        self.var_rng_num_max_float = tk.DoubleVar(value=1.)
        self.spb_rng_num_max_float = ttk.Spinbox(self.frm_rng_num, from_=0, to=1000, increment=0.5, textvariable=self.var_rng_num_max_float, width=4)
        self.spb_rng_num_max_float.grid(row=2, column=3)

        self.bt_rng_num_float = ttk.Button(self.frm_rng_num, text='N Floats', width=10, command=self.rng_gen_float)
        self.bt_rng_num_float.grid(row=2, column=4)

        # Byte stream
        self.frm_rng_stream = ttk.Frame(self.frm_rng, name='stream', padding=PAD)
        self.frm_rng_stream.grid(row=0, column=0, sticky='nsew')
        self.frm_rng_stream.columnconfigure([0,1,2,3], weight=1)
        self.frm_rng_stream.rowconfigure([0,1,2], weight=1)

        self.lb_rng_stream_ammount = ttk.Label(self.frm_rng_stream, text='Bytes per stream')
        self.lb_rng_stream_ammount.grid(row=0, column=0, columnspan=2, sticky='w')

        self.var_rng_stream_ammount = tk.IntVar(value=10)
        self.spb_rng_stream_ammount = ttk.Spinbox(self.frm_rng_stream, from_=1, to=CTRL_PANEL_N_MAX, increment=5, textvariable=self.var_rng_stream_ammount, width=5)
        self.spb_rng_stream_ammount.grid(row=0, column=1, columnspan=2)

        self.lb_rng_stream_interval = ttk.Label(self.frm_rng_stream, text='Stream \ninterval (ms)')
        self.lb_rng_stream_interval.grid(row=1, column=0, sticky='w')

        self.var_rng_stream_interval = tk.IntVar(value=200)
        self.spb_rng_stream_interval = ttk.Spinbox(self.frm_rng_stream, from_=1, to=RNG_BYTE_STREAM_MAX_INTERVAL_MS, increment=100, textvariable=self.var_rng_stream_interval, width=4)
        self.spb_rng_stream_interval.grid(row=1, column=1)

        self.lb_rng_stream_byte_pp = ttk.Label(self.frm_rng_stream, text='Post Proc.')
        self.lb_rng_stream_byte_pp.grid(row=1, column=2)

        self.cbb_rng_stream_byte_pp = ttk.Combobox(self.frm_rng_stream, width=7)
        self.cbb_rng_stream_byte_pp.grid(row=1, column=3)
        self.cbb_rng_stream_byte_pp.state(['readonly'])
        self.cbb_rng_stream_byte_pp['values'] = list(D_RNG_POSTPROC.keys())
        self.cbb_rng_stream_byte_pp.set(list(D_RNG_POSTPROC.keys())[0])

        self.bt_rng_stream_start = ttk.Button(self.frm_rng_stream, text='Start / Get', width=10, command=self.rng_gen_byte_stream_start)
        self.bt_rng_stream_start.grid(row=2, column=0, columnspan=2)

        self.bt_rng_stream_stop = ttk.Button(self.frm_rng_stream, text='Stop', width=10, command=self.rng_gen_byte_stream_stop)
        self.bt_rng_stream_stop.grid(row=2, column=2, columnspan=2)

        # Notebook
        self.nb_rng.add(self.frm_rng_data, text='Data ')
        self.nb_rng.add(self.frm_rng_num, text='Numbers ')
        self.nb_rng.add(self.frm_rng_stream, text='Byte Stream ')


    def widgets_health(self):
        self.frm_health.columnconfigure([0,1], weight=1)
        self.frm_health.rowconfigure([0,1,2], weight=1)

        # Startup
        self.lbf_health_startup = ttk.Labelframe(self.frm_health, text='Startup Tests', padding=(PAD, PAD))
        self.lbf_health_startup.grid(row=0, column=0, sticky='nsew', padx=PAD, pady=PAD)
        self.lbf_health_startup.columnconfigure([0], weight=1)
        self.lbf_health_startup.rowconfigure([0,1], weight=1)

        self.bt_rng_health_startup_run = ttk.Button(self.lbf_health_startup, text='Run', width=10, command=self.health_startup_run)
        self.bt_rng_health_startup_run.grid(row=0, column=0)

        self.bt_rng_health_startup_get = ttk.Button(self.lbf_health_startup, text='Get', width=10, command=self.health_startup_get)
        self.bt_rng_health_startup_get.grid(row=1, column=0)

        # Continuous
        self.lbf_health_cont = ttk.Labelframe(self.frm_health, text='Continuous Tests', padding=(PAD, PAD))
        self.lbf_health_cont.grid(row=1, column=0, sticky='nsew', padx=PAD, pady=(0, PAD))
        self.lbf_health_cont.columnconfigure([0], weight=1)
        self.lbf_health_cont.rowconfigure([0], weight=1)

        self.bt_health_cont_get = ttk.Button(self.lbf_health_cont, text='Get', width=10, command=self.health_continuous_get)
        self.bt_health_cont_get.grid(row=0, column=0)

        # Results
        self.lbf_health_results = ttk.Labelframe(self.frm_health, text='Results', padding=(PAD, PAD))
        self.lbf_health_results.grid(row=0, column=1, rowspan=3, sticky='nsew', padx=(0, PAD), pady=PAD)
        self.lbf_health_results.columnconfigure([0], weight=1)
        self.lbf_health_results.rowconfigure([0], weight=1)

        self.txt_health_results = tk.Text(self.lbf_health_results, width=50, state='disabled', wrap='word')
        self.txt_health_results.grid(row=0, column=0, sticky='nsew')


    def widgets_periph(self):
        self.frm_periph.columnconfigure([0,1], weight=1)
        self.frm_periph.rowconfigure([0,1], weight=1)

        # Digital IO
        self.lbf_periph_digi = ttk.Labelframe(self.frm_periph, text='Digital IO', padding=(PAD, PAD))
        self.lbf_periph_digi.grid(row=0, column=0, sticky='nsew', padx=PAD, pady=PAD)
        self.lbf_periph_digi.columnconfigure([0,1,2,3], weight=1)
        self.lbf_periph_digi.rowconfigure([0,1,2,3], weight=1)

        self.lb_periph_port = ttk.Label(self.lbf_periph_digi, text='Port')
        self.lb_periph_port.grid(row=0, column=0, sticky='w')

        self.var_periph_port = tk.IntVar(value=1)
        self.cbb_periph_port = ttk.Combobox(self.lbf_periph_digi, width=5, textvariable=self.var_periph_port)
        self.cbb_periph_port.grid(row=0, column=1, sticky='w')
        self.cbb_periph_port.state(['readonly'])
        self.cbb_periph_port['values'] = list(range(1, PERIPH_PORTS + 1))
        self.cbb_periph_port.bind('<<ComboboxSelected>>', self.periph_digi_state_update)

        self.lb_periph_mode = ttk.Label(self.lbf_periph_digi, text='Mode')
        self.lb_periph_mode.grid(row=1, column=0, sticky='w')

        self.cbb_periph_mode = ttk.Combobox(self.lbf_periph_digi, width=8)
        self.cbb_periph_mode.grid(row=1, column=1, sticky='w')
        self.cbb_periph_mode.state(['readonly'])
        self.cbb_periph_mode['values'] = ['INPUT', 'OUTPUT']
        self.cbb_periph_mode.set('INPUT')
        self.cbb_periph_mode.bind('<<ComboboxSelected>>', self.periph_digi_mode)

        self.lb_periph_state = ttk.Label(self.lbf_periph_digi, text='State')
        self.lb_periph_state.grid(row=2, column=0, sticky='w')

        self.var_periph_state = tk.IntVar(value=0)
        self.cbb_periph_state = ttk.Combobox(self.lbf_periph_digi, width=5, textvariable=self.var_periph_state)
        self.cbb_periph_state.grid(row=2, column=1, sticky='w')
        self.cbb_periph_state.state(['readonly'])
        self.cbb_periph_state['values'] = [0, 1]

        self.bt_periph_state_get = ttk.Button(self.lbf_periph_digi, text='Get', width=5, command=self.periph_digi_state_get)
        self.bt_periph_state_get.grid(row=2, column=2)

        self.bt_periph_state_set = ttk.Button(self.lbf_periph_digi, text='Set', width=5, command=self.periph_digi_state_set)
        self.bt_periph_state_set.grid(row=2, column=3)

        self.lb_periph_pulse_dur = ttk.Label(self.lbf_periph_digi, text='Dur. (us)')
        self.lb_periph_pulse_dur.grid(row=3, column=0, sticky='w')

        self.var_periph_pulse_dur = tk.IntVar(value=100)
        self.spb_periph_port = ttk.Spinbox(self.lbf_periph_digi, from_=1, to=100000, increment=1, textvariable=self.var_periph_pulse_dur, width=5)
        self.spb_periph_port.grid(row=3, column=1, sticky='w')

        self.bt_periph_pulse = ttk.Button(self.lbf_periph_digi, text='Pulse', width=7, command=self.periph_digi_pulse)
        self.bt_periph_pulse.grid(row=3, column=2, columnspan=2)

        ## Notebook
        self.nb_periph = ttk.Notebook(self.frm_periph)
        self.nb_periph.grid(row=0, column=1, sticky='nsew', padx=(0, PAD), pady=PAD)

        # D1
        self.frm_periph_d1 = ttk.Frame(self.frm_periph, padding=(PAD, PAD))
        self.frm_periph_d1.grid(row=0, column=0, sticky='nsew', padx=(0, PAD), pady=PAD)
        self.frm_periph_d1.columnconfigure([0,1,2], weight=1)
        self.frm_periph_d1.rowconfigure([0,1,2,3], weight=1)

        self.lb_periph_d1_timing_dbg = ttk.Label(self.frm_periph_d1, text='Timing Debug')
        self.lb_periph_d1_timing_dbg.grid(row=0, column=0, columnspan=2, sticky='w')

        self.cbb_periph_d1_timing_dbg = ttk.Combobox(self.frm_periph_d1, width=5)
        self.cbb_periph_d1_timing_dbg.grid(row=0, column=2)
        self.cbb_periph_d1_timing_dbg.state(['readonly'])
        self.cbb_periph_d1_timing_dbg['values'] = ['On', 'Off']
        self.cbb_periph_d1_timing_dbg.set('Off')
        self.cbb_periph_d1_timing_dbg.bind('<<ComboboxSelected>>', self.periph_d1_timing_debug)

        self.lb_periph_d1_trigger = ttk.Label(self.frm_periph_d1, text='Trigger Input')
        self.lb_periph_d1_trigger.grid(row=1, column=0, columnspan=2, sticky='w')

        self.cbb_periph_d1_trigger_on = ttk.Combobox(self.frm_periph_d1, width=5)
        self.cbb_periph_d1_trigger_on.grid(row=1, column=2)
        self.cbb_periph_d1_trigger_on.state(['readonly'])
        self.cbb_periph_d1_trigger_on['values'] = ['On', 'Off']
        self.cbb_periph_d1_trigger_on.set('Off')
        self.cbb_periph_d1_trigger_on.bind('<<ComboboxSelected>>', self.periph_d1_trigger_input)

        self.lb_periph_d1_comparator = ttk.Label(self.frm_periph_d1, text='Comparator')
        self.lb_periph_d1_comparator.grid(row=2, column=0, sticky='w')

        self.cbb_periph_d1_comparator_neg = ttk.Combobox(self.frm_periph_d1, width=7)
        self.cbb_periph_d1_comparator_neg.grid(row=2, column=1)
        self.cbb_periph_d1_comparator_neg.state(['readonly'])
        self.cbb_periph_d1_comparator_neg['values'] = ['Neg=D5', 'Neg=0']
        self.cbb_periph_d1_comparator_neg.set('Neg=0')
        self.cbb_periph_d1_comparator_neg.bind('<<ComboboxSelected>>', self.periph_d1_comparator)

        self.cbb_periph_d1_comparator_on = ttk.Combobox(self.frm_periph_d1, width=5)
        self.cbb_periph_d1_comparator_on.grid(row=2, column=2)
        self.cbb_periph_d1_comparator_on.state(['readonly'])
        self.cbb_periph_d1_comparator_on['values'] = ['On', 'Off']
        self.cbb_periph_d1_comparator_on.set('Off')
        self.cbb_periph_d1_comparator_on.bind('<<ComboboxSelected>>', self.periph_d1_comparator)

        self.lb_periph_d1_delay = ttk.Label(self.frm_periph_d1, text='Delay Dur. (us)')
        self.lb_periph_d1_delay.grid(row=3, column=0, sticky='w')

        self.var_periph_d1_delay_dur = tk.IntVar(value=10)
        self.spb_periph_d1_delay_dur = ttk.Spinbox(self.frm_periph_d1, from_=1, to=100000, increment=1, textvariable=self.var_periph_d1_delay_dur, width=5)
        self.spb_periph_d1_delay_dur.grid(row=3, column=1)

        self.bt_periph_d1_delay = ttk.Button(self.frm_periph_d1, text='Test', width=7, command=self.periph_d1_delay_test)
        self.bt_periph_d1_delay.grid(row=3, column=2)

        # D2
        self.frm_periph_d2 = ttk.Frame(self.frm_periph, padding=(PAD, PAD))
        self.frm_periph_d2.grid(row=0, column=0, sticky='nsew', padx=PAD, pady=(0, PAD))
        self.frm_periph_d2.columnconfigure([0,1], weight=1)
        self.frm_periph_d2.rowconfigure([0,1], weight=1)

        self.lb_periph_d2_input_capture = ttk.Label(self.frm_periph_d2, text='Input Capture')
        self.lb_periph_d2_input_capture.grid(row=0, column=0)

        self.cbb_periph_d2_input_capture_on = ttk.Combobox(self.frm_periph_d2, width=7)
        self.cbb_periph_d2_input_capture_on.grid(row=0, column=1)
        self.cbb_periph_d2_input_capture_on.state(['readonly'])
        self.cbb_periph_d2_input_capture_on['values'] = ['On', 'Off']
        self.cbb_periph_d2_input_capture_on.set('Off')
        self.cbb_periph_d2_input_capture_on.bind('<<ComboboxSelected>>', self.periph_d2_input_capture)

        self.lb_periph_d2_input_capture_interval = ttk.Label(self.frm_periph_d2, text='Capture Interval (s)')
        self.lb_periph_d2_input_capture_interval.grid(row=1, column=0)

        self.var_periph_d2_input_capture_interval = tk.StringVar()
        self.en_periph_d2_input_capture_interval = ttk.Entry(self.frm_periph_d2, width=10, textvariable=self.var_periph_d2_input_capture_interval)
        self.en_periph_d2_input_capture_interval.grid(row=1, column=1)
        self.en_periph_d2_input_capture_interval.state(['readonly'])

        # D3
        self.frm_periph_d3 = ttk.Frame(self.frm_periph, padding=(PAD, PAD))
        self.frm_periph_d3.grid(row=0, column=0, sticky='nsew', padx=(0, PAD), pady=(0, PAD))
        self.frm_periph_d3.columnconfigure([0,1,2], weight=1)
        self.frm_periph_d3.rowconfigure([0,1,2,3,4], weight=1)

        self.lb_periph_d3_trigger_out_interval = ttk.Label(self.frm_periph_d3, text='Trigger Output\nInterval (ms)')
        self.lb_periph_d3_trigger_out_interval.grid(row=0, column=0, sticky='w')

        self.var_periph_d3_trigger_out_interval = tk.IntVar(value=10)
        self.spb_periph_d3_trigger_out_interval = ttk.Spinbox(self.frm_periph_d3, from_=1, to=100000, increment=1, textvariable=self.var_periph_d3_trigger_out_interval, width=5, command=self.periph_d3_trigger_output)
        self.spb_periph_d3_trigger_out_interval.grid(row=0, column=1)

        self.cbb_periph_d3_trigger_out_on = ttk.Combobox(self.frm_periph_d3, width=5)
        self.cbb_periph_d3_trigger_out_on.grid(row=0, column=2)
        self.cbb_periph_d3_trigger_out_on.state(['readonly'])
        self.cbb_periph_d3_trigger_out_on['values'] = ['On', 'Off']
        self.cbb_periph_d3_trigger_out_on.set('Off')
        self.cbb_periph_d3_trigger_out_on.bind('<<ComboboxSelected>>', self.periph_d3_trigger_output)

        self.lb_periph_d3_pwm = ttk.Label(self.frm_periph_d3, text='PWM Output')
        self.lb_periph_d3_pwm.grid(row=1, column=0, sticky='w')

        self.cbb_periph_d3_pwm_on = ttk.Combobox(self.frm_periph_d3, width=5)
        self.cbb_periph_d3_pwm_on.grid(row=1, column=2)
        self.cbb_periph_d3_pwm_on.state(['readonly'])
        self.cbb_periph_d3_pwm_on['values'] = ['On', 'Off']
        self.cbb_periph_d3_pwm_on.set('Off')
        self.cbb_periph_d3_pwm_on.bind('<<ComboboxSelected>>', self.periph_d3_pwm)

        self.lb_periph_d3_pwm_presc = ttk.Label(self.frm_periph_d3, text='Prescaler')
        self.lb_periph_d3_pwm_presc.grid(row=2, column=1, sticky='w')

        self.var_periph_d3_pwm_presc = tk.IntVar(value=1)
        self.cbb_periph_d3_pwm_presc = ttk.Combobox(self.frm_periph_d3, width=5, textvariable=self.var_periph_d3_pwm_presc)
        self.cbb_periph_d3_pwm_presc.grid(row=2, column=2)
        self.cbb_periph_d3_pwm_presc.state(['readonly'])
        self.cbb_periph_d3_pwm_presc['values'] = list(range(1,5+1))
        self.cbb_periph_d3_pwm_presc.bind('<<ComboboxSelected>>', self.periph_d3_pwm)

        self.lb_periph_d3_pwm_top = ttk.Label(self.frm_periph_d3, text='Top')
        self.lb_periph_d3_pwm_top.grid(row=3, column=1, sticky='w')

        self.var_periph_d3_pwm_top = tk.IntVar(value=65535)
        self.spb_periph_d3_pwm_top = ttk.Spinbox(self.frm_periph_d3, from_=1, to=65535, increment=1000, textvariable=self.var_periph_d3_pwm_top, width=5, command=self.periph_d3_pwm)
        self.spb_periph_d3_pwm_top.grid(row=3, column=2)

        self.lb_periph_d3_pwm_duty = ttk.Label(self.frm_periph_d3, text='Duty (%)')
        self.lb_periph_d3_pwm_duty.grid(row=4, column=1, sticky='w')

        self.var_periph_d3_pwm_duty = tk.DoubleVar(value=10)
        self.spb_periph_d3_pwm_duty = ttk.Spinbox(self.frm_periph_d3, from_=1, to=100, increment=5, textvariable=self.var_periph_d3_pwm_duty, width=5, command=self.periph_d3_pwm)
        self.spb_periph_d3_pwm_duty.grid(row=4, column=2)

        # D4
        self.frm_periph_d4 = ttk.Frame(self.frm_periph, padding=(PAD, PAD))
        self.frm_periph_d4.grid(row=0, column=0, sticky='nsew', padx=PAD, pady=(0, PAD))
        self.frm_periph_d4.columnconfigure([0,1], weight=1)
        self.frm_periph_d4.rowconfigure([0], weight=1)

        self.lb_periph_d4_pin_change = ttk.Label(self.frm_periph_d4, text='Pin Change')
        self.lb_periph_d4_pin_change.grid(row=0, column=0)

        self.cbb_periph_d4_pin_change_on = ttk.Combobox(self.frm_periph_d4, width=7)
        self.cbb_periph_d4_pin_change_on.grid(row=0, column=1)
        self.cbb_periph_d4_pin_change_on.state(['readonly'])
        self.cbb_periph_d4_pin_change_on['values'] = ['On', 'Off']
        self.cbb_periph_d4_pin_change_on.set('Off')
        self.cbb_periph_d4_pin_change_on.bind('<<ComboboxSelected>>', self.periph_d4_pin_change)

        # D5
        self.frm_periph_d5 = ttk.Frame(self.frm_periph, padding=(PAD, PAD))
        self.frm_periph_d5.grid(row=0, column=0, sticky='nsew', padx=PAD, pady=(0, PAD))
        self.frm_periph_d5.columnconfigure([0,1,2,3], weight=1)
        self.frm_periph_d5.rowconfigure([0,1,2,3], weight=1)

        self.lb_periph_d5_adc = ttk.Label(self.frm_periph_d5, text='ADC')
        self.lb_periph_d5_adc.grid(row=0, column=0)

        self.var_periph_d5_adc = tk.StringVar()
        self.en_periph_d5_adc = ttk.Entry(self.frm_periph_d5, textvariable=self.var_periph_d5_adc, width=12)
        self.en_periph_d5_adc.state(['readonly'])
        self.en_periph_d5_adc.grid(row=0, column=1)

        self.bt_periph_d5_adc = ttk.Button(self.frm_periph_d5, text='Get', width=7, command=self.periph_d5_adc_read)
        self.bt_periph_d5_adc.grid(row=0, column=2)

        self.lb_periph_d5_adc_ref = ttk.Label(self.frm_periph_d5, text='Reference')
        self.lb_periph_d5_adc_ref.grid(row=1, column=1)

        self.cbb_periph_d5_adc_ref = ttk.Combobox(self.frm_periph_d5, width=4)
        self.cbb_periph_d5_adc_ref.grid(row=1, column=2)
        self.cbb_periph_d5_adc_ref.state(['readonly'])
        self.cbb_periph_d5_adc_ref['values'] = ['5V', '2.6V']
        self.cbb_periph_d5_adc_ref.set('5V')

        self.lb_periph_d5_adc_prescaler = ttk.Label(self.frm_periph_d5, text='Prescaler')
        self.lb_periph_d5_adc_prescaler.grid(row=2, column=1)

        self.var_periph_d5_adc_prescaler = tk.IntVar(value=6)
        self.cbb_periph_d5_adc_prescaler = ttk.Combobox(self.frm_periph_d5, width=3, textvariable=self.var_periph_d5_adc_prescaler)
        self.cbb_periph_d5_adc_prescaler.grid(row=2, column=2)
        self.cbb_periph_d5_adc_prescaler.state(['readonly'])
        self.cbb_periph_d5_adc_prescaler['values'] = list(range(1, 7+1))

        self.lb_periph_d5_adc_oversampling = ttk.Label(self.frm_periph_d5, text='Oversampling')
        self.lb_periph_d5_adc_oversampling.grid(row=3, column=1)

        self.var_periph_d5_adc_oversampling = tk.IntVar(value=0)
        self.cbb_periph_d5_adc_oversampling = ttk.Combobox(self.frm_periph_d5, width=3, textvariable=self.var_periph_d5_adc_oversampling)
        self.cbb_periph_d5_adc_oversampling.grid(row=3, column=2)
        self.cbb_periph_d5_adc_oversampling.state(['readonly'])
        self.cbb_periph_d5_adc_oversampling['values'] = list(range(0, 6+1))

        # Notebook
        self.nb_periph.add(self.frm_periph_d1, text=' D1 ')
        self.nb_periph.add(self.frm_periph_d2, text=' D2 ')
        self.nb_periph.add(self.frm_periph_d3, text=' D3 ')
        self.nb_periph.add(self.frm_periph_d4, text=' D4 ')
        self.nb_periph.add(self.frm_periph_d5, text=' D5 ')


    def widgets_led(self):
        self.frm_led.columnconfigure([0,1], weight=1)
        self.frm_led.rowconfigure([0,1], weight=1)

        # Color
        self.lbf_led_color = ttk.Labelframe(self.frm_led, text='Color', padding=(PAD, PAD))
        self.lbf_led_color.grid(row=0, column=0, sticky='nsew', padx=PAD, pady=PAD)
        self.lbf_led_color.columnconfigure([0,1,2], weight=1)
        self.lbf_led_color.rowconfigure([0,1,2,3], weight=1)

        self.var_led_color = tk.IntVar(value=0)
        self.scl_led_color = ttk.Scale(self.lbf_led_color, orient=tk.HORIZONTAL, length=170, from_=0, to=255, variable=self.var_led_color, command=self.led_color_scale)
        self.scl_led_color.grid(row=0, column=0, columnspan=2)

        self.var_led_color_str = tk.StringVar(value='RED')
        self.cbb_led_color = ttk.Combobox(self.lbf_led_color, width=7, textvariable=self.var_led_color_str)
        self.cbb_led_color.grid(row=0, column=2)
        self.cbb_led_color.state(['readonly'])
        self.cbb_led_color['values'] = list(D_LED_COLOR.keys())
        self.cbb_led_color.bind('<<ComboboxSelected>>', self.led_color_cbb)

        self.lb_led_color_fade = ttk.Label(self.lbf_led_color, text='Fade Dur. (ms)')
        self.lb_led_color_fade.grid(row=1, column=0)

        self.var_led_color_fade_dur = tk.IntVar(value=1000)
        self.spb_led_color_fade_dur = ttk.Spinbox(self.lbf_led_color, from_=500, to=10000, increment=500, textvariable=self.var_led_color_fade_dur, width=5)
        self.spb_led_color_fade_dur.grid(row=1, column=1)

        self.var_led_color_fade_str = tk.StringVar(value='RED')
        self.cbb_led_color_fade = ttk.Combobox(self.lbf_led_color, width=7, textvariable=self.var_led_color_fade_str)
        self.cbb_led_color_fade.grid(row=1, column=2)
        self.cbb_led_color_fade.state(['readonly'])
        self.cbb_led_color_fade['values'] = list(D_LED_COLOR.keys())
        self.cbb_led_color_fade.bind('<<ComboboxSelected>>', self.led_color_fade)

        self.lb_led_color_osc_cycles = ttk.Label(self.lbf_led_color, text='Osc. Cycles')
        self.lb_led_color_osc_cycles.grid(row=2, column=0)

        self.var_led_color_osc_cycles = tk.IntVar(value=3)
        self.spb_led_color_osc_cycles = ttk.Spinbox(self.lbf_led_color, from_=1, to=10, increment=1, textvariable=self.var_led_color_osc_cycles, width=5)
        self.spb_led_color_osc_cycles.grid(row=2, column=1)

        self.lb_led_color_osc_dur = ttk.Label(self.lbf_led_color, text='Osc. Dur. (ms)')
        self.lb_led_color_osc_dur.grid(row=3, column=0)

        self.var_led_color_osc_dur = tk.IntVar(value=3000)
        self.spb_led_color_osc_dur = ttk.Spinbox(self.lbf_led_color, from_=500, to=10000, increment=500, textvariable=self.var_led_color_osc_dur, width=5)
        self.spb_led_color_osc_dur.grid(row=3, column=1)

        self.bt_led_color_osc = ttk.Button(self.lbf_led_color, text='Oscillate', width=8, command=self.led_color_oscillate)
        self.bt_led_color_osc.grid(row=2, column=2, rowspan=2)

        # Intensity
        self.lbf_led_intensity = ttk.Labelframe(self.frm_led, text='Intensity', padding=(PAD, PAD))
        self.lbf_led_intensity.grid(row=0, column=1, sticky='nsew', padx=(0, PAD), pady=PAD)
        self.lbf_led_intensity.columnconfigure([0,1], weight=1)
        self.lbf_led_intensity.rowconfigure([0,1,2,3], weight=1)

        self.var_led_int_scale = tk.IntVar(value=0)
        self.scl_led_int = ttk.Scale(self.lbf_led_intensity, orient=tk.HORIZONTAL, length=170, from_=0, to=255, variable=self.var_led_int_scale, command=self.led_intensity_scale)
        self.scl_led_int.grid(row=0, column=0, columnspan=2)

        self.var_led_int_spb = tk.IntVar(value=0)
        self.spb_led_int = ttk.Spinbox(self.lbf_led_intensity, from_=0, to=255, increment=10, textvariable=self.var_led_int_spb, width=5, command=self.led_intensity_spb)
        self.spb_led_int.grid(row=0, column=2)

        self.lb_led_int_fade = ttk.Label(self.lbf_led_intensity, text='Fade Dur. (ms)')
        self.lb_led_int_fade.grid(row=1, column=0)

        self.var_led_int_fade_dur = tk.IntVar(value=1000)
        self.spb_led_int_fade_dur = ttk.Spinbox(self.lbf_led_intensity, from_=500, to=10000, increment=500, textvariable=self.var_led_int_fade_dur, width=5)
        self.spb_led_int_fade_dur.grid(row=1, column=1)

        self.var_led_int_fade = tk.IntVar(value=0)
        self.cbb_led_int_fade = ttk.Combobox(self.lbf_led_intensity, width=7, textvariable=self.var_led_int_fade)
        self.cbb_led_int_fade.grid(row=1, column=2)
        self.cbb_led_int_fade.state(['readonly'])
        self.cbb_led_int_fade['values'] = [0, 64, 128, 192, 255]
        self.cbb_led_int_fade.bind('<<ComboboxSelected>>', self.led_intensity_fade)

        self.lb_led_int_spacer1 = ttk.Label(self.lbf_led_intensity, text=' ')
        self.lb_led_int_spacer1.grid(row=2, column=0)

        self.lb_led_int_spacer2 = ttk.Label(self.lbf_led_intensity, text=' ')
        self.lb_led_int_spacer2.grid(row=3, column=0)


    def widgets_lamp(self):
        self.frm_lamp.columnconfigure([0,1], weight=1)
        self.frm_lamp.rowconfigure([0,1], weight=1)

        # Commands
        self.lbf_lamp_comm = ttk.Labelframe(self.frm_lamp, text='Commands', padding=(PAD, PAD))
        self.lbf_lamp_comm.grid(row=0, column=0, sticky='nsew', padx=PAD, pady=PAD)
        self.lbf_lamp_comm.columnconfigure([0,1], weight=1)
        self.lbf_lamp_comm.rowconfigure([0,1,2], weight=1)

        self.lb_lamp_mode = ttk.Label(self.lbf_lamp_comm, text='Lamp Mode')
        self.lb_lamp_mode.grid(row=0, column=0)

        self.cbb_lamp_mode_on = ttk.Combobox(self.lbf_lamp_comm, width=7)
        self.cbb_lamp_mode_on.grid(row=0, column=1)
        self.cbb_lamp_mode_on.state(['readonly'])
        self.cbb_lamp_mode_on['values'] = ['On', 'Off']
        self.cbb_lamp_mode_on.set('Off')
        self.cbb_lamp_mode_on.bind('<<ComboboxSelected>>', self.lamp_mode)

        self.lb_lamp_debug = ttk.Label(self.lbf_lamp_comm, text='Lamp Debug')
        self.lb_lamp_debug.grid(row=1, column=0)

        self.cbb_lamp_debug_on = ttk.Combobox(self.lbf_lamp_comm, width=7)
        self.cbb_lamp_debug_on.grid(row=1, column=1)
        self.cbb_lamp_debug_on.state(['readonly'])
        self.cbb_lamp_debug_on['values'] = ['On', 'Off']
        self.cbb_lamp_debug_on.set('Off')
        self.cbb_lamp_debug_on.bind('<<ComboboxSelected>>', self.lamp_debug_on)

        self.bt_lamp_stats = ttk.Button(self.lbf_lamp_comm, text='Get Stats', width=12, command=self.lamp_stats)
        self.bt_lamp_stats.grid(row=2, column=0, columnspan=2)

        # Output
        self.lbf_lamp_out = ttk.Labelframe(self.frm_lamp, text='Output', padding=(PAD, PAD))
        self.lbf_lamp_out.grid(row=0, column=1, sticky='nsew', padx=(0, PAD), pady=PAD)
        self.lbf_lamp_out.columnconfigure([0], weight=1)
        self.lbf_lamp_out.rowconfigure([0], weight=1)

        self.txt_lamp = tk.Text(self.lbf_lamp_out, width=23, state='disabled', wrap='word', height=8)
        self.txt_lamp.grid(row=0, column=0, sticky='nsew')


    def widgets_state(self):
        # HEALTH
        if (not self.rng.health_startup_enabled) and (not self.rng.health_continuous_enabled):
            # Disable notebook tab
            tab_id = [tab_id for tab_id in self.nb.tabs() if 'health' in tab_id][0]
            self.nb.tab(tab_id, state=['disabled'])
        elif not self.rng.health_startup_enabled:
            # Disable health startup Labelframe
            self.lbf_health_startup.state(['disabled'])
            for child in self.lbf_health_startup.winfo_children():
                child.configure(state='disable')
        elif not self.rng.health_continuous_enabled:
            # Disable health startup Labelframe
            self.lbf_health_cont.state(['disabled'])
            for child in self.lbf_health_cont.winfo_children():
                child.configure(state='disable')

        # PERIPH
        if not self.rng.peripherals_enabled:
            # Disable notebook tab
            tab_id = [tab_id for tab_id in self.nb.tabs() if 'periph' in tab_id][0]
            self.nb.tab(tab_id, state=['disabled'])

        # LED
        if not self.rng.led_enabled:
            # Disable notebook tab
            tab_id = [tab_id for tab_id in self.nb.tabs() if 'led' in tab_id][0]
            self.nb.tab(tab_id, state=['disabled'])

        # LAMP
        if not (self.rng.led_enabled and self.rng.lamp_enabled):
            # Disable notebook tab
            tab_id = [tab_id for tab_id in self.nb.tabs() if 'lamp' in tab_id][0]
            self.nb.tab(tab_id, state=['disabled'])


    def notebook_tab_change(self, tk_event=None):
        # Retrieve info and update widgets
        if 'eeprom' in self.nb.select():
            self.eeprom_get()

        elif 'rng' in self.nb.select():
            self.rng_setup_get()
            self.rng_output_set('', '')

        elif 'health' in self.nb.select():
            self.health_startup_get()

        elif 'periph' in self.nb.select():
            self.periph_digi_state_update()

        elif 'led' in self.nb.select():
            self.led_color_scale()

        elif 'lamp' in self.nb.select():
            lamp_mode = 'On' if self.rng.lamp_mode else 'Off'
            lamp_debug = 'On' if self.rng.lamp_debug else 'Off'
            self.cbb_lamp_mode_on.set(lamp_mode)
            self.cbb_lamp_debug_on.set(lamp_debug)

        # Stop lamp
        if self.rng.lamp_mode:
            self.rng.snd_lamp_mode(False)

        # Stop bytes stream
        if self.rng.rng_streaming:
            self.rng_gen_byte_stream_stop()


    def eeprom_get(self):
        # Firmware
        firmware_dict = self.rng.get_eeprom_firmware()
        if firmware_dict:
            self.var_eeprom_firmw_version.set(firmware_dict['version'])
            modules_enabled = [key for key in firmware_dict if (key != 'version' and firmware_dict[key] == True)]
            modules_enabled = [m.replace('_enabled', '') for m in modules_enabled]
            self.var_eeprom_firmw_modules.set(modules_enabled)

        # PWM
        pwm = self.rng.get_eeprom_pwm()
        self.cbb_eeprom_pwm_freq.set(pwm['freq_str'])
        self.var_eeprom_pwm_duty.set(pwm['duty'])

        # RNG
        rng = self.rng.get_eeprom_rng()
        self.var_eeprom_rng_si.set(rng['sampling_interval_us'])

        # LED
        if self.rng.led_enabled:
            led = self.rng.get_eeprom_led()
            self.cbb_eeprom_led_attached.set('True' if led['led_attached'] else 'False')

        # LAMP
        if self.rng.led_enabled and self.rng.lamp_enabled:
            lamp = self.rng.get_eeprom_lamp()
            self.var_eeprom_lamp_exp_dur.set(lamp['exp_dur_max_ms'] // 1000)
            self.var_eeprom_lamp_z_sig.set('{:.3f}'.format(lamp['exp_z_significant']))
            self.var_eeprom_lamp_mag_smooth.set(lamp['exp_mag_smooth_n_trials'])


    def eeprom_set(self):
        if tkm.askyesno(message=('Save parameters to EEPROM?'), detail=''):
            # PWM
            freq_str = self.cbb_eeprom_pwm_freq.get()
            duty = self.var_eeprom_pwm_duty.get()
            self.rng.snd_eeprom_pwm(D_PWM_FREQ[freq_str], duty)

            # RNG
            sampling_interval_us = self.var_eeprom_rng_si.get()
            self.rng.snd_eeprom_rng(sampling_interval_us)

            # LED
            if self.rng.led_enabled:
                led_attached = True if self.cbb_eeprom_led_attached.get() == 'True' else False
                self.rng.snd_eeprom_led(led_attached)

            # LAMP
            if self.rng.led_enabled and self.rng.lamp_enabled:
                exp_dur_max_ms = self.var_eeprom_lamp_exp_dur.get() * 1000
                exp_z_significant = self.var_eeprom_lamp_z_sig.get()
                exp_mag_smooth_n_trials = self.var_eeprom_lamp_mag_smooth.get()
                self.rng.snd_eeprom_lamp(exp_dur_max_ms, exp_z_significant, exp_mag_smooth_n_trials)


    def eeprom_set_defaults(self):
        if tkm.askyesno(message=('Restore EEPROM to default values?'), detail=''):
            self.rng.snd_eeprom_reset_to_default()
            self.eeprom_get()


    def rng_notebook_tab_change(self, tk_event=None):
        # Clear data txts
        self.rng_output_set('', '')

        # Stop bytes stream
        if self.rng.rng_streaming:
            self.rng_gen_byte_stream_stop()


    def rng_setup_get(self):
        # PWM
        pwm = self.rng.get_pwm_setup()
        self.cbb_pwm_freq.set(pwm['freq_str'])
        self.var_pwm_duty.set(pwm['duty'])

        # RNG
        rng = self.rng.get_rng_setup()
        self.var_rng_si.set(rng['sampling_interval_us'])


    def rng_setup_set(self):
        # PWM
        freq_str = self.cbb_pwm_freq.get()
        duty = self.var_pwm_duty.get()
        self.rng.snd_pwm_setup(D_PWM_FREQ[freq_str], duty)

        # RNG
        sampling_interval_us = self.var_rng_si.get()
        self.rng.snd_rng_setup(sampling_interval_us)


    def rng_output_set(self, data_a, data_b):
        if data_a is None:
            data_a = ''
        data_a_fmt = '{}'.format(data_a).replace('[', '').replace(']', '').replace('\n', '')
        self.txt_rng_a.configure(state='normal')
        self.txt_rng_a.delete(1.0, 'end')
        self.txt_rng_a.insert(1.0, data_a_fmt)
        self.txt_rng_a.configure(state='disabled')

        if data_b is None:
            data_b = ''
        data_b_fmt = '{}'.format(data_b).replace('[', '').replace(']', '').replace('\n', '')
        self.txt_rng_b.configure(state='normal')
        self.txt_rng_b.delete(1.0, 'end')
        self.txt_rng_b.insert(1.0, data_b_fmt)
        self.txt_rng_b.configure(state='disabled')


    def rng_gen_pulse_count(self):
        n = self.var_rng_data_ammount.get()
        if n > CTRL_PANEL_N_MAX:
            n = CTRL_PANEL_N_MAX
            self.var_rng_data_ammount.set(CTRL_PANEL_N_MAX)

        pc_a, pc_b = self.rng.get_rng_pulse_counts(n, output_type='array')
        self.rng_output_set(pc_a, pc_b)


    def rng_gen_bit(self):
        bit_src = self.cbb_rng_data_bit_src.get()
        bit_src_id = D_RNG_BIT_SRC[bit_src]

        if bit_src == 'AB':
            bit_a, bit_b = self.rng.get_rng_bits(bit_src_id)
        elif bit_src == 'AB_RND':
            rng, bit = self.rng.get_rng_bits(bit_src_id)
            bit_a, bit_b = (bit, '') if rng == 'A' else ('', bit)
        elif bit_src == 'B':
            bit_a = ''
            bit_b = self.rng.get_rng_bits(bit_src_id)
        else:
            bit_a = self.rng.get_rng_bits(bit_src_id)
            bit_b = ''

        self.rng_output_set(bit_a, bit_b)


    def rng_gen_byte(self):
        n = self.var_rng_data_ammount.get()
        if n > CTRL_PANEL_N_MAX:
            n = CTRL_PANEL_N_MAX
            self.var_rng_data_ammount.set(CTRL_PANEL_N_MAX)

        postproc = self.cbb_rng_data_byte_pp.get()
        postproc_id = D_RNG_POSTPROC[postproc]

        bytes_a, bytes_b = self.rng.get_rng_bytes(n, postproc_id, output_type='array')        
        self.rng_output_set(bytes_a, bytes_b)


    def rng_gen_integer(self):
        n = self.var_rng_num_ammount.get()
        if n > CTRL_PANEL_N_MAX:
            n = CTRL_PANEL_N_MAX
            self.var_rng_num_ammount.set(CTRL_PANEL_N_MAX)
        min = self.var_rng_num_min_int.get()
        max = self.var_rng_num_max_int.get()

        delta = max - min
        if delta < 2**8:
            ints = self.rng.get_rng_int8s(n, delta, output_type='array').astype('u2')
        elif delta < 2**16:
            ints = self.rng.get_rng_int16s(n, delta, output_type='array').astype('u4')

        if ints is not None:
            ints += min
            self.rng_output_set(ints, '')


    def rng_gen_float(self):
        n = self.var_rng_num_ammount.get()
        if n > CTRL_PANEL_N_MAX:
            n = CTRL_PANEL_N_MAX
            self.var_rng_num_ammount.set(CTRL_PANEL_N_MAX)

        min = self.var_rng_num_min_float.get()
        max = self.var_rng_num_max_float.get()
        delta = max - min
        if delta < 0:
            self.lg.error('{} Floats: Provide delta >= 0'.format(self.name))
            return

        floats = self.rng.get_rng_floats(n, output_type='array')
        if floats is not None:
            floats = min + delta * floats            
            self.rng_output_set(floats, '')


    def rng_gen_byte_stream_start(self):
        n = self.var_rng_stream_ammount.get()
        if n > CTRL_PANEL_N_MAX:
            n = CTRL_PANEL_N_MAX
            self.var_rng_stream_ammount.set(CTRL_PANEL_N_MAX)

        interval_ms = self.var_rng_stream_interval.get()
        if interval_ms > RNG_BYTE_STREAM_MAX_INTERVAL_MS:
            interval_ms = RNG_BYTE_STREAM_MAX_INTERVAL_MS
            self.var_rng_stream_interval.set(RNG_BYTE_STREAM_MAX_INTERVAL_MS)

        postproc = self.cbb_rng_stream_byte_pp.get()
        postproc_id = D_RNG_POSTPROC[postproc]

        # Register callback
        self.rng.cbkreg_stream_data_available(self.rng_byte_stream_data)

        # Start stream
        self.rng.snd_rng_byte_stream_start(n, interval_ms, postproc_id)


    def rng_gen_byte_stream_stop(self, tk_event=None):
        if self.rng.rng_streaming:
            self.rng.snd_rng_byte_stream_stop()


    def rng_byte_stream_data(self):
        bytes_a, bytes_b = self.rng.get_rng_byte_stream_data(output_type='array')
        self.rng_output_set(bytes_a, bytes_b)


    def health_results_set(self, results_str):
        self.txt_health_results.configure(state='normal')
        self.txt_health_results.delete(1.0, 'end')
        self.txt_health_results.insert(1.0, results_str)
        self.txt_health_results.configure(state='disabled')


    def health_startup_run(self):
        self.rng.snd_health_startup_run()
        self.after(750, self.health_startup_get)


    def health_startup_get(self):
        success, res = self.rng.get_health_startup_results()
        res_str = 'Pulse Count = {}\n  RNG_A = {:.1f}  RNG_B = {:.1f}  TRESH = {:.1f}\n\n'\
                  'Pulse Count Difference = {}\n  RNG_A = {:.1f}  RNG_B = {:.1f}  TRESH = {:.1f}\n\n'\
                  'Bit Bias = {}\n  RNG_A = {:.2f}  RNG_B = {:.2f}  TRESH = {:.2f}\n\n'\
                  'Byte Bias = {}\n  RNG_A = {:.1f}  RNG_B = {:.1f}  TRESH = {:.1f}\n\n'\
                  'Startup Result = {}'\
                  .format(*res['pulse_count'], *res['pulse_count_diff'], *res['bit_bias'], *res['byte_bias'], success)

        self.health_results_set(res_str)


    def health_continuous_get(self):
        errors_n, res = self.rng.get_health_continuous_errors()
        res_str = 'Repetitive Count Errors\n  RNG_A = {}\n  RNG_B = {}\n\n'\
                  'Adaptative Proportion Errors\n  RNG_A = {}\n  RNG_B = {}\n\n'\
                  'Total Errors = {}'\
                  .format(res['repetitive_count_a'], res['repetitive_count_b'],
                          res['adaptative_proportion_a'], res['adaptative_proportion_b'], errors_n)

        self.health_results_set(res_str)


    def periph_digi_state_update(self, tk_event=None):
        # Update mode and state
        port_id = self.var_periph_port.get()
        state, mode = self.rng.get_periph_digi_state(port_id)
        self.cbb_periph_mode.set(mode)
        self.var_periph_state.set(state)


    def periph_digi_mode(self, tk_event=None):
        port_id = self.var_periph_port.get()
        mode = self.cbb_periph_mode.get()
        mode_id = 0 if mode == 'INPUT' else 1

        self.rng.snd_periph_digi_mode(port_id, mode_id)


    def periph_digi_state_get(self):
        port_id = self.var_periph_port.get()

        # Change mode?
        if self.cbb_periph_mode.get() == 'OUTPUT':
            self.cbb_periph_mode.set('INPUT')
            self.periph_digi_mode()

        state, mode = self.rng.get_periph_digi_state(port_id)
        if state is not None:
            self.var_periph_state.set(state)


    def periph_digi_state_set(self):
        port_id = self.var_periph_port.get()

        # Change mode?
        if self.cbb_periph_mode.get() == 'INPUT':
            self.cbb_periph_mode.set('OUTPUT')
            self.periph_digi_mode()

        state = self.var_periph_state.get()
        self.rng.snd_periph_digi_state(port_id, state)


    def periph_digi_pulse(self):
        port_id = self.var_periph_port.get()

        pulse_dur_us = self.var_periph_pulse_dur.get()
        if pulse_dur_us > 100000:
            pulse_dur_us = 100000
            self.var_periph_pulse_dur.set(100000)

        # Change mode?
        if self.cbb_periph_mode.get() == 'INPUT':
            self.cbb_periph_mode.set('OUTPUT')
            self.periph_digi_mode()

        self.rng.snd_periph_digi_pulse(port_id, pulse_dur_us)


    def periph_d1_timing_debug(self, tk_event=None):
        on = True if self.cbb_periph_d1_timing_dbg.get() == 'On' else False
        self.rng.snd_rng_timing_debug_d1(on)


    def periph_d1_trigger_input(self, tk_event=None):
        on = True if self.cbb_periph_d1_trigger_on.get() == 'On' else False
        self.rng.snd_periph_d1_trigger_input(on)


    def periph_d1_comparator(self, tk_event=None):
        neg = True if self.cbb_periph_d1_comparator_neg.get() == 'Neg=D5' else False
        on = True if self.cbb_periph_d1_comparator_on.get() == 'On' else False
        self.rng.snd_periph_d1_comparator(neg, on)


    def periph_d1_delay_test(self, tk_event=None):
        delay_us = self.var_periph_d1_delay_dur.get()
        if delay_us > 100000:
            delay_us = 100000
            self.var_periph_d1_delay_dur.set(100000)

        self.rng.snd_periph_d1_delay_us_test(delay_us)


    def periph_d2_input_capture(self, tk_event=None):
        on = True if self.cbb_periph_d2_input_capture_on.get() == 'On' else False
        self.rng.snd_periph_d2_input_capture(on)

        # Register callback
        if on:
            self.rng.cbkreg_d2_input_capture_available(self.periph_d2_input_capture_data)
        else:
            self.rng.cbkreg_d2_input_capture_available(None)


    def periph_d2_input_capture_data(self):
        interval_s = self.rng.get_periph_d2_input_capture()
        self.var_periph_d2_input_capture_interval.set('{:.3f}'.format(interval_s))


    def periph_d3_trigger_output(self, tk_event=None):
        on = True if self.cbb_periph_d3_trigger_out_on.get() == 'On' else False

        interval_ms = self.var_periph_d3_trigger_out_interval.get()
        if interval_ms is None:
            return
        if interval_ms > RNG_BYTE_STREAM_MAX_INTERVAL_MS:
            interval_ms = RNG_BYTE_STREAM_MAX_INTERVAL_MS
            self.var_periph_d3_trigger_out_interval.set(RNG_BYTE_STREAM_MAX_INTERVAL_MS)

        self.rng.snd_periph_d3_timer3_trigger_output(interval_ms, on)


    def periph_d3_pwm(self, tk_event=None):
        on = True if self.cbb_periph_d3_pwm_on.get() == 'On' else False

        freq_prescaler = self.var_periph_d3_pwm_presc.get()
        top = self.var_periph_d3_pwm_top.get()
        duty = int(self.var_periph_d3_pwm_duty.get()/100 * 65535)

        self.rng.snd_periph_d3_timer3_pwm(freq_prescaler, top, duty, on)


    def periph_d4_pin_change(self, tk_event=None):
        on = True if self.cbb_periph_d4_pin_change_on.get() == 'On' else False
        self.rng.snd_periph_d4_pin_change(on)


    def periph_d5_adc_read(self):
        ref_5v = True if self.cbb_periph_d5_adc_ref.get() == '5V' else False
        clk_prescaler = self.var_periph_d5_adc_prescaler.get()
        oversampling_n_bits = self.var_periph_d5_adc_oversampling.get()

        adc_read = self.rng.get_periph_d5_adc_read(ref_5v, clk_prescaler, oversampling_n_bits, on=True)
        self.var_periph_d5_adc.set('{:.3f}'.format(adc_read))


    def led_color_scale(self, tk_event=None):
        color_hue = self.var_led_color.get()
        intensity = self.var_led_int_scale.get()

        color_str = ''
        if color_hue in D_LED_COLOR_INV:
            color_str = D_LED_COLOR_INV[color_hue]
        self.var_led_color_str.set(color_str)
        self.rng.snd_led_color(color_hue, intensity)


    def led_color_cbb(self, tk_event=None):
        color_str = self.var_led_color_str.get()
        color_hue = D_LED_COLOR[color_str]
        intensity = self.var_led_int_scale.get()

        self.var_led_color.set(color_hue)
        self.rng.snd_led_color(color_hue, intensity)


    def led_color_fade(self, tk_event=None):
        color_str = self.var_led_color_fade_str.get()
        color_hue = D_LED_COLOR[color_str]
        duration_ms = self.var_led_color_fade_dur.get()

        if self.rng.snd_led_color_fade(color_hue, duration_ms):
            self.after(duration_ms, lambda: [self.var_led_color.set(color_hue), self.var_led_color_str.set(color_str)])


    def led_color_oscillate(self):
        n_cycles = self.var_led_color_osc_cycles.get()
        duration_ms = self.var_led_color_osc_dur.get()
        self.rng.snd_led_color_oscillate(n_cycles, duration_ms)


    def led_intensity_scale(self, tk_event=None):
        intensity = self.var_led_int_scale.get()

        self.var_led_int_spb.set(intensity)
        self.rng.snd_led_intensity(intensity)


    def led_intensity_spb(self, tk_event=None):
        intensity = self.var_led_int_spb.get()

        self.var_led_int_scale.set(intensity)
        self.rng.snd_led_intensity(intensity)


    def led_intensity_fade(self, tk_event=None):
        intensity = self.var_led_int_fade.get()
        duration_ms = self.var_led_int_fade_dur.get()

        if self.rng.snd_led_intensity_fade(intensity, duration_ms):
            self.after(duration_ms, lambda: [self.var_led_int_scale.set(intensity), self.var_led_int_spb.set(intensity)])


    def lamp_mode(self, tk_event=None):
        on = True if self.cbb_lamp_mode_on.get() == 'On' else False

        self.rng.snd_lamp_mode(on)


    def lamp_debug_on(self, tk_event=None):
        on = True if self.cbb_lamp_debug_on.get() == 'On' else False

        self.rng.snd_lamp_debug(on)

        # Register callback
        if on:
            self.rng.cbkreg_lamp_debug(self.lamp_debug_data)
        else:
            self.rng.cbkreg_lamp_debug(None)


    def lamp_output_set(self, output_str):
        self.txt_lamp.configure(state='normal')
        self.txt_lamp.delete(1.0, 'end')
        self.txt_lamp.insert(1.0, output_str)
        self.txt_lamp.configure(state='disabled')


    def lamp_debug_data(self):
        dbg_dict = self.rng.get_lamp_debug_data()

        debug_str = 'LAMP Debug\n\nz={:+1.2f}, mag={:3.0f}, mag_avg={:3.0f}'\
                    .format(dbg_dict['z'], dbg_dict['mag'], dbg_dict['mag_avg'])
        self.lamp_output_set(debug_str)


    def lamp_stats(self, tk_event=None):
        stats = self.rng.get_lamp_statistics()
        exp_n = stats['exp_n']

        if exp_n:
            res_str = 'LAMP Statistics\n\n'\
                      'Total of {} experiments, where {} ({:.2f}%) reached statistical significance\n\n'\
                      'Color distribution (%):\n'\
                      '  R={:.2f} O={:.2f} Y={:.2f} G={:.2f}\n'\
                      '  C={:.2f} B={:.2f} PU={:.2f} PI={:.2f}\n'\
                      .format(exp_n, stats['exp_n_zsig'], stats['exp_n_zsig']/exp_n*100,
                              stats['red']/exp_n*100, stats['orange']/exp_n*100, stats['yellow']/exp_n*100,
                              stats['green']/exp_n*100, stats['cyan']/exp_n*100, stats['blue']/exp_n*100,
                              stats['purple']/exp_n*100, stats['pink']/exp_n*100)

        else:
            res_str = 'LAMP Statistics\n\n'\
                      'No experiment recorded'

        self.lamp_output_set(res_str)


rava_subapp_control_panel = {'class':RAVA_SUBAPP_CTRL_PANEL,
                             'menu_title':'Control Panel',
                             'show_button':True,
                             'use_rng':True
                             }