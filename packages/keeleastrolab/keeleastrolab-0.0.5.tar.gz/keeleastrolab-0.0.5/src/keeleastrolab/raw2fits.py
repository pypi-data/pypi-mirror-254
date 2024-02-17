# -*- coding: utf-8 -*-
"""
raw2fits
==============
 Convert digital camera raw files to FITS format.

Functions 
---------
 main() - raw2fits

"""

import argparse
import rawpy
import exifread
from astropy.io import fits
import astrometry
import textwrap
import sys
import os
import io
from contextlib import contextmanager
import tempfile
from astropy.time import Time
from astropy.coordinates import EarthLocation, SkyCoord, AltAz
from photutils.detection import DAOStarFinder
from . import tools
import numpy as np
import csv

__all__ = ['raw2fits']

# From https://eli.thegreenplace.net/2015/redirecting-all-kinds-of-stdout-in-python/
@contextmanager
def stderr_redirector(stream):
    # The original fd stderr points to. Usually 1 on POSIX systems.
    original_stderr_fd = sys.stderr.fileno()

    def _redirect_stderr(to_fd):
        """Redirect stderr to the given file descriptor."""
        # Flush and close sys.stderr - also closes the file descriptor (fd)
        sys.stderr.close()
        # Make original_stderr_fd point to the same file as to_fd
        os.dup2(to_fd, original_stderr_fd)
        # Create a new sys.stderr that points to the redirected fd
        sys.stderr = io.TextIOWrapper(os.fdopen(original_stderr_fd, 'wb'))

    # Save a copy of the original stderr fd in saved_stderr_fd
    saved_stderr_fd = os.dup(original_stderr_fd)
    try:
        # Create a temporary file and redirect stderr to it
        tfile = tempfile.TemporaryFile(mode='w+b')
        _redirect_stderr(tfile.fileno())
        # Yield to caller, then redirect stderr back to the saved fd
        yield
        _redirect_stderr(saved_stderr_fd)
        # Copy contents of temporary file to the given stream
        tfile.flush()
        tfile.seek(0, io.SEEK_SET)
        stream.write(tfile.read())
    finally:
        tfile.close()
        os.close(saved_stderr_fd)

