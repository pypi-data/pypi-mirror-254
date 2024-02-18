import numpy as np
import astropy.units as u
import astropy.constants as const
import scipy.constants as spconst
#from astropy.cosmology import Planck15 as cosmo
from astropy.cosmology import FlatLambdaCDM
cosmo = FlatLambdaCDM(H0=70.0, Om0=0.3, Tcmb0=2.725)
import M2_ProposalTools.numerical_integration as ni
from astropy.coordinates import Angle #
import scipy

defaultYM = 'A10'

def inst_params(instrument):

    if instrument == "MUSTANG":
        fwhm1 = 8.7*u.arcsec  # arcseconds
        norm1 = 0.94          # normalization
        fwhm2 = 28.4*u.arcsec # arcseconds
        norm2 = 0.06          # normalization
        fwhm  = 9.0*u.arcsec
        smfw  = 10.0*u.arcsec
        freq  = 90.0*u.gigahertz # GHz
        FoV   = 42.0*u.arcsec #

    ### I don't use the double Guassian much. The only idea was to use it to
    ### get a better estimate of the beam volume, but we know that is variable.
    if instrument == "MUSTANG2":
        fwhm1 = 8.9*u.arcsec  # arcseconds
        norm1 = 0.97          # normalization
        fwhm2 = 25.0*u.arcsec # arcseconds
        norm2 = 0.03          # normalization
        fwhm  = 9.0*u.arcsec
        smfw  = 10.0*u.arcsec
        freq  = 90.0*u.gigahertz # GHz
        FoV   = 4.25*u.arcmin 
        
    if instrument == "NIKA":
        fwhm1 = 8.7*2.0*u.arcsec  # arcseconds
        norm1 = 0.94     # normalization
        fwhm2 = 28.4*2.0*u.arcsec # arcseconds
        norm2 = 0.06     # normalization
        fwhm  = 18.0*u.arcsec
        smfw  = 10.0*u.arcsec
        freq  = 150.0*u.gigahertz    # GHz
        FoV   = 2.15*u.arcmin 
        
    if instrument == "NIKA2":
        fwhm1 = 8.7*2.0*u.arcsec  # arcseconds
        norm1 = 0.94     # normalization
        fwhm2 = 28.4*2.0*u.arcsec # arcseconds
        norm2 = 0.06     # normalization
        fwhm  = 18.0*u.arcsec
        smfw  = 10.0*u.arcsec
        freq  = 150.0*u.gigahertz    # GHz
        FoV   = 6.5*u.arcmin 
        
    if instrument == "BOLOCAM":
        fwhm1 = 8.7*7.0*u.arcsec  # arcseconds
        norm1 = 0.94     # normalization
        fwhm2 = 28.4*7.0*u.arcsec # arcseconds
        norm2 = 0.06     # normalization
        fwhm  = 58.0*u.arcsec
        smfw  = 60.0*u.arcsec
        freq  = 140.0*u.gigahertz    # GHz
        FoV   = 8.0*u.arcmin * (u.arcmin).to("arcsec")
        
    if instrument == "ACT90":
        fwhm1 = 2.16*60.0*u.arcsec  # arcseconds
        norm1 = 1.0     # normalization
        fwhm2 = 1.0*u.arcsec # arcseconds
        norm2 = 0.00     # normalization
        fwhm  = 2.16*60.0*u.arcsec
        smfw  = 2.0*60.0*u.arcsec
        freq  = 97.0*u.gigahertz    # GHz
        FoV   = 60.0*u.arcmin #* (u.arcmin).to("arcsec")
        
    if instrument == "ACT150":
        fwhm1 = 1.3*60.0*u.arcsec  # arcseconds
        norm1 = 1.0     # normalization
        fwhm2 = 1.0*u.arcsec # arcseconds
        norm2 = 0.00     # normalization
        fwhm  = 1.3*60.0*u.arcsec
        smfw  = 1.2*60.0*u.arcsec
        freq  = 148.0*u.gigahertz    # GHz
        FoV   = 60.0*u.arcmin #* (u.arcmin).to("arcsec")
        
