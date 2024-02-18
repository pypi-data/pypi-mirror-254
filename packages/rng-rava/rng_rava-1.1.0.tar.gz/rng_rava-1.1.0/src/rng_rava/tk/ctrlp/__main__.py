"""
Copyright (c) 2023 Gabriel Guerrer

Distributed under the MIT license - See LICENSE for details
"""

"""
This code evokes the RAVA's Tk Control Panel application.

To execute it, enter the following command: python3 -m rng_rava.tk.ctrlp
"""

from rng_rava.tk import RAVA_APP
from rng_rava.tk.ctrlp import rava_subapp_control_panel

TITLE = 'RAVA Control Panel'
SUBAPPS = [rava_subapp_control_panel]


def main():
    # RAVA main app
    tkapp = RAVA_APP(title=TITLE, subapp_dicts=SUBAPPS, cfg_log_name='rava_ctrlp')

    # Enter Tk loop
    tkapp.mainloop()


if __name__ == '__main__':
    main()