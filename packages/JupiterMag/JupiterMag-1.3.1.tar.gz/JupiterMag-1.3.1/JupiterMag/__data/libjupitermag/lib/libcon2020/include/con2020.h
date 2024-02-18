
#ifndef __LIBCON2020_H__
#define __LIBCON2020_H__

#define _USE_MATH_DEFINES
#include <math.h>
#include <stdio.h>
#include <stdlib.h>

#ifdef __cplusplus
	#include <algorithm>
	#include <string>
#else
	#include <string.h>
	#include <stdbool.h>
#endif
#define LIBCON2020_VERSION_MAJOR 1
#define LIBCON2020_VERSION_MINOR 1
#define LIBCON2020_VERSION_PATCH 0

#define deg2rad M_PI/180.0
#define rad2deg 180.0/M_PI


#ifdef __cplusplus
extern "C" {
#endif
	/* these wrappers can be used to get the magnetic field vectors */
	void Con2020FieldArray(int n, double *p0, double *p1, double *p2,
					double *B0, double *B1, double *B2);
	
	void Con2020Field(double p0, double p1, double p2,
			double *B0, double *B1, double *B2);


	void GetCon2020Params(double *mui, double *irho, double *r0, double *r1,
					double *d, double *xt, double *xp, char *eqtype,
					bool *Edwards, bool *ErrChk, bool *CartIn, bool *CartOut, 
					bool *smooth, double *DeltaRho, double *DeltaZ,
					double *g, char *azfunc, double *wO_open, double *wO_om,
					double *thetamm, double *dthetamm, double *thetaoc, double *dthetaoc);
						
	
	void SetCon2020Params(double mui, double irho, double r0, double r1,
					double d, double xt, double xp, const char *eqtype,
					bool Edwards, bool ErrChk, bool CartIn, bool CartOut, 
					bool smooth, double DeltaRho, double DeltaZ,
					double g, const char *azfunc, double wO_open, double wO_om,
					double thetamm, double dthetamm, double thetaoc, double dthetaoc);

	void Con2020AnalyticField(	int n, double a, 
							double *rho, double *z, 
							double *Brho, double *Bz);

	void Con2020AnalyticFieldSmooth(	int n, double a, 
							double *rho, double *z, 
							double *Brho, double *Bz);


/***************************************************************
*
*   NAME : ScalarPotentialSmallRho(rho,z,a,mui2,D)
*
*   DESCRIPTION : Calcualte the small rho approximation
*       of the scalar potential accoring to Edwards et al.,
*       2001 (equation 8).
*
*   INPUTS : 
*       double  rho     Cylindrical rho coordinate (in disc 
*                       coordinate system, Rj)
*       double  z       z-coordinate, Rj
*       double  a       inner edge of semi-infinite current 
*                       sheet, Rj
*       double mui2     mu_0 I_0 /2 parameter (default 139.6 nT)
*       double D        Current sheet half-thickness, Rj
*
***************************************************************/
	double ScalarPotentialSmallRho( double rho, double z, double a,
									double mui2, double D);


/***************************************************************
*
*   NAME : ScalarPotentialLargeRho(rho,z,a,mui2,D,deltaz)
*
*   DESCRIPTION : Calcualte the large rho approximation
*       of the scalar potential accoring to Edwards et al.,
*       2001 (equation 12).
*
*   INPUTS : 
*       double  rho     Cylindrical rho coordinate (in disc 
*                       coordinate system, Rj)
*       double  z       z-coordinate, Rj
*       double  a       inner edge of semi-infinite current 
*                       sheet, Rj
*       double mui2     mu_0 I_0 /2 parameter (default 139.6 nT)
*       double D        Current sheet half-thickness, Rj
*       double deltaz   Scale length over which to smooth 4th
*                        term of the equation
*
***************************************************************/
	double ScalarPotentialLargeRho( double rho, double z, double a,
									double mui2, double D, double deltaz);


/***************************************************************
*
*   NAME : ScalarPotential(rho,z,a,mui2,D,deltarho,deltaz)
*
*   DESCRIPTION : Calculate the small/large rho approximation
*       of the scalar potential accoring to Edwards et al.,
*       2001 (equations 8 & 12).
*
*   INPUTS : 
*       double  rho     Cylindrical rho coordinate (in disc 
*                       coordinate system, Rj)
*       double  z       z-coordinate, Rj
*       double  a       inner edge of semi-infinite current 
*                       sheet, Rj
*       double mui2     mu_0 I_0 /2 parameter (default 139.6 nT)
*       double D        Current sheet half-thickness, Rj
*       double deltarho Scale length to smoothly transition from
*                       small to large rho approx
*       double deltaz   Scale length over which to smooth 4th
*                        term of the equation
*
***************************************************************/
	double ScalarPotential( double rho, double z, double a,
							double mui2, double D, 
							double deltarho, double deltaz);

	/*************************************************************
	*
	*	NAME: f_theta(thetai)
	*
	*	DESCRIPTION: Equation 5 of Cowley et al., 2008
	*
	*	INPUTS:
	*		double thetai	colatitude of the ionospheric footprint
	*						in radians!
	*
	*	RETURNS:
	*		double f_theta	1 + 0.25*tan^2 thetai
	*
	*************************************************************/
	double f_thetai(double thetai);

	/*************************************************************
	*
	*	NAME: OmegaRatio(thetai,wO_open,wO_om,thetamm,dthetamm,
	*						thetaoc,dthetaoc)
	*
	*	DESCRIPTION: Ratio of the angular velocity mapped to
	*		thetai to the planetary rotation. Equation 15 of 
	*		Cowley et al., 2008.
	*
	*	INPUTS:
	*		double thetai	colatitude of the ionospheric footprint
	*						in radians!
	*		double wO_open	angular velocity ratio of open flux to
	*						planetary spin
	*		double wO_om	angular velocity ratio of outer magnetosphere
	*						to planetary spin
	*		double thetamm	ionospheric footprint latitude of the 
	*						middle magnetosphere (where plasma 
	*						goes from rigid corotation to subcorotation)
	*						in radians.
	*		double dthetamm	width of the middle magnetosphere in radians.
	*		double thetaoc	ionospheric latitude of the open-closed field
	*						line boundary, in radians.
	*		double dthetaoc	width of the open-closed field line boundary,
	*						in radians.
	*
	*	RETURNS:
	*		double wO		Ratio of plasma angular veloctiy to Jupiter
	*						spin.
	*
	*************************************************************/
	double OmegaRatio(	double thetai, double wO_open, double wO_om,
						double thetamm, double dthetamm,
						double thetaoc, double dthetaoc);

	/*************************************************************
	*
	*	NAME: PedersenCurrent(thetai,g,wO_open,wO_om,thetamm,dthetamm,
	*						thetaoc,dthetsoc)
	*
	*	DESCRIPTION: Calculate the Pedersen current which maps to a
	*		given ionospheric latitude using equation 6 of Cowley et
	*		al., 2008.
	*
	*	INPUTS:
	*		double thetai	colatitude of the ionospheric footprint
	*						in radians!
	*		double g		dipole coefficient, nT.
	*		double wO_open	angular velocity ratio of open flux to
	*						planetary spin
	*		double wO_om	angular velocity ratio of outer magnetosphere
	*						to planetary spin
	*		double thetamm	ionospheric footprint latitude of the 
	*						middle magnetosphere (where plasma 
	*						goes from rigid corotation to subcorotation)
	*						in radians.
	*		double dthetamm	width of the middle magnetosphere in radians.
	*		double thetaoc	ionospheric latitude of the open-closed field
	*						line boundary, in radians.
	*		double dthetaoc	width of the open-closed field line boundary,
	*						in radians.
	*	RETURNS:
	*		double Ihp		Ionospheric Pedersen current.
	*
	*************************************************************/
	double PedersenCurrent(	double thetai, double g, 
						double wO_open, double wO_om,
						double thetamm, double dthetamm,
						double thetaoc, double dthetaoc );				

	/*************************************************************
	*
	*	NAME: ThetaIonosphere(r,theta,g,r0,r1,mui2,D,deltarho,deltaz)
	*
	*	DESCRIPTION: Use the flux functions of the CAN model and a 
	*		dipole field to map the current position to a position
	*		on the ionosphere.
	*
	*	INPUTS:
	*		double r		radial coordinate, Rj.
	*		double theta	colatitude, radians.
	*		double g		dipole coefficient, nT.
	*		double r0		Inner edge of the current sheet, Rj.
	*		double r1		Outer edge of the current sheet, Rj.
	*		double mui2		current parameter, nT.
	*		double D		half-thickness of the current sheet, Rj.
	*		double deltarho	scale distance of the smoothing between
	*						inner and outer approximations, Rj.
	*		double deltaz	scale distance to smooth across the
	*						+/-D boundary, Rj.
	*
	*	RETURNS:
	*		double thetai	Ionospheric latitude in radians.
	*
	*
	*************************************************************/
	double ThetaIonosphere(	double r, double theta, double g,
							double r0, double r1,
							double mui2, double D, 
							double deltarho, double deltaz);

	/*************************************************************
	*
	*	NAME: BphiLMIC(r,theta,g,r0,r1,mui2,D,deltarho,deltaz,
	*					wO_open,wO_om,thetamm,dthetamm,
	*					thetaom,dthetaom)
	*
	*	DESCRIPTION: Calculate the azimuthal field using the LMIC 
	*		model.
	*
	*	INPUTS:
	*		double r		radial coordinate, Rj.
	*		double theta	colatitude, radians.
	*		double g		dipole coefficient, nT.
	*		double r0		Inner edge of the current sheet, Rj.
	*		double r1		Outer edge of the current sheet, Rj.
	*		double mui2		current parameter, nT.
	*		double D		half-thickness of the current sheet, Rj.
	*		double deltarho	scale distance of the smoothing between
	*						inner and outer approximations, Rj.
	*		double deltaz	scale distance to smooth across the
	*						+/-D boundary, Rj.
	*		double wO_open	angular velocity ratio of open flux to
	*						planetary spin
	*		double wO_om	angular velocity ratio of outer magnetosphere
	*						to planetary spin
	*		double thetamm	ionospheric footprint latitude of the 
	*						middle magnetosphere (where plasma 
	*						goes from rigid corotation to subcorotation)
	*						in radians.
	*		double dthetamm	width of the middle magnetosphere in radians.
	*		double thetaoc	ionospheric latitude of the open-closed field
	*						line boundary, in radians.
	*		double dthetaoc	width of the open-closed field line boundary,
	*						in radians.
	*
	*	RETURNS:
	*		double Bphi		Azimuthal field, nT.
	*
	*************************************************************/
	double BphiLMIC(double r, double theta, double g,
							double r0, double r1,
							double mui2, double D, 
							double deltarho, double deltaz,
							double wO_open, double wO_om,
							double thetamm, double dthetamm,
							double thetaoc, double dthetaoc );

	/*************************************************************
	*
	*	NAME: BphiIonosphere(thetai,g,wO_open,wO_om,thetamm,dthetamm,
	*					thetaom,dthetaom)
	*
	*	DESCRIPTION: Calculate the ionospheric azimuthal field using the LMIC 
	*		model.
	*
	*	INPUTS:
	*		double thetai	ionospheric colatitude, radians.
	*		double g		dipole coefficient, nT.
	*		double wO_open	angular velocity ratio of open flux to
	*						planetary spin
	*		double wO_om	angular velocity ratio of outer magnetosphere
	*						to planetary spin
	*		double thetamm	ionospheric footprint latitude of the 
	*						middle magnetosphere boundary (where plasma 
	*						goes from rigid corotation to subcorotation)
	*						in radians.
	*		double dthetamm	width of the middle magnetosphere boundary
	*						in radians.
	*		double thetaoc	ionospheric latitude of the open-closed field
	*						line boundary, in radians.
	*		double dthetaoc	width of the open-closed field line boundary,
	*						in radians.
	*
	*	RETURNS:
	*		double Bphi		Azimuthal field, nT.
	*
	*************************************************************/
	double BphiIonosphere( 	double thetai, double g,
							double wO_open, double wO_om,
							double thetamm, double dthetamm,
							double thetaoc, double dthetaoc );
#ifdef __cplusplus
}


