import os;
import sys;
import time;
import math as ma;
import cmath as cma;
import numpy as np;
from matplotlib import pyplot as plt;


lib_notes = '''
---     NOTES     ---\n
This file will end up being the main library of functions that will be used\n
in the main program files. For all the mathematical functions, complex\n
numbers will the main port of numerical dealings.\n
\n
All functions listed below are the ones fully finished and thus usable.\n
\n
--- FUNCTION LIST ---\n
 --    RELABEL    --\n
sin(val) - returns sin of val\n
asin(val) - returns arcsin of val\n
\n
cos(val) - returns cos of val\n
acos(val) - returns arccos of val\n
\n
tan(val) - returns tan of val\n
atan(val) - returns arctan of val\n
\n
sqrt(val) - returns sqrt of val\n
shape(arr) - returns the shape of an arr\n
\n
 --    CUSTOMS    --\n
vec_check(v_list) - check if all vecs are the same length\n
vec3_check(v_list) - check if list only contains 3D vectors\n
det_2x2(m) - returns the determinant of a 2x2 matrix\n
vec_mult(const,v) - multiplies vec by a constant\n
vec_add(v0,v1) - adds two vectors element-wise\n
vec_min(v0,v1) - subtracts first inp vec from the second element-wise\n
vec_dot(v0,v1) - returns dot product of two vectors\n
vec_cross(v0,v1) - returns cross product between two vectors\n
vec_dot2(v0) - returns my sq dot notation (dot vec with itself)\n
vec_dotL(v_list) - returns dot product of a set of vectors (my notation)\n
\n
 --     PLOTS     --\n
 --     DEBUG     --\n
 notes(lib_notes) - print this output\n
\n
'''

#--    RELABEL    --#
def sin(x) : return cma.sin(x);
def asin(x) : return cma.asin(x);

def cos(x) : return cma.cos(x);
def acos(x) : return cma.acos(x);

def tan(x) : return cma.tan(x);
def atan(x) : return cma.atan(x);

def sqrt(x) : return cma.sqrt(x);
# returns the shape of array as python list
def shape(arr) : return [i for i in np.asarray(arr).shape];

#--    CUSTOMS    --#
def vec_check(v_list) :
	lens = {};
	lens.add(len(v_list[0]));
	for v in v_list :
		v_len = len(v);
		lens.add(v_len);
		if v_len not in lens :
			return -1;
	return 1;

def vec3_check(v_list) :
	for v in v_list :
		if len(v) != 3 :
			return -1;
	return 1;

def vec_mult(const,v) :
	v_len = len(v);
	i_list = range(0,v_len);
	return [const*v[i] for i in i_list];

def vec_add(v0,v1) :
	if vec_check([v0,v1]) == -1 :
		exit('VEC_ADD ERR - vector lengths not equal.');
	else :
		v_len = len(v0);
		i_list = range(0,v_len);
		return [v0[i] + v1[i] for i in i_list];

def vec_min(v0,v1) :
	if vec_check([v0,v1]) == -1 :
		exit('VEC_MIN ERR - vector lengths not equal.');
	else :
		v_len = len(v0);
		i_list = range(0,v_len);
		return [v1[i] - v0[i] for i in i_list];
		
def vec_dot(v0,v1) :
	if vec_check([v0,v1]) == -1 :
		exit('VEC_DOT ERR - vector lengths not equal.');
	else :
		v_len = len(v0);
		i_list = range(0,v_len);
		return sum([v0[i]*v1[i] for i in i_list]);

def vec_dot2(v) :
	v_len = len(v0);
	i_list = range(0,v_len);
	return sum([v[i]*v[i] for i in i_list]);

def vec_dotL(v_list) :
	if vec_check(v_list) == -1 :
		exit('VEC_DOT2 ERR - vector lengths not equal.');
	else :
		v_len = len(v_list[0]);
		n_list = len(v_list);
		i_list = range(0,v_len);
		outp = 0;
		for i in i_list :
			tmp = 1;
			for n in n_list :
				tmp *= v_list[n][i];
			outp += tmp;
		return outp;

def det_2x2(m) :
	if shape(m) != [2,2] :
		exit('DET_2X2 ERR - non 2x2 matrix input.');
	else :
		return ((m[0][0]*m[1][1]) - (m[0][1]*m[1][0]));

def vec_cross(v0,v1) :
	if vec3_check([v0,v1]) == -1 :
		exit('VEC_CROSS ERR - not all vectors are 3D.');
	else :
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


#--     PLOTS     --#

#--     DEBUG     --#
def notes() : print(lib_notes);