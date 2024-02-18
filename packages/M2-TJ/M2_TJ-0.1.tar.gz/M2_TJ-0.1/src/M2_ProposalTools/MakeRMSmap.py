import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors
from matplotlib import cm
from reproject import reproject_interp
from astropy.wcs import WCS
from astropy.io import fits
import scipy.ndimage

def get_rms_cmap():

    mycmap=cm.get_cmap('tab20b')
    mydcm=cm.get_cmap('tab20b',256)
    newcolors = mydcm(np.linspace(0,1,256))
    mycmap.set_under('w')
    mycmap.set_over('w')
    
    return mycmap

def plot_rms_general(hdul,rmsmap,savefile,vmin=18,vmax=318,myfs=15,nscans=None,
                     prntinfo=True,cmark=True,ggmIsImg=False,tlo=True,
                     cra=0,cdec=0,ggm=False,ggmCut=0.05,cc='k',ncnts=0,title=None,
                     tsource=0,R500=0,r5col="c",zoom=1,noaxes=False):

    #norm=colors.Normalize(vmin=vmin, vmax=vmax)
    #norm=colors.LogNorm(vmin=vmin, vmax=vmax)
    norm=colors.SymLogNorm(linthresh=40,vmin=vmin, vmax=vmax)
    tmin = np.round(vmin/10)*10
    tmax = 40
    lticks = np.arange(tmin,tmax+10,10)
    lgfull = np.array([40,100,200,400,800])
    lgticks = lgfull[(lgfull <=vmax)]
    myticks = np.hstack((lticks,lgticks))
    mycmap = get_rms_cmap()

    img = hdul[0].data
    hdr = hdul[0].header
    w   = WCS(hdr)
    pixsize = np.sqrt(np.abs(np.linalg.det(w.pixel_scale_matrix))) * 3600.0 # in arcseconds

    figsize = (7,5)
    dpi     = 200 # default??
    myfig = plt.figure(1,figsize=figsize)
    myfig.clf()
    if tlo:
        ax = myfig.add_subplot(1,1,1, projection=w,position=[0.05,0.05,0.8,0.8])
    else:
        ax = myfig.add_subplot(1,1,1, projection=w)
    
    if ggm:
        ggmImg = scipy.ndimage.gaussian_gradient_magnitude(img*1e6,2.0)
        #im     = ax.imshow(ggmImg,cmap=mycmap)
        ggmMax = np.max(ggmImg)
        gi     = (ggmImg > ggmMax*ggmCut)
        ggmStd = np.std(ggmImg[gi])
        if ncnts > 0:
            clvls  = np.logspace(np.log10(ggmStd*3),np.log10(ggmMax),ncnts)
        else:
            clvls  = np.arange(ggmStd*3,ggmMax,ggmStd)

    whitemap = np.ones(rmsmap.shape)*vmax + 1
    im0 = ax.imshow(whitemap,norm=norm,cmap=mycmap)
    if zoom > 1:
        ax_zoom(zoom,ax)
        
    ax.set_xlabel("RA (J2000)",fontsize=myfs)
    ax.set_ylabel("Dec (J2000)",fontsize=myfs)
    gi = (rmsmap > 0)
    minrms = np.min(rmsmap[gi])
    xlims = ax.get_xlim()
    ylims = ax.get_ylim()
    dx    = xlims[1] - xlims[0]
    dy    = ylims[1] - ylims[0]
    alphas   = np.zeros(rmsmap.shape)
    if prntinfo:
        xpos = int(np.round(xlims[1] - dx*myfs*3/100.0))
        ypos = int(np.round(ylims[0] ))
        txthght = int(np.round(dy*myfs/(figsize[1]*25)))
        txtwdth1 = int(np.round(dx*myfs/35.0))
        txtwdth2 = int(np.round(dx*myfs/12.0))
        print("==========================================")
        print(xpos,ypos,txthght,txtwdth1,dx,myfs)
        #alphas[xpos:xpos+txtwdth1,ypos:ypos+txthght] = 0.2
        alphas[ypos:ypos+txthght,xpos:xpos+txtwdth1] = 0.9
        if tsource > 0:
            xos = int(np.round(xlims[0]))
            yos = int(np.round(ylims[1] - dy*myfs/150.0))
            alphas[yos:yos+txthght,xos:xos+txtwdth2] = 0.9

        truncate_par = 10.0 #do not user lower than 7-10, larger means much slower code
        mode_BC = 'constant' 
        alphas = scipy.ndimage.filters.gaussian_filter(alphas , txthght/10.0,truncate=truncate_par, mode=mode_BC)
    print(alphas.shape,txthght,ypos,yos,xpos,xos,txtwdth1,txtwdth2)
    #import pdb;pdb.set_trace()
    if ggmIsImg:
        im = ax.imshow(ggmImg,cmap=mycmap)
    else:
        #im = ax.imshow(rmsmap,norm=norm,alpha=alphas,cmap=mycmap)
        im = ax.imshow(rmsmap,norm=norm,cmap=mycmap)
        if ggm and (ncnts > 0):
            ax.contour(ggmImg,clvls,linestyles='--',colors=cc)
        #import pdb;pdb.set_trace()
        
    if R500 > 0:
        goodrad = R500/pixsize
        plot_circ(ax,hdr,cra,cdec,goodrad,color=r5col,lw=4)

    im0 = ax.imshow(whitemap,norm=norm,alpha=alphas,cmap=mycmap)

    #if zoom > 1:
    #    ax_zoom(zoom,ax)
            
    if prntinfo:
        xpos = xlims[1] - dx*myfs/40
        ypos = ylims[0] + dy*0.03
        ax.text(xpos,ypos,"Min. RMS: "+"{:.1f}".format(minrms),fontsize=myfs)
        if tsource > 0:
            xos = xlims[0] + dx*0.03
            yos = ylims[1] - dy*0.08
            ax.text(xos,yos,"t on source (hrs): "+"{:.1f}".format(tsource),fontsize=myfs)
    #ax.set_title(title,fontsize=myfs)
    cbar_num_format = "%d"
    mycb = myfig.colorbar(im,ax=ax,ticks=myticks,format=cbar_num_format)
    mycb.set_label(r"Noise ($\mu$K)",fontsize=myfs)
    #mycb = myfig.colorbar(im,ax=ax,ticks=[20,30,40,100,200],label=r"Noise ($\mu$K)")
    #mycb.ax.set_xticklabels(['20','30','40','100','200'])
    mycb.ax.tick_params(labelsize=myfs)

    if noaxes:
        ax.set_axis_off()
    
    if not (title is None):
        ax.set_title(title)

    if cmark:
        mark_radec(ax,hdr,cra,cdec)
    #else:
    #    mark_center_a399(ax,img,hdr)
    #cent = [cx,cy] # Cluster center

    if prntinfo and not nscans is None:
        nsint = [int(nscan) for nscan in nscans]
        for i,nsi in enumerate(nsint):
            ax.text(5+i*100,5,repr(nsi),fontsize=myfs)

    if tlo:
        print("I already did this")
        #myfig.tight_layout()
        #myfig.subplots_adjust(left=0.01,bottom=0.01,top=0.05)
        #myfig.subplots_adjust(left=0.01,bottom=0.01)
        #ax.subplot_adjust(right=0.1,left=0.01,bottom=0.01,top=0.01)
    myfig.savefig(savefile,format='png')
    myfig.clf()