/***********************************************************************
 * NAME : j0(x)
 * 
 * DESCRIPTION : Fucntion to calculate an estimate of the Bessel 
 * function j0 using code based on the Cephes C library
 * (Cephes Mathematical Functions Library, http://www.netlib.org/cephes/).
 * 
 * INPUTS :
 * 		double 	x	position to calculate J0 at.
 * 
 * RETURNS :
 * 		double j	j0 function evaluated at x.
 * 
 * ********************************************************************/
double j0(double x);

/***********************************************************************
 * NAME : j1(x)
 * 
 * DESCRIPTION : Fucntion to calculate an estimate of the Bessel 
 * function j1 using code based on the Cephes C library
 * (Cephes Mathematical Functions Library, http://www.netlib.org/cephes/).
 * 
 * INPUTS :
 * 		double 	x	position to calculate J1 at.
 * 
 * RETURNS :
 * 		double j	j1 function evaluated at x.
 * 
 * ********************************************************************/
double j1(double x);

/***********************************************************************
 * NAME : j0(n,x,j)
 * 
 * DESCRIPTION : Fucntion to calculate an estimate of the Bessel 
 * function j0 using code based on the Cephes C library
 * (Cephes Mathematical Functions Library, http://www.netlib.org/cephes/).
 * 
 * INPUTS :
 * 		int 	n	Number of elements in x
 * 		double 	*x	position to calculate J0 at.
 * 
 * OUTPUTS :
 * 		double *j	j0 function evaluated at x.
 * 
 * ********************************************************************/
