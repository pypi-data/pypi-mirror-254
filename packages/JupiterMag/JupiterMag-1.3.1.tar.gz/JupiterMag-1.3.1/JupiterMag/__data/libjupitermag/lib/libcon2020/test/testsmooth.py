import numpy as np
import matplotlib.pyplot as plt
import ctypes
import platform

#define some dtypes
c_char_p = ctypes.c_char_p
c_bool = ctypes.c_bool
c_int = ctypes.c_int
c_float = ctypes.c_float
c_double = ctypes.c_double
c_float_ptr = np.ctypeslib.ndpointer(ctypes.c_float,flags="C_CONTIGUOUS")

#this one is a hack found at: https://stackoverflow.com/a/32138619/15482422
#it allows us to send None instead of an array which is treated as NULL
c_double_ptr_base = np.ctypeslib.ndpointer(ctypes.c_double,flags="C_CONTIGUOUS")
def _from_param(cls, obj):
        if obj is None:
            return obj
        return c_double_ptr_base.from_param(obj)
c_double_ptr = type('c_double_ptr',(c_double_ptr_base,),{'from_param':classmethod(_from_param)})

c_double_ptr_ptr = np.ctypeslib.ndpointer(np.uintp,ndim=1,flags="C_CONTIGUOUS")
c_int_ptr = np.ctypeslib.ndpointer(ctypes.c_int,flags="C_CONTIGUOUS")
c_bool_ptr = np.ctypeslib.ndpointer(ctypes.c_bool,flags="C_CONTIGUOUS")
c_char_p_ptr = ctypes.POINTER(c_char_p) 

if platform.system() == 'Linux':
    lib = ctypes.CDLL('../lib/libcon2020.so')
else:
    lib = ctypes.CDLL('../lib/libcon2020.dylib')

setCon2020Params = lib.SetCon2020Params
setCon2020Params.restype = None
setCon2020Params.argtypes = [
     c_double,        #mui
    c_double,        #irho
    c_double,        #r0
    c_double,        #r1
    c_double,        #d
    c_double,        #xt
    c_double,        #xp
    c_char_p,        #eqtype
    c_bool,            #Edwards
    c_bool,            #ErrChk
    c_bool,            #CartIn
    c_bool,            #CartOut
    c_bool,         #Smooth
    c_double,    #DeltaRho
    c_double,    #DeltaZ
    c_double,        #g
    c_char_p,            #azfunc
    c_double,        #wO_open
    c_double,        #wO_om
    c_double,        #thetamm
    c_double,        #dthetamm
    c_double,        #thetaoc
    c_double        #dthetaoc
]

con2020FieldArray = lib.Con2020FieldArray
con2020FieldArray.restype = None
con2020FieldArray.argtypes = [
    c_int,            #number of input elements
    c_double_ptr,    #x/r array
    c_double_ptr,    #y/t array
    c_double_ptr,    #z/p array
    c_double_ptr,    #Bx/Br output array
    c_double_ptr,    #Bx/Br output array
    c_double_ptr    #Bx/Br output array]
]

getCon2020Params = lib.GetCon2020Params
getCon2020Params.restype = None
getCon2020Params.argtypes = [	
    c_double_ptr,		#mui
    c_double_ptr,		#irho
    c_double_ptr,		#r0
    c_double_ptr,		#r1
    c_double_ptr,		#d
    c_double_ptr,		#xt
    c_double_ptr,		#xp
    c_char_p,		#eqtype
    c_bool_ptr,			#Edwards
    c_bool_ptr,			#ErrChk
    c_bool_ptr,			#CartIn
    c_bool_ptr,			#CartOut
    c_bool_ptr, 		#Smooth
    c_double_ptr,		#DeltaRho
    c_double_ptr,		#Deltaz,
    c_double_ptr,		#g
    c_char_p,			#azfunc
    c_double_ptr,		#wO_open
    c_double_ptr,		#wO_om
    c_double_ptr,		#thetamm
    c_double_ptr,		#dthetamm
    c_double_ptr,		#thetaoc
    c_double_ptr		#dthetaoc
]

