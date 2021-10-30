// codes for comments
/*
	WAI - works as intended
*/

// includes
#include <stdio.h>
#include <stdlib.h>
#include <tgmath.h>
#include <string.h>
#include <complex.h>
// dot product of two vectors
double dot(double *v0, double *v1) {
	double outp = 0;
	for (int i = 0; i < 3; i++) {
		outp += (v0[i]*v1[i]);
	}
	return outp;
}
// add two vectors
void add(double *v0, double *v1, double *result) {
	for (int i = 0; i < 3; i++) {
		result[i] = (v0[i] + v1[i]);
	}
}
// discriminant for my phi version of quadratics
double D_phi(double a, double b, double c) {
	return pow(b,2) - (a*c);
}
// calc xyz comps of a line
double line_comp(double t, double m, double d) {
	return (m*t) - d;
}

void t_intersects(double *m, double *d, double *o, double r, double complex *t_out) {
	// phi_a
	double pa = dot(m,m);
	// phi_b
	double dpo[3];
	add(d,o,dpo);
	double pb = dot(m,dpo);
	// phi_c
	double pc = dot(d,d) + dot(o,o) + (2*dot(d,o)) - pow(r,2);
	// discriminant

}

int main() {
	printf("\n");
	// knowing that I am only working with 3 dim vectors...
	// use that assumption for the creation of functions.

	// grad of line components
	double mx = 0.05;
	double my = 0;
	double mz = -0.05;
	double m[3] = {mx,my,mz};
	// line component offsets
	double dx = -0.1;
	double dy = 0.05;
	double dz = -0.05;
	double d[3] = {dx,dy,dz};
	// sphere params, orig & radius
	double ox = 0.5;
	double oy = 0.25;
	double oz = -0.25;
	double o[3] = {ox,oy,oz};
	double r = 1; // radius

	double complex t_ints[2];



	printf("\n");
	return 0;
}

////////////////////////////////////////////////////////////////////////////////
// scraps
/*

len of vec
int len = sizeof(vec)/sizeof(vec[0]);

*/