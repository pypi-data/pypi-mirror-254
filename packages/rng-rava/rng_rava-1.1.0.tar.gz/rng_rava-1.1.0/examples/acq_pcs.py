'''
This example illustrates the generation of pulse counts to memory array using 
the RAVA_ACQUISITION class. The generation runs in threaded mode.

This example code is in the public domain.
Author: Gabriel Guerrer
'''

import rng_rava as rava

# Variables
OUT_FILE = False                        # Array output
N_PCS = 100000                          # 100K
N_CHUNK = 10000                         # Update progress every 10K
RNG_OUT = 'AB'                          # Generate 2 files, one for each RNG core
THREADED = True                         # Non-blocking mode

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

# Define finished function
def finished(future):
    outputs, progress, time_str = future.result()

    # Print first 100 entries from each array
    print(outputs[0][:100])
    print(outputs[1][:100])
    
    # Close RAVA device
    rng.close()

# Acquisition
future = rng_acq.get_pulse_counts(rng, N_PCS, N_CHUNK, RNG_OUT, OUT_FILE, threaded=THREADED)
future.add_done_callback(finished)