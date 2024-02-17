# -*- coding: utf-8 -*-
"""
tools
=====

 Functions related to analysing data from from a digital camera.

"""

import rawpy
from rawpy import LibRawTooBigError
import exifread
import errno
import os
import csv
import numpy as np
from astropy.coordinates import SkyCoord
from astropy.wcs import WCS
from astropy.visualization.wcsaxes import WCSAxes
import matplotlib.pyplot as plt
import matplotlib
from astropy.io import fits
from photutils.centroids import centroid_sources
from photutils.aperture import CircularAperture, CircularAnnulus
from photutils.aperture import aperture_photometry as AperturePhotometry
from astropy.table import Table
from warnings import warn

__all__ = ['aperture_photometry', 'inspect_aperture', 'inspect_image',
           'read_raw']

def aperture_photometry(data, x, y, error=None, box_size=11, 
                        radius=4, r_inner=6, r_outer=12, 
                        bkg_reject_tol=5):
    """
    Synthetic aperture photometry at positions specified on an image.

    Uses a circular aperture photometry to compute counts above the local
    background for point sources in an image at approximate positions (x,y)
    in pixel coordinates with origin (0,0).

     The position of the apertures is computed from the centroid of a box with
    size (box_size x box_size) centred at each of the input (x,y) positions.
    Set box_size < 3 to disable this option. N.B. must be an odd integer.

     The local background for each point source in computed from the mean
    value in an annulus centred at the same position as the aperture. The mean
    is calculated after rejecting points more than bkg_reject_tol*m.a.d. from
    the median value in the annulas,  where m.a.d. is the median absolute
    deviation of the pixels in the annulus. 

     The standard error on the flux measurement is computed if the standard
     error on each input pixel is provided in the input array "error". This
     includes the uncertainty on the local background level computed from the
     standard error on the mean for non-rejected pixels in each annulus.

    :param data: image with point sources

    :param x: array of point source x coordinates in pixels
    
    :param y: array of point source y coordinates in pixels

    :param error: image standard error values - same size as data.

    :param box_size: box size for computing point source positions.

    :param radius: aperture radius in pixels.

    :param r_inner: inner radius of annulus for background estimate in pixels.

    :param r_outer: outer radius of annulus for background estimate in pixels.

    :bkg_reject_tol: Tolerance to reject pixels for local background estimate.

    :returns: An astropy.table table of the photometry and other information.

    :Example:

     >>> from keeleastrolab.tools import aperture_photometry
     >>> phot_table = aperture_photometry(data, [123.1, 234.5],[76.2, 99.3])
    
    """
    if box_size < 3:
        xcen = x
        ycen = y
    else:
        xcen, ycen = centroid_sources(data, x, y, box_size=box_size)

    positions = np.transpose((xcen,ycen))

    apertures = CircularAperture(positions, r=radius)
    sky_annuli = CircularAnnulus(positions, r_in=r_inner, r_out=r_outer)

    peak = []
    bkg_med = []
    bkg_mad = []
    bkg_mean = []
    bkg_sem = []
    bkg_n = []
    for ap,an in zip(apertures, sky_annuli):
        peak.append(data[ap.to_mask().to_image(data.shape) > 0].max())
        # Used method = 'center' so mask values are 0 or 1 so we can avoid
        # complications of using weighted statistics.
        am = an.to_mask(method='center') # ApertureMask object
        dm = am.to_image(data.shape) > 0 # aperture bool mask, same size as data
        an_med = np.median(data[dm])     # median value in annulus
        an_mad = np.median(np.abs(data[dm]-an_med))  # m.a.d. in annulus
        # Mask for outliers, same size as data 
        data_an_bad = (abs(data - an_med) > (bkg_reject_tol*an_mad)) & dm
        # Mask for values for local background estimate, same size as # data
        use_mask = dm & ~data_an_bad
        n = np.sum(use_mask)
        an_mean = np.mean(data[use_mask])
        if n > 1:
            an_sem = np.std(data[use_mask])/np.sqrt(np.sum(use_mask)-1)
        else:
            an_sem = np.nan
        bkg_med.append(an_med)
        bkg_mad.append(an_mad)
        bkg_mean.append(an_mean)
        bkg_sem.append(an_sem)
        bkg_n.append(n)

    d = [x,y,peak,bkg_mean,bkg_sem,bkg_n,bkg_med,bkg_mad]
    n = ['x','y','peak','bkg_mean','bkg_sem','bkg_n','bkg_med','bkg_mad']
    results = Table(d,names=n)
    phot_table = AperturePhotometry(data, apertures, error=error)
    results.add_column(phot_table['id'], name='id', index=0)
    results['aperture_sum'] = phot_table['aperture_sum']
    if error is not None:
        results['aperture_sum_err'] = phot_table['aperture_sum_err']

    apareas = apertures.area_overlap(data)
    results['bkg_total'] = results['bkg_mean'] * apareas
    flux = phot_table['aperture_sum'] - results['bkg_total']
    results.add_column(flux, index=3,name='flux')
    if error is not None:
        bkg_total_err = results['bkg_sem'] * apareas
        results['bkg_total_err'] = bkg_total_err
        flux_err = np.hypot(phot_table['aperture_sum_err'],bkg_total_err)
        results.add_column(flux_err, index=4,name='flux_err')
        for col in ['flux_err', 'bkg_total_err','aperture_sum_err']:
            results[col].info.format = '%.2f'

    for col in ['x','y','flux','peak','bkg_mean','bkg_sem','bkg_total',
                'aperture_sum']:
        results[col].info.format = '%.2f'

    # Add meta data to table for use with inspect_aperture
    results.meta['box_size'] = box_size
    results.meta['radius'] = radius
    results.meta['r_inner'] = r_inner
    results.meta['r_outer'] = r_outer
    results.meta['bgrejtol'] = bkg_reject_tol
    results.meta['datasum'] = np.sum(data)   # used as a checksum

    return results

