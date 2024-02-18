#include <stdio.h>
#include <con2020.h>

int main () {
	/* create an instance of the model */
	Con2020 model;

	/* set coordinate system to be Cartesian SIII (default) */
	model.SetCartIn(true);
	model.SetCartOut(true);

	/* create some variables to stor a field vector in,
	 * note that positions are in units of Rj */
	double x = 11.0;
	double y = 5.0;
	double z = -10.0;
	double Bx, By, Bz;

	/* call the model */
	model.Field(x,y,z,&Bx,&By,&Bz);
	printf("B=[%5.1f,%5.1f,%5.1f] nT at [%4.1f,%4.1f,%4.1f] Rj\n",Bx,By,Bz,x,y,z);

	/* alternatively obtain an array of field vectors in spherical polar coords */
	model.SetCartIn(false);
	model.SetCartOut(false);
	double r[] = {5.0,10.0,15.0};
	double theta[] = {1.0,1.5,2.0};
	double phi[] = {0.0,0.1,0.2};
	double Br[3], Bt[3], Bp[3];

	model.Field(3,r,theta,phi,Br,Bt,Bp);
	int i;
	for (i=0;i<3;i++) {
		printf("B=[%5.1f,%5.1f,%5.1f] nT at r = %4.1f Rj, theta = %4.1f rad, phi = %4.1f rad\n",Br[i],Bt[i],Bp[i],r[i],theta[i],phi[i]);
	}
	
	return 0;
}