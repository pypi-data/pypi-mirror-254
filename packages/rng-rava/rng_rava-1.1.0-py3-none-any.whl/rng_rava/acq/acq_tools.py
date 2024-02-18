"""
Copyright (c) 2024 Gabriel Guerrer

Distributed under the MIT license - See LICENSE for details
"""

"""
Functions utilized by the Acquisition module.
"""

## GENERIC

def get_ammount_prefix_str(n):
    if n / (1000) < 1:
        ammount_str = '{:.0f}'.format(n)
    elif n / (1000000) < 1:
        ammount_str = '{:.0f}K'.format(n / 1000)
    elif n / (1000000000) < 1:
        ammount_str = '{:.0f}M'.format(n / 1000000)
    elif n / (1000000000000) < 1:
        ammount_str = '{:.0f}G'.format(n / 1000000000)
    elif n / (1000000000000000) < 1:
        ammount_str = '{:.0f}T'.format(n / 1000000000000)
    return ammount_str


def get_ammount_prefix_number(n, prefix):
    if 'K' in prefix.upper():
        return n * 1000
    elif 'M' in prefix.upper():
        return n * 1000000
    elif 'G' in prefix.upper():
        return n * 1000000000
    elif 'T' in prefix.upper():
        return n * 1000000000000