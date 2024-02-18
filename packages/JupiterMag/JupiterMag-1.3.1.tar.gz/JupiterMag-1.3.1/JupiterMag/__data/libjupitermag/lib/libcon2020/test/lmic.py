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

_COmegaRatio = lib.OmegaRatio
_COmegaRatio.restype = c_double
_COmegaRatio.argtypes = [	c_double,
							c_double,
							c_double,
							c_double,
							c_double,
							c_double,
							c_double]

_CPedersenCurrent = lib.PedersenCurrent
_CPedersenCurrent.restype = c_double
_CPedersenCurrent.argtypes = [	c_double,
								c_double,
								c_double,
								c_double,
								c_double,
								c_double,
								c_double,
								c_double]

_CBphiLMIC = lib.BphiLMIC
_CBphiLMIC.restype = c_double
_CBphiLMIC.argtypes = [	c_double,
						c_double,
						c_double,
						c_double,
						c_double,
						c_double,
						c_double,
						c_double,
						c_double,
						c_double,
						c_double,
						c_double,
						c_double,
						c_double,
						c_double,]

_CBphiIonosphere = lib.BphiIonosphere
_CBphiIonosphere.restype = c_double
_CBphiIonosphere.argtypes = [	c_double,
								c_double,
								c_double,
								c_double,
								c_double,
								c_double,
								c_double,
								c_double,]

def lmic(fig=None,maps=[1,1,0,0]):
	

	#define parameters for CAN model
	r0 = 7.8
	r1 = 51.4
	mui2 = 139.6
	D = 3.6
	deltarho = 1.0
	deltaz = 0.1

	#dipole parameter
	g10 = 410993.4
	g11 = -71305.9
	h11 =  20958.4
	g = np.sqrt(g10**2 + g11**2 + h11**2)

	#LMIC parameters
	dtor = np.pi/180.0
	wO_open = 0.1
	wO_om = 0.35
	thetamm = 16.1*dtor
	dthetamm = 0.5*dtor
	thetaoc = 10.716*dtor
	dthetaoc = 0.125*dtor

	#ionospheric radius
	Ri = 67350000.0
	Rj = 71492000.0
	ri = Ri/Rj

	#thetai
	n = 1000
	thetadeg = np.linspace(0.0,20.0,n,dtype='float64')
	thetai = thetadeg*dtor
	

	#calculate angular velocity ratio
	print('Calculating angular velocity ratio')
	wO = np.zeros(n,dtype='float64')
	for i in range(0,n):
		wO[i] = _COmegaRatio(thetai[i],wO_open,wO_om,thetamm,dthetamm,thetaoc,dthetaoc)

	#calculate pedersen current
	print('Calculating Pedersen current')
	IhP = np.zeros(n,dtype='float64')
	for i in range(0,n):
		IhP[i] = _CPedersenCurrent(thetai[i],g,wO_open,wO_om,thetamm,dthetamm,thetaoc,dthetaoc)/1e6

	#calculate Bphi at the ionosphere
	print('Calculating Bphi')
	Bp = np.zeros(n,dtype='float64')
	Bpi = np.zeros(n,dtype='float64')
	for i in range(0,n):
		Bp[i] = _CBphiLMIC(ri,thetai[i],g,r0,r1,mui2,D,deltarho,deltaz,
					wO_open,wO_om,thetamm,dthetamm,thetaoc,dthetaoc)
		Bpi[i] = _CBphiIonosphere(thetai[i],g,wO_open,wO_om,thetamm,dthetamm,thetaoc,dthetaoc)

	#plot colors
	coltail = [0.776,0.824,0.965]
	colom = [1.0,1.0,0.702]
	colmm = [1.0,0.702,0.702]
	colboundary = [0.7,1.0,0.7]
	colim = [1.0,1.0,1.0]
	cols = [coltail,colboundary,colom,colmm,colim]
	labs = ['Tail','','OM','MM','IM']
	x = np.array([0.0,thetaoc-dthetaoc,thetaoc+dthetaoc,thetamm-dthetamm,thetamm+dthetamm,20.0*dtor])/dtor

	plt.figure(figsize=(8,11))
	
	ax0 = plt.subplot2grid((3,1),(0,0))
	ax0.plot(thetadeg,wO,color='black')
	ax0.set_ylim(0.0,1.2)
	ax0.set_xlim(thetadeg[0],thetadeg[-1])
	ax0.set_xlabel(r'$\theta_i$ ($^\circ$)')
	ax0.set_ylabel(r'$\omega_i/\Omega_J$')

	ax1 = plt.subplot2grid((3,1),(1,0))
	ax1.plot(thetadeg,IhP,color='black')
	ax1.set_ylim(0.0,60.0)
	ax1.set_xlim(thetadeg[0],thetadeg[-1])
	ax1.set_xlabel(r'$\theta_i$ ($^\circ$)')
	ax1.set_ylabel(r'$I_{hP}(\theta_i)$ (MA)')

	ax2 = plt.subplot2grid((3,1),(2,0))
	ax2.plot(thetadeg,Bpi,color='black')
	ax2.plot(thetadeg,Bp,color='black',linestyle=':')
	ax2.set_ylim(-650.0,0.0)
	ax2.set_xlim(thetadeg[0],thetadeg[-1])
	ax2.set_xlabel(r'$\theta_i$ ($^\circ$)')
	ax2.set_ylabel(r'$B_{\phi}$ (nT)')

	axs = [ax0,ax1,ax2]

	for ax in axs:

		ylim = ax.get_ylim()
		yf = [ylim[0],ylim[0],ylim[1],ylim[1]]
		for i in range(0,len(x)-1):
			xf = [x[i],x[i+1],x[i+1],x[i]]
			ax.fill(xf,yf,color=cols[i])
			ax.text(0.5*(x[i] + x[i+1]),0.95*(ylim[1]-ylim[0])+ylim[0],labs[i],ha='center',va='center')

		ax.vlines(x[1:3],ylim[0],ylim[1],color=[0.0,1.0,0.0])
		ax.vlines(x[3:5],ylim[0],ylim[1],color=[1.0,0.0,0.0])

		


	plt.savefig('testlmic.png')
	plt.close()
	print('saved test/testlmic.png')

if __name__ == '__main__':
	lmic()