def MagtoSIII(x,y,z,xt,xp):
    '''
    Convert from a dipole/current sheet based coordinate system back to
    Right-handed System III.
    
    Inputs
    ======
    x : float
        x coordinate in dipole/current sheet coordinates
    y : float
        y coordinate in dipole/current sheet coordinates
    z : float
        z coordinate in dipole/current sheet coordinates
    xt : float
        Current sheet/dipole tilt (degrees)
    xp : float
        Azimuth of tilt (degrees)
        
    Returns
    =======
    ox : float
        x-coordinate 
    oy : float
        y-coordinate 
    oz : float
        z-coordinate 
    
    '''

    dtor = np.pi/180.0
    xtr = dtor*xt
    xpr = dtor*xp
    cosxt = np.cos(xtr)
    sinxt = np.sin(xtr)
    cosxp = np.cos(xpr)
    sinxp = np.sin(xpr)
    

    xtmp = x*cosxt + z*sinxt
    ox = xtmp*cosxp - y*sinxp
    oy = xtmp*sinxp + y*cosxp
    oz = -x*sinxt + z*cosxt


    return ox,oy,oz
    





def SIIItoMag(x,y,z,xt,xp):
    '''
    Convert Right-handed System III coordinates to a dipole/current
    sheet based coordinate system.
    
    Inputs
    ======
    x : float
        x coordinate in SIII
    y : float
        y coordinate in SIII
    z : float
        z coordinate in SIII
    xt : float
        Current sheet/dipole tilt (degrees)
    xp : float
        Azimuth of tilt (degrees)
        
    Returns
    =======
    ox : float
        x-coordinate 
    oy : float
        y-coordinate 
    oz : float
        z-coordinate 
    
    '''
    
    #some sines and cosines
    dtor = np.pi/180.0
    xtr = dtor*xt
    xpr = dtor*xp
    cosxt = np.cos(xtr)
    sinxt = np.sin(xtr)
    cosxp = np.cos(xpr)
    sinxp = np.sin(xpr)
    

    xtmp = x*cosxp + y*sinxp
    ox = xtmp*cosxt -z*sinxt
    oy = -x*sinxp + y*cosxp
    oz = xtmp*sinxt + z*cosxt

    return ox,oy,oz
    


def _GetCFG():
	'''
	Get the current config dictionary
	
	
	'''
	eqtype = ctypes.c_char_p("        ".encode('utf-8'))
	mui = np.zeros(1,dtype='float64')
	irho = np.zeros(1,dtype='float64')
	r0 = np.zeros(1,dtype='float64')
	r1 = np.zeros(1,dtype='float64')
	d = np.zeros(1,dtype='float64')
	xt = np.zeros(1,dtype='float64')
	xp = np.zeros(1,dtype='float64')
	Edwards = np.zeros(1,dtype='bool')
	ErrChk = np.zeros(1,dtype='bool')
	CartIn = np.zeros(1,dtype='bool')
	CartOut = np.zeros(1,dtype='bool')
	Smooth = np.zeros(1,dtype='bool')
	DeltaRho = np.zeros(1,dtype='float64')
	DeltaZ = np.zeros(1,dtype='float64')

	g = np.zeros(1,dtype='float64')
	azfunc = ctypes.c_char_p("          ".encode('utf-8'))
	wO_open = np.zeros(1,dtype='float64')
	wO_om = np.zeros(1,dtype='float64')
	thetamm = np.zeros(1,dtype='float64')
	dthetamm = np.zeros(1,dtype='float64')
	thetaoc = np.zeros(1,dtype='float64')
	dthetaoc = np.zeros(1,dtype='float64')


	getCon2020Params(mui,irho,r0,r1,d,xt,xp,eqtype,Edwards,ErrChk,
						CartIn,CartOut,Smooth,DeltaRho,DeltaZ,g,azfunc,
						wO_open,wO_om,thetamm,dthetamm,thetaoc,dthetaoc)
	
	cfg = {}
	cfg['mu_i'] = mui[0]
	cfg['i_rho'] = irho[0]
	cfg['r0'] = r0[0]
	cfg['r1'] = r1[0]
	cfg['d'] = d[0]
	cfg['xt'] = xt[0]
	cfg['xp'] = xp[0]
	cfg['Edwards'] = Edwards[0]
	cfg['error_check'] = ErrChk[0]
	cfg['CartesianIn'] = CartIn[0]
	cfg['CartesianOut'] = CartOut[0]
	cfg['equation_type'] = eqtype.value.decode()
	cfg['Smooth'] = Smooth[0]
	cfg['DeltaRho'] = DeltaRho[0]
	cfg['DeltaZ'] = DeltaZ[0]

	cfg['g'] = g[0]
	cfg['azfunc'] = azfunc.value.decode()
	cfg['wO_open'] = wO_open[0]
	cfg['wO_om'] = wO_om[0]
	cfg['thetamm'] = thetamm[0]
	cfg['dthetamm'] = dthetamm[0]
	cfg['thetaoc'] = thetaoc[0]
	cfg['dthetaoc'] = dthetaoc[0]

	return cfg

