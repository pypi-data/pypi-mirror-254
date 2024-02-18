#include "lmic.h"


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
double f_thetai(double thetai) {

	double tanti = tan(thetai);
	return 1.0 + 0.25*tanti*tanti;
}

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
					double thetaoc, double dthetaoc) {

	double term1 = 0.5*(wO_om - wO_open)*(1.0 + tanh((thetai - thetaoc)/dthetaoc));
	double term2 = 0.5*(1.0 - wO_om)*(1.0 + tanh((thetai - thetamm)/dthetamm));
	
	double wO = wO_open + term1 + term2;

	return wO;
}

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
					double thetaoc, double dthetaoc ) {

	/* height intergrated conductivity*/
	double SigmaP = 0.25;

	/* ionospheric radius (m)*/
	double Ri = 67350000.0;

	/* equatorial radius (m)*/
	double Rj = 71492000.0;
	
	/* magnetic field at thetai */
	double B = abs(2.0* g*cos(thetai)*pow(Rj/Ri,3.0))*1e-9;

	/* calculate rhoi */
	double rhoi = Ri*sin(thetai);

	/* get domega*/
	double wO = OmegaRatio(thetai,wO_open,wO_om,thetamm,dthetamm,thetaoc,dthetaoc);
	double OmegaJ = 1.758e-4;
	double domega = OmegaJ*(1 - wO);

	/* ftheta*/
	double ft = f_thetai(thetai);

	/* the current */
	double Ihp = 2.0*M_PI*SigmaP*rhoi*rhoi*domega*B*ft;

	return Ihp;
}

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
						double deltarho, double deltaz) {
	
	/* calculate cylindrical coords*/
	double rho = r*sin(theta);
	double z = r*cos(theta);

	/* get the CAN flux */
	double Fcan = FluxCan(rho,z,r0,r1,mui2,D,deltarho,deltaz);
	
	/* dipole flux */
	double Fdip = FluxDip(r,theta,g);

	/* ionospheric radius (m)*/
	double Ri = 67350000.0;

	/* equatorial radius (m)*/
	double Rj = 71492000.0;

	/* theta ionosphere, yay! */
	double thetai = asin(sqrt((Ri/Rj)*(Fcan + Fdip)/g));	

	return thetai;
}

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
double BphiLMIC(double r, double theta, double g,
						double r0, double r1,
						double mui2, double D, 
						double deltarho, double deltaz,
						double wO_open, double wO_om,
						double thetamm, double dthetamm,
						double thetaoc, double dthetaoc ) {

	/* ionospheric latitude */
	double thetai = ThetaIonosphere(r,theta,g,r0,r1,mui2,D,deltarho,deltaz);

	/* sign of the latitude */
	double slat = sgn(M_PI/2 - theta);

	/* Pedersen Current */
	double IhP = PedersenCurrent(thetai,g,wO_open,wO_om,thetamm,
								dthetamm,thetaoc,dthetaoc);

	/* constants */
	double Rj = 71492000.0;
	double mu0 = 4*M_PI*1e-7;

	/* rho (m)*/
	double rho = r*sin(theta)*Rj;

	/* calculate Bphi */
	double Bphi = (-slat*mu0*IhP)/(2*M_PI*rho);

	return Bphi*1e9;

}


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
						double thetaoc, double dthetaoc ) {


	/* sign of the latitude */
	double slat = sgn(M_PI/2 - thetai);

	/* Pedersen Current */
	double IhP = PedersenCurrent(thetai,g,wO_open,wO_om,thetamm,
								dthetamm,thetaoc,dthetaoc);

	/* constants */
	double Ri = 67350000.0;
	double mu0 = 4*M_PI*1e-7;

	/* rho (m)*/
	double rho = Ri*sin(thetai);

	/* calculate Bphi */
	double Bphi = (-slat*mu0*IhP)/(2*M_PI*rho);

	return Bphi*1e9;

}