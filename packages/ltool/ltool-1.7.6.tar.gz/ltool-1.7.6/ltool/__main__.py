#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 11:15:48 2016

@author: lidar2
"""
import os
import sys
import warnings
import logging
import getpass
import datetime
from .tools.geom_dtf import feature_id, geom_prop, mask_layers
from .readers.read_scc_db import read_scc_db, trim_arrays, interp_arrays, check_arrays
from .readers.get_files import database
from .readers.parse_config import parse_config
from .export.export_nc import export_nc, nc_name
from .export.update_scc_db import products, product_error, main_error
from .readers.read_config import config
from .debug import log_pack
from .version import __version__
# from .debug.plot import debug_layers

logger = logging.getLogger()

def setup_directories(cfg):
    """ Check if the output folder exists. If not, create it."""
    output_dir = cfg.scc['output-dir']

    log_dir = cfg.scc['log-dir']
    if log_dir:
        if not os.path.isdir(log_dir):
            os.makedirs(log_dir)
            logger.info("Logging directory does not exist. Creating it. %s" % log_dir)

    if not os.path.isdir(output_dir):
        logger.info("Output directory does not exist. Creating it. %s" % output_dir)
        os.makedirs(output_dir)

    return()

def main(args=None):
###############################################################################
# O) Definitions
###############################################################################
    log_pack.scc_logger(logger)
    logger.setLevel('DEBUG')
    start_time = datetime.datetime.now()
    
    logger.info(f"------ ltool version {__version__} ------")
    logger.info("----------------------------------------------------------------")
    logger.info("------ Processing started on %s ------" % start_time)
    
#Ignores all warnings --> they are not printed in terminal
    warnings.filterwarnings('ignore')

    logger.info("Parsing ltool options ")    
    try:
        meas_id, cfg_path = parse_config()
    except Exception as e:
        logger.error("Error while parsing ltool options ")
        sys.exit(2)
    logger.info("Options succesfully parsed ")    
   
#Reading of the configuration file    
    logger.info("Parsing the configuration file ")    
    try:
        cfg = config(cfg_path)
    except Exception as e:
        logger.error("Error while reading the configuration file ")
        sys.exit(2)
    logger.info("Configuration file succesfully parsed ")    
    
# Make directories if they do not exist
    try:
        setup_directories(cfg)
    except Exception as e:
        logger.error("Error while setting up required directories ")
        main_error(meas_id, cfg = cfg, maincode = 3)
        sys.exit(2)
    logger.info("Directories set up succesfully ")    
    
# Add filepath configuration for logging purposes
    log_pack.add_filepath(cfg, meas_id, logger)
    
# Change logging level according to config file
    logger.setLevel(cfg.scc['log-level'].upper())
    
# Get array of input files from an scc database query
    logger.info(f"------ ltool version {__version__} ------")
    logger.info("----------------------------------------------------------------")
    logger.info("------ Processing started on %s ------" % start_time)
    logger.info("Quering the measurement paths in the SCC database ")
    try:
        files, rpath, alphas, snr_factor, wct_peak_margin, \
            prod_type_id, prod_id = \
                database(meas_id, cfg = cfg)
    except Exception as e:
        logger.error("Error while executing a measurement ID query in the SCC database ")
        main_error(meas_id, cfg = cfg, maincode = 4)
        sys.exit(2)

    logger.info("Measurement paths succesfully collected ") 

# Terminate the code if no layer products are defined
    if len(prod_id) == 0:
        logger.error("No product to calculate. Please define at least one LTOOL product for the current configuration ")
        main_error(meas_id, cfg = cfg, maincode = 5)
        sys.exit(2)
    else:
        error = len(prod_id) * [False] 
# From now on different exit codes will be used per product

    for i in range(len(prod_id)):
###############################################################################
# A) Preprocessing
###############################################################################
# A.1) Reading lidar profiles
# Optical Profiles
        logger.info("Section A: Reading the SCC files ")
        try:
            dt_start, alt, prod, prod_err, metadata, wave, rh = \
                read_scc_db(path = files[i])
        
        except Exception as e:
            logger.error("Error while reading the SCC input file ")
            error[i] = product_error(meas_id = meas_id, prod_id = prod_id[i], 
                                     cfg = cfg, exitcode = 6)
            continue

        try:
            alt, prod, prod_err, alt_b, step = \
                trim_arrays(alt = alt, prod = prod, 
                            prod_err = prod_err, rh = rh)
        except Exception as e:
            logger.error(f"Error while trimming the product/error arrays for product ID: {prod_id[i]} ")
            error[i] = product_error(meas_id = meas_id, prod_id = prod_id[i], 
                                     cfg = cfg, exitcode = 7)
            continue
            
        try:
            alt, prod, prod_err = \
                interp_arrays(alt = alt, prod = prod, prod_err = prod_err,
                              step = step, end_fill = alphas[i]/2.)
        except Exception as e:
            logger.error(f"Error while interpolating gaps in the product/error arrays for product ID: {prod_id[i]} ")
            error[i] = product_error(meas_id = meas_id, prod_id = prod_id[i], 
                                     cfg = cfg, exitcode = 8)
            continue

#        from matplotlib import pyplot as plt
#        plt.plot(alt,prod)
#        plt.fill_between(alt,prod-prod_err,prod+prod_err,alpha=0.3)
#        plt.savefig(f'./prof_{prod_id[i]}.png',dpi=300)
#        plt.close()
        
        try:
            check_arrays(alt, prod, prod_err)
        except Exception as e:
            logger.error(f"Insufficient data points in the SCC file for product ID: {prod_id[i]} ")
            error[i] = product_error(meas_id = meas_id, prod_id = prod_id[i], 
                                     cfg = cfg, exitcode = 9)
            continue                
        logger.info("       All SCC files succesfully read ")

###############################################################################
# B) Geometrical retrievals
############################################################################### 
        logger.info(f"****** Proccessing file: {os.path.basename(files[i])} ******")
        logger.info("Section B: Proceeding to the layering algorithm ")
        
# B.1) Identify layers and each base and top
        try:
            rl_flag, bases, tops, wct, wct_err = \
                feature_id(alt, sig = prod, sig_err = prod_err,
                           alpha = alphas[i], snr_factor = snr_factor[i], 
                           wct_peak_margin = wct_peak_margin[i], 
                           floor = alt_b, step = step, log = logger)

        except Exception as e:
            logger.error("Error while identifying layer boundaries ")
            error[i] = product_error(meas_id = meas_id, prod_id = prod_id[i], 
                                     cfg = cfg, exitcode = 10)
            continue
        logger.info("       Potential layer boundaries succesfully identified ")
        
# B.2) Use base and top to the profile to extract aditional geometrical properties
        try:
            geom = geom_prop(rl_flag, bases, tops, alt, prod, log = logger)

        except Exception as e:
            logger.error("Error while calculating layer properties ")
            error[i] = product_error(meas_id = meas_id, prod_id = prod_id[i], 
                                     cfg = cfg, exitcode = 11)
            continue
        logger.info("       Layer properties succesfully calculated ")

###############################################################################
# C) Exporting
###############################################################################
        logger.info("Section C: Exporting layer properties ")
# C.1) Export to netcdf
# C.1.i) Netcdf filename
        try:
            fname = nc_name(metadata, prod_id = prod_id[i], 
                            prod_type_id = prod_type_id[i], wave = wave[i])
        except Exception as e:
            logger.error("Error while creating the netcdf filename ")
            error[i] = product_error(meas_id = meas_id, prod_id = prod_id[i], 
                                     cfg = cfg, exitcode = 12)
            continue
        logger.info("       Netcdf filename succesfully created ")
            
# C.1.ii) Netcdf file 
        if len(geom) > 0:       
            try:
                dir_out = os.path.join(cfg.scc['output-dir'],rpath[i])
                geom_dts = \
                    export_nc(geom, metadata = metadata, alpha = alphas[i], 
                              wave = wave[i], snr_factor = snr_factor[i], 
                              wct_peak_margin = wct_peak_margin[i], 
                              ltool_ver = __version__, fname = fname, 
                              dir_out = dir_out)
            except Exception as e:
                logger.info(dir_out)
                logger.error("Error while creating the netcdf files ")
                error[i] = product_error(meas_id = meas_id, prod_id = prod_id[i], 
                                         cfg = cfg, exitcode = 13)
                continue
            logger.info("       Exporting in NetCDF format succesfully completed ")

## C.2) Save in lists
#        if len(geom) > 0:       
#            list_geom = []
#            list_geom_dts = []
#            list_dates = []                         
#
#            list_dates.append(dt_start[i])
#            list_geom.append(geom)
#            list_geom_dts.append(geom_dts)
        
# C.3) Update the database
        if len(geom) > 0:       
            try:
                fpath = os.path.join(rpath[i],fname)
                products(fpath, meas_id = meas_id, prod_id = prod_id[i], cfg = cfg)
            except Exception as e:
                logger.error("Error while updating the scc database ")
                error[i] = product_error(meas_id = meas_id, prod_id = prod_id[i], 
                                         cfg = cfg, exitcode = 14)
                continue
            logger.info("       SCC database succesfully updated ")
        else:
            logger.warning("       No layers were identified for this measurement! ")

###############################################################################
# End of Program
############################################################################### 
    stop_time = datetime.datetime.now()
    duration = stop_time - start_time
    
    logger.info("------ Processing finished on %s ------" % stop_time)
    logger.info("------ Total duration: %s ------" % duration)
    logger.info("----------------------------------------------------------------")
    logging.shutdown()
    
    if sum(error) == 0: 
        sys.exit(0)
    elif sum(error) == len(error):
        sys.exit(2)
    else:
        sys.exit(1)