void j0(int n, double *x, double *j);

/***********************************************************************
 * NAME : j1(n,x,j)
 * 
 * DESCRIPTION : Fucntion to calculate an estimate of the Bessel 
 * function j1 using code based on the Cephes C library
 * (Cephes Mathematical Functions Library, http://www.netlib.org/cephes/).
 * 
 * INPUTS :
 * 		int 	n	Number of elements in x
 * 		double 	*x	position to calculate J1 at.
 * 
 * OUTPUTS :
 * 		double *j	j1 function evaluated at x.
 * 
 * ********************************************************************/
void j1(int n, double *x, double *j);

/***********************************************************************
 * NAME : j0(n,x,multx,j)
 * 
 * DESCRIPTION : Fucntion to calculate an estimate of the Bessel 
 * function j0 using code based on the Cephes C library
 * (Cephes Mathematical Functions Library, http://www.netlib.org/cephes/).
 * 
 * INPUTS :
 * 		int 	n	Number of elements in x
 * 		double 	*x	position to calculate J0(x*multx) at.
 * 		double multx	Constant to multiply x by
 * 
 * OUTPUTS :
 * 		double *j	j0 function evaluated at x*multx.
 * 
 * ********************************************************************/
void j0(int n, double *x, double multx, double *j);

/***********************************************************************
 * NAME : j1(n,x,multx,j)
 * 
 * DESCRIPTION : Fucntion to calculate an estimate of the Bessel 
 * function j1 using code based on the Cephes C library
 * (Cephes Mathematical Functions Library, http://www.netlib.org/cephes/).
 * 
 * INPUTS :
 * 		int 	n	Number of elements in x
 * 		double 	*x	position to calculate J1(x*multx) at.
 * 		double multx	Constant to multiply x by
 * 
 * OUTPUTS :
 * 		double *j	j1 function evaluated at x*multx.
 * 
 * ********************************************************************/