#    else:
#        fwhm1=9.0*u.arcsec ; norm1=1.0
#        fwhm2=30.0*u.arcsec ; norm2=0.0
#        fwhm = 9.0*u.arcsec ; smfw = 10.0*u.arcsec
#        freq = 90.0*u.gigahertz 
#        FoV   = 1.0*u.arcmin * (u.arcmin).to("arcsec")
#        
#    import pdb; pdb.set_trace()

    return fwhm1,norm1,fwhm2,norm2,fwhm,smfw,freq,FoV


def get_d_ang(z):

    d_ang = cosmo.comoving_distance(z) / (1.0 + z)

    return d_ang

def get_cosmo():

    return cosmo

def Theta500_from_M500_z(m500,z):
    
    d_ang = get_d_ang(z)
    r500,p500 = R500_P500_from_M500_z(m500,z)
    r500ang   = (r500/d_ang).decompose()
    #print(r500ang)
    
    return r500ang.value

def M500_from_R500_z(R500,z):

    dens_crit = cosmo.critical_density(z)
    E   = cosmo.H(z)/cosmo.H(0)
    h70 = (cosmo.H(0) / (70.0*u.km / u.s / u.Mpc))

    M500 = (4*np.pi/3)* dens_crit * R500**3 * 500
    M500 = M500.to("M_sun")

    return M500

def R500_P500_from_M500_z(M500,z):

    dens_crit = cosmo.critical_density(z)
    E   = cosmo.H(z)/cosmo.H(0)
    h70 = (cosmo.H(0) / (70.0*u.km / u.s / u.Mpc))

    
    #P500 = (1.65 * 10**-3) * ((E)**(8./3)) * ((
    #    M500 * h70)/ ((3*10**14) * const.M_sun)
    #    )**(2./3) * h70**2 * u.keV / u.cm**3
    P500 = (1.65 * 10**-3) * ((E)**(8./3)) * ((
        M500 * h70)/ ((3*10**14 * h70**(-1)) * const.M_sun)
        )**(2./3+0.11) * h70**2 * u.keV / u.cm**3
    R500 = (3 * M500/(4*np.pi * 500 * dens_crit))**(1./3)

    return R500, P500

def y_delta_from_mdelta(m_delta,z,delta=500,ycyl=False,YMrel=defaultYM,h70=1.0):
    """
    Finds A,B (scaling law terms, in get_AAA_BBB()) and applies them.
    """
    
    h       = cosmo.H(z)/cosmo.H(0)
    d_a     = get_d_ang(z).to('Mpc').value
    iv      = h**(-1./3)*d_a

    #print(YMrel)
    AAA,BBB = get_AAA_BBB(YMrel,delta,ycyl=ycyl,h70=h70)

    y_delta = m_delta**AAA * 10**BBB / (iv.value**2)

    return y_delta

