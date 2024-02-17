# -*- coding: utf-8 -*-
"""
stackfits
==============
 Convert digital camera raw files to FITS format.

Functions 
---------
 main() - stackfits

"""

import argparse
from astropy.io import fits
import textwrap
import sys
import os
import numpy as np
from astropy.time import Time

__all__ = ['stackfits']

def stackfits(files, ext=0, stack_function='mean',  norm_func=None,
              output='stack.fits', overwrite=False):
    hduls = []
    for file in files:
        hdul = fits.open(file,memmap=True)
        if hdul[ext].data is None:
            raise ValueError(f'No data in extension {ext} for file {file}')
        hduls.append(hdul)

    if norm_func is None:
        nv = np.ones(len(hduls))
    elif norm_func == 'mean':
        nv = [np.mean(h[ext].data) for h in hduls]
    elif norm_func == 'median':
        nv = [np.median(h[ext].data) for h in hduls]
    else:
        q = float(norm_func[1:])
        nv = [np.percentile(h[ext].data, q) for h in hduls]

    if stack_function == 'mean':
        stack = np.mean([h[ext].data/n for h,n in zip(hduls,nv)], axis=0)
    elif stack_function == 'median':
        stack = np.median([h[ext].data/n for h,n in zip(hduls,nv)], axis=0)
    elif stack_function == 'sum':
        stack = np.sum([h[ext].data/n for h,n in zip(hduls,nv)], axis=0)
    else:
        raise ValueError('Invalid stack_function')
    hdr = fits.PrimaryHDU().header
    try:
        hdr['EXPTIME'] = np.sum([h[0].header['EXPTIME'] for h in hduls])
    except KeyError:
        pass
    try:
        hdr['JD'] = np.round(np.mean([h[0].header['JD'] for h in hduls]),5) 
    except KeyError:
        pass
    try:
        jd = np.mean([Time(h[0].header['DATE-OBS']).jd for h in hduls])
        t = Time(jd,format='jd').isot
        if '.' in t:
            t = t[:t.index('.')]
        hdr['DATE-OBS'] = t
    except KeyError:
        pass
    fits.writeto(output,stack,hdr,overwrite=overwrite)

def main():

    # Set up command line switches
    parser = argparse.ArgumentParser(
        description='Combine images stored in FITS files',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog = textwrap.dedent('''\

        Combines images stored in a series of FITS files by computing the
        mean, median or sum of values pixel-by-pixel.

        Uses memory mapping to avoid loading all the images into memory. 

        The images to be combined must all be the same size.

        Where possible, the total exposure time and mean observing date of the
        images taken from the FITS keyword values EXPTIME, DATE-OBS and JD
        will be written to the header of the output file.

        The images can be normalized prior to being combined by dividing the
        pixel values in each image by a constant computed from all the pixel
        values in the same image using one of the following statistics: mean,
        median, p90 (90-th percentile), p95 (95-th percentile), p99 (99-th
        percentile). Use the --norm option to select this option and to
        specify the statistic to be used, e.g. "--norm median". 

        The input image can be stored in either the primary header data unit
        (ext=0) or in the image extension number specified specified using the
        --ext option.

        '''))

    parser.add_argument('files', nargs='*', type=str, 
        help='FITS files to be combined')

    parser.add_argument('-f', '--fitsfile', default='stack.fits', type=str,
        help='''
        FITS file for output (default: %(default)s)
        ''')

    parser.add_argument('-x', '--ext', default=0, type=int,
        help='''
        FITS extension number for images to be combined (default: %(default)d)
        ''')

    parser.add_argument('-m', '--method', default='mean', 
        choices=['mean','median','sum'],
        help='''
        Method to use to combine images (default: %(default)s)
        ''')

    parser.add_argument('-n', '--norm', default=None, 
        choices=[None, 'mean','median','p90','p95','p99'],
        help='''
        Normalize images using the statistic specified (default: %(default)s)
        ''')

    parser.add_argument('-o', '--overwrite', action='store_const',
                        dest='overwrite', const=True, default=False,
        help='Overwrite existing output FITS files')

    args = parser.parse_args()

    if len(args.files) == 0:
        parser.print_usage()
        sys.exit(1)

    stackfits(args.files, ext=args.ext, stack_function=args.method,
              norm_func=args.norm, output=args.fitsfile,
              overwrite=args.overwrite)