void j1(int n, double *x, double multx, double *j);






template <typename T> T clip(T x, T mn, T mx) {
	return std::min(mx,std::max(x,mn));
}


/* function pointer for input conversion */
class Con2020; /*this is needed for the pointer below */ 
typedef void (Con2020::*InputConvFunc)(int,double*,double*,double*,
						double*,double*,double*,double*,double*,
						double*,double*,double*,double*);
/* Output conversion */
typedef void (Con2020::*OutputConvFunc)(int,double*,double*,double*,
				double*,double*,double*,double*,
				double*,double*,double*,
				double*,double*,double*);

/* Model function */
typedef void (Con2020::*ModelFunc)(double,double,double,double*,double*,double*);

/* analytical approximation equations */
typedef void (Con2020::*Approx)(double,double,double,double,double,double*,double*);

/* azimuthal function */
typedef void (Con2020::*AzimFunc)(double,double,double,double*);

class Con2020 {
	public:
		/* constructors */
		Con2020();
		Con2020(double,double,double,double,double,double,double,const char*,bool,bool,bool,bool);
	
		/* destructor */
		~Con2020();
		
		/* these functions will be used to set the equations used, if
		 * they need to be changed post-initialisation */
		void SetEdwardsEqs(bool);
		void SetEqType(const char*);
		void SetAzCurrentParameter(double);
		void SetRadCurrentParameter(double);
		void SetR0(double);
		void SetR1(double);
		void SetCSHalfThickness(double);
		void SetCSTilt(double);
		void SetCSTiltAzimuth(double);
		void SetErrCheck(bool);
		void SetCartIn(bool);
		void SetCartOut(bool);
		void SetSmooth(bool);
		void SetDeltaRho(double);
		void SetDeltaZ(double);
		void SetOmegaOpen(double);
		void SetOmegaOM(double);
		void SetThetaMM(double);
		void SetdThetaMM(double);
		void SetThetaOC(double);
		void SetdThetaOC(double);
		void SetG(double);
		void SetAzimuthalFunc(const char*);
		
