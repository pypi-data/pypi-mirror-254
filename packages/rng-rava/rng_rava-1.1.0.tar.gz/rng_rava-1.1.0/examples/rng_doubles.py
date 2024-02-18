'''
This example showcases the RNG generation of double precision floating-point
numbers.

This example code is in the public domain.
Author: Gabriel Guerrer
'''

import numpy as np
import rng_rava as rava

# Find RAVA device and connect
rng = rava.RAVA_RNG()
dev_sns = rava.find_rava_sns()
if len(dev_sns):
    rng.connect(serial_number=dev_sns[0])
else:
    print('No device found')
    exit()

def get_rng_doubles(n_doubles):
    if n_doubles >= (2**16) // 8:
        print('RNG Doubles: Maximum n_doubles is {}'.format((2**16) // 8))
        return None

    # 64 bits floating point number
    bytes_res = rng.get_rng_bytes(n_bytes=n_doubles*8, output_type='array', timeout=None)
    if bytes_res is None:
        return
    rnd_bytes_a, rnd_bytes_b = bytes_res

    # XOR them    
    rnd_bytes = np.bitwise_xor(rnd_bytes_a, rnd_bytes_b).tobytes()
    
    # Convert bytes to ints    
    rnd_ints = np.frombuffer(rnd_bytes, dtype=np.uint64)
    
    # IEEE754 bit pattern for single precision floating point value in the
    # range of 1.0 - 2.0. Uses the first 52 bits and fixes the float
    # exponent to 1023
    rnd_ints_tmp = (rnd_ints & 0xFFFFFFFFFFFFF) | 0x3FF0000000000000
    rnd_doubles = np.frombuffer(rnd_ints_tmp.tobytes(), dtype=np.float64)
    return rnd_doubles - 1

# Get and print 100 doubles
doubles = get_rng_doubles(100)
doubles_str = '\n'.join(['{:.16f}'.format(d) for d in doubles])
print(doubles_str)

# Close device
rng.close()