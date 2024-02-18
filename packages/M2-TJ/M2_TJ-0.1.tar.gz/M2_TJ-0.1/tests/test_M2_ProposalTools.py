import pytest
import M2_ProposalTools.WorkHorse as WH
import M2_ProposalTools.FilterImages as FI
import M2_ProposalTools.MakeRMSmap as MRM
import numpy as np
import os
import astropy.units as u

def test_locate_xfer_files():

    #xferfile       = "xfer_Function_3p0_21Aonly_PCA5_0f08Filtering.txt"
    xferfile       = "src/M2_ProposalTools/xfer_Function_3p0_21Aonly_PCA5_0f08Filtering.txt"
    fileexists     = os.path.exists(xferfile)
    assert fileexists

    
    
def test_HDU_generation():

    Center  = [280.0, 45.0]                     # Arbitrary RA and Dec
    pixsize = 2.0                               # arcseconds
    xsize   = 12.0                              # arcminutes; this is a bit larger than typical
    ysize   = 12.0                              # arcminutes
    nx      = int(np.round(xsize*60/pixsize))   # Number of pixels (must be an integer!)
    ny      = int(np.round(ysize*60/pixsize))   # Number of pixels (must be an integer!)
    TemplateHDU = MRM.make_template_hdul(nx,ny,Center,pixsize)

    assert len(TemplateHDU) == 1

def test_RMS_generation():    

    Center  = [280.0, 45.0]                     # Arbitrary RA and Dec
    pixsize = 2.0                               # arcseconds
    xsize   = 12.0                              # arcminutes; this is a bit larger than typical
    ysize   = 12.0                              # arcminutes
    nx      = int(np.round(xsize*60/pixsize))   # Number of pixels (must be an integer!)
    ny      = int(np.round(ysize*60/pixsize))   # Number of pixels (must be an integer!)
    Ptgs    = [Center]                          # Pointings should be a list of (RA,Dec) array-like values.
    sizes   = [-3.5]                            # Let's try offset scans! Here, 3.5' scans, offset
    times   = [10.0]                            # 10 hours
    offset  = 1.5                               # 1.5 arcminute offset (the default, but we may change it)

    TemplateHDU = MRM.make_template_hdul(nx,ny,Center,pixsize)
    RMSmap,nscans = MRM.make_rms_map(TemplateHDU,Ptgs,sizes,times,offset=offset)

    nPixX,nPixY = RMSmap.shape
    c1          = (nx == nPixX)
    c2          = (ny == nPixY)
    c3          = (np.max(RMSmap) > 0)
    assert c1*c2*c3

def test_A10_generation():

    M500       = 3.9*1e14*u.M_sun
    z          = 0.86
    pixsize    = 2.0
    ymap       = WH.make_A10Map(M500,z,pixsize=pixsize,Dist=True)
    c1         = np.max(ymap) > 0
    c2         = np.max(ymap) < 1e-2
    
    assert c1*c2
