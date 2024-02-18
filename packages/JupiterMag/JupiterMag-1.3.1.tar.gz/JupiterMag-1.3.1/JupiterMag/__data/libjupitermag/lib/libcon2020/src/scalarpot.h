#ifndef __SCALARPOT_H__
#define __SCALARPOT_H__
#include <stdio.h>
#include <stdlib.h>
#define _USE_MATH_DEFINES
#include <math.h>

extern "C" {

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

}

#endif
