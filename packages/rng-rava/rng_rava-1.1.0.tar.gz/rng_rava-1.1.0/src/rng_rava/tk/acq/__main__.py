"""
Copyright (c) 2024 Gabriel Guerrer

Distributed under the MIT license - See LICENSE for details
"""

"""
This code evokes the RAVA's Tk Acquisition application.

To execute it, enter the following command: python3 -m rng_rava.tk.acq
"""

from rng_rava.tk import RAVA_APP
from rng_rava.tk.acq import rava_subapp_acquisition
from rng_rava.tk.ctrlp import rava_subapp_control_panel

TITLE = 'RAVA Acquisition'
rava_subapp_control_panel['show_button'] = False
SUBAPPS = [rava_subapp_control_panel, rava_subapp_acquisition]


def main():
    # RAVA main app
    tkapp = RAVA_APP(title=TITLE, subapp_dicts=SUBAPPS, cfg_log_name='rava_acq')

    # Enter Tk loop
    tkapp.mainloop()


if __name__ == '__main__':
    main()