def raw2fits(file, wcs=True, channel='G', N=1, verbose=1,  
             overwrite=False, extension='fits',
             threshold=10, fwhm=4,
             site='Keele Observatory', elev=208, 
             object_name=None,
             position_hint=None, radius_deg=15):

    def get_rational(rational_string):
        split = rational_string.split('/')
        if len(split) == 1:
            return int(split[0])
        else:
            return float(split[0])/float(split[1])

    data,exif = tools.read_raw(file, channel)
    if verbose > 2: print(f'\nRead file {file}')

    if N > 1:
        if verbose > 2: print(f'  Binning data {N}x{N}')
        s = data.shape
        x = data[0:s[0]//N*N,0:s[1]//N*N] # Trim excess pixels
        s = x.shape
        y = x.reshape(s[0]//N, N, s[1]//N, N)
        del x
        data = y.sum(axis=(1, 3))
        del y
        if verbose > 2:
            print(f'  Input image size = {s[0]} x {s[1]} pixels')
            s = data.shape
            print(f'  Output image size = {s[0]} x {s[1]} pixels')
    else:
        if verbose > 2:
            print(f'  No pixel binning applied')
            s = data.shape
            print(f'  Input image size = {s[0]} x {s[1]} pixels')

    if verbose > 2:
        print(f'  Writing channel {channel} to primary header data unit')
    hdu = fits.PrimaryHDU(data)
    hdul = fits.HDUList(hdu)
    hdr = hdul[0].header
    hdr['CHANNEL'] = channel,'Channel (R,G,B)'

    hdr['SITENAME'] = site
    hdr['SITEELEV'] = elev
    obssite = EarthLocation.of_address(site)
    latstr = obssite.lat.to_string(sep=' ',precision=0)
    hdr['LATITUDE'] = latstr
    lonstr = obssite.lon.to_string(sep=' ',precision=0,alwayssign=True)
    hdr['LONGITUD'] = lonstr
    if verbose > 2:
        print(f'  Found data for observing site {site}')
        print(f'    Elevation = {elev:0.1f} m')
        print(f'    Latitude  = {latstr}')
        print(f'    Longitude = {lonstr}')

    flnm = os.path.splitext(os.path.split(file)[1])[0]
    txt = f'{flnm:12.12s} '
    if 'Image DateTime' in exif:
        dstr,tstr = str(exif['Image DateTime']).split()
        if verbose > 2:
            print(f'  Found "Image DateTime" EXIF tag: {dstr} {tstr}')
        dateobs = dstr.replace(':','-')+'T'+tstr
        hdr['DATE-OBS'] = dateobs
        obstime = Time(dateobs)
        hdr['MJD-OBS'] = round(obstime.mjd,5)
        jd = obstime.jd
        if verbose > 2:
            print(f'  Julian Date at start of exposure = {jd:0.5f}')
        hdr['JD_SOBS']=round(jd,5),'Julian Date at start of exposure'
        if 'EXIF ExposureTime' in exif:
            jd += get_rational(str(exif['EXIF ExposureTime']))/86400/2
            hdr['JD']=round(jd,5),'Julian Date (UTC) at mid-exposure'
            if verbose > 2:
                print(f'  Julian Date (UTC) at mid-exposure = {jd:0.5f}')
        txt += dstr.replace(':','-')+' '+tstr
    else:
        if verbose > 2:
            print(f'  No "Image DateTime" EXIF tag in file')
        txt += '                    '

    if N>1:
        hdr['BINNING'] = N,'binning factor applied to raw data'

    if object_name is not None:
        hdr['OBJECT'] = object_name,'From astrometry position hint'

    d = {'EXPTIME':'EXIF ExposureTime',
         'FNUMBER':'EXIF FNumber',
         'ISO':'EXIF ISOSpeedRatings',
         'FOCALLEN':'EXIF FocalLength'}
    for k in d:
        tag = d[k]
        if tag in exif:
            s = str(exif[tag])
            if verbose > 2: print(f'  Found "{tag}" : {s}')
            v = get_rational(s)
            hdr[k] = v, tag
            if k == "EXPTIME":
                txt += f'{s:>7.7}'
            elif k == 'FNUMBER':
                txt += f'{v:5.1f}'
            elif k == "ISO":
                txt += f'{s:>5.5}'
            elif k == "FOCALLEN":
                txt += f'{s:>5.5}'
            else:
                txt += f'{s:>8.8}'
        else:
            if k == "EXPTIME":
                txt += f'       '
            elif k == 'FNUMBER':
                txt += '     '
            elif k == "ISO":
                txt += '     '    
            elif k == "FOCALLEN":
                txt += f'     '
            else:
                txt += '        '
    
    d = {'MAKE':'Image Make',
         'MODEL':'Image Model',
         'LENSNAME':'EXIF LensModel',
         'SNUMBODY': 'EXIF BodySerialNumber',
         'SNUMLENS': 'EXIF LensSerialNumber'}
    for k in d:
        tag = d[k]
        try:
            s = str(exif[tag]).strip()
        except KeyError:
            continue
        if verbose > 2: print(f'  Found "{tag}" : {s}')
        if len(s) > 68:
            hdr[k] = s[:68], tag
        else:
            hdr[k] = s, tag

    if ("Image Make" in exif) & ("Image Model" in exif):
        db = tools.list_camera_database(return_dict=True)
        make = str(exif["Image Make"]).strip()
        model = str(exif["Image Model"]).strip()
        key = f'{make}_{model}'.replace(' ','_')
        if verbose > 2: print(f'  Found "Image Make" EXIF tag: {make}')
        if verbose > 2: print(f'  Found "Image Model" EXIF tag: {model}')
        if key in db:
            xres = float(db[key]['XResolution'])
            yres = float(db[key]['YResolution'])
            w=float(db[key]['Width'])
            h=float(db[key]['Height'])
            # Factor 2 here because we use the option half_size=True
            # to read image with rawpy
            xpixsz = N*1000*w/xres*2
            ypixsz = N*1000*h/yres*2
            hdr['XPIXSZ'] = round(xpixsz,1),'pixel width, micron'
            hdr['YPIXSZ'] = round(ypixsz,1),'pixel height, micron'
            if verbose > 2:
                print(f'  Found camera in camera_database.csv')
                print(f'    XResolution: {xres:0.0f}')
                print(f'    YResolution: {yres:0.0f}')
                print(f'    Width: {w}')
                print(f'    Height: {h}')
        else:
            if verbose > 2: print(f'  No match in camera_database.csv')
    else:
        xpixsz,ypixsz = None,None
        if verbose > 2:
            print(f'  Missing "Image Make" or "Image Model" EXIF tag')

    med = np.median(data)
    medabsdev = np.median(np.abs(data-med))

    if verbose == 2:
        txt += f' {np.mean(data):8.1f} {np.std(data):8.1f} {med:6.0f}'
        txt += f' {medabsdev:9.1f} '
    if verbose > 2:
        print(f'  Image mean = {np.mean(data):0.1f}')
        print(f'  Image std. dev. = {np.std(data):0.1f}')
        print(f'  Image median = {np.median(data):0.0f}')
        print(f'  Image median abs. dev. = {medabsdev:0.1f}')

    if xpixsz is not None and 'EXIF FocalLength' in exif:
        fl = get_rational(str(exif['EXIF FocalLength']))
        wim = data.shape[1]*3.43775*xpixsz/fl  # image width, arcmin 
        him = data.shape[0]*3.43775*ypixsz/fl  # image height, arcmin 
        if verbose > 2:
            print(f'  Image size [arcmin] = {wim:0.1f} x {him:0.1f}')
    else:
        wim,him = None,None

    if wcs and wim is None:
        if verbose > 2:
            print('  WCS solution not attempted - could not determine image'
                  ' size.')
    elif wcs:
        t = round(threshold*medabsdev,1)
        if verbose > 2:
            print(f'  Running DAOStarFinder(fwhm={fwhm}, threshold={t})')
        daofind = DAOStarFinder(fwhm=fwhm, threshold=t)
        sources = daofind(data)
        if verbose > 2:
            for l in sources.pformat():
                    print(f'   {l}')

        arcsec_per_pixel = 206.265*0.5*(xpixsz+ypixsz)/fl

        # Select index file scales 
        # See https://astrometry.net/doc/readme.html
        package_root = os.path.abspath(os.path.dirname(__file__))
        csvfile_path = os.path.join(package_root, 'astrometry_index_files.csv')
        thi = np.sqrt(wim*him)/2
        tlo = thi/2
        scales = []   # set of index file scales
        with open (csvfile_path) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                dmin = float(row['dmin'])
                dmax = float(row['dmax'])
                if (thi > dmin) & (tlo < dmax):
                    scales.append(int(row['scale']))
        if verbose > 2:
            print('  Selected index file scales '+str(scales))
        solver = astrometry.Solver(
                astrometry.series_4100.index_files(
                    cache_directory=package_root, scales=scales))
        if position_hint is None:
            phint = None
            if verbose > 2:
                print('  No position hint provided.')
        else:
            ra_deg=position_hint.ra.degree
            dec_deg=position_hint.dec.degree
            phint = astrometry.PositionHint(
                    ra_deg=ra_deg, dec_deg=dec_deg, radius_deg=radius_deg)
            if verbose > 2:
                print(f'  Using position hint {ra_deg=:0.3f}, {dec_deg=:0.3f},'
                      f'{radius_deg=:0.2f}')

        lower_arcsec_per_pixel=0.9*arcsec_per_pixel
        upper_arcsec_per_pixel=1.1*arcsec_per_pixel
        shint = astrometry.SizeHint(
                lower_arcsec_per_pixel=lower_arcsec_per_pixel,
                upper_arcsec_per_pixel=upper_arcsec_per_pixel)
        if verbose > 2:
            print(f'  Using size hint {lower_arcsec_per_pixel=:0.2f},'
                f' {upper_arcsec_per_pixel=:0.2f}')

        xy = np.transpose((sources['xcentroid'], sources['ycentroid']))
        spar = astrometry.SolutionParameters(
                logodds_callback=lambda logodds_list: (
                    astrometry.Action.STOP
                    if logodds_list[0] > 100.0
                    else astrometry.Action.CONTINUE),)
        # Suppress printed error messages from astrometry
        f = io.BytesIO()
        with stderr_redirector(f):
            solution = solver.solve(stars=xy,
                                    size_hint=shint,
                                    position_hint=phint,
                                    solution_parameters=spar)
        if solution.has_match():
            best_match = solution.best_match()
            center_ra_deg = best_match.center_ra_deg
            center_dec_deg = best_match.center_dec_deg
            arcsec_per_pixel = best_match.scale_arcsec_per_pixel 
            n_match = len(best_match.stars)
            if verbose > 2:
                print(f"  Found plate solution")
                print(f"{    center_ra_deg=:0.5f}")
                print(f"{    center_dec_deg=:0.5f}")
                print(f"{    arcsec_per_pixel=:0.2f}")
                print(f"{    n_match=}")
                if obstime is not None and obssite is not None:
                    a = AltAz(obstime=obstime,location=obssite)
                    altaz_p = position_hint.transform_to(a)
                    c = SkyCoord(center_ra_deg,center_dec_deg,unit='degree')
                    altaz_c = c.transform_to(a)
                    print(f"  Object : Azimuth = {altaz_p.az:0.1f},"
                          f"Altitude = {altaz_p.alt:.1f}")
                    print(f"  Image:   Azimuth = {altaz_c.az:0.1f},"
                          f"Altitude = {altaz_c.alt:.1f}")
                    azoff,altoff = altaz_c.spherical_offsets_to(altaz_p)
                    print(f"  Offset (az, alt) from centre to object = "
                          f"{azoff:.1f}, {altoff:0.1f}")
                    raoff,decoff = c.spherical_offsets_to(position_hint)
                    print(f"  Offset (ra, dec) from centre to object = "
                          f"{raoff:.1f}, {decoff:0.1f}")
            elif verbose > 0:
                txt += f' {center_ra_deg:8.4f} {center_dec_deg:+8.4f}'
                txt += f' {n_match:8d}'
            wcs_fields = best_match.wcs_fields
            for key in wcs_fields:
                hdr[key] = wcs_fields[key]
        else:
            if verbose > 2:
                print(f"  Failed to find plate solution")


    elif wcs and (verbose > 2):
        if xpixsz is None:
            print('  WCS not attempted - pixel size information missing')
        if 'EXIF FocalLength' not in exif:
            print('  WCS not attempted - EXIF FocalLength tag missing') 

    fitsfile = os.path.splitext(file)[0]+extension

    for hdu in hdul:
        hdu.add_checksum()
    hdul.writeto(fitsfile,overwrite=overwrite)

    if verbose in [1,2]:
        print(txt)


def main():

    # Set up command line switches
    parser = argparse.ArgumentParser(
        description='Convert digital camera raw files to FITS format',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog = textwrap.dedent('''\

        For each raw file given on the command line, create a FITS file
        containing the data from one channel in the primary header data unit.

        The image meta-data provided in the EXIF tags in the raw file are
        converted to FITS header keyword values as shown in the table below.
        Missing EXIF tags are not written and no error is reported in this
        case. 

         EXIF                    FITS      Notes   
         -------------------------------------------------------------------- 
         "Image DateTime"        DATE-OBS  ISO 8601 format
         "Image Make"            MAKE      Truncated to 68 characters
         "Image Model"           MODEL     Truncated to 68 characters
         "EXIF ExposureTime"     EXPTIME   seconds
         "EXIF FNumber"          FNUMBER   
         "EXIF ISOSpeedRatings"  ISO       
         "EXIF FocalLength"      FOCALLEN  mm
         "EXIF LensModel"        LENSNAME  Truncated to 68 characters
         "EXIF BodySerialNumber" SNUMBODY  
         "EXIF LensSerialNumber" SNUMLENS 

        If the --wcs option is used then the photutils routine DAOStarFinder
        is used to detect stars in the image and their positions are passed to
        the astrometry.net plate solver running locally to find the parameters
        of a WCS transformation that are added to FITS header. 

        N.B. this is slow. Providing an accurate position hint and reducing
        the search radius, or reducing the number of detected stars can both
        help to speed up the process. 

        For star detection, the median absolute deviation from the image
        median (MedAbsDev) of all image pixel values is computed and the
        sources are selected if their peak value is THRESHOLD*MedAbsDev above
        the image median value. 

        Position hints for the astrometry solver must be specified as a source
        name to be passed to astropy.coordinates.SkyCoord.from_name(). It is
        possible to pass coordinates to this routine in the format
        "JHHMMSS.SS[+-]DDMMSS.S", e.g. "J000508.81+675024.0". If the star name
        includes spaces, pass the argument in quotes or replace spaces with
        "_", e.g. "raw2fits -p del_Cep IMG_0001.CR2". The identifier passed
        with this argument is added to the FITS header with keyword "OBJECT".

        If the MAKE and MODEL values in the EXIF data are found in the file
        camera_database.csv then the image pixel width and height in microns
        are added to the FITS header using the keywords XPIXSZ and YPIXSZ,
        respectively. If binning is used then XPIXSZ and YPIXSZ correspond to
        the binned pixel size, not the original pixel size.

        The level of output can be controlled with the --verbose option.

         Level   Output 
         ------------------------------------------------------------------- 
             0   None.
             1   One-line summary per file, 80 character width.
             2   One-line summary per file, 132 character width.
             3   Full details of image processing steps and WCS calibration.

        If --wcs is specified and the astrometric calibration is succesful and
        --verbose 1 or 2 then the final three columns printed to standard
        output will show the RA and declination of the central pixel followed
        by the number of matched stars used in the WCS calibration (n_match).

        If --wcs is specified and the astrometric calibration is succesful and
        --verbose 3 is used then RA and declination of the central pixel are
        printed to standard output together with the offset from the
        coordinates obtained from position_hint to this pixel in RA,
        declination, altitide and azimuth. 

        The string specified with the --site option is sent to the function
        astropy.coordinates.EarthLocation.of_address() to obtain the latitude
        and longitude of the observer. These are added to the output FITS file
        headers with the keywords SITENAME, LATITUDE and  LONGITUD. The
        elevation of the observing site can also be set using the --elev
        option and is stored in the output FITS file headers with the keyword
        SITEELEV. 

        If --verbose 2 is used, the following statistics for the binned image
        pixel values are also printed  - mean, median, standard deviation,
        median absolute deviation from the image median (MedAbsDev).

        Digital camera images typically have two green "G" channels. These are
        added together  to form a single image for output to the FITS file.

        '''))

    parser.add_argument('files', nargs='*', type=str, 
        help='Raw files to be converted to FITS format')

    parser.add_argument('-c', '--channel', default='G', type=str,
        choices = ['R','G','B'],
        help='Channel to store in FITS file (default: %(default)s)')

    parser.add_argument('-x', '--extension', default='.fits', type=str,
        help='New filename extension (default: %(default)s)')

    parser.add_argument('-o', '--overwrite', action='store_const',
                        dest='overwrite', const=True, default=False,
        help='Overwrite existing FITS files')

    parser.add_argument('-b', '--binning', default=1, type=int, dest='N',
        help='''
        Combine output pixels in NxN blocks
        (default: %(default)d)
        ''')

    parser.add_argument('-w', '--wcs', action='store_const',
        dest='wcs', const=True, default=False,
        help='Attempt to compute WCS parameters for FITS header')

    parser.add_argument('-t', '--threshold', default=10.0, type=float,
        help='''
        Threshold as factor of image MedAbsDev for star detection
        (default: %(default)3.1f)
        ''')

    parser.add_argument('-s', '--site', default='Keele Observatory', type=str,
        help='Location of observer (default: %(default)s)')

    parser.add_argument('-e', '--elev', default=208., type=float,
        help='Elevation of observer in metres  (default: %(default)s)')

    parser.add_argument('-f', '--fwhm', default=4.0, type=float,
        help='''
        Width of gaussian kernel for source detection algorithm
        (default: %(default)3.1f)
        ''')

    parser.add_argument('-p', '--position-hint', default=None, type=str,
        help='Position hint for astrometry solver')

    parser.add_argument('-r', '--radius', default=10., type=float,
        help='Search radius around position hint (degrees)')

    parser.add_argument('-v', '--verbose', default=2, type=int, 
        choices = [0,1,2,3],
        help='''
        Control level of detail printed to standard output
        (default: %(default)d)
        ''')

    args = parser.parse_args()

    if len(args.files) == 0:
        parser.print_usage()
        sys.exit(1)

    for file in args.files:
        # rawpy gives wierd errors for missing/unreadable files so quick
        # do a quick dry-run to check files exist and are readable first
        with open(file,'r') as f:
            pass

    if args.verbose in [1,2]:
        txt='File         Date       Time     Texp   f/   ISO  f.l.'
        if args.verbose == 2:
            txt += ' Mean     StdDev   Median MedAbsDev'
        if args.wcs:
            txt += '  RA       Dec       n_match'
        print(txt)

    # Take this out of the loop
    if args.position_hint is None:
        coords = None
    else:
        coords = SkyCoord.from_name(args.position_hint)

    for file in args.files:
        raw2fits(file, args.wcs, args.channel, args.N, args.verbose,
                 args.overwrite, args.extension, args.threshold, args.fwhm,
                 args.site, args.elev, args.position_hint, coords, args.radius)

