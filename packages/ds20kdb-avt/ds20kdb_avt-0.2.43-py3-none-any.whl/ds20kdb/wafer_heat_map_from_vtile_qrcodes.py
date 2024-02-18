#!/usr/bin/env python3
"""
Generate a heat map showing the original wafer location of SiPMs attached to
vTiles.

Intended to help identify any problematic wafer regions associated with
troublesome vTiles.
"""

import argparse
import collections
import itertools
import sys
import types


try:
    from ds20kdb import visual
except ModuleNotFoundError:
    print('Please install ds20kdb-avt')
    sys.exit(3)
except ImportError:
    print('Please upgrade to the latest ds20kdb-avt version')
    sys.exit(3)
else:
    from ds20kdb import interface


##############################################################################
# command line option handler
##############################################################################


def check_arguments():
    """
    handle command line options

    --------------------------------------------------------------------------
    args : none
    --------------------------------------------------------------------------
    returns : none
    --------------------------------------------------------------------------
    """
    parser = argparse.ArgumentParser(
        description='Generate a heat map showing the original wafer location\
        of SiPMs attached to vTiles. Intended to help identify any problematic\
        wafer regions associated with troublesome vTiles.\
        Support requests to: Alan Taylor,\
        Dept. of Physics, University of Liverpool, avt@hep.ph.liv.ac.uk.')
    parser.add_argument(
        'qrcodes', nargs='+', metavar='qrcodes',
        help='One or more vTile QR codes from which to generate the heat map.\
        vTile Serial numbers are also acceptable.',
        type=int)

    args = parser.parse_args()

    return args


##############################################################################
# main
##############################################################################


def value_to_vtile_id(value, qr_to_id):
    """
    Obtain the vTile ID for the supplied QR code or serial number. For the
    latter case we are assuming the serial numbers are for the VETO on behalf
    of the user.

    --------------------------------------------------------------------------
    args
        value : int or string, supplied value as QR code or serial number
            e.g. 23062913000173001 or 173
        qr_to_id : dict
            e.g. {'22061703000024001': 4, '22060103000012001': 5, ...}
    --------------------------------------------------------------------------
    returns : int (SiPM ID) or None
    --------------------------------------------------------------------------
    """
    if interface.qr_code_valid(value):
        try:
            return qr_to_id[str(value)]
        except KeyError:
            return None

    # Anything that doesn't look like a QR code should be a serial number.
    # Attempt to find the serial number in all known vTile QR codes.
    try:
        return next(
            i for q, i in qr_to_id.items() if int(value) == int(str(q)[9:-3])
        )
    except StopIteration:
        return None


def get_vtile_ids_from_values(dbi, values):
    """
    Get vTile IDs from a list of QR codes and/or serial numbers.

    --------------------------------------------------------------------------
    args
        dbi : ds20kdb.interface.Database
            Instance of the Database interface class; allows communication
            with the database.
        values : list of values (QR codes or serial numbers)
            e.g. [22061703000024001, 413, 414, '415', ...]
    --------------------------------------------------------------------------
    returns : set of vTile IDs
        e.g. {189, 190, 191, ...}
    --------------------------------------------------------------------------
    """
    # get look-up table and reverse mapping
    id_to_qr = dbi.vtile_id_to_qrcode_lut()
    qr_to_id = {v: k for (k, v) in id_to_qr.items()}

    return {value_to_vtile_id(value, qr_to_id) for value in values}


def get_sipm_ids_from_vtile_ids(dbi, vtile_ids):
    """
    Get a list of SiPM IDs for all the supplied vTile IDs.

    --------------------------------------------------------------------------
    args
        dbi : ds20kdb.interface.Database
            Instance of the Database interface class; allows communication
            with the database.
        vtile_ids : list of vTile IDs
            e.g. [189, 190, 191, ...]
    --------------------------------------------------------------------------
    returns : set of SiPM IDs
        e.g. {134348, 134349, 154845, ...}
    --------------------------------------------------------------------------
    """
    columns = [f'sipm_{x}' for x in range(1, 25)]
    sipm_ids = set()
    for vtile_id in vtile_ids:
        try:
            sipm_ids |= set(
                dbi.get('vtile', vtile_pid=vtile_id).data[columns].values[-1]
            )
        except TypeError:
            pass

    return sipm_ids


def get_locations_from_sipm_ids(dbi, sipm_ids):
    """
    Get (column, row) locations for all supplied SiPM IDs.

    --------------------------------------------------------------------------
    args
        dbi : ds20kdb.interface.Database
            Instance of the Database interface class; allows communication
            with the database.
        vtile_ids : list of vTile IDs
            e.g. [189, 190, 191, ...]
    --------------------------------------------------------------------------
    returns : collections.Counter(), {(int, int): int, ...}
        number of occurrences of each location in the dataset
        e.g.
            {
                (6, 3): 3, (14, 4): 3,
                (7, 3): 2, (5, 21): 2, (6, 21): 2, ...
                (3, 13): 1, (4, 13): 1, (5, 13): 1, ...
            }
    --------------------------------------------------------------------------
    """
    dfr = dbi.get('sipm').data[['sipm_pid', 'column', 'row']]

    return collections.Counter(
        itertools.chain(
            tuple(dfr[dfr['sipm_pid'] == sipm_id][['column', 'row']].values[-1])
            for sipm_id in sipm_ids
        )
    )


##############################################################################
# main
##############################################################################

def main():
    """
    Generate a wafer map suitable for picking good SiPMs from a wafer using a
    die ejector, such that they may be transferred to trays and later
    installed onto vTiles.
    """
    args = check_arguments()

    dbi = interface.Database()
    vtile_ids = get_vtile_ids_from_values(dbi, args.qrcodes)
    sipm_ids = get_sipm_ids_from_vtile_ids(dbi, vtile_ids)

    count_grp = get_locations_from_sipm_ids(dbi, sipm_ids)

    fgrp = collections.defaultdict(set)
    for loc, freq in count_grp.items():
        fgrp[freq].add(loc)

    def col(group_num, num_groups):
        grey = 64 + group_num * (192 // num_groups)
        return grey, grey, grey

    num_groups = len(fgrp)

    clut = {
        f: col(f, num_groups)
        for f in range(1, len(fgrp) + 1)
    }

    sipm_groups = [
        {
            'name': str(frq),
            'locations': sipm_locations,
            'sipm_colour': clut[frq],
            'text_colour': frq,
        }
        for frq, sipm_locations in fgrp.items()
    ]

    status = types.SimpleNamespace(success=0, unreserved_error_code=3)

    visual.DrawWafer(
        wafer_lot='',
        wafer_number='',
        sipm_groups=sipm_groups,
        group_name=True,

    ).save()

    return status.success


##############################################################################
if __name__ == '__main__':
    sys.exit(main())