def mark_radec(ax,hdr,ra,dec):

    w     = WCS(hdr)           
    #pixs  = get_pixs(hdr)/60.0 # In arcminutes
    x0,y0 = w.wcs_world2pix(ra,dec,0)

    ax.plot(x0,y0,'xr')

def plot_circ(ax,hdr,ra,dec,goodrad,color="r",ls='--',lw=2):

    thetas = np.arange(181)*2*np.pi/180
    w      = WCS(hdr)           
    #pixs  = get_pixs(hdr)/60.0 # In arcminutes
    x0,y0  = w.wcs_world2pix(ra,dec,0)

    xs     = x0 + np.cos(thetas)*goodrad
    ys     = y0 + np.sin(thetas)*goodrad

    ax.plot(xs,ys,ls=ls,lw=lw,color=color)
    
def plot_rms(hdul,rmsmap,savefile,vmin=18,vmax=318,myfs=15,nscans=None,
             prntinfo=True,cmark=True):

    #norm=colors.Normalize(vmin=vmin, vmax=vmax)
    #norm=colors.LogNorm(vmin=vmin, vmax=vmax)
    norm=colors.SymLogNorm(linthresh=40,vmin=vmin, vmax=vmax)
    mycmap = get_rms_cmap()

    img = hdul[0].data
    hdr = hdul[0].header
    w   = WCS(hdr)

    myfig = plt.figure(1,figsize=(7,5))
    myfig.clf()
    ax = myfig.add_subplot(1,1,1, projection=w)

    
    im = ax.imshow(rmsmap,norm=norm,cmap=mycmap)
    ax.set_xlabel("RA (J2000)",fontsize=myfs)
    ax.set_ylabel("Dec (J2000)",fontsize=myfs)
    gi = (rmsmap > 0)
    minrms = np.min(rmsmap[gi])
    if prntinfo:
        ax.text(500,5,"Min. RMS: "+"{:.1f}".format(minrms))
    #ax.set_title(title,fontsize=myfs)
    #plot_circ(ax,goodcen,goodrad,color=r5col,ls='--',lw=2)
    mycb = myfig.colorbar(im,ax=ax,label=r"Noise ($\mu$K)")
    #mycb = myfig.colorbar(im,ax=ax,ticks=[20,30,40,100,200],label=r"Noise ($\mu$K)")
    #mycb.ax.set_xticklabels(['20','30','40','100','200'])
    mycb.ax.tick_params(labelsize=myfs)

    if cmark:
        mark_center_shock(ax,img,hdr)
    else:
        mark_center_a399(ax,img,hdr)
    cent = [340.6766932,53.05341666] # Cluster center
    if prntinfo and not nscans is None:
        nsint = [int(nscan) for nscan in nscans]
        for i,nsi in enumerate(nsint):
            ax.text(5+i*100,5,repr(nsi),fontsize=myfs)
        
    myfig.savefig(savefile,format='png')

