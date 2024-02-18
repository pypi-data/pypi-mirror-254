"""
Copyright (c) 2024 Gabriel Guerrer

Distributed under the MIT license - See LICENSE for details
"""

"""
The Acquisition sub-app features a GUI interface for utilizing the 
RAVA_ACQUISITION class, which allows the generation of files comprising pulse 
counts, bytes, or numbers extracted from a RAVA device.
"""

from glob import glob
import os
import os.path
import time
import datetime

import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as tkm

import numpy as np

from rng_rava.acq import RAVA_ACQUISITION, ACQ_BYTES_RNG_OUT, get_ammount_prefix_number, get_ammount_prefix_str
from rng_rava.rava_defs import D_RNG_POSTPROC
from rng_rava.tk import RAVA_SUBAPP

### VARS

PAD = 10


### RAVA_SUBAPP_ACQUISITION

class RAVA_SUBAPP_ACQUISITION(RAVA_SUBAPP):

    cfg_default_str = '''
    [ACQUISITION]        
    chunk_bytes = 10000
    chunk_numbers = 5000
    delete_incomplete = True
    path_out = 
    '''

    def __init__(self, parent):
        ## Initialize RAVA_SUBAPP
        name = 'RAVA_SUBAPP ACQUISITION'
        win_title = 'Acquisition'
        win_geometry = '510x280'
        win_resizable = False
        if not super().__init__(parent, name=name, win_title=win_title, win_geometry=win_geometry, win_resizable=win_resizable):
            return

        # Windows
        self.win_progress = WIN_PROGRESS(self)
        self.win_progress.hide()        

        # Widgets
        self.nb = ttk.Notebook(self, padding=PAD)        
        self.nb.grid(row=0, column=0, sticky='nsew')

        self.frm_pcs = ttk.Frame(self, name='pulsecounts')
        self.frm_pcs.grid(row=0, column=0, sticky='nsew')
        self.pcs_widgets()

        self.frm_bytes = ttk.Frame(self, name='bytes')
        self.frm_bytes.grid(row=0, column=0, sticky='nsew')
        self.bytes_widgets()

        self.nfrm_nums = ttk.Frame(self, name='numbers')
        self.nfrm_nums.grid(row=0, column=0, sticky='nsew')
        self.nums_widgets()

        self.nb.add(self.frm_pcs, text=' Pulse Counts ')
        self.nb.add(self.frm_bytes, text=' Bytes ')
        self.nb.add(self.nfrm_nums, text=' Numbers ')
        
        ## Start
        
        # Config        
        delete_incomplete = self.master.cfg_read('ACQUISITION', 'delete_incomplete', bool)
        out_path = self.master.cfg_read('ACQUISITION', 'path_out')
        self.var_acq_path.set(out_path)

        # RAVA_ACQUISITION
        self.rng_acq = RAVA_ACQUISITION(delete_incomplete=delete_incomplete)
        self.rng_acq.cbkreg_progress(self.win_progress.prog_update)        
        

    def pcs_widgets(self):
        self.frm_pcs.columnconfigure([0], weight=1)
        self.frm_pcs.columnconfigure([1], weight=7)
        self.frm_pcs.rowconfigure([0,1,2], weight=1)

        ## Path
        self.lb_pcs_path = ttk.Label(self.frm_pcs, text='Out Path')
        self.lb_pcs_path.grid(row=0, column=0)

        self.var_acq_path = tk.StringVar(value='')
        self.en_pcs_path = ttk.Entry(self.frm_pcs, textvariable=self.var_acq_path)
        self.en_pcs_path.grid(row=0, column=1, sticky='ew')

        self.bt_pcs_path_search = ttk.Button(self.frm_pcs, width=2, text='...', command=self.acq_path_search)
        self.bt_pcs_path_search.grid(row=0, column=2, padx=PAD)

        ## PCs parameters
        self.frm_pcs_pars = ttk.Frame(self.frm_pcs, name='pcs_pars')
        self.frm_pcs_pars.grid(row=1, column=0, columnspan=3, sticky='nsew', padx=2*PAD)
        self.frm_pcs_pars.columnconfigure([0,1,2,3], weight=1)
        self.frm_pcs_pars.rowconfigure([0,1,2], weight=1)

        # Sampling Interval
        self.lb_pcs_si = ttk.Label(self.frm_pcs_pars, text='SI (min, max, step)')
        self.lb_pcs_si.grid(row=0, column=0, sticky='w')

        self.var_pcs_si_min = tk.IntVar(value=10)
        self.spb_pcs_si_min = ttk.Spinbox(self.frm_pcs_pars, from_=1, to=100, increment=1, textvariable=self.var_pcs_si_min, width=8)
        self.spb_pcs_si_min.grid(row=0, column=1, sticky='w')

        self.var_pcs_si_max = tk.IntVar(value=10)
        self.spb_pcs_si_max = ttk.Spinbox(self.frm_pcs_pars, from_=1, to=100, increment=1, textvariable=self.var_pcs_si_max, width=8)
        self.spb_pcs_si_max.grid(row=0, column=2, sticky='w')

        self.var_pcs_si_step = tk.IntVar(value=1)
        self.spb_pcs_si_step = ttk.Spinbox(self.frm_pcs_pars, from_=1, to=100, increment=1, textvariable=self.var_pcs_si_step, width=8)
        self.spb_pcs_si_step.grid(row=0, column=3, sticky='w')

        # N PCs
        self.lb_pcs_n = ttk.Label(self.frm_pcs_pars, text='N PCs per SI')
        self.lb_pcs_n.grid(row=1, column=0, sticky='w')

        self.var_pcs_n = tk.DoubleVar(value=50)
        self.spb_pcs_n = ttk.Spinbox(self.frm_pcs_pars, from_=1, to=999, increment=1, textvariable=self.var_pcs_n, width=8)
        self.spb_pcs_n.grid(row=1, column=1, sticky='w')

        self.cbb_pcs_n_mult = ttk.Combobox(self.frm_pcs_pars, width=8)
        self.cbb_pcs_n_mult.grid(row=1, column=2, sticky='w')
        self.cbb_pcs_n_mult.state(['readonly'])
        self.cbb_pcs_n_mult['values'] = ['', 'K', 'M', 'G', 'T']
        self.cbb_pcs_n_mult.set('K')

        # Preset
        self.lb_pcs_preset = ttk.Label(self.frm_pcs_pars, text='Preset')
        self.lb_pcs_preset.grid(row=2, column=0, sticky='w')
        
        self.cbb_pcs_preset = ttk.Combobox(self.frm_pcs_pars, width=8, )
        self.cbb_pcs_preset.grid(row=2, column=1, sticky='w')
        self.cbb_pcs_preset.state(['readonly'])
        self.cbb_pcs_preset['values'] = ['Report', 'Detailed']        
        self.cbb_pcs_preset.bind('<<ComboboxSelected>>', self.pcs_preset_sel)
        self.cbb_pcs_preset.set('Report')

        ## Generate
        self.bt_pcs_generate = ttk.Button(self.frm_pcs, text='Generate', command=self.pcs_generate)
        self.bt_pcs_generate.grid(row=2, column=0, columnspan=3)


    def bytes_widgets(self):
        self.frm_bytes.columnconfigure([0], weight=1)
        self.frm_bytes.columnconfigure([1], weight=7)
        self.frm_bytes.rowconfigure([0,1,2], weight=1)

        ## Path
        self.lb_bytes_path = ttk.Label(self.frm_bytes, text='Out Path')
        self.lb_bytes_path.grid(row=0, column=0)

        self.en_bytes_path = ttk.Entry(self.frm_bytes, textvariable=self.var_acq_path)
        self.en_bytes_path.grid(row=0, column=1, sticky='ew')

        self.bt_bytes_path_search = ttk.Button(self.frm_bytes, width=2, text='...', command=self.acq_path_search)
        self.bt_bytes_path_search.grid(row=0, column=2, padx=PAD)

        ## Bin pars
        self.frm_bytes_pars = ttk.Frame(self.frm_bytes, name='binary_pars')
        self.frm_bytes_pars.grid(row=1, column=0, columnspan=3, sticky='nsew', padx=2*PAD)
        self.frm_bytes_pars.columnconfigure([0,1,2,3], weight=1)
        self.frm_bytes_pars.rowconfigure([0,1,2], weight=1)

        # N bytes
        self.lb_bytes_n = ttk.Label(self.frm_bytes_pars, text='N Bytes')
        self.lb_bytes_n.grid(row=0, column=0, sticky='w')

        self.var_bytes_n = tk.DoubleVar(value=125)
        self.spb_bytes_n = ttk.Spinbox(self.frm_bytes_pars, from_=1, to=999, increment=1, textvariable=self.var_bytes_n, width=12)
        self.spb_bytes_n.grid(row=0, column=1, sticky='w')

        self.cbb_bytes_n_mult = ttk.Combobox(self.frm_bytes_pars, width=8)
        self.cbb_bytes_n_mult.grid(row=0, column=2, sticky='w')
        self.cbb_bytes_n_mult.state(['readonly'])
        self.cbb_bytes_n_mult['values'] = ['B', 'KB', 'MB', 'GB', 'TB']
        self.cbb_bytes_n_mult.set('MB')

        # Post-proc
        self.lb_bytes_postproc = ttk.Label(self.frm_bytes_pars, text='Post-proc')
        self.lb_bytes_postproc.grid(row=1, column=0, sticky='w')

        self.cbb_bytes_postproc = ttk.Combobox(self.frm_bytes_pars, width=13)
        self.cbb_bytes_postproc.grid(row=1, column=1, sticky='w')
        self.cbb_bytes_postproc.state(['readonly'])
        self.cbb_bytes_postproc['values'] = list(D_RNG_POSTPROC.keys())
        self.cbb_bytes_postproc.set('NONE')

        # Output rng cores
        self.lb_bytes_rngout = ttk.Label(self.frm_bytes_pars, text='RNG Out')
        self.lb_bytes_rngout.grid(row=1, column=2, sticky='w')

        self.cbb_bytes_rngout = ttk.Combobox(self.frm_bytes_pars, width=10)
        self.cbb_bytes_rngout.grid(row=1, column=3, sticky='w')
        self.cbb_bytes_rngout.state(['readonly'])
        self.cbb_bytes_rngout['values'] = ACQ_BYTES_RNG_OUT
        self.cbb_bytes_rngout.set('AB')

        # Preset
        self.lb_bytes_preset = ttk.Label(self.frm_bytes_pars, text='Preset')
        self.lb_bytes_preset.grid(row=2, column=0, sticky='w')
        
        self.cbb_bytes_preset = ttk.Combobox(self.frm_bytes_pars, width=8, )
        self.cbb_bytes_preset.grid(row=2, column=1, sticky='w')
        self.cbb_bytes_preset.state(['readonly'])
        self.cbb_bytes_preset['values'] = ['Report']        
        self.cbb_bytes_preset.bind('<<ComboboxSelected>>', self.bytes_preset_sel)
        self.cbb_bytes_preset.set('Report')

        ## Generate
        self.bt_bytes_generate = ttk.Button(self.frm_bytes, text='Generate', command=self.bytes_generate)
        self.bt_bytes_generate.grid(row=2, column=0, columnspan=3)


    def nums_widgets(self):
        self.nfrm_nums.columnconfigure([0], weight=1)
        self.nfrm_nums.columnconfigure([1], weight=7)
        self.nfrm_nums.rowconfigure([0,1,2], weight=1)

        ## Path
        self.lb_nums_path = ttk.Label(self.nfrm_nums, text='Out Path')
        self.lb_nums_path.grid(row=0, column=0)

        self.en_nums_path = ttk.Entry(self.nfrm_nums, textvariable=self.var_acq_path)
        self.en_nums_path.grid(row=0, column=1, sticky='ew')

        self.bt_nums_path_search = ttk.Button(self.nfrm_nums, width=2, text='...', command=self.acq_path_search)
        self.bt_nums_path_search.grid(row=0, column=2, padx=PAD)

        ## Number options
        self.nfrm_nums_pars = ttk.Frame(self.nfrm_nums, name='number_pars')
        self.nfrm_nums_pars.grid(row=1, column=0, columnspan=3, sticky='nsew', padx=2*PAD)
        self.nfrm_nums_pars.columnconfigure([0,1,2,3], weight=1)
        self.nfrm_nums_pars.rowconfigure([0,1,2], weight=1)

        # Number type
        self.lb_nums_type = ttk.Label(self.nfrm_nums_pars, text='Number (type, N)')
        self.lb_nums_type.grid(row=0, column=0, sticky='w')
        
        self.cbb_nums_type = ttk.Combobox(self.nfrm_nums_pars, width=9)
        self.cbb_nums_type.grid(row=0, column=1, sticky='w')
        self.cbb_nums_type.state(['readonly'])
        self.cbb_nums_type['values'] = ['INT', 'FLOAT']
        self.cbb_nums_type.set('INT')
        self.cbb_nums_type.bind('<<ComboboxSelected>>', self.nums_type_sel)

        self.var_nums_n = tk.DoubleVar(value=10)
        self.spb_nums_n = ttk.Spinbox(self.nfrm_nums_pars, from_=1, to=999, increment=1, textvariable=self.var_nums_n, width=8)
        self.spb_nums_n.grid(row=0, column=2, sticky='w')

        self.cbb_nums_n_mult = ttk.Combobox(self.nfrm_nums_pars, width=9)
        self.cbb_nums_n_mult.grid(row=0, column=3, sticky='w')
        self.cbb_nums_n_mult.state(['readonly'])
        self.cbb_nums_n_mult['values'] = ['', 'K', 'M', 'G', 'T']
        self.cbb_nums_n_mult.set('M')        

        # Number range
        self.lb_nums_range = ttk.Label(self.nfrm_nums_pars, text='Range (min, max)')
        self.lb_nums_range.grid(row=1, column=0, sticky='w')

        self.var_nums_range_min = tk.DoubleVar(value=0)
        self.spb_nums_range_min = ttk.Spinbox(self.nfrm_nums_pars, from_=1, to=999, increment=1, textvariable=self.var_nums_range_min, width=8)
        self.spb_nums_range_min.grid(row=1, column=1, sticky='w')

        self.var_nums_range_max = tk.DoubleVar(value=99)
        self.spb_nums_range_max = ttk.Spinbox(self.nfrm_nums_pars, from_=1, to=999, increment=1, textvariable=self.var_nums_range_max, width=8)
        self.spb_nums_range_max.grid(row=1, column=2, sticky='w')

        # Binary output
        self.lb_nums_out_type = ttk.Label(self.nfrm_nums_pars, text='Out Type')
        self.lb_nums_out_type.grid(row=2, column=0, sticky='w')

        self.cbb_nums_out_type = ttk.Combobox(self.nfrm_nums_pars, width=9)
        self.cbb_nums_out_type.grid(row=2, column=1, sticky='w')
        self.cbb_nums_out_type.state(['readonly'])
        self.cbb_nums_out_type['values'] = ['Binary', 'Text']
        self.cbb_nums_out_type.set('Binary')
        self.cbb_nums_out_type.bind('<<ComboboxSelected>>', self.nums_out_type_sel)

        # Separator
        self.lb_nums_out_sep = ttk.Label(self.nfrm_nums_pars, text='Text Separator')
        self.lb_nums_out_sep.grid(row=2, column=2, sticky='w')

        self.cbb_nums_out_sep = ttk.Combobox(self.nfrm_nums_pars, width=9)
        self.cbb_nums_out_sep.grid(row=2, column=3, sticky='w')
        self.cbb_nums_out_sep.state(['readonly'])
        self.cbb_nums_out_sep['values'] = ['LINE', ',', ';']
        self.cbb_nums_out_sep.set('LINE')
        self.cbb_nums_out_sep.state(['disabled'])

        ## Generate
        self.bt_nums_generate = ttk.Button(self.nfrm_nums, text='Generate', command=self.nums_generate)
        self.bt_nums_generate.grid(row=2, column=0, columnspan=3)


    def acquisition_finished(self, future):
        # Get result
        outputs, progress, time_str = future.result()

        if progress == 0:
            tkm.showerror(parent=self, title='Error', message='Acquisition failed')
            return

        # Show result info
        if progress == 100:
            title_msg = 'Success'
        else: 
            title_msg = 'Canceled'

        time_msg = 'Time = ' + time_str
        
        if len(outputs):
            detail_msg = '\nGenerated files\n{}'.format(outputs)
        else: 
            detail_msg = '\nIncomplete files deleted'

        tkm.showinfo(parent=self.win_progress, title=title_msg, message=time_msg, detail=detail_msg)        

        # Close win_progress
        self.win_progress.hide()


    def acq_path_search(self):
        out_path0 = self.var_acq_path.get()        
        out_path0 = out_path0 if out_path0 and os.path.exists(out_path0) else '/'
        out_path = tk.filedialog.askdirectory(parent=self, initialdir=out_path0, mustexist=True)
        if out_path:
            self.var_acq_path.set(out_path)
            self.master.cfg_write('ACQUISITION', 'path_out', out_path)

    
    def pcs_preset_sel(self, tk_event=None):
        if self.cbb_pcs_preset.get() == 'Report':
            self.var_pcs_si_min.set(10)
            self.var_pcs_si_max.set(10)
            self.var_pcs_si_step.set(1)
            self.var_pcs_n.set(50)
            self.cbb_pcs_n_mult.set('K')

        elif self.cbb_pcs_preset.get() == 'Detailed':
            self.var_pcs_si_min.set(1)
            self.var_pcs_si_max.set(10)
            self.var_pcs_si_step.set(1)
            self.var_pcs_n.set(10)
            self.cbb_pcs_n_mult.set('M')

    
    def pcs_generate(self):
        # Read vars
        out_path = self.var_acq_path.get()
        if not os.access(out_path, os.W_OK):
            tkm.showerror(parent=self, message='Error', detail='Cannot write on the chosen directory')
            return
        
        si_min = self.var_pcs_si_min.get()
        si_max = self.var_pcs_si_max.get()
        si_step = self.var_pcs_si_step.get()        
        si_range = np.arange(si_min, si_max + 1, si_step)
        n_si_range = len(si_range)
        if n_si_range == 0:
            tkm.showerror(parent=self, message='Error', detail='Please choose a proper Sampling Interval range')
            return

        n_pcs = int(get_ammount_prefix_number(n=self.var_pcs_n.get(), prefix=self.cbb_pcs_n_mult.get()))
        n_chunk = self.master.cfg_read('ACQUISITION', 'chunk_bytes', int)

        # Save cfg
        self.master.cfg_write('ACQUISITION', 'path_out', out_path)

        # Info
        self.lg.info('{}: Generating {} Pulse Counts in the range ({}, {}, {})'
                     .format(self.name, n_pcs, n_si_range, si_min, si_max, si_step))

        # Start
        time_start = time.perf_counter()

        # Data
        pcs_a = np.zeros(shape=(n_si_range, n_pcs), dtype=np.uint8)
        pcs_b = np.zeros(shape=(n_si_range, n_pcs), dtype=np.uint8)

        # Save initial RAVA setup
        pwm_setup = self.rng.get_pwm_setup()
        rng_setup = self.rng.get_rng_setup()

        # Show progress window
        with self.win_progress:

            # Loop PCs acquisition        
            canceled = False
            for i, si in enumerate(si_range):

                # Update progress window title
                self.win_progress.set_extra_title('{}/{}'.format(i+1, n_si_range))

                # Set Sampling Interval
                self.rng.snd_rng_setup(si)

                # Collect PCs
                outputs, _, _ = self.rng_acq.get_pulse_counts(rng=self.rng, n_pcs=n_pcs, n_chunk=n_chunk, rng_out='AB', 
                                                            out_file=False, out_path='', threaded=False)
                if len(outputs):
                    pcs_a[i], pcs_b[i] = outputs

                # Canceled?
                if not self.win_progress.acquiring:
                    canceled = True
                    break

        # Restore initial SI
        self.rng.snd_rng_setup(**rng_setup)

        # Timing
        time_s = time.perf_counter() - time_start
        time_td = datetime.timedelta(seconds=time_s)
        time_str = '{}'.format(str(time_td).split('.')[0])

        # Finished without cancelling?
        if not canceled:
            # Save Data
            sn = self.rng.dev_serial_number
            n_pcs_str = get_ammount_prefix_str(n_pcs)
            out_name = '{}_PCS_{}_SI_{}_{}_{}__'.format(sn, n_pcs_str, si_min, si_max, si_step)
            n_out_name = len(glob(os.path.join(out_path, out_name + '*.npz')))
            output_file = os.path.join(out_path, out_name + '{}.npz'.format(n_out_name + 1))
            
            np.savez_compressed(output_file, pwm_setup=pwm_setup, rng_setup=rng_setup, si_range=si_range, 
                                pcs_a=pcs_a, pcs_b=pcs_b)

            # Info screen
            tkm.showinfo(parent=self, title='Success', message='Time = ' + time_str, detail='\nGenerated file\n{}'.format([output_file]))

        else:
            # Info screen
            tkm.showinfo(parent=self, title='Canceled', message='Time = ' + time_str, detail='\nIncomplete files deleted')


    def bytes_preset_sel(self, tk_event=None):
        if self.cbb_bytes_preset.get() == 'Report':
            self.var_bytes_n.set(125)
            self.cbb_bytes_n_mult.set('MB')
            self.cbb_bytes_postproc.set('NONE')
            self.cbb_bytes_rngout.set('AB')


    def bytes_generate(self):
        # Read vars
        out_path = self.var_acq_path.get()
        if not os.access(out_path, os.W_OK):
            tkm.showerror(parent=self, message='Error', detail='Cannot write on the chosen directory')
            return

        n_bytes = int(get_ammount_prefix_number(n=self.var_bytes_n.get(), prefix=self.cbb_bytes_n_mult.get()))
        postproc = self.cbb_bytes_postproc.get()
        rng_out = self.cbb_bytes_rngout.get()
        n_chunk = self.master.cfg_read('ACQUISITION', 'chunk_bytes', int)

        # Save cfg
        self.master.cfg_write('ACQUISITION', 'path_out', out_path)

        # Info
        self.lg.info('{}: Generating {} Bytes; postproc={}, rng_out={}'.format(self.name, n_bytes, postproc, rng_out))

        # Start byte acquisition
        self.win_progress.show()        

        result_future = self.rng_acq.get_bytes(rng=self.rng, n_bytes=n_bytes, n_chunk=n_chunk, postproc=postproc, 
                                               rng_out=rng_out, out_file=True, out_path=out_path, threaded=True)
        result_future.add_done_callback(self.acquisition_finished)


    def nums_type_sel(self, tk_event=None):
        if self.cbb_nums_type.get() == 'INT':
            self.var_nums_range_min.set(0)
            self.var_nums_range_max.set(999)
        else:
            self.var_nums_range_min.set(0)
            self.var_nums_range_max.set(1)


    def nums_out_type_sel(self, tk_event=None):
        if self.cbb_nums_out_type.get() == 'Binary':
            self.cbb_nums_out_sep.state(['disabled'])
        else:
            self.cbb_nums_out_sep.state(['!disabled'])


    def nums_generate(self):
        ## Read vars
        out_path = self.var_acq_path.get()
        if not os.access(out_path, os.W_OK):
            tkm.showerror(parent=self, title='Error', message='Cannot write on the chosen directory')
            return
        
        num_type_str = self.cbb_nums_type.get()
        num_type = int if num_type_str == 'INT' else float
        n_nums = int(get_ammount_prefix_number(n=self.var_nums_n.get(), prefix=self.cbb_nums_n_mult.get()))
        num_min = self.var_nums_range_min.get()
        num_max = self.var_nums_range_max.get()
        out_binary = True if self.cbb_nums_out_type.get() == 'Binary' else False
        out_separator = self.cbb_nums_out_sep.get()
        out_separator = '\n' if out_separator == 'LINE' else out_separator
        n_chunk = self.master.cfg_read('ACQUISITION', 'chunk_numbers', int)

        # Save cfg
        self.master.cfg_write('ACQUISITION', 'path_out', out_path)

        # Info
        self.lg.info('{}: Generating {} {} Numbers; range=[{}, {}]'
                     .format(self.name, n_nums, num_type_str, num_min, num_max))

        # Start number acquisition
        self.win_progress.show()        

        result_future = self.rng_acq.get_numbers(rng=self.rng, n_nums=n_nums, n_chunk=n_chunk, num_type=num_type, 
                                                 num_min=num_min, num_max=num_max, out_file=True, out_path=out_path, 
                                                 out_file_binary=out_binary, out_file_separator=out_separator, 
                                                 threaded=True)
        result_future.add_done_callback(self.acquisition_finished)


