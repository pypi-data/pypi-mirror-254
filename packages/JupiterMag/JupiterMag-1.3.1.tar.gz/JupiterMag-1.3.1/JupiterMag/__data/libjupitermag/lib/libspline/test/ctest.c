#include <stdio.h>
#include "../include/spline.h"

int main() {

	/* create arrays of x and y values*/
	double x[] = {-5.0,-4.0,-3.0,-2.0,-1.0,1.0,2.0,3.0,4.0,5.0};
	double y[10];
	int n = 10;
	int i;
	for (i=0;i<n;i++) {
		y[i] = pow(x[i],3.0);
	}

	/* print the arrays */
	printf("x = [");
	for (i=0;i<n;i++) {
		printf(" %4.1f",x[i]);
		if (i != n-1) {
			printf(",");
		}
	}
	printf("]\n");

	printf("y = [");
	for (i=0;i<n;i++) {
		printf(" %4.1f",y[i]);
		if (i != n-1) {
			printf(",");
		}
	}
	printf("]\n");


	/* create test position and interpolate */
	double xt, yt;
	xt = 0.0;
	spline(n,x,y,1,&xt,&yt);
	printf("y = %3.1f at x = %3.1f\n",yt,xt);


}


