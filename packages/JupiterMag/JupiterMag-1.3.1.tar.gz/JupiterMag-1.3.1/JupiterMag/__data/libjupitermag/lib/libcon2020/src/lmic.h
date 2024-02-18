#ifndef __LMIC_H__
#define __LMIC_H__
#include <stdio.h>
#include <stdlib.h>
#include "flux.h"
#include "sgn.h"
#define _USE_MATH_DEFINES
#include <math.h>
#ifndef M_PI
#define M_PI		3.14159265358979323846
#endif

extern "C" {
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
}
#endif