def get_AAA_BBB(YMrel,delta,ycyl=False,h70=1.0):
    """
    Basically just a repository of Y-M relations.
    YMrel must be either:
       (1) 'A10' (Arnaud 2010)
       (2) 'A11' (Anderson 2011)
       (3) 'M12' (Marrone 2012)
       (4) 'P14' (Planck 2014), or
       (5) 'P17' (Planelles 2017)

    All are converted to Y = 10^BBB * M^AAA; mass (M) is in units of solar masses; Y is in Mpc^2 (i.e. with D_A^2 * E(z)^-2/3)
    
    """

    if delta == 2500:
        if YMrel == 'A10':
            AAA    = 1.637;   BBB = -28.13  # From Comis+ 2011
        #if ycyl:
        #    AAA = 1.60;   BBB = -27.4   # From Comis+ 2011
        if YMrel == 'A11':
            AAA    = 1.637;   BBB = -28.13  # From Comis+ 2011
        #if ycyl:
        #    AAA = 1.60;   BBB = -27.4   # From Comis+ 2011
        elif YMrel == 'M12':
            #BBB = -29.66909090909 ???
            BBB = -30.669090909090908
            AAA = 1.0 / 0.55
        elif YMrel == 'M12-SS':
            BBB = -28.501666666666667
            AAA = 5.0/3.0
        elif YMrel == 'P14':
            AAA = 1.755          #### NOT PLANCK!!!
            BBB = -29.6833076    # -4.585
        elif YMrel == 'P17':     # Planelles 2017
            AAA = 1.755
            BBB = -29.6833076    # -4.585
        elif YMrel == 'H20':     #### NOT He et al. 2020!!!
            AAA = 1.755
            BBB = -29.6833076    # -4.585
        else:
            print('using Comis+ 2011 values')
            
    elif delta == 500:
        if YMrel == 'A10':
            AAA   = 1.78
            Jofx  = 0.7398 if ycyl else 0.6145  # Actually I(x) in A10, but, it plays the same role, so use this variable
            #print(Jofx,' ycyl: ',ycyl)
            Bofx  = 2.925e-5 * Jofx * h70**(-1) / (3e14/h70)**AAA
            #BBB = np.log10(Bofx.value)
            BBB = np.log10(Bofx)
        elif YMrel == 'A11':
            Btabulated = 14.06 # But this is some WEIRD Y_SZ (M_sun * keV) - M relation
            Bconversion = -18.855
            Aconversion = -24.176792495381836
            AAA    = 1.67;   BBB = Btabulated + Bconversion + Aconversion  # Anderson+ 2011, Table 6
        #if ycyl:
        #    AAA = 1.60;   BBB = -27.4   # From Comis+ 2011
        elif YMrel == 'M12':
            #BBB = -30.66909090909 # BBB = -16.567
            BBB = -37.65227272727
            AAA = 1.0 / 0.44
        elif YMrel == 'M12-SS':
            BBB = -28.735
            AAA = 5.0/3.0
        elif YMrel == 'P14':
            AAA = 1.79
            BBB = -30.6388907    # 
        elif YMrel == 'P17':
            AAA = 1.685
            BBB = -29.0727644    # -4.585
        elif YMrel == 'H20':
            AAA = 1.790
            BBB = -30.653047     # -4.739
        else:
            print('Woops')
            #print(YMrel,delta)
    else:
        import pdb;pdb.set_trace()

    return AAA,BBB

def get_xymap(map,pixsize,xcentre=[],ycentre=[],oned=True,cpix=0):
    """
    Returns a map of X and Y offsets (from the center) in arcseconds.

    INPUTS:
    -------
    map      - a 2D array for which you want to construct the xymap
    pixsize  - a quantity (with units of an angle)
    xcentre  - The number of the pixel that marks the X-centre of the map
    ycentre  - The number of the pixel that marks the Y-centre of the map

    """

    #cpix=0
    ny,nx=map.shape
    ypix = pixsize.to("arcsec").value # Generally pixel sizes are the same...
    xpix = pixsize.to("arcsec").value # ""
    if xcentre == []:
        xcentre = nx/2.0
    if ycentre == []:
        ycentre = ny/2.0

    #############################################################################
    ### Label w/ the transpose that Python imposes?
    #y = np.outer(np.zeros(ny)+1.0,np.arange(0,xpix*(nx), xpix)- xpix* xcentre)   
    #x = np.outer(np.arange(0,ypix*(ny),ypix)- ypix * ycentre, np.zeros(nx) + 1.0)
    #############################################################################
    ### Intuitive labelling:
    x = np.outer(np.zeros(ny)+1.0,np.arange(nx)*xpix- xpix* xcentre)   
    y = np.outer(np.arange(ny)*ypix- ypix * ycentre, np.zeros(nx) + 1.0)

    #import pdb;pdb.set_trace()
    if oned == True:
        x = x.reshape((nx*ny)) #How important is the tuple vs. integer?
        y = y.reshape((nx*ny)) #How important is the tuple vs. integer?

    
    return x,y

