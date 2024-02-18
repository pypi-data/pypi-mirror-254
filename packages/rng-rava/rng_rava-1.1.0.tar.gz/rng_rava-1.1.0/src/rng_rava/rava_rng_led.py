"""
Copyright (c) 2023 Gabriel Guerrer

Distributed under the MIT license - See LICENSE for details
"""

"""
The RAVA_RNG_LED class implements the code for controlling the LED and LAMP
modules within the RAVA circuit. It allows users to adjust the color and the
intensity of the attached LED. Users can also activate the LAMP mode and
retrieve statistical information on its operation.

For more information on how LED and LAMP modules operate, refer to the firmware
documentation.
"""

import struct

from rng_rava.rava_rng import RAVA_RNG
from rng_rava.rava_defs import *

### RAVA_RNG_LED

class RAVA_RNG_LED(RAVA_RNG):

    def __init__(self):
        super().__init__(dev_name='RAVA_LED')

        # Variables defined upon connection
        self.led_attached = None

        # Variables
        self.led_color = None
        self.led_intensity = None
        self.lamp_mode = None
        self.lamp_debug = None

        # Callback functions
        self.cbkfcn_lamp_debug = lambda: None


    def connect(self, serial_number):
        if not super().connect(serial_number=serial_number):
            return False

        # LED firmware enabled?
        if not self.led_enabled:
            self.lg.warning('{} Connect: LED code is disabled in the firmware'.format(self.dev_name))

        # LED attached?
        self.led_attached = self.get_eeprom_led()['led_attached']
        if not self.led_attached:
            self.lg.warning('{} Connect: Firmware claims no LED is attached.'
                           '\n{}  If false, fix it with snd_eeprom_led(led_attached=True)'
                           .format(self.dev_name, LOG_FILL))

        return True


    ## SERIAL

    def process_serial_comm(self, comm_id, comm_data):
        super().process_serial_comm(comm_id=comm_id, comm_data=comm_data)

        # LED_STATUS
        if comm_id == D_DEV_COMM['LED_STATUS']:
            # color, intensity, color_fading, intensity_fading
            self.put_queue_data('LED_STATUS', self.unpack_rava_msgdata(comm_data, 'BBBB'))

        # LAMP_DEBUG
        elif comm_id == D_DEV_COMM['LAMP_DEBUG']:
            # z, mag, mag_avg
            self.put_queue_data('LAMP_DEBUG', self.unpack_rava_msgdata(comm_data, 'fBB'))
            # Callback
            try:
                self.cbkfcn_lamp_debug()
            except:
                pass

        # LAMP_STATISTICS
        elif comm_id == D_DEV_COMM['LAMP_STATISTICS']:
            exp_n, exp_n_zsig, n_extra_bytes = self.unpack_rava_msgdata(comm_data, 'HHB')
            exp_colors_bytes = self.read_serial(n_extra_bytes)
            if exp_colors_bytes is None:
                exp_colors = 8*[0]
            else:
                exp_colors = struct.unpack('<HHHHHHHH', exp_colors_bytes)
            self.put_queue_data('LAMP_STATISTICS', (exp_n, exp_n_zsig, *exp_colors))


    ## CALLBACK REGISTER

    def cbkreg_lamp_debug(self, fcn_lamp_debug):
        if callable(fcn_lamp_debug):
            self.cbkfcn_lamp_debug = fcn_lamp_debug
            self.lg.debug('{} Callback: Registering Lamp Debug function to {}'
                          .format(self.dev_name, fcn_lamp_debug.__name__))
        elif fcn_lamp_debug is None:
            self.cbkfcn_lamp_debug = lambda: None
            self.lg.debug('{} Callback: Unregistering Lamp Debug function'.format(self.dev_name))
        else:
            self.lg.error('{} Callback: Provide fcn_lamp_debug as a function'.format(self.dev_name))


    ## LED

    def snd_led_color(self, color_hue, intensity=255):
        if color_hue >= 2**8:
            self.lg.error('{} LED Color: Provide color_hue as a 8-bit integer'.format(self.dev_name))
            return None
        if intensity >= 2**8:
            self.lg.error('{} LED Color: Provide intensity as a 8-bit integer'.format(self.dev_name))
            return None

        self.led_color = color_hue
        self.led_intensity = intensity
        comm = 'LED_COLOR'
        return self.snd_rava_msg(comm, [color_hue, intensity], 'BB')


    def snd_led_color_fade(self, color_hue_tgt, duration_ms):
        if color_hue_tgt >= 2**8:
            self.lg.error('{} LED Color: Provide color_hue_tgt as a 8-bit integer'.format(self.dev_name))
            return None
        if duration_ms >= 2**16:
            self.lg.error('{} LED Color: Provide duration_ms as a 16-bit integer'.format(self.dev_name))
            return None

        if duration_ms == 0:
            self.lg.error('{} LED Color: Provide duration_ms > 0'.format(self.dev_name))
            return None
        if color_hue_tgt - self.led_color == 0:
            return None

        self.led_color = color_hue_tgt
        comm = 'LED_COLOR_FADE'
        return self.snd_rava_msg(comm, [color_hue_tgt, duration_ms], 'BH')


    def snd_led_color_oscillate(self, n_cycles, duration_ms):
        if n_cycles >= 2**8:
            self.lg.error('{} LED Color: Provide n_cycles as a 8-bit integer'.format(self.dev_name))
            return None
        if duration_ms >= 2**16:
            self.lg.error('{} LED Color: Provide duration_ms as a 16-bit integer'.format(self.dev_name))
            return None

        if n_cycles == 0:
            self.lg.error('{} LED Color: Provide n_cycles > 0'.format(self.dev_name))
            return None
        if duration_ms == 0:
            self.lg.error('{} LED Color: Provide duration_ms > 0'.format(self.dev_name))
            return None

        comm = 'LED_COLOR_OSCILLATE'
        return self.snd_rava_msg(comm, [n_cycles, duration_ms], 'BH')


    def snd_led_intensity(self, intensity):
        if intensity >= 2**8:
            self.lg.error('{} LED Intensity: Provide intensity as a 8-bit integer'.format(self.dev_name))
            return None

        self.led_intensity = intensity
        comm = 'LED_INTENSITY'
        return self.snd_rava_msg(comm, [intensity], 'B')


    def snd_led_intensity_fade(self, intensity_tgt, duration_ms):
        if intensity_tgt >= 2**8:
            self.lg.error('{} LED Intensity: Provide intensity_tgt as a 8-bit integer'.format(self.dev_name))
            return None
        if duration_ms >= 2**16:
            self.lg.error('{} LED Intensity: Provide duration_ms as a 16-bit integer'.format(self.dev_name))
            return None

        if duration_ms == 0:
            self.lg.error('{} LED Intensity: Provide duration_ms > 0'.format(self.dev_name))
            return None
        if intensity_tgt - self.led_intensity == 0:
            return None

        self.led_intensity = intensity_tgt
        comm = 'LED_INTENSITY_FADE'
        return self.snd_rava_msg(comm, [intensity_tgt, duration_ms], 'BH')


    def snd_led_fade_stop(self):
        comm = 'LED_FADE_STOP'
        return self.snd_rava_msg(comm)


    def get_led_status(self, timeout=GET_TIMEOUT_S):
        comm = 'LED_STATUS'
        if self.snd_rava_msg(comm):
            color_hue, intensity, color_fading, intensity_fading = self.get_queue_data(comm, timeout=timeout)
            if color_hue in D_LED_COLOR_INV:
                color_str = D_LED_COLOR_INV[color_hue]
            else:
                color_str = ''
            return {'color_hue':color_hue, 'color':color_str, 'intensity':intensity,
                    'color_fading':color_fading, 'intensity_fading':intensity_fading}


    ## LAMP

    def snd_lamp_mode(self, on=True):
        self.lamp_mode = on

        comm = 'LAMP_MODE'
        return self.snd_rava_msg(comm, [on], 'B')


    def get_lamp_statistics(self, timeout=GET_TIMEOUT_S):
        # Every get command resets the statistics values
        comm = 'LAMP_STATISTICS'
        if self.snd_rava_msg(comm):
            data_vars = self.get_queue_data(comm, timeout=timeout)
            data_names = ['exp_n', 'exp_n_zsig',
                          'red', 'orange', 'yellow', 'green', 'cyan', 'blue', 'purple', 'pink']
            return dict(zip(data_names, data_vars))


    def snd_lamp_debug(self, on=True):
        self.lamp_debug = on
        comm = 'LAMP_DEBUG'
        return self.snd_rava_msg(comm, [on], 'B')


    def get_lamp_debug_data(self, timeout=GET_TIMEOUT_S):
        comm = 'LAMP_DEBUG'
        data_vars = self.get_queue_data(comm, timeout=timeout)

        # Timeout?
        if data_vars is None:
            return None

        data_names = ['z', 'mag', 'mag_avg']
        return dict(zip(data_names, data_vars))