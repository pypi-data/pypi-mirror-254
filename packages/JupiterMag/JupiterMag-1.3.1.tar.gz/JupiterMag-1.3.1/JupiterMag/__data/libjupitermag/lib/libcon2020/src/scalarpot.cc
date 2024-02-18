#include "scalarpot.h"

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
                                double mui2, double D) {
    
    double a2 = a*a;
    double zpd = z + D;
    double zmd = z - D;
    double zpd2 = zpd*zpd;
    double zmd2 = zmd*zmd;
    double zpda = sqrt(zpd2 + a2);
    double zmda = sqrt(zmd2 + a2);
    double zpda3 = zpda*zpda*zpda;
    double zmda3 = zmda*zmda*zmda;

    double term0 = (rho/2.0)*log((zpd + zpda)/(zmd + zmda));
    double term1 = (rho*rho*rho/16.0)*(zpd/zpda3 - zmd/zmda3);

    double A = mui2*(term0 + term1);
    return A;

}



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
                                double mui2, double D, double deltaz) {
    
    double a2 = a*a;
    double rho2 = rho*rho;
    double zpd = z + D;
    double zmd = z - D;
    double zpd2 = zpd*zpd;
    double zmd2 = zmd*zmd;
    double zpdr = sqrt(zpd2 + rho2);
    double zmdr = sqrt(zmd2 + rho2);


	double term0 = (1/(2*rho))*(zpd*zpdr - zmd*zmdr);
	double term1 = (rho/2)*log((zpd + zpdr)/(zmd + zmdr));
	double term2 = (a2/(4*rho))*(zmd/zmdr - zpd/zpdr);

    /* the final term should actually be a case statement, but this is
    Stan's smooth version*/
	double zpddz = zpd/deltaz;
	double zmddz = zmd/deltaz;
	double tanpd = tanh(zpddz);
	double tanmd = tanh(zmddz);
	double term3 = (-1/rho)*(D*z*(tanpd + tanmd) + 0.5*(D*D + z*z)*(tanpd - tanmd));

    double A = mui2*(term0 + term1 + term2 + term3);
    return A;

}

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
                                double deltarho, double deltaz) {

    double As = ScalarPotentialSmallRho(rho,z,a,mui2,D);
    double Al = ScalarPotentialLargeRho(rho,z,a,mui2,D,deltaz);

    double tanhradr = tanh((rho - a)/deltarho);

    /* another of Stan's smoothing functions */
    double A = 0.5*As*(1 - tanhradr) + 0.5*Al*(1 + tanhradr);

    return A;
}