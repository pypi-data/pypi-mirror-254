#include "flux.h"

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