def make_a10_map(M500,z,xymap,Theta500,nx,ny,nb_theta_range=150,Dist=False):

    minpixrad = (1.0*u.arcsec).to('rad')
    tnx       = [minpixrad.value,10.0*Theta500]  # In radians
    thetas    = np.logspace(np.log10(tnx[0]),np.log10(tnx[1]), nb_theta_range)
    d_ang     = get_d_ang(z)
    radkpc    = thetas*d_ang.to("kpc")
    PresProf  = a10_from_m500_z(M500, z,radkpc,Dist=Dist)
    to,yProf  = get_yProf(radkpc,PresProf,z)
    #x2p,y2p   = xymap
    #origshape = x2p.shape
    #xy2pass   = (x2p.flatten(),y2p.flatten())
    #print(xy2pass[0].shape,thetas.shape,yProf.shape,origshape)
    
    flatymap  = grid_profile(thetas,yProf,xymap)
    ymap      = flatymap.reshape((nx,ny))

    return ymap
    
def grid_profile(rads, profile, xymap, geoparams=[0,0,0,1,1,1,0,0],myscale=1.0,axis='z'):

    ### Get new grid:
    arc2rad =  4.84813681109536e-06 # arcseconds to radians
    (x,y) = xymap
    x,y = rot_trans_grid(x,y,geoparams[0],geoparams[1],geoparams[2]) # 0.008 sec per call
    x,y = get_ell_rads(x,y,geoparams[3],geoparams[4])                # 0.001 sec per call
    theta = np.sqrt(x**2 + y**2)*arc2rad
    theta_min = rads[0]*2.0 # Maybe risky, but this is defined so that it is sorted.
    bi=(theta < theta_min);   theta[bi]=theta_min
    mymap  = np.interp(theta,rads,profile)
    
    if axis == 'x':
        xell = (x/(geoparams[3]*myscale))*arc2rad # x is initially presented in arcseconds
        modmap = geoparams[5]*(xell**2)**(geoparams[6]) # Consistent with model creation??? (26 July 2017)
    if axis == 'y':
        yell = (y/(geoparams[4]*myscale))*arc2rad # x is initially presented in arcseconds
        modmap = geoparams[5]*(yell**2)**(geoparams[6]) # Consistent with model creation??? (26 July 2017)
    if axis == 'z':
        modmap = geoparams[5]

    if modmap != 1:
        mymap *= modmap   # Very important to be precise here.
    if geoparams[7] > 0:
        angmap = np.arctan2(y,x)
        bi = (abs(angmap) > geoparams[7]/2.0)
        mymap[bi] = 0.0

    return mymap

def rot_trans_grid(x,y,xs,ys,rot_rad):

    xnew = (x - xs)*np.cos(rot_rad) + (y - ys)*np.sin(rot_rad)
    ynew = (y - ys)*np.cos(rot_rad) - (x - xs)*np.sin(rot_rad)

    return xnew,ynew

def get_ell_rads(x,y,ella,ellb):

    xnew = x/ella ; ynew = y/ellb

    return xnew, ynew

def a10_from_m500_z(m500, z,rads,Dist=False):
    """
    INPUTS:
    m500    - A quantity with units of mass
    z       - redshift.
    rads    - A quantity array with units of distance.
    """
    
    r500, p500 = R500_P500_from_M500_z(m500,z)
    if Dist:
        c500= 1.083
        p=3.202
        a=1.4063
        b=5.4905
        c=0.3798
    else:
        c500= 1.177
        p=8.403
        a=1.0510
        b=5.4905
        c=0.3081
    gnfw_prof  = gnfw(r500,p500,rads,c500=c500,p=p,a=a,b=b,c=c)
    
    return gnfw_prof

def get_yProf(radii,pprof,z):

    d_ang      = get_d_ang(z)
    thetas     = (radii/d_ang).decompose().value
    Pdl2y      = get_Pdl2y(z,d_ang)
    unitless_profile_clust = (pprof * Pdl2y).decompose().value
    yProf_clust = ni.int_profile(thetas, unitless_profile_clust,thetas)

    return thetas,yProf_clust