def mark_center_a399(ax,img,hdr):

    a399 = (44.48500,13.01638888) # A399 centroid, degrees
    xymap = make_xymap(img,hdr,a399[0],a399[1])
    pixs  = get_pixs(hdr)
    xx,yy = xymap
    ax.plot(-xx[0,0]*60/pixs,-yy[0,0]*60/pixs,'xk',ms=10,mew=3)

    
def mark_center_shock(ax,img,hdr,pltslices=False,nocen=False):

    p3   = (340.6766932,53.05341666)  # RA, dec in degrees
    xymap = make_xymap(img,hdr,p3[0],p3[1])
    #rmap  = make_rmap(xymap)
    #tmap  = np.arctan2(xymap[1],xymap[0])
    t1    = 80
    t2    = 145
    pixs  = get_pixs(hdr)
    tarr  = np.arange(t1,t2)*np.pi/180
    xx,yy = xymap
    shk_x = (np.cos(tarr)*470 - 60*xx[0,0])/pixs
    shk_y = (np.sin(tarr)*470 - 60*yy[0,0])/pixs

    ishkrad = 4.7*60
    ishk_x = (np.cos(tarr)*ishkrad - 60*xx[0,0])/pixs
    ishk_y = (np.sin(tarr)*ishkrad - 60*yy[0,0])/pixs
    
    #print(shk_x,shk_y)
    #import pdb;pdb.set_trace()
    if not pltslices:
        ax.plot(shk_x,shk_y,'k',lw=2)
    ax.plot(ishk_x,ishk_y,'--k',lw=2)
    if not nocen:
        ax.plot(-xx[0,0]*60/pixs,-yy[0,0]*60/pixs,'xk',ms=10,mew=3)

    
def get_scanlen(scansize):

    # Scansize in arcminutes
    t_minutes = 6.56365 + 0.585*scansize

    return t_minutes

def get_rmsprof_from_s(radii,s):

    pars = get_mapspd_pars(s)
    rawrms = pars[0] + pars[1]*radii + pars[3]*np.exp(radii/pars[2])
    rms    = np.sqrt(2)*rawrms
    
    return rms

