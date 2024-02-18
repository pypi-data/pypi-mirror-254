
#ifndef __LIBSPLINE_H__
#define __LIBSPLINE_H__

#define _USE_MATH_DEFINES
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#define LIBSPLINE_VERSION_MAJOR 0
#define LIBSPLINE_VERSION_MINOR 2
#define LIBSPLINE_VERSION_PATCH 0

#ifdef __cplusplus
extern "C" {
#endif
	void spline(int n0, double *x0, double *y0, 
				int n1, double *x1, double *y1);
#ifdef __cplusplus
}


extern "C" {
}


class Spline {
	public:
		Spline(int,double*,double*);
		Spline(const Spline &);
		~Spline();
		void Interpolate(int,double*,double*);
	
		int n_;
		double *a_, *b_, *c_, *d_;
		double *x_, *y_;
		bool del_;
};
#endif
#endif
