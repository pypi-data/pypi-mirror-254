# libspline

Simple spline library in C++

## Install

In Linux and Mac, run

```bash
make

sudo make install
```

Under windows, run the batch file:

```powershell
.\compile.bat
```

## Usage

This package includes a header which is compatible with both C andC++ (`spline.c`). Below are two very simple examples of how to use this code.

### C++

This is a C++ example:

```cpp
/* contents of cppexample.cc */
#include <stdio.h>
#include <spline.h>

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

	/* load the spline object */
	Spline s(n,x,y);

	/* create test position and interpolate */
	double xt, yt;
	xt = 0.0;
	s.Interpolate(1,&xt,&yt);
	printf("y = %3.1f at x = %3.1f\n",yt,xt);


}

```

which can be compiled then run using

```bash
g++ cppexample.cc -o cppexample -lspline
./compile
```
### C

This is a C example, which would work in C++ also. The `spline()` wrapper function can also be linked to other languages.

```c
/* contents of cexample.c */
#include <stdio.h>
#include <spline.h>

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

```
To compile and run:
```bash
gcc cexample.c -o cexample -lm -lspline
./cexample
```