def get_rmsprofile(radii,pars):
    #P[0] + P[1] + P[3]*exp(R/P[2])
    rawrms = pars[0] + pars[1]*radii + pars[3]*np.exp(radii/pars[2])
    rms    = np.sqrt(2)*rawrms
    
    return rms
       
def get_mapwts(radii,pars):
    #P[0] + P[1] + P[3]*exp(R/P[2])
    #rawrms = pars[0] + pars[1]*radii + pars[3]*np.exp(radii/pars[2])
    #rms    = np.sqrt(2)*rawrms
    rms = get_rmsprofile(radii,pars)
    wts = 1.0/rms**2

    return wts

def make_arb_map(size,pixsize,scansz,hours,vmin=1,vmax=21):

    Cy2Trj = -2.8166406800215875 # For assumed 7keV.
    myfs    = 7
    npix    = int(size*60/pixsize)
    cent    = npix//2
    x1      = np.arange(npix)
    x       = np.outer(x1,np.ones(npix)) - cent
    y       = x.T
    r       = pixsize*make_rmap((x,y))/60.0 # in arcminutes
    edge    = scansz+2.1
    gr      = (r < edge)
    pars    = get_mapspd_pars(scansz)
    wts     = np.zeros(r.shape)
    wts[gr] = get_mapwts(r[gr],pars)*hours
    rms     = np.zeros(r.shape)
    rms[gr] = 1.0/np.sqrt(wts[gr]) / np.abs(Cy2Trj)
    
    avgrms  = 1.0/np.sqrt(np.mean(wts)) / np.abs(Cy2Trj)

    norm=colors.Normalize(vmin=vmin, vmax=vmax)
    mycmap = get_rms_cmap()
    myfig = plt.figure(1,figsize=(7,5))
    myfig.clf()
    ax = myfig.add_subplot(1,1,1)
    sztit = "{:d}".format(size)+r"$^{\prime}$"
    hrs   = "{:d}".format(int(hours))
    mytit = sztit+r" $\times$ "+sztit+" ; "+hrs+" hours"
    scsz =  "{:.1f}".format(scansz)+r"$^{\prime}$"
    ax.set_title(mytit+"; Scan radius = "+scsz)
    im = ax.imshow(rms,norm=norm,cmap=mycmap,origin="lower")
    mycb = myfig.colorbar(im,ax=ax)
    mycb.set_label(r"RMS, Compton $y * 10^6$",fontsize=myfs)
    mycb.ax.tick_params(labelsize=myfs)
    #ax.text(25,25,"{:.2f}".format(avgrms))
    qddir = "/home/data/MUSTANG2/SimulatedObservations/QuickAndDirty/"
    savefile=qddir+"FiveArcminuteScan_"+hrs+"hours.png"
    myfig.savefig(savefile,format='png')

    print(avgrms)

    
def get_mapspd_pars(size):

    if size == 2.5:
        p = [39.5533, 1.0000, 1.0000, 2.2500]
    if size == 3.0:
        p = [37.3425, 1.5000, 1.5000, 6.9000]
    if size == 3.5:
        p = [27.9775, 2.0000, 2.0000, 11.5500]
    if size == 4.0:
        p = [32.3852, 2.5000, 2.5000, 16.2000]
    if size == 4.5:
        p = [28.5789, 3.0000, 3.0000, 20.8500]
    if size == 5.0:
        p = [43.2951, 3.5000, 3.5000, 25.5000]

    return p
        
def make_rmap(xymap):

    rmap = np.sqrt(xymap[0]**2 + xymap[1]**2)

    return rmap
        
def make_xymap(img,hdr,ra,dec):

    w     = WCS(hdr)           
    pixs  = get_pixs(hdr)/60.0 # In arcminutes
    x0,y0 = w.wcs_world2pix(ra,dec,0)
    print(pixs,x0,y0)
    #pdb.set_trace()
    xsz, ysz = img.shape
    xar = np.outer(np.arange(xsz),np.zeros(ysz)+1.0)
    yar = np.outer(np.zeros(xsz)+1.0,np.arange(ysz))
    xarr = xar.transpose()
    yarr = yar.transpose()
    ####################
    dxa = (xarr - x0)*pixs
    dya = (yarr - y0)*pixs
    
    return (dxa,dya)
    #return (dya,dxa)

