'''
This example illustrates the generation of random bytes to binary files using 
the RAVA_ACQUISITION class.

This example code is in the public domain.
Author: Gabriel Guerrer
'''

import rng_rava as rava

# Variables
OUT_FILE = True                         # File output
OUT_PATH = './'                         # Update with the desired output path
N_BYTES = 1000000                       # 1MB
N_CHUNK = 10000                         # Update progress every 10KB
POSTPROC = 'NONE'                       # No post-processing
RNG_OUT = 'AB'                          # Generate 2 files, one for each RNG core
THREADED = False                        # Blocking mode

# Find RAVA device and connect
rng = rava.RAVA_RNG()
dev_sns = rava.find_rava_sns()
if len(dev_sns):
    rng.connect(serial_number=dev_sns[0])
else:
    print('No device found')
    exit()

# Create acquisition instance
rng_acq = rava.acq.RAVA_ACQUISITION()

# Register progress callback
rng_acq.cbkreg_progress(lambda progress: print('{:.0f}%'.format(progress)))

# Acquisition
outputs, progress, time_str = rng_acq.get_bytes(rng, N_BYTES, N_CHUNK, POSTPROC, RNG_OUT, OUT_FILE, OUT_PATH, THREADED)

# Close RAVA device
rng.close()