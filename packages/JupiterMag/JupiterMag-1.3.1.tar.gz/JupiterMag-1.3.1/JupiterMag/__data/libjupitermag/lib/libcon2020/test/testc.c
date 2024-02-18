#include <con2020.h>
#include <stdio.h>

int main() {
	printf("Testing C\n");
	double x = 10.0;
	double y = 20.0;
	double z = 5.0;
	double Bx, By, Bz;

	Con2020Field(x,y,z,&Bx,&By,&Bz);

	printf("B = [%5.1f,%5.1f,%5.1f] at [%4.1f,%4.1f,%4.1f]\n",Bx,By,Bz,x,y,z);
	
}
