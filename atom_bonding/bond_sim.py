import math as ma;
import numpy as np;
import cmath as cma;
import time,os,sys;
from matplotlib import pyplot as plt;

# atomic radii
atom_rad0 = 1;
elec_neg0 = 1;

atom_rad1 = 1;
elec_neg1 = 1;
# num of electrons involved in the covalent bond
electrons_shared = 1;

## Functions - Whether relabels or completely custom

# re-labelling maths functions
def sqrt(x) : return cma.sqrt(x);
def sin(x) : return cma.sin(x);
def cos(x) : return cma.cos(x);
def tan(x) : return cma.tan(x);
def pow(x,n) : return x**n;

# all vectors will be three-vectors as will be working in xyz

# determinant of a 2x2 matrix
def det(m) : return ((m[0][0]*m[1][1]) - (m[0][1]*m[1][0]));
# length/distance between two xyz points
def pnt_dist(ri,rj) : return sqrt(sum([pow((rj[i]-ri[i]),2) for i in [0,1,2]]));
# add second vector to the first
def vec_add(ri,rj) : return [ri[i] + rj[i] for i in [0,1,2]];
# minus the first vector from the second element-wise
def vec_minus(ri,rj) : return [rj[i] - ri[i] for i in [0,1,2]];
# multiply a vector by a constant
def vec_mult(r,n) : return [n*r[i] for i in [0,1,2]];
# dot product of two vectors
def vec_dot(ri,rj) : return sum([(ri[i]*rj[i]) for i in [0,1,2]]);
# cross product of two vectors
def vec_cross(ri,rj) :
	m0 = [	[ri[1],ri[2]],
			[rj[1],rj[2]]];
	d0 = det(m0);

	m1 = [	[ri[0],ri[2]],
			[rj[0],rj[2]]];
	d1 = det(m1);

	m2 = [	[ri[0],ri[1]],
			[rj[0],rj[1]]];
	d2 = det(m2);

	return [d0,-d1,d2];
# Coulomb force vector output
def Coulomb_F(ri,rj,qi,qj,kq) : return [(kq*qi*qj)*((rj[i] - ri[i])/pow(pnt_dist(ri,rj),3)) for i in [0,1,2]];
# Gravitational force vector output
def Gravity_F(ri,rj,Mi,Mj,kG) : return [(kG*Mi*Mj)*((rj[i] - ri[i])/pow(pnt_dist(ri,rj),3)) for i in [0,1,2]];
# Lorentz force vector output
def Lorentz_F(qi,vi,vj,Ej,Bj) :
	# F = q(E + [v x B])
	relative_v = vec_minus(vj,vi);
	vxB = vec_cross(relative_v,Bj);
	in_brackets = vec_add(Ej,vxB);
	return vec_mult(in_brackets,qi);
# whatever other force is there.