### WIN_PROGRESS

class WIN_PROGRESS(tk.Toplevel):

    def __init__(self, parent):
        # Initiate WIN_PROGRESS
        super().__init__(parent)
        self.name = 'WIN_PROGRESS'
        self.title(' Progress ')
        self.geometry('350x100+{}+{}'.format(self.master.winfo_x() + self.master.winfo_width() + 10, self.master.winfo_y()))
        self.rowconfigure([0], weight=1)
        self.columnconfigure([0], weight=1)
        self.resizable(False, False) # No resize
        self.protocol('WM_DELETE_WINDOW', lambda: None)

        # Widgets
        self.frame = ttk.Frame(self, padding=(PAD, PAD))
        self.frame.grid(row=0, column=0, sticky='nsew')
        self.frame.columnconfigure([0], weight=1)
        self.frame.rowconfigure([0,1], weight=1)

        self.var_progress = tk.DoubleVar(value=0)
        self.pb_progress = ttk.Progressbar(self.frame, orient=tk.HORIZONTAL, length=200, mode='determinate', variable=self.var_progress, maximum=100.0)
        self.pb_progress.grid(row=0, column=0, sticky='ew', padx=2*PAD)

        self.bt_cancel = ttk.Button(self.frame, text='Cancel', command=self.prog_cancel)
        self.bt_cancel.grid(row=1, column=0)

        # Start
        self.acquiring = False

    
    def set_extra_title(self, extra_str=''):
        self.title(' Progress ' + extra_str)


    def show(self):
        self.acquiring = True
        self.prog_update(0)
        self.geometry('350x100+{}+{}'.format(self.master.winfo_x() + self.master.winfo_width() + 10, self.master.winfo_y()))
        self.wm_deiconify()
        self.master.update()    # Update widgets on non-threaded mode
        self.grab_set()         # Can't perform other actions while progress window is shown


    def hide(self):
        self.acquiring = False
        self.grab_release()
        self.withdraw()
        self.set_extra_title('')
    

    def __enter__(self):
        self.show()


    def __exit__(self, exc_type, exc_val, exc_tb):
        self.hide()


    def prog_update(self, progress):
        self.var_progress.set(progress)
        self.master.update()    # Update widgets on non-threaded mode


    def prog_cancel(self):        
        if tkm.askyesno(parent=self, title=('Cancel'), message='Cancel?'):
            self.acquiring = False
            try:
                self.master.rng_acq.stop()
            except:
                pass


rava_subapp_acquisition = {'class':RAVA_SUBAPP_ACQUISITION,
                           'menu_title':'Acquisition',
                           'show_button':True,
                           'use_rng':True
                           }