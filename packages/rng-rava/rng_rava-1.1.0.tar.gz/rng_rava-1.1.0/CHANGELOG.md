## v1.0.1
* Changed maximum line length from 80 to 120. This change does not apply to the code's documentation
* Using "not in" and "is not None"
* Correcting firmware version in eeprom_firmware
* Adding callbacks
* Setting logger name to 'rava'
* Changed health startup results format
* Including hardware float generation

## v1.0.2
* Checking for n > 0 in data generation
* Max n of pulse counts, bytes, ints, and floats changed to 2^16 (instead of 2^32)
* Improved the disconnection detection methodology
* Corrected the int_delta in integers generation

## v1.1.0
* Adding numpy requirement
* Changing parameter list_output to output_type
* Including acq submodule for acquiring data from a RAVA device
* Including acq_pcs.py, acq_bytes.py, acq_ints.py, and acq_floats.py to examples/
* Including tk submodule for GUI apps defining RAVA_APP and RAVA_SUBAPP classes
* Including tk.acq used to evoke the tk acquire subapp via python3 -m rng_rava.tk.acq
* Including tk.ctrlp used to evoke the tk control panel subapp via python3 -m rng_rava.tk.ctrlp