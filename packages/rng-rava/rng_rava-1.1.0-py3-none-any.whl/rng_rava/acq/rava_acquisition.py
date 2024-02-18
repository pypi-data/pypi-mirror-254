"""
Copyright (c) 2024 Gabriel Guerrer

Distributed under the MIT license - See LICENSE for details
"""

"""
The RAVA_ACQUISITION class implements the generation of extensive datasets
comprising random bytes, numbers or pulse counts extracted from a RAVA device.
Generation can occur in either threaded or blocking mode, and the output
can be presented as a memory array or a disk file.

For the get_pulse_counts() and get_bytes() functions, when out_file=True, they 
generate binary files. In contrast, the get_numbers() function provides the 
option to produce a text file by setting the parameter out_file_binary=False. 
In the text output, entries are separated by the out_separator character. 
When get_numbers() has the parameter out_file_binary=True, the files are 
saved using the numpy npy file format.

The get_numbers() function generates one file or array, which alternates entries 
from both RNG cores. The get_pulse_counts() and get_bytes() functions accept a 
rng_out parameter, which can be:
* 'A': 1 output file, RNG core A only
* 'B': 1 output file, RNG core B only
* 'AB': 2 output files, RNG cores A and B independent data

For get_bytes(), the parameter rng_out also accepts:
* 'AB_XOR': 1 output file, obtained by XORing RNG cores A and B output
* 'AB_ALT': 1 output file, with alternating bytes from RNG cores A and B. 
   Requires half of the time to produce n_bytes

A progress callback is established by registering a function through 
cbkreg_progress(). This function is invoked every time a data chunk of size 
n_chunk is generated, providing information about the progress percentage.
"""

import os.path
from glob import glob
import time
import logging
import itertools
import concurrent.futures
import threading
import datetime

import numpy as np

from rng_rava.acq.acq_tools import get_ammount_prefix_str
from rng_rava.rava_defs import D_RNG_POSTPROC, LOG_FILL


### VARS

ACQ_PCS_RNG_OUT = ['A', 'B', 'AB']
ACQ_BYTES_RNG_OUT = ['A', 'B', 'AB', 'AB_XOR', 'AB_ALT']


### RAVA_ACQUISITION