		/* these mamber functions will be the "getter" version of the
		 * above setters */
		bool GetEdwardsEqs();
		void GetEqType(char*);
		double GetAzCurrentParameter();
		double GetRadCurrentParameter();
		double GetR0();
		double GetR1();
		double GetCSHalfThickness();
		double GetCSTilt();
		double GetCSTiltAzimuth();
		bool GetErrCheck();
		bool GetCartIn();
		bool GetCartOut();
		bool GetSmooth();
		double GetDeltaRho();
		double GetDeltaZ();
		double GetOmegaOpen();
		double GetOmegaOM();
		double GetThetaMM();
		double GetdThetaMM();
		double GetThetaOC();
		double GetdThetaOC();
		double GetG();
		void GetAzimuthalFunc(char *);

		/* This function will be used to call the model, it is overloaded
		 * so that we have one for arrays, one for scalars */
		void Field(int,double*,double*,double*,double*,double*,double*);
		void Field(double,double,double,double*,double*,double*);

		/* a function for testing purposes...*/
		void AnalyticField(double,double,double,double*,double*);
		void AnalyticFieldSmooth(double,double,double,double*,double*);

		/* expose the model function pointer*/
		ModelFunc _Model;

	private:
		/* model parameters */
		double mui_,irho_,r0_,r1_,d_,xt_,xp_,disctilt_,discshift_;
		double r0sq_, r1sq_;
		double cosxp_,sinxp_,cosxt_,sinxt_;
		char eqtype_[9];
		bool Edwards_, ErrChk_;
		bool CartIn_,CartOut_;
		double deltaz_,deltarho_;
		bool smooth_;

		/* LMIC parameters*/
		double wO_open_, wO_om_, thetamm_, dthetamm_, thetaoc_, dthetaoc_, g_;
		char azfunc_[10];
		
		/* Bessel function arrays - arrays prefixed with r and z are
		 * to be used for integrals which calcualte Brho and Bz,
		 * respectively */
		int *rnbes_;			/* number of elements for each Bessel function (rho)*/
		int *znbes_;			/* same as above for z */
		double **rlambda_;/* Lambda array to integrate over rho*/
		double **zlambda_;/* Lambda array to integrate over z*/
		double **rj0_lambda_r0_; /* j0(lambda*r0) */
		double **rj1_lambda_rho_;/* j1(lambda*rho) */
		double **zj0_lambda_r0_; /* j0(lambda*r0) */
		double **zj0_lambda_rho_;/* j0(lambda*rho) */

		
		/* arrays to multiply be stuff to be integrated */
		/* these arrays will store the parts of equations 14, 15, 17 
		 * and 18 of Connerny 1981 which only need to be calculated once*/
		double **Eq14_;		/* j0(lambda*r0)*sinh(lamba*d)/lambda */
		double **Eq15_;     /* j0(lambda*r0)*sinh(lamba*d)/lambda */
		double **Eq17_;     /* j0(lambda*r0)*exp(-lamba*d)/lambda */
		double **Eq18_;     /* j0(lambda*r0)/lambda */
		double **ExpLambdaD_;
		

		/* integration step sizes */
		static constexpr double dlambda_ = 1e-4;
		static constexpr double dlambda_brho_ = 1e-4;
		static constexpr double dlambda_bz_ = 5e-5;
		
		/* Arrays containing maximum lambda values */
		double rlmx_array_[6];
		double zlmx_array_[6];


		/* coordinate conversions for positions */
		InputConvFunc _ConvInput;
		void _SysIII2Mag(int,double*,double*,double*,
						double*,double*,double*,double*,double*,
						double*,double*,double*,double*);
		void _PolSysIII2Mag(int,double*,double*,double*,
						double*,double*,double*,double*,double*,
						double*,double*,double*,double*);
		
		
		/* coordinate conversion for magnetic field vector */
		OutputConvFunc _ConvOutput;
		void _BMag2SysIII(int,double*,double*,double*,
							double*,double*,double*,double*,
							double*,double*,double*,
							double*,double*,double*);
		void _BMag2PolSysIII(int,double*,double*,double*,
							double*,double*,double*,double*,
							double*,double*,double*,
							double*,double*,double*);	