def _SetCFG(cfg):
	'''
	Set the model config using a dictionary.
	
	'''
	
	eqtype = ctypes.c_char_p(cfg['equation_type'].encode('utf-8'))
	mui = np.array([cfg['mu_i']],dtype='float64')
	irho = np.array([cfg['i_rho']],dtype='float64')
	r0 = np.array([cfg['r0']],dtype='float64')
	r1 = np.array([cfg['r1']],dtype='float64')
	d = np.array([cfg['d']],dtype='float64')
	xt = np.array([cfg['xt']],dtype='float64')
	xp = np.array([cfg['xp']],dtype='float64')
	Edwards = np.array([cfg['Edwards']],dtype='bool')
	ErrChk = np.array([cfg['error_check']],dtype='bool')
	CartIn = np.array([cfg['CartesianIn']],dtype='bool')
	CartOut = np.array([cfg['CartesianOut']],dtype='bool')
	Smooth = np.array([cfg['Smooth']],dtype='bool')
	DeltaRho = np.array([cfg['DeltaRho']],dtype='float64')
	DeltaZ = np.array([cfg['DeltaZ']],dtype='float64')

	g = np.array([cfg['g']],dtype='float64')
	azfunc = ctypes.c_char_p(cfg['azfunc'].encode('utf-8'))
	wO_open = np.array([cfg['wO_open']],dtype='float64')
	wO_om = np.array([cfg['wO_om']],dtype='float64')
	thetamm = np.array([cfg['thetamm']],dtype='float64')
	dthetamm = np.array([cfg['dthetamm']],dtype='float64')
	thetaoc = np.array([cfg['thetaoc']],dtype='float64')
	dthetaoc = np.array([cfg['dthetaoc']],dtype='float64')



	
	setCon2020Params(mui,irho,r0,r1,d,xt,xp,eqtype,Edwards,ErrChk,
						CartIn,CartOut,Smooth,DeltaRho,DeltaZ,g,azfunc,
						wO_open,wO_om,thetamm,dthetamm,thetaoc,dthetaoc)
    
