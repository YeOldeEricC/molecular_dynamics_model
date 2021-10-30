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

double dot(double *v0, double *v1) {
	double outp = 0;
	for (int i = 0; i < 3; i++) {
		outp += (v0[i]*v1[i]);
	}
	return outp;
}

void add_vec(double *v0, double *v1, double *result) {
	for (int i = 0; i < 3; i++) {
		result[i] = (v0[i] + v1[i]);
	}
}

double line_comp(double t, double m, double d) {
	return (m*t) - d;
}

int main() {
	printf("\n");
	// knowing that I am only working with 3 dim vectors...
	// use that assumption for the creation of functions.

	// grad of line components


	double dot_prod = dot(vec0,vec1);
	add_vec(vec0,vec1,res);

	printf("dot prod: %f\n",dot_prod);
	printf("vec add: [%f,%f,%f]\n",res[0],res[1],res[2]);


	printf("\n");
	return 0;
}

////////////////////////////////////////////////////////////////////////////////
// scraps
/*

len of vec
int len = sizeof(vec)/sizeof(vec[0]);

*/