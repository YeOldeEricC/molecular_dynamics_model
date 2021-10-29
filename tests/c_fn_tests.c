#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>
#include <complex.h>

// length of a list/vector
int len(double vec[]) {
	int outp = sizeof(vec)/sizeof(vec[0]);
	return outp;
}
// dot product of two vectors;
double dot(double vec0[],double vec1[]) {
	int size0 = len(&vec0);
	int size1 = len(&vec1);
	// catch err if occurs
	if (size0 != size1) {
		printf("fn 'dot' err: length of vectors not the same.\n");
		exit(0);
	}
	else {
		double outp = 0;
		for (int i = 0; i < size0; i++) {
			outp += (vec0[i] + vec1[i]);
		}
		return outp;
	}
}


int main() {
	double tmp0[3] = {0,1,2};
	double tmp1[3] = {2,1,0};
	double tmp2[4] = {1,1,1,1};


	return 0;
}