def testSmooth():
    '''
    Test the smooth (tanh) transition over r0 and r1
    
    
    '''
    n = np.int32(100)

    #use default r0 and r1
    r0 = 7.8
    r1 = 51.4

    #get MAG arrays along equator
    mlt = 0.0
    mltr = mlt*np.pi/12.0
    
    rho0 = np.linspace(r0-5,r0+5,n)
    x0 = -rho0*np.cos(mltr)
    y0 = -rho0*np.sin(mltr)
    z0 = np.zeros(n)

    rho1 = np.linspace(r1-30,r1+30,n)
    x1 = -rho1*np.cos(mltr)
    y1 = -rho1*np.sin(mltr)
    z1 = np.zeros(n)

    #convert to SIII
    x0,y0,z0 = MagtoSIII(x0,y0,z0,9.3,155.8)
    x1,y1,z1 = MagtoSIII(x1,y1,z1,9.3,155.8)


    #get params
    cfg = _GetCFG()

    #set smooth off
    cfg['Smooth'] = False
    cfg['DeltaRho'] = 1.0
    cfg['equation_type'] = 'analytic'
    _SetCFG(cfg)

    #get B
    Bx0 = np.zeros(n,dtype='float64')
    By0 = np.zeros(n,dtype='float64')
    Bz0 = np.zeros(n,dtype='float64')

    Bx1 = np.zeros(n,dtype='float64')
    By1 = np.zeros(n,dtype='float64')
    Bz1 = np.zeros(n,dtype='float64')

    con2020FieldArray(n,x0,y0,z0,Bx0,By0,Bz0)
    con2020FieldArray(n,x1,y1,z1,Bx1,By1,Bz1)

    #turn smoothing on
    cfg['Smooth'] = True
    _SetCFG(cfg)

    #get B
    
    Bx0s = np.zeros(n,dtype='float64')
    By0s = np.zeros(n,dtype='float64')
    Bz0s = np.zeros(n,dtype='float64')

    Bx1s = np.zeros(n,dtype='float64')
    By1s = np.zeros(n,dtype='float64')
    Bz1s = np.zeros(n,dtype='float64')

    con2020FieldArray(n,x0,y0,z0,Bx0s,By0s,Bz0s)
    con2020FieldArray(n,x1,y1,z1,Bx1s,By1s,Bz1s)
  

    plt.figure(figsize=(8,11))
    ax0 = plt.subplot2grid((2,1),(0,0))
    ax1 = plt.subplot2grid((2,1),(1,0))

    ax0.plot(rho0,Bx0-np.nanmean(Bx0),color='red',linestyle='--',label='$B_x$')
    ax0.plot(rho0,By0-np.nanmean(By0),color='green',linestyle='--',label='$B_y$')
    ax0.plot(rho0,Bz0-np.nanmean(Bz0),color='blue',linestyle='--',label='$B_z$')

    ax0.plot(rho0,Bx0-np.nanmean(Bx0s),color='red',linestyle='-',label='$B_x$ (smooth)')
    ax0.plot(rho0,By0-np.nanmean(By0s),color='green',linestyle='-',label='$B_y$ (smooth)')
    ax0.plot(rho0,Bz0-np.nanmean(Bz0s),color='blue',linestyle='-',label='$B_z$ (smooth)')

    ylim = ax0.get_ylim()
    ax0.set_ylim(ylim)
    ax0.vlines(r0,ylim[0],ylim[1],color='grey',linestyle=':')
    ax0.legend()

    ax1.plot(rho1,Bx1-np.nanmean(Bx1),color='red',linestyle='--',label='$B_x$')
    ax1.plot(rho1,By1-np.nanmean(By1),color='green',linestyle='--',label='$B_y$')
    ax1.plot(rho1,Bz1-np.nanmean(Bz1),color='blue',linestyle='--',label='$B_z$')

    ax1.plot(rho1,Bx1-np.nanmean(Bx1s),color='red',linestyle='-',label='$B_x$ (smooth)')
    ax1.plot(rho1,By1-np.nanmean(By1s),color='green',linestyle='-',label='$B_y$ (smooth)')
    ax1.plot(rho1,Bz1-np.nanmean(Bz1s),color='blue',linestyle='-',label='$B_z$ (smooth)')

    ylim = ax1.get_ylim()
    ax1.set_ylim(ylim)
    ax1.vlines(r1,ylim[0],ylim[1],color='grey',linestyle=':')
    ax1.legend()

    ax0.set_xlabel('$\\rho$ (R$_J$)')
    ax1.set_xlabel('$\\rho$ (R$_J$)')

    plt.savefig('testsmooth.png')
    plt.close()

    print('Testing single point (normal)')
    #get params
    cfg = _GetCFG()

    #set smooth off
    cfg['Smooth'] = False
    cfg['DeltaRho'] = 0.0
    cfg['equation_type'] = 'analytic'
    _SetCFG(cfg)
    i = 5
    x = np.array([x0[i]])
    y = np.array([y0[i]])
    z = np.array([z0[i]])

    Bx = np.zeros(1,dtype='float64')
    By = np.zeros(1,dtype='float64')
    Bz = np.zeros(1,dtype='float64')

    con2020FieldArray(1,x,y,z,Bx,By,Bz)

    #turn smoothing on
    print('Testing single point (smooth)')
    cfg['Smooth'] = True
    _SetCFG(cfg)

    Bxs = np.zeros(1,dtype='float64')
    Bys = np.zeros(1,dtype='float64')
    Bzs = np.zeros(1,dtype='float64')

    con2020FieldArray(1,x,y,z,Bxs,Bys,Bzs)