def get_pixs(hdr):

    if 'CDELT1' in hdr.keys():
        pixs= abs(hdr['CDELT1'] * hdr['CDELT2'])**0.5 * 3600.0    
    if 'CD1_1' in hdr.keys():
        pixs= abs(hdr['CD1_1'] * hdr['CD2_2'])**0.5 * 3600.0
    if 'PC1_1'  in hdr.keys():
        if 'PC2_1'  in hdr.keys():
            pc21 = hdr['PC2_1']
            pc12 = hdr['PC1_2']
        else:
            pc21 = 0.0; pc12 = 0.0
            
        pixs= abs(hdr['PC1_1']*hdr['CDELT1'] * \
                  hdr['PC2_2']*hdr['CDELT2'])**0.5 * 3600.0

    return pixs

def reproject_fillzeros(hduin,hdrout,hdu_in=0):

    imgout, fpout = reproject_interp(hduin,hdrout,hdu_in=hdu_in)
    foo           = np.isnan(imgout)
    badind        = np.where(foo)
    imgout[foo]   = 0.0

    return imgout, fpout
         
def make_rms_map(hdul,ptgs,szs,time,offset=1.5):
    
    img  = hdul[0].data
    hdr  = hdul[0].header

    sll = []
    for sz in szs:
        sl  = get_scanlen(sz)
        sll.append(sl)

    sla = np.array(sll)
    times = np.asarray(time)

    ns   = times*60/sla

    wtmap  = np.zeros(img.shape)
    rmsmap = np.zeros(img.shape)
    for p,s,t in zip(ptgs,szs,time):
        #pars = get_mapspd_pars(s)
        #xymap = make_xymap(img,hdr,p[0],p[1])
        #rmap  = make_rmap(xymap)
        #edge  = (s+2.1) # arcseconds
        #gi = (rmap < edge)
        #wts = get_mapwts(rmap[gi],pars)
        #wtmap[gi] = wtmap[gi]+wts*t
        wtmap = add_to_wtmap(img,hdr,wtmap,p,s,t,offset=offset)
    gi = (wtmap > 0)
    rmsmap[gi] = 1.0/np.sqrt(wtmap[gi])

    return rmsmap, ns

def add_to_wtmap(img,hdr,wtmap,p,s,t,offset=1.5):

    degoff = offset/60.0 # Offset in degrees
    if s>0:
        pars = get_mapspd_pars(s)
        xymap = make_xymap(img,hdr,p[0],p[1])
        rmap  = make_rmap(xymap)
        edge  = (s+2.1) # arcseconds
        gi = (rmap < edge)
        wts = get_mapwts(rmap[gi],pars)
        wtmap[gi] = wtmap[gi]+wts*t
    else:
        pars   = get_mapspd_pars(-s)
        cosdec = np.cos(p[1]*np.pi/180.0) 
        for i in range(4):
            newx = p[0] + np.cos(np.pi*i/2)*degoff/cosdec
            newy = p[1] + np.sin(np.pi*i/2)*degoff
            xymap = make_xymap(img,hdr,newx,newy)
            rmap  = make_rmap(xymap) # arcminutes
            edge  = (2.1-s) # arcminutes
            gi = (rmap < edge)
            wts = get_mapwts(rmap[gi],pars)
            wtmap[gi] = wtmap[gi]+wts*t/4.0
        
    return wtmap

def ax_zoom(zoom,ax):
    ax_x = ax.get_xlim()
    ax_y = ax.get_ylim()
    dx   = (ax_x[1] - ax_x[0])/2
    dy   = (ax_y[1] - ax_y[0])/2
    newd = (1.0 - 1.0/zoom)
    newx = [ax_x[0]+newd*dx,ax_x[1]-newd*dx]
    newy = [ax_y[0]+newd*dy,ax_y[1]-newd*dy]
    ax.set_xlim(newx)
    ax.set_ylim(newy)

