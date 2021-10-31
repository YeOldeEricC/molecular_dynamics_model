// codes for comments
/*
	WAI - works as intended
*/

// includes
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
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
// calc single xyz comp of a line
double line_comp(double t, double m, double d) {
	return (m*t) - d;
}
// calc all comps at once
void line_comps(double complex t, double *m, double *d, double complex *result) {
	result[0] = (m[0]*t) - d[0]; // x
	result[1] = (m[1]*t) - d[1]; // y
	result[2] = (m[2]*t) - d[2]; // z
}
// find the vals of t where the line intersects a sphere
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
	double disc = D_phi(pa,pb,pc);
	double complex sqrt_D = csqrt(disc);
	t_out[0] = (pb-sqrt_D)/pa;
	t_out[1] = (pb+sqrt_D)/pa;
}
// distance between two vectors
double dist(double complex *x0, double complex *x1) {
	int i;
	double outp,tmp;
	if (cimag(x0[0]) != 0) {
		outp = 0;
	}
	else {
		double outp_sq = 0;
		for (i = 0; i < 3; i++) {
			tmp = creal(x1[i]) - creal(x0[i]);
			outp_sq += pow(tmp,2);
		}
		outp = sqrt(outp_sq);
	}
	return outp;
}

int main() {
	printf("\n");
	// knowing that I am only working with 3 dim vectors...
	// use that assumption for the creation of functions.

	// grad of line components
	double mx = 0.5;
	double my = 0.5;
	double mz = -0.5;
	double m[3] = {mx,my,mz};
	// line component offsets
	double dx = -0.5;
	double dy = 0.5;
	double dz = -0.5;
	double d[3] = {dx,dy,dz};
	// sphere params, orig & radius
	double ox = 0.5;
	double oy = 0.5;
	double oz = -0.5;
	double o[3] = {ox,oy,oz};
	
	double complex t_ints[2];
	double complex pt0[3];
	double complex pt1[3];
	double dist01;
	double r=0;

	//double r = 0.02; // radius
	for (int i = 0; i < 10000; i++) {
		r += 0.025;
		t_intersects(m,d,o,r,t_ints);
		line_comps(t_ints[0],m,d,pt0);
		line_comps(t_ints[1],m,d,pt1);
		dist01 = dist(pt0,pt1);
		printf("%d %f %f\n",i,r,dist01);
	}

	//printf("t parts: t0=%+f%+fi, t1=%+f%+fi\n",creal(t_ints[0]),cimag(t_ints[0]),creal(t_ints[1]),cimag(t_ints[1]));	
	//printf("\n");
	//printf("x0=%+f%+fi\ny0=%+f%+fi\nz0=%+f%+fi\n",creal(pt0[0]),cimag(pt0[0]),creal(pt0[1]),cimag(pt0[1]),creal(pt0[2]),cimag(pt0[2]));
	//printf("\n");
	//printf("x1=%+f%+fi\ny1=%+f%+fi\nz1=%+f%+fi\n",creal(pt1[0]),cimag(pt1[0]),creal(pt1[1]),cimag(pt1[1]),creal(pt1[2]),cimag(pt1[2]));
	//printf("\n");

	printf("\n");
	return 0;
}

////////////////////////////////////////////////////////////////////////////////
// scraps
/*

len of vec
int len = sizeof(vec)/sizeof(vec[0]);

*/