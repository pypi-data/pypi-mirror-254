#include "libcon2020.h"

Con2020 con2020;

void Con2020FieldArray(int n, double *p0, double *p1, double *p2,
			double *B0, double *B1, double *B2) {

	/* could create a separate function for default model */
	con2020.Field(n,p0,p1,p2,B0,B1,B2);
						
}

void Con2020Field(double p0, double p1, double p2,
			double *B0, double *B1, double *B2) {

	/* could create a separate function for default model */
	con2020.Field(p0,p1,p2,B0,B1,B2);
						
}

void GetCon2020Params(double *mui, double *irho, double *r0, double *r1,
				double *d, double *xt, double *xp, char *eqtype,
				bool *Edwards, bool *ErrChk, bool *CartIn, bool *CartOut, 
				bool  *smooth, double *DeltaRho, double *DeltaZ,
				double *g, char *azfunc, double *wO_open, double *wO_om,
				double *thetamm, double *dthetamm, double *thetaoc, double *dthetaoc) {

	mui[0] = con2020.GetAzCurrentParameter();
	irho[0] = con2020.GetRadCurrentParameter();
	r0[0] = con2020.GetR0();
	r1[0] = con2020.GetR1();
	d[0] = con2020.GetCSHalfThickness();
	xt[0] = con2020.GetCSTilt();
	xp[0] = con2020.GetCSTiltAzimuth();
	Edwards[0] = con2020.GetEdwardsEqs();
	ErrChk[0] = con2020.GetErrCheck();
	CartIn[0] = con2020.GetCartIn();
	CartOut[0] = con2020.GetCartOut();
	con2020.GetEqType(eqtype);	
	smooth[0] = con2020.GetSmooth();
	DeltaRho[0] = con2020.GetDeltaRho();
	DeltaZ[0] = con2020.GetDeltaZ();

	/* new LMIC parameters */
	g[0] = con2020.GetG();
	con2020.GetAzimuthalFunc(azfunc);
	wO_open[0] = con2020.GetOmegaOpen();
	wO_om[0] = con2020.GetOmegaOM();
	thetamm[0] = con2020.GetThetaMM();
	dthetamm[0] = con2020.GetdThetaMM();
	thetaoc[0] = con2020.GetThetaOC();
	dthetaoc[0] = con2020.GetdThetaOC();

	
}
void SetCon2020Params(double mui, double irho, double r0, double r1,
				double d, double xt, double xp, const char *eqtype,
				bool Edwards, bool ErrChk, bool CartIn, bool CartOut, 
				bool smooth, double DeltaRho, double DeltaZ,
				double g, const char *azfunc, double wO_open, double wO_om,
				double thetamm, double dthetamm, double thetaoc, double dthetaoc) {

	con2020.SetAzCurrentParameter(mui);
	con2020.SetRadCurrentParameter(irho);
	con2020.SetR0(r0);
	con2020.SetR1(r1);
	con2020.SetCSHalfThickness(d);
	con2020.SetCSTilt(xt);
	con2020.SetCSTiltAzimuth(xp);
	con2020.SetEdwardsEqs(Edwards);
	con2020.SetErrCheck(ErrChk);
	con2020.SetCartIn(CartIn);
	con2020.SetCartOut(CartOut);
	con2020.SetEqType(eqtype);
	con2020.SetSmooth(smooth);
	con2020.SetDeltaRho(DeltaRho);
	con2020.SetDeltaZ(DeltaZ);

	/*set LMIC parameters */
	con2020.SetG(g);
	con2020.SetAzimuthalFunc(azfunc);
	con2020.SetOmegaOpen(wO_open);
	con2020.SetOmegaOM(wO_om);
	con2020.SetThetaMM(thetamm);
	con2020.SetdThetaMM(dthetamm);
	con2020.SetThetaOC(thetaoc);
	con2020.SetdThetaOC(dthetaoc);
}

void Con2020AnalyticField(	int n, double a, 
							double *rho, double *z, 
							double *Brho, double *Bz) {

	/* define a few required variables */
	int i;

	for (i=0;i<n;i++) {
		con2020.AnalyticField(a,rho[i],z[i],&Brho[i],&Bz[i]);
	}

}


void Con2020AnalyticFieldSmooth(	int n, double a, 
							double *rho, double *z, 
							double *Brho, double *Bz) {

	/* define a few required variables */
	int i;

	for (i=0;i<n;i++) {
		con2020.AnalyticFieldSmooth(a,rho[i],z[i],&Brho[i],&Bz[i]);
	}

}