def read_raw(file, channel='G'):
    """
    Read image data for one colour and EXIF information from a raw file.

    If there two channels corresponding to the selected colour (typically for
    'G') then the two image data values are summed.
    
    Return image data as a numpy array, an EXIF tags dictionary.

    :param file: full path to file containing raw image data.

    :returns: image_data, exif_info

    :Example:

     >>> from keeleastrolab import tools
     >>> green_image, exif_info = tools.read_raw('IMG_0001.CR2')
     >>> blue_image, _ = tools.read_raw('IMG_0001.CR2',channel='B')
    
    """

    try:
        with rawpy.imread(file) as raw:
            raw_image = raw.raw_image_visible
            raw_colors = raw.raw_colors_visible
            color_desc = raw.color_desc.decode()
            if channel not in color_desc:
                msg = f'No such colour {channel} in raw image file {file}'
                raise ValueError(msg)
            new_shape = [s//2 for s in raw_image.shape]
            image_data  = np.zeros(new_shape)
            for i,c in enumerate(color_desc):
                if c == channel:
                    image_data += raw_image[raw_colors == i].reshape(new_shape)
    except LibRawTooBigError:
        raise FileNotFoundError(
                errno.ENOENT, os.strerror(errno.ENOENT), file)

    with open(file,'rb') as fp:
        exif_info = exifread.process_file(fp, details=False)

    return image_data, exif_info



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

     >>> from keeleastrolab import tools
     >>> print(tools.list_camera_to_database())

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

def inspect_aperture(aperture_id, data, results_table, figsize=None, 
                     vertical=False,  margin=3, 
                     pmin=50, pmax=99, cmap='Greens', title=None):
    """ 
    Diagnostic plot for an aperture used for aperture_photometry 

    The first panel shows an image of the data together with the aperture used
    to measure the source flux (red) and the annulus used to measure the local
    background level (blue). Any pixels excluded from the calculation of the
    local background level are marked with a red cross. 

    The second panel shows a histogram of the pixel data values used to
    measure the local background level. The mean value is indicated by a
    vertical line and the limits used to reject pixels from the calculation
    are shown with dashed lines. 

    :param aperture_id: aperture to plot (from id column of results_table)

    :param data: image data array used in aperture_photometry

    :param results_table: output astropy.table from aperture_photometry

    :param figsize: figure size for matplot Figure object

    :param vertical: plots one above the other (True) or side-by-side (False) 

    :param margin: margin around annulus in pixels for image display

    :param pmin: percentile data value for minimum of image display scaling

    :param pmax: percentile data value for maximum of image display scaling

    :param cmap: colour map name for image display

    :title: optional plot title

    :returns:  matplotlib Figure object.

    """

    r = results_table[results_table['id'] == aperture_id]
    h = results_table.meta
    xy = np.array([r['x'],r['y']]).T
    aperture = CircularAperture(xy, h['radius'])[0]
    annulus = CircularAnnulus(xy, r_in=h['r_inner'], r_out=h['r_outer'])[0]

    if figsize is None:
        if vertical:
            fs = (3,6)
        else:
            fs = (7,3)
    else:
        fs = figsize

    if vertical:
        fig,axes = plt.subplots(nrows=2, figsize=fs)
    else:
        fig,axes = plt.subplots(ncols=2, figsize=fs)

    img = axes[0].imshow(data,
                         vmin=np.percentile(data,pmin),
                         vmax=np.percentile(data,pmax),
                         origin='lower',cmap=cmap)
    aperture.plot(ax=axes[0],color='r', lw=2)
    annulus.plot(ax=axes[0],color='b', lw=2)
    bb = annulus.bbox
    axes[0].set_xlim(bb.ixmin-margin, bb.ixmax+margin)
    axes[0].set_ylim(bb.iymin-margin, bb.iymax+margin)
    axes[0].set_xlabel('Column [pixels]')
    axes[0].set_ylabel('Row [pixels]')
    axes[0].set_title(title)
    
    # Find and plot pixels rejected from sky aperture
    if abs(np.sum(data) - h['datasum']) > 0:
        warn('Data for display differs from data used for aperture_photometry')
    else:
        xx,yy = np.meshgrid(np.arange(data.shape[1]),np.arange(data.shape[0]))
        am = annulus.to_mask(method='center') # ApertureMask object
        dm = am.to_image(data.shape) > 0 # aperture bool mask, same size as data
        an_med = np.median(data[dm])     # median value in annulus
        an_mad = np.median(np.abs(data[dm]-an_med))  # m.a.d. in annulus
        # Mask for outliers, same size as data 
        data_an_bad = (abs(data - an_med) > (h['bgrejtol']*an_mad)) & dm
        axes[0].plot(xx[data_an_bad],yy[data_an_bad],'rx')
        use_mask = dm & ~data_an_bad
        hist = axes[1].hist(data[dm])
        an_mean = np.mean(data[use_mask])
        xlo = an_med-h['bgrejtol']*an_mad
        xhi = an_med+h['bgrejtol']*an_mad
        axes[1].set_xlim(xlo-0.5*(xhi-xlo), xhi+0.5*(xhi-xlo))
        axes[1].axvline(an_mean,c='r',label='Mean')
        axes[1].axvline(xlo,c='r',ls='--',label='Limits')
        axes[1].axvline(xhi,c='r',ls='--')
        axes[1].set_xlabel('Data value')
        axes[1].set_ylabel('N')

    fig.tight_layout()
    return fig
    
def inspect_image(fitsfile, pmin=90, pmax=99.9, cmap='Greens', 
                  swap_axes = None, figsize=(9,6)):
    class myWCSAxes(WCSAxes):
        def _display_world_coords(self, x, y):
            if not self._drawn:
                return ""
            pixel = np.array([x, y])
            coords = self._all_coords[self._display_coords_index]
            world = coords._transform.transform(np.array([pixel]))[0]
            c=SkyCoord(world[0],world[1],unit='degree') 
            r=c.ra.to_string(unit='hour',fields=2,pad=True,format='unicode')
            d=c.dec.to_string(fields=2,pad=True,alwayssign=True,format='unicode')
            return f"{r}, {d} ({x:6.1f}, {y:6.1f})"

    def format_cursor_data(self,data):
        return f': {data:6.0f}'

    matplotlib.artist.Artist.format_cursor_data=format_cursor_data

    fig = plt.figure(figsize=(9,6))
    data,hdr = fits.getdata(fitsfile,header=True)
    wcs = WCS(hdr)
    if wcs.has_celestial:
        ax = myWCSAxes(fig, [0.1,0.1,0.8,0.8], wcs=wcs)
        img = ax.imshow(data,
            vmin=np.percentile(data,pmin),
            vmax=np.percentile(data,pmax),
            origin='lower',cmap=cmap)
        lon = ax.coords[0]
        lat = ax.coords[1]
        if swap_axes is None:
            pc = wcs.pixel_scale_matrix
            _swap_axes = np.hypot(pc[0,0],pc[1,1]) < np.hypot(pc[1,0],pc[0,1])
        else:
            _swap_axes = swap_axes
        if _swap_axes:
            lon.set_ticks_position('lr')
            lon.set_ticklabel_position('lr')
            lat.set_ticks_position('tb')
            lat.set_ticklabel_position('tb')
            ax.set_xlabel('Dec')
            ax.set_ylabel('RA')
        else:
            lat.set_ticks_position('lr')
            lat.set_ticklabel_position('lr')
            lon.set_ticks_position('tb')
            lon.set_ticklabel_position('tb')
            ax.set_xlabel('RA')
            ax.set_ylabel('Dec')
        ax.grid()
        fig.tight_layout()
        fig.add_axes(ax);  # axes have to be explicitly added to the figure
    else:
        plt.imshow(data,
                vmin=np.percentile(data,pmin),
                vmax=np.percentile(data,pmax),
                origin='lower',cmap=cmap)
        plt.xlabel('Column')
        plt.ylabel('Row')
        fig.tight_layout()
    return fig