		/* Functions to update function pointers */
		void _SetIOFunctions();
		void _SetModelFunctions();
		
							
		/* Azimuthal field */
		AzimFunc _AzimuthalField;
		void _BphiConnerney(int,double*,double*,double*,double*);
		void _BphiConnerney(double,double,double,double*);
		void _BphiLMIC(double,double,double,double*);
		Approx _LargeRho;
		Approx _SmallRho;		
		/* analytic equations */
		void _Analytic(double,double,double,double*,double*,double*);
		void _AnalyticSmooth(double,double,double,double*,double*,double*);
		void _SolveAnalytic(int,double*,double*,double,double*,double*);
		void _AnalyticInner(double,double,double*,double*);
		void _AnalyticOuter(double,double,double*,double*);
		void _AnalyticInnerSmooth(double,double,double*,double*);
		void _AnalyticOuterSmooth(double,double,double*,double*);
		void _LargeRhoConnerney(double,double,double,double,double,double*,double*);
		void _SmallRhoConnerney(double,double,double,double,double,double*,double*);
		void _LargeRhoEdwards(double,double,double,double,double,double*,double*);
		void _LargeRhoEdwardsSmooth(double,double,double,double,double,double*,double*);
		void _SmallRhoEdwards(double,double,double,double,double,double*,double*);
		
		/* integral-related functions */
		void _Integral(double,double,double,double*,double*,double*);
		void _IntegralInner(double, double, double,	double*, double*);
		void _InitIntegrals();
		void _RecalcIntegrals();
		void _DeleteIntegrals();
		void _IntegralChecks(int,double*,int*,int[]);
		void _IntegralCheck(double,int*);
		void _SolveIntegral(int,double*,double*,double*,double*,double*);
		void _IntegrateEq14(int,double,double,double,double*);
		void _IntegrateEq15(int,double,double,double*);
		void _IntegrateEq17(int,double,double,double*);
		void _IntegrateEq18(int,double,double,double*);

		/* hybrid */
		void _Hybrid(double,double,double,double*,double*,double*);
};



/* we want to initialize the model objects with its parameters */
extern Con2020 con2020;

extern "C" {
}

double polyeval(double x, double *c, int d);

double pol1eval(double x, double *c, int d);


/***********************************************************************
 * NAME : smoothd(z,dz,d)
 * 
 * DESCRIPTION : Smooth fucntion for crossing the current sheet 
 * (replaces the last bit of equation 12 in Edwards et al 2000).
 * 
 * INPUTS : 
 * 		double z	z-coordinate in dipole coordinate system (Rj)
 * 		double dz	Scale of the transition to use (Rj)
 * 		double d	Half thickness of the current sheet.
 * 
 * RETURNS : 
 * 		double out	Smoothed function across the current sheet.
 * 
 * ********************************************************************/
double smoothd(double z, double dz, double d);



double trap(int n, double *x, double *y);
double trapc(int n, double dx, double *y);

/***************************************************************
*
*   NAME : FluxCan(rho,z,r0,r1,mui2,D,deltarho,deltaz)
*
*   DESCRIPTION : Calculate the flux contribution from the 
* 		CAN current sheet (using Edwards et al. 2001 equations).
*
*   INPUTS : 
*       double  rho     Cylindrical rho coordinate (in disc 
*                       coordinate system, Rj)
*       double  z       z-coordinate, Rj
*       double  r0       inner edge of semi-infinite current 
*                       sheet, Rj
*		double 	r1		inner edge of the outer portion of the 
*						current sheet to be subtracted
*       double mui2     mu_0 I_0 /2 parameter (default 139.6 nT)
*       double D        Current sheet half-thickness, Rj
*       double deltarho Scale length to smoothly transition from
*                       small to large rho approx
*       double deltaz   Scale length over which to smooth 4th
*                        term of the equation
*
***************************************************************/
double FluxCan(	double rho,double z, double r0, double r1,
				double mui2, double D, 
				double deltarho, double deltaz) {

	double A0 = ScalarPotential(rho,z,r0,mui2,D,deltarho,deltaz);
	double A1 = ScalarPotential(rho,z,r1,mui2,D,deltarho,deltaz);

	/* according to Edwards et al., 2001 the flux is simply
	rho times the scalar potential */
	double F = rho*(A0 - A1);

	return F;
}

/***************************************************************
*
*   NAME : FluxDip(r,theta,g)
*
*   DESCRIPTION : Calculate the flux cfunction for a dipole
*
*   INPUTS : 
*       double  r 		radial coordinate, Rj
*       double  theta   Colatitude, Rads
*       double  g		Magnetic dipole coefficient, nT
*
***************************************************************/
double FluxDip(double r, double theta, double g) {

	double sint = sin(theta);
	double F = (g*sint*sint)/r;
	return F;
}



template <typename T> T sgn(T x) {
	return (x > 0) - (x < 0);
}

extern "C" {
}


extern "C" {
}
#endif
#endif