class RAVA_ACQUISITION:

    def __init__(self, delete_incomplete=True):
        # Set vars
        self.name = 'RAVA_ACQUISITION'
        self.delete_incomplete = delete_incomplete

        # Logging
        self.lg = logging.getLogger('rava')

        # Threading
        self.acquiring = threading.Event()
        self.thread_executor = concurrent.futures.ThreadPoolExecutor(max_workers=1)

        # Callback functions
        self.cbkfcn_progress = lambda progress: None


    ## CALLBACKS

    def cbkreg_progress(self, fcn_acquire_progress):
        if callable(fcn_acquire_progress):
            self.cbkfcn_progress = fcn_acquire_progress
            self.lg.debug('{} Callback: Registering Progress function to {}'
                          .format(self.name, fcn_acquire_progress.__name__))
        elif fcn_acquire_progress is None:
            self.cbkfcn_progress = lambda progress: None
            self.lg.debug('{} Callback: Unregistering Progress function'.format(self.name))
        else:
            self.lg.error('{} Callback: Provide fcn_acquire_progress as a function or None'.format(self.name))


    ## GENERAL

    def stop(self):
        self.lg.info('{}: Stopping acquisition'.format(self.name))
        self.acquiring.clear()


    ## PULSE COUNTS

    def get_filenames_pulse_counts(self, rng, n_pcs, rng_out, out_path):
        # RNG serial number
        sn = rng.dev_serial_number

        # Filenames base
        ammount_str = get_ammount_prefix_str(n_pcs)
        filename_a = '{}_PCS_{}_A__'.format(sn, ammount_str)
        filename_b = '{}_PCS_{}_B__'.format(sn, ammount_str)

        # Filenames count
        n_filename_a = len(glob(os.path.join(out_path, filename_a + '*.bin')))
        n_filename_b = len(glob(os.path.join(out_path, filename_b + '*.bin')))
        n_filename_ab = max(n_filename_a, n_filename_b)

        # Result Filename: count corrected + path
        if rng_out == 'A':
            filename_a = os.path.join(out_path, '{}{}.bin'.format(filename_a, n_filename_a + 1))
            return filename_a, None

        elif rng_out == 'B':
            filename_b = os.path.join(out_path, '{}{}.bin'.format(filename_b, n_filename_b + 1))
            return None, filename_b

        elif rng_out == 'AB':
            filename_a = os.path.join(out_path, '{}{}.bin'.format(filename_a, n_filename_ab + 1))
            filename_b = os.path.join(out_path, '{}{}.bin'.format(filename_b, n_filename_ab + 1))
            return filename_a, filename_b


    def get_pulse_counts(self, rng, n_pcs, n_chunk=10000, rng_out='AB', out_file=False, out_path='', threaded=False):
        # Test function inputs
        if not rng.connected():
            self.lg.error('{} Pulse Counts: Trying to acquire data from a disconnected RNG'.format(self.name))
            return [], 0, ''

        if self.acquiring.is_set():
            self.lg.error('{} Pulse Counts: RNG is already acquiring'.format(self.name))
            return [], 0, ''

        if out_file and not os.path.isdir(out_path):
            self.lg.error('{} Pulse Counts: The provided out_path doesn\'t exists'.format(self.name))
            return [], 0, ''

        if n_pcs <= 0:
            self.lg.error('{} Pulse Counts: Provide n_pcs > 0'.format(self.name))
            return [], 0, ''

        if n_chunk <= 0:
            self.lg.error('{} Pulse Counts: Provide n_chunk > 0'.format(self.name))
            return [], 0, ''

        if rng_out not in ACQ_PCS_RNG_OUT:
            self.lg.error('{} Pulse Counts: Unknown rng_out. Please choose from {}'.format(self.name, ACQ_PCS_RNG_OUT))
            return [], 0, ''

        # Start generation
        out_type = 'file' if out_file else 'array'
        self.lg.info('{} Pulse Counts: Starting {} acquisition with device {}'
                     .format(self.name, out_type, rng.dev_serial_number))

        args = (rng, n_pcs, n_chunk, rng_out, out_file, out_path)

        if threaded:
            result_future = self.thread_executor.submit(self.loop_pulse_counts, *args)
            return result_future
        else:
            result = self.loop_pulse_counts(*args)
            return result


    def loop_pulse_counts(self, rng, n_pcs, n_chunk, rng_out, out_file, out_path):
        # Set variables
        time_start = time.perf_counter()
        n_acquired = 0
        n_remaining = n_pcs
        progress = 0.
        self.acquiring.set()

        # Output
        out_path = '' if not out_file else out_path
        filename_a, filename_b = self.get_filenames_pulse_counts(rng, n_pcs, rng_out, out_path)

        if out_file:
            f_a = open(filename_a, mode='bw') if filename_a else None
            f_b = open(filename_b, mode='bw') if filename_b else None
            output_type = 'bytes'
        else:
            array_a = np.zeros(n_pcs, dtype=np.uint8) if filename_a else None
            array_b = np.zeros(n_pcs, dtype=np.uint8) if filename_b else None
            output_type = 'array'

        # Loop
        while self.acquiring.is_set():

            # Define n, the ammount of bytes to be generated
            if n_remaining // n_chunk:
                n = n_chunk
            else:
                n = n_remaining

            # Generate n pcs
            pcs_a, pcs_b = rng.get_rng_pulse_counts(n, output_type=output_type, timeout=None)

            # Test for RNG disconnection
            if (pcs_a is None) or (pcs_b is None):
                self.acquiring.clear()
                self.cbkreg_finished(None)
                continue

            # Write pcs
            if out_file:
                if rng_out == 'A':
                    f_a.write(pcs_a)

                elif rng_out == 'B':
                    f_b.write(pcs_b)

                elif rng_out == 'AB':
                    f_a.write(pcs_a)
                    f_b.write(pcs_b)

            else:
                if rng_out == 'A':
                    array_a[n_acquired:n_acquired+n] = pcs_a

                elif rng_out == 'B':
                    array_b[n_acquired:n_acquired+n] = pcs_b

                elif rng_out == 'AB':
                    array_a[n_acquired:n_acquired+n] = pcs_a
                    array_b[n_acquired:n_acquired+n] = pcs_b

            # Update n_acquired
            n_acquired += n

            # Progress callback
            progress = n_acquired / n_pcs * 100
            try:
                self.cbkfcn_progress(progress)
            except Exception as e:
                self.lg.error('{} Pulse Counts: Error calling cbkfcn_progress -- {}'.format(self.name, e))

            # Finished? Quit loop
            n_remaining = n_pcs - n_acquired

            if n_remaining == 0:
                self.acquiring.clear()

        # Output
        if out_file:
            f_a.close() if f_a else None
            f_b.close() if f_b else None
            outputs = [f for f in [filename_a, filename_b] if f is not None]
            outputs_str = ', '.join(outputs)
        else:
            outputs = [a for a in [array_a, array_b] if a is not None]
            outputs_str = ['array' for a in outputs]

        # Delete incomplete?
        if self.delete_incomplete and (progress < 100):
            if out_file:
                [os.remove(f) for f in outputs]
            else:
                for a in outputs:
                    del a
            outputs = []
            outputs_str = ['None']

        # Elapsed time
        time_s = time.perf_counter() - time_start
        time_td = datetime.timedelta(seconds=time_s)
        time_str = '{}'.format(str(time_td).split('.')[0])

        # Print info
        out_type = 'file' if out_file else 'array'
        self.lg.info('{} Pulse Counts: Finished {} acquisition with device {}\n{}Progress = {:.0f}%, Time={}\n{}Generated: {}'
            .format(self.name, out_type, rng.dev_serial_number, LOG_FILL, progress, time_str, LOG_FILL, outputs_str))

        # Return data
        return (outputs, progress, time_str)


    ## BYTES

    def get_filenames_bytes(self, rng, n_bytes, postproc, rng_out, out_path):
        # RNG serial number
        sn = rng.dev_serial_number

        # Postproc ID
        postproc_id = D_RNG_POSTPROC[postproc]

        # Filenames base
        ammount_str = get_ammount_prefix_str(n_bytes)
        filename_a = '{}_BYTES_{}_PP{}_A__'.format(sn, ammount_str, postproc_id)
        filename_b = '{}_BYTES_{}_PP{}_B__'.format(sn, ammount_str, postproc_id)
        filename_abxor = '{}_BYTES_{}_PP{}_AB_XOR__'.format(sn, ammount_str, postproc_id)
        filename_abalt = '{}_BYTES_{}_PP{}_AB_ALT__'.format(sn, ammount_str, postproc_id)

        # Filenames count
        n_filename_a = len(glob(os.path.join(out_path, filename_a + '*.bin')))
        n_filename_b = len(glob(os.path.join(out_path, filename_b + '*.bin')))
        n_filename_ab = max(n_filename_a, n_filename_b)
        n_filename_abxor = len(glob(os.path.join(out_path, filename_abxor + '*.bin')))
        n_filename_abalt = len(glob(os.path.join(out_path, filename_abalt + '*.bin')))

        # Result Filename: count corrected + path
        if rng_out == 'A':
            filename_a = os.path.join(out_path, '{}{}.bin'.format(filename_a, n_filename_a + 1))
            return filename_a, None

        elif rng_out == 'B':
            filename_b = os.path.join(out_path, '{}{}.bin'.format(filename_b, n_filename_b + 1))
            return None, filename_b

        elif rng_out == 'AB':
            filename_a = os.path.join(out_path, '{}{}.bin'.format(filename_a, n_filename_ab + 1))
            filename_b = os.path.join(out_path, '{}{}.bin'.format(filename_b, n_filename_ab + 1))
            return filename_a, filename_b

        elif rng_out == 'AB_XOR':
            filename_ab = os.path.join(out_path, '{}{}.bin'.format(filename_abxor, n_filename_abxor + 1))
            return filename_ab, None

        elif rng_out == 'AB_ALT':
            filename_ab = os.path.join(out_path, '{}{}.bin'.format(filename_abalt, n_filename_abalt + 1))
            return filename_ab, None


    def get_bytes(self, rng, n_bytes, n_chunk=10000, postproc='NONE', rng_out='AB', out_file=False, out_path='',
                  threaded=False):
        # Test function inputs
        if not rng.connected():
            self.lg.error('{} Bytes: Trying to acquire data from a disconnected RNG'.format(self.name))
            return [], 0, ''

        if self.acquiring.is_set():
            self.lg.error('{} Bytes: RNG is already acquiring'.format(self.name))
            return [], 0, ''

        if out_file and not os.path.isdir(out_path):
            self.lg.error('{} Bytes: The provided out_path doesn\'t exists'.format(self.name))
            return [], 0, ''

        if n_bytes <= 0:
            self.lg.error('{} Bytes: Provide n_bytes > 0'.format(self.name))
            return [], 0, ''

        if n_chunk <= 0:
            self.lg.error('{} Bytes: Provide n_chunk > 0'.format(self.name))
            return [], 0, ''

        if postproc not in D_RNG_POSTPROC.keys():
            self.lg.error('{} Bytes: Unknown postproc. Please choose from {}'.format(self.name, D_RNG_POSTPROC.keys()))
            return [], 0, ''

        if rng_out not in ACQ_BYTES_RNG_OUT:
            self.lg.error('{} Bytes: Unknown rng_out. Please choose from {}'.format(self.name, ACQ_BYTES_RNG_OUT))
            return [], 0, ''

        # Start generation
        out_type = 'file' if out_file else 'array'
        self.lg.info('{} Bytes: Starting {} acquisition with device {}'.format(self.name, out_type, rng.dev_serial_number))

        args = (rng, n_bytes, n_chunk, postproc, rng_out, out_file, out_path)

        if threaded:
            result_future = self.thread_executor.submit(self.loop_bytes, *args)
            return result_future
        else:
            result = self.loop_bytes(*args)
            return result


    def loop_bytes(self, rng, n_bytes, n_chunk, postproc, rng_out, out_file, out_path):
        # Set variables
        time_start = time.perf_counter()
        postproc_id = D_RNG_POSTPROC[postproc]
        n_acquired = 0
        n_remaining = n_bytes
        progress = 0.
        self.acquiring.set()

        # Output
        out_path = '' if not out_file else out_path
        filename_a, filename_b = self.get_filenames_bytes(rng, n_bytes, postproc, rng_out, out_path)

        if out_file:
            f_a = open(filename_a, mode='bw') if filename_a else None
            f_b = open(filename_b, mode='bw') if filename_b else None
            output_type = 'bytes'
        else:
            array_a = np.zeros(n_bytes, dtype=np.uint8) if filename_a else None
            array_b = np.zeros(n_bytes, dtype=np.uint8) if filename_b else None
            output_type = 'array'

        # Loop
        while self.acquiring.is_set():

            # Define n, the ammount of bytes to be generated
            if n_remaining // n_chunk:
                n = n_chunk
            else:
                n = n_remaining

            if rng_out == 'AB_ALT':
                n = n // 2

            # Generate n bytes
            bytes_a, bytes_b = rng.get_rng_bytes(n, postproc_id, output_type=output_type, timeout=None)

            # Test for RNG disconnection
            if (bytes_a is None) or (bytes_b is None):
                self.acquiring.clear()
                self.cbkreg_finished(None)
                continue

            # Write bytes
            if out_file:
                if rng_out == 'A':
                    f_a.write(bytes_a)

                elif rng_out == 'B':
                    f_b.write(bytes_b)

                elif rng_out == 'AB':
                    f_a.write(bytes_a)
                    f_b.write(bytes_b)

                elif rng_out == 'AB_XOR':
                    int_a = int.from_bytes(bytes_a, 'little')
                    int_b = int.from_bytes(bytes_b, 'little')
                    int_abxor = int_a ^ int_b
                    bytes_ab = int_abxor.to_bytes(len(bytes_a), 'little')
                    f_a.write(bytes_ab)

                elif rng_out == 'AB_ALT': # Alternate rng A and B bytes
                    bytes_ab = bytes(itertools.chain.from_iterable(zip(bytes_a, bytes_b)))
                    f_a.write(bytes_ab)

            else:
                if rng_out == 'A':
                    array_a[n_acquired:n_acquired+n] = bytes_a

                elif rng_out == 'B':
                    array_b[n_acquired:n_acquired+n] = bytes_b

                elif rng_out == 'AB':
                    array_a[n_acquired:n_acquired+n] = bytes_a
                    array_b[n_acquired:n_acquired+n] = bytes_b

                elif rng_out == 'AB_XOR':
                    bytes_ab = np.bitwise_xor(bytes_a, bytes_b)
                    array_a[n_acquired:n_acquired+n] = bytes_ab

                elif rng_out == 'AB_ALT': # Alternate rng A and B bytes
                    bytes_ab = list(itertools.chain.from_iterable(zip(bytes_a, bytes_b)))
                    array_a[n_acquired:n_acquired+2*n] = bytes_ab

            # Update n_acquired
            if rng_out == 'AB_ALT':
                n_acquired += 2*n
            else:
                n_acquired += n

            # Progress callback
            progress = n_acquired / n_bytes * 100
            try:
                self.cbkfcn_progress(progress)
            except Exception as e:
                self.lg.error('{} Bytes: Error calling cbkfcn_progress -- {}'.format(self.name, e))

            # Finished? Quit loop
            n_remaining = n_bytes - n_acquired

            if n_remaining == 0:
                self.acquiring.clear()

        # Output
        if out_file:
            f_a.close() if f_a else None
            f_b.close() if f_b else None
            outputs = [f for f in [filename_a, filename_b] if f is not None]
            outputs_str = ', '.join(outputs)
        else:
            outputs = [a for a in [array_a, array_b] if a is not None]
            outputs_str = ['array' for a in outputs]

        # Delete incomplete?
        if self.delete_incomplete and (progress < 100):
            if out_file:
                [os.remove(f) for f in outputs]
            else:
                for a in outputs:
                    del a
            outputs = []
            outputs_str = ['None']

        # Elapsed time
        time_s = time.perf_counter() - time_start
        time_td = datetime.timedelta(seconds=time_s)
        time_str = '{}'.format(str(time_td).split('.')[0])

        # Print info
        out_type = 'file' if out_file else 'array'
        self.lg.info('{} Bytes: Finished {} acquisition with device {}\n{}Progress = {:.0f}%, Time={}\n{}Generated: {}'
                .format(self.name, out_type, rng.dev_serial_number, LOG_FILL, progress, time_str, LOG_FILL, outputs_str))

        # Return data
        return outputs, progress, time_str


    ## NUMBERS

    def get_filenames_numbers(self, rng, out_file_binary, out_path, n_nums, num_type):
        # RNG serial number
        sn = rng.dev_serial_number

        # Extension
        ext = 'npy' if out_file_binary else 'dat'

        # Filenames base
        num_type_str = 'INT' if num_type is int else 'FLOAT'
        ammount_str = get_ammount_prefix_str(n_nums)
        filename = '{}_{}_{}__'.format(sn, num_type_str, ammount_str)

        # Filenames count
        n_filename = len(glob(os.path.join(out_path, filename + '*.{}'.format(ext))))

        # Result Filename: count corrected + path
        return os.path.join(out_path, '{}{}.{}'.format(filename, n_filename + 1, ext))


    def get_numbers(self, rng, n_nums, n_chunk=5000, num_type=float, num_min=0, num_max=1,
                    out_file=False, out_path='', out_file_binary=True, out_file_separator='\n', threaded=False):
        # Test function inputs
        if not rng.connected():
            self.lg.error('{} Numbers: Trying to acquire data from a disconnected RNG'.format(self.name))
            return [], 0, ''

        if self.acquiring.is_set():
            self.lg.error('{} Numbers: RNG is already acquiring'.format(self.name))
            return [], 0, ''

        if out_file and not os.path.isdir(out_path):
            self.lg.error('{} Numbers: The provided out_path doesn\'t exists'.format(self.name))
            return [], 0, ''

        if n_nums <= 0:
            self.lg.error('{} Numbers: Provide n_nums > 0'.format(self.name))
            return [], 0, ''

        if n_chunk <= 0:
            self.lg.error('{} Numbers: Provide n_chunk > 0'.format(self.name))
            return [], 0, ''

        if num_type not in [int, float]:
            self.lg.error('{} Numbers: Unknown num_type. Please choose from [int, float]'.format(self.name))
            return [], 0, ''

        if num_type is int:
            num_delta = num_max - num_min
            if num_delta >= 65536:
                self.lg.error('{} Numbers: Provide num_max - num_min < 65536'.format(self.name))
                return [], 0, ''

        if out_file_separator not in [',', ';', '.', '\n']:
            self.lg.error('{} Numbers: Unknown out_file_separator. Please choose from {}'
                     .format(self.name, [',', ';', '.', '\n']))
            return [], 0, ''

        # Start generation
        out_type = 'file' if out_file else 'array'
        self.lg.info('{} Numbers: Starting {} acquisition with device {}'.format(self.name, out_type, rng.dev_serial_number))

        args = (rng, n_nums, n_chunk, num_type, num_min, num_max, out_file, out_path, out_file_binary, out_file_separator)

        if threaded:
            result_future = self.thread_executor.submit(self.loop_numbers, *args)
            return result_future
        else:
            result = self.loop_numbers(*args)
            return result


    def loop_numbers(self, rng, n_nums, n_chunk, num_type, num_min, num_max, out_file, out_path, out_file_binary, out_file_separator):
        # Set variables
        time_start = time.perf_counter()
        n_acquired = 0
        n_remaining = n_nums
        progress = 0.
        self.acquiring.set()
        num_delta = num_max - num_min

        # Output dtype
        if num_type is int:
            if num_min + num_delta < 2**8:
                dtype_out = np.uint8
            elif num_min + num_delta < 2**16:
                dtype_out = np.uint16
            elif num_min + num_delta < 2**32:
                dtype_out = np.uint32
        else:
            dtype_out = np.float32

        # Output
        if out_file and out_file_binary == False:
            filename = self.get_filenames_numbers(rng, out_file_binary, out_path, n_nums, num_type)
            f = open(filename, mode='w')
        elif out_file and out_file_binary == True:
            filename = self.get_filenames_numbers(rng, out_file_binary, out_path, n_nums, num_type)
            array = np.zeros(n_nums, dtype=dtype_out)
        else:
            array = np.zeros(n_nums, dtype=dtype_out)

        # Loop
        while self.acquiring.is_set():

            # Define n, the ammount of bytes to be generated
            if n_remaining // n_chunk:
                n = n_chunk
            else:
                n = n_remaining

            # Generate n numbers
            if num_type is int and num_delta < 256:
                nums = rng.get_rng_int8s(n, int(num_delta), output_type='array', timeout=None)
            elif num_type is int and num_delta < 65536:
                nums = rng.get_rng_int16s(n, int(num_delta), output_type='array', timeout=None)
            else:
                nums = rng.get_rng_floats(n, output_type='array', timeout=None)

            # Test for RNG disconnection
            if nums is None:
                self.acquiring.clear()
                self.cbkreg_finished(None)
                continue

            # Correct range
            if num_type is int:
                nums = int(num_min) + nums.astype(dtype_out)
            else:
                nums = num_min + nums * num_delta

            # Write numbers
            if out_file and out_file_binary == False:
                nums.tofile(f, sep=out_file_separator)
                if n == n_chunk:
                    f.write(out_file_separator)
            else:
                array[n_acquired:n_acquired+n] = nums

            # Update n_acquired
            n_acquired += n

            # Progress callback
            progress = n_acquired / n_nums * 100
            try:
                self.cbkfcn_progress(progress)
            except Exception as e:
                self.lg.warning('{} Numbers: Error calling cbkfcn_progress -- {}'.format(self.name, e))

            # Finished? Quit loop
            n_remaining = n_nums - n_acquired

            if n_remaining == 0:
                self.acquiring.clear()

        # Output
        if out_file and out_file_binary == False:
            f.close()

            outputs = [filename]
            outputs_str = ', '.join(outputs)
        elif out_file and out_file_binary == True:
            np.save(filename, array)

            outputs = [filename]
            outputs_str = ', '.join(outputs)
        else:
            outputs = [array]
            outputs_str = ['array' for a in outputs]

        # Delete incomplete?
        if self.delete_incomplete and (progress < 100):
            if out_file:
                [os.remove(filename) for f in outputs]
            else:
                for a in outputs:
                    del a
            outputs = []
            outputs_str = ['None']

        # Elapsed time
        time_s = time.perf_counter() - time_start
        time_td = datetime.timedelta(seconds=time_s)
        time_str = '{}'.format(str(time_td).split('.')[0])

        # Print info
        out_type = 'file' if out_file else 'array'
        self.lg.info('{} Numbers: Finished {} acquisition with device {}\n{}Progress = {:.0f}%, Time={}\n{}Generated: {}'
                .format(self.name, out_type, rng.dev_serial_number, LOG_FILL, progress, time_str, LOG_FILL, outputs_str))

        # Return data
        return outputs, progress, time_str