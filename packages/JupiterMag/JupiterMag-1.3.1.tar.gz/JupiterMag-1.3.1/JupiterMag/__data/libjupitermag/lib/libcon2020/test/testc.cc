#include <con2020.h>
#include <stdio.h>
#define _USE_MATH_DEFINES
#include <math.h>

int main() {
	printf("Testing C++\n");
	double x = 10.0;
	double y = 20.0;
	double z = 5.0;
	double Bx, By, Bz;

	Con2020Field(x,y,z,&Bx,&By,&Bz);

	printf("B = [%5.1f,%5.1f,%5.1f] at [%4.1f,%4.1f,%4.1f]\n",Bx,By,Bz,x,y,z);

	double thetamm, dthetamm, thetaoc, dthetaoc;
	thetamm = con2020.GetThetaMM();
	dthetamm = con2020.GetdThetaMM();
	thetaoc = con2020.GetThetaOC();
	dthetaoc = con2020.GetdThetaOC();
	printf("thetamm = %f\n",thetamm);
	printf("dthetamm = %f\n",dthetamm);
	printf("thetaoc = %f\n",thetaoc);
	printf("dthetaoc = %f\n",dthetaoc);

	thetamm = con2020.GetThetaMM();
	dthetamm = con2020.GetdThetaMM();
	thetaoc = con2020.GetThetaOC();
	dthetaoc = con2020.GetdThetaOC();
	printf("thetamm = %f\n",thetamm);
	printf("dthetamm = %f\n",dthetamm);
	printf("thetaoc = %f\n",thetaoc);
	printf("dthetaoc = %f\n",dthetaoc);

	/* test field output at R = 0.0 */

	Con2020Field(0.0,0.0,0.0,&Bx,&By,&Bz);
	printf("Testing R = 0: \n");
	printf("B = [%5.1f,%5.1f,%5.1f] at [%4.1f,%4.1f,%4.1f]\n",Bx,By,Bz,0.0,0.0,0.0);

	printf("Testing rho = 0.0; z = 5.0\n");
	double Brho, Bphi;
	Con2020 obj;
	(obj.*obj._Model)(0.0,5.0,5.0,&Brho,&Bphi,&Bz);

	printf("Brho,Bphi,Bz = [%5.1f,%5.1f,%5.1f]\n",Brho,Bphi,Bz);

}