def gnfw(R500, P500, radii, c500= 1.177, p=8.403, a=1.0510, b=5.4905, c=0.3081):

    cosmo = get_cosmo()
    h70 = (cosmo.H(0) / (70.0*u.km / u.s / u.Mpc))

    P0 = P500 * p * h70**-1.5
    rP = R500 / c500 # C_500 = 1.177
    rf =  (radii/rP).decompose().value # rf must be dimensionless
    result = (P0 / (((rf)**c)*((1 + (rf)**a))**((b - c)/a)))

    return result

def get_Pdl2y(z,d_ang):

    szcv,szcu = get_sz_values()
    Pdl2y     = (szcu['thom_cross']*d_ang/szcu['m_e_c2']).to("cm**3 keV**-1")

    return Pdl2y

def get_sz_values():
    ########################################################
    ### Astronomical value...
    tcmb = 2.72548*u.K # Kelvin (uncertainty = 0.00057)
    ### Reference:
    ### http://iopscience.iop.org/article/10.1088/0004-637X/707/2/916/meta
    
    ### Standard physical values.
    thom_cross = (spconst.value("Thomson cross section") *u.m**2).to("cm**2")
    m_e_c2 = (const.m_e *const.c**2).to("keV")
    kpctocm = 3.0856776 *10**21
    boltzmann = spconst.value("Boltzmann constant in eV/K")/1000.0 # keV/K  
    planck = const.h.to("eV s").value/1000.0 # keV s
    c = const.c
    keVtoJ = (u.keV).to("J") # I think I need this...) 
    Icmb = 2.0 * (boltzmann*tcmb.value)**3 / (planck*c.value)**2
    Icmb *= keVtoJ*u.W *u.m**-2*u.Hz**-1*u.sr**-1 # I_{CMB} in W m^-2 Hz^-1 sr^-1
    JyConv = (u.Jy).to("W * m**-2 Hz**-1")
    Jycmb = Icmb.to("Jy sr**-1")  # I_{CMB} in Jy sr^-1
    MJycmb= Jycmb.to("MJy sr**-1")

    ### The following constants (and conversions) are just the values (in Python):
    sz_cons_values={"thom_cross":thom_cross.value,"m_e_c2":m_e_c2.value,
                    "kpctocm":kpctocm,"boltzmann":boltzmann,
                    "planck":planck,"tcmb":tcmb.value,"c":c.value,}
    ### The following "constants" have units attached (in Python)!
    sz_cons_units={"Icmb":Icmb,"Jycmb":Jycmb,"thom_cross":thom_cross,
                   "m_e_c2":m_e_c2}

    return sz_cons_values, sz_cons_units

def make_A10Map(M500,z,pixsize=2,h70=1,nb_theta_range=150,Dist=False):

    Theta500   = Theta500_from_M500_z(M500,z)
    minpixrad  = (1.0*u.arcsec).to('rad')
    tnx        = [minpixrad.value,10.0*Theta500]  # In radians
    thetas     = np.logspace(np.log10(tnx[0]),np.log10(tnx[1]), nb_theta_range)
    map_vars   = {"thetas":thetas}
    nx         = int( np.round( (Theta500*3600*180/np.pi)*3 / 2.0 ) )
    mapshape   = (nx,nx)
    zeromap    = np.zeros(mapshape)
    xymap      = get_xymap(zeromap,pixsize=pixsize*u.arcsec)
    ymap       = make_a10_map(M500,z,xymap,Theta500,nx,nx,Dist=Dist)

    return ymap


def smooth_by_M2_beam(image,pixsize=2.0):
    """
    Smooths an image by a double Gaussian.
    """

    
    fwhm1,norm1,fwhm2,norm2,fwhm,smfw,freq,FoV = inst_params("MUSTANG2")

    sig2fwhm  = np.sqrt(8.0*np.log(2.0)) 
    pix_sig1  = fwhm1/(pixsize*sig2fwhm)
    pix_sig2  = fwhm2/(pixsize*sig2fwhm)
    map1      = scipy.ndimage.filters.gaussian_filter(image, pix_sig1)
    map2      = scipy.ndimage.filters.gaussian_filter(image, pix_sig2)

    bcmap     = map1*norm1 + map2*norm2

    return bcmap
