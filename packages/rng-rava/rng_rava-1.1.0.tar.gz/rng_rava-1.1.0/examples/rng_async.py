'''
This example showcases asynchronous RNG functionality.

This example code is in the public domain.
Author: Gabriel Guerrer
'''

import asyncio
import rng_rava as rava

async def main():
    # Create a RAVA instance and set the logging level to DEBUG
    rng = rava.RAVA_RNG_AIO()
    rng.log_level('DEBUG')

    # Find RAVA device and connect
    dev_sns = rava.find_rava_sns()
    if len(dev_sns):
        await rng.connect(dev_sns[0])
    else:
        print('No device found')
        exit()

    # Request configuration
    print('\nPWM setup: {}\n'.format(await rng.get_pwm_setup()))
    print('\nRNG setup: {}\n'.format(await rng.get_rng_setup()))

    # Generate random data
    N_DATA = 30
    results = await asyncio.gather(
        rng.get_rng_pulse_counts(n_counts=N_DATA, output_type='list'),
        rng.get_rng_bits(bit_source_id=rava.D_RNG_BIT_SRC['AB']),
        rng.get_rng_bytes(n_bytes=N_DATA, postproc_id=rava.D_RNG_POSTPROC['NONE'], output_type='list'),
        rng.get_rng_int8s(n_ints=N_DATA, int_delta=100, output_type='list'),
        rng.get_rng_int16s(n_ints=N_DATA, int_delta=1000, output_type='list'),
        rng.get_rng_floats(n_floats=N_DATA, output_type='list')
    )
    print('\nRNG data: {}\n'.format(results))

    # Close device
    rng.close()

asyncio.run(main())