def make_template_hdul(nx,ny,cntr,pixsize,cx=None,cy=None):

    if cx is None:
        cx = nx/2.0
    if cy is None:
        cy = ny/2.0
    ### Let's make some WCS information as if we made 1 arcminute pixels about Coma's center:
    w = WCS(naxis=2)
    w.wcs.crpix = [cx,cy]
    w.wcs.cdelt = np.array([-pixsize/3600.0,pixsize/3600.0])
    w.wcs.crval = [cntr[0], cntr[1]]
    w.wcs.ctype = ["RA---SIN", "DEC--SIN"]
    hdr = w.to_header()

    zero_img    = np.zeros((nx,ny))
    Phdu        = fits.PrimaryHDU(zero_img,header=hdr)
    TempHdu     = fits.HDUList([Phdu])

    return TempHdu

def calc_RMS_profile(hdul,rmsmap,Cntr,rmax=None):

    img                    = hdul[0].data
    hdr                    = hdul[0].header
    xymap                  = make_xymap(img,hdr,Cntr[0],Cntr[1])
    xmap                   = xymap[0]
    #pixs                   = np.median(xmap[1:,0]-xmap[:-1,0]) # in arcminutes
    pixs                   = np.median(xmap[0,1:]-xmap[0,:-1]) # in arcminutes
    print(pixs)
    rmap                   = make_rmap(xymap) # arcminutes
    rbin,ybin,yerr,ycnts   = bin_two2Ds(rmap,rmsmap,binsize=pixs*2.0)

    return rbin,ybin

def bin_two2Ds(independent,dependent,binsize=1,witherr=False,withcnt=False):

    flatin = independent.flatten()
    flatnt = dependent.flatten()
    inds = flatin.argsort()

    abscissa = flatin[inds]
    ordinate = flatnt[inds]

    nbins = int(np.ceil((np.max(abscissa) - np.min(abscissa))/binsize))
    abin  = np.zeros(nbins)
    obin  = np.zeros(nbins)
    oerr  = np.zeros(nbins)
    cnts  = np.zeros(nbins) 
    for i in range(nbins):
        blow = i*binsize
        gi = (abscissa >= blow)*(abscissa < blow+binsize)
        abin[i] = np.mean(abscissa[gi])
        obin[i] = np.mean(ordinate[gi])
        if witherr:
            oerr[i] = np.std(ordinate[gi]) / np.sqrt(np.sum(gi))
        if withcnt:
            cnts[i] = np.sum(gi)

    return abin,obin,oerr,cnts

def bin_log2Ds(independent,dependent,nbins=10,witherr=False,withcnt=False):

    flatin = independent.flatten()
    flatnt = dependent.flatten()
    inds   = flatin.argsort()

    abscissa = flatin[inds]
    ordinate = flatnt[inds]

    #nbins = int(np.ceil((np.max(abscissa) - np.min(abscissa))/binsize))
    agtz    = (abscissa > 0)
    lgkmin  = np.log10(np.min(abscissa[agtz]))
    lgkmax  = np.log10(np.max(abscissa))
    bins  = np.logspace(lgkmin,lgkmax,nbins+1)
    abin  = np.zeros(nbins)
    obin  = np.zeros(nbins)
    oerr  = np.zeros(nbins)
    cnts  = np.zeros(nbins) 
    for i,(blow,bhigh) in enumerate(zip(bins[:-1],bins[1:])):
        gi = (abscissa >= blow)*(abscissa < bhigh)
        abin[i] = np.mean(abscissa[gi])
        obin[i] = np.mean(ordinate[gi])
        if witherr:
            oerr[i] = np.std(ordinate[gi]) / np.sqrt(np.sum(gi))
        if withcnt:
            cnts[i] = np.sum(gi)

    return abin,obin,oerr,cnts

def calculate_RMS_within(Rads,RMSprof,Rmaxes=[2,3,4]):

    Variance = RMSprof**2
    Rstack   = np.hstack([0,Rads])
    Area     = Rstack[1:]**2 - Rstack[:-1]**2

    VarCum   = np.cumsum(Variance*Area)
    AreCum   = np.cumsum(Area)
    VarAvg   = VarCum/AreCum

    RMSwi    = []
    for Rmax in Rmaxes:
        gi = (Rads < Rmax)
        MyVars = VarAvg[gi]
        RMSwi.append(np.sqrt(MyVars[-1]))

    return RMSwi