def testSmoothZ():
    
    n = np.int32(100)

    rho0 = 5.0
    rho1 = 25.0
    zr0 = -20
    zr1 = 20

    #get MAG arrays along equator
    mlt = 0.0
    mltr = mlt*np.pi/12.0
    
    x0 = -rho0*np.cos(mltr) + np.zeros(n)
    y0 = -rho0*np.sin(mltr) + np.zeros(n)
    z0 = np.linspace(zr0,zr1,n)

    x1 = -rho1*np.cos(mltr) + np.zeros(n)
    y1 = -rho1*np.sin(mltr) + np.zeros(n)
    z1 = np.linspace(zr0,zr1,n)

    #convert to SIII
    x0,y0,z0 = MagtoSIII(x0,y0,z0,9.3,155.8)
    x1,y1,z1 = MagtoSIII(x1,y1,z1,9.3,155.8)
    zm = np.linspace(zr0,zr1,n)

    #get params
    cfg = _GetCFG()

    #set smooth off
    cfg['Smooth'] = False
    cfg['equation_type'] = 'analytic'
    _SetCFG(cfg)

    #get B
    Bx0 = np.zeros(n,dtype='float64')
    By0 = np.zeros(n,dtype='float64')
    Bz0 = np.zeros(n,dtype='float64')

    Bx1 = np.zeros(n,dtype='float64')
    By1 = np.zeros(n,dtype='float64')
    Bz1 = np.zeros(n,dtype='float64')

    con2020FieldArray(n,x0,y0,z0,Bx0,By0,Bz0)
    con2020FieldArray(n,x1,y1,z1,Bx1,By1,Bz1)

    #turn smoothing on
    cfg['Smooth'] = True
    _SetCFG(cfg)

    #get B
    
    Bx0s = np.zeros(n,dtype='float64')
    By0s = np.zeros(n,dtype='float64')
    Bz0s = np.zeros(n,dtype='float64')

    Bx1s = np.zeros(n,dtype='float64')
    By1s = np.zeros(n,dtype='float64')
    Bz1s = np.zeros(n,dtype='float64')

    con2020FieldArray(n,x0,y0,z0,Bx0s,By0s,Bz0s)
    con2020FieldArray(n,x1,y1,z1,Bx1s,By1s,Bz1s)
  

    plt.figure(figsize=(8,11))
    ax0 = plt.subplot2grid((2,1),(0,0))
    ax1 = plt.subplot2grid((2,1),(1,0))

    ax0.plot(zm,Bx0-np.nanmean(Bx0),color='red',linestyle='--',label='$B_x$')
    ax0.plot(zm,By0-np.nanmean(By0),color='green',linestyle='--',label='$B_y$')
    ax0.plot(zm,Bz0-np.nanmean(Bz0),color='blue',linestyle='--',label='$B_z$')

    ax0.plot(zm,Bx0-np.nanmean(Bx0s),color='red',linestyle='-',label='$B_x$ (smooth)')
    ax0.plot(zm,By0-np.nanmean(By0s),color='green',linestyle='-',label='$B_y$ (smooth)')
    ax0.plot(zm,Bz0-np.nanmean(Bz0s),color='blue',linestyle='-',label='$B_z$ (smooth)')

    ylim = ax0.get_ylim()
    ax0.set_ylim(ylim)
    D = cfg['d']
    ax0.vlines([-D,0.0,+D],ylim[0],ylim[1],color='grey',linestyle=':')
    ax0.legend()

    ax1.plot(zm,Bx1-np.nanmean(Bx1),color='red',linestyle='--',label='$B_x$')
    ax1.plot(zm,By1-np.nanmean(By1),color='green',linestyle='--',label='$B_y$')
    ax1.plot(zm,Bz1-np.nanmean(Bz1),color='blue',linestyle='--',label='$B_z$')

    ax1.plot(zm,Bx1-np.nanmean(Bx1s),color='red',linestyle='-',label='$B_x$ (smooth)')
    ax1.plot(zm,By1-np.nanmean(By1s),color='green',linestyle='-',label='$B_y$ (smooth)')
    ax1.plot(zm,Bz1-np.nanmean(Bz1s),color='blue',linestyle='-',label='$B_z$ (smooth)')

    ylim = ax1.get_ylim()
    ax1.set_ylim(ylim)
    ax1.vlines([-D,0.0,+D],ylim[0],ylim[1],color='grey',linestyle=':')
    ax1.legend()

    ax0.set_xlabel('$z_{mag}$ (R$_J$)')
    ax1.set_xlabel('$z_{mag}$ (R$_J$)')

    plt.savefig('testsmoothz.png')
    plt.close()


if __name__ == '__main__':
    
    testSmooth()
    testSmoothZ()