# -*- coding: utf-8 -*-
"""
dslr 
====

 Functions related to analysing data from from a digital camera.

"""

import rawpy
from rawpy import LibRawTooBigError
import exifread
import errno
import os
import csv

__all__ = [ 'read_raw','pixel_size_from_exif']

def read_raw(file, channel_index=None):
    """
    Read image data and EXIF information from a raw file.

    Return image data as a numpy array and EXIF tags dictionary.

    If channel_index=None (default) then all 3 channels of data are returned
    as an n_row x n_columns x 3 image cube.

    N.B. the first channel number is 0, not 1.

    :param file: full path to file containing raw image data.
    :param channel_index: Which channel to load.

    :returns: image_data, tags

    :Example:

     The two following code snippets are equivalent

     >>> from keeleastrolab import dslr
     >>> image_data, exif_info = dslr.read_raw('IMG_0001.CR2')
     >>> channel0 = image_data[:,:,0]

     >>> from keeleastrolab import dslr
     >>> channel0, exif_info = dslr.read_raw('IMG_0001.CR2',channel_index=0)
    
    """

    try:
        with rawpy.imread(file) as raw:
            image_data = raw.postprocess(output_bps=16,
                                         no_auto_scale=True,
                                         half_size=True,
                                         no_auto_bright=True)
    except LibRawTooBigError:
        raise FileNotFoundError(
                errno.ENOENT, os.strerror(errno.ENOENT), file)

    with open(file,'rb') as fp:
        exif_info = exifread.process_file(fp, details=False)
    if channel_index is None:
        return image_data, exif_info

    return image_data[:,:,channel_index], exif_info

def list_camera_database(return_dict=False):
    """
    Print sensor size and resolution data for all cameras in the database.

    Sensor sizes are width x height in mm.

    Set return_dict=True to return the database as a python dictionary,
    otherwise the results are returned as a string.

    Each value in the returned dictionary if return_dict=True is itself a
    dictionary with the following keys: Make, Model, SensorWidth,
    SensorHeight, ImageWidth, ImageLength

    :param return_dict: return database as a dictionary if True.

    :returns: database as a string or a python dictionary.

    :Example:

     >>> from keeleastrolab import dslr
     >>> print(dslr.list_camera_to_database())

    """
    package_root = os.path.abspath(os.path.dirname(__file__))
    database_path = os.path.join(package_root, 'camera_database.csv')
    with open (database_path) as csvfile:
        reader = csv.DictReader(csvfile)
        if return_dict:
            r = {}
            for row in reader:
                key = f'{row["Make"]}_{row["Model"]}'.replace(' ','_')
                r[key] = row
            return r
        else:
            t = "Make                Model                "
            t += "Width  Height XResolution YResolution\n"
            for row in reader:
                t += f'{row["Make"]:19.19} {row["Model"]:18.18} '
                t += f'{row["Width"]:>7} {row["Height"]:>7} '
                t += f'{row["XResolution"]:>11} {row["YResolution"]:>11}\n'
            return t

