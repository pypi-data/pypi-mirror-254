'''
This example illustrates the generation of random floats to a binary file 
(numpy npy) using the RAVA_ACQUISITION class.

This example code is in the public domain.
Author: Gabriel Guerrer
'''

import rng_rava as rava

# Variables
OUT_FILE = True                         # File output
OUT_PATH = './'                         # Update with the desired output path
OUT_BINARY = True                       # Output as a binary file
N_NUMS = 500000                         # 500k floats
N_CHUNK = 5000                          # Update progress every 5K floats
NUM_TYPE = float                        # Produce floats
NUM_MIN = 0                             # Float range (0,1]
NUM_MAX = 1
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
outputs, progress, time_str = rng_acq.get_numbers(rng, N_NUMS, N_CHUNK, NUM_TYPE, NUM_MIN, NUM_MAX, 
                                                  OUT_FILE, OUT_PATH, OUT_BINARY, threaded=THREADED)

# Close RAVA device
rng.close()