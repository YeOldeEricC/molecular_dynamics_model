import os;
import sys;
import time;
import math as ma;
import cmath as cma;
import numpy as np;
from matplotlib import pyplot as plt;

###
'''
-- IN CODE NOTES --
if function or marked with one of the following symbols, it means:
	#- mtw -#	=>	made, tested, working
	#- msw -#	=>	made, should work
	#- mnt -#	=>	made, not tested
	#- mnw -#	=>	made, not working
	#- nmy -#	=>	not made yet
	#- 

-- ROUGH LETTER KEY --
m - made
n - not
t - tested
y - yet
w - work / working
s - should
'''
###

LIB_NOTES = '''
--- GENERAL FUNCTION LIBRARY ---

---     NOTES     ---
All functions listed below are the ones fully finished
and thus should be usable.

--- FUNCTION LIST ---
 --    RELABEL    --
sin(val) - returns sin of val
asin(val) - returns arcsin of val
cos(val) - returns cos of val
acos(val) - returns arccos of val
tan(val) - returns tan of val
atan(val) - returns arctan of val
sqrt(val) - returns sqrt of val

c_sin(val) - returns complex result for sin of val
c_asin(val) - returns complex result for arcsin of val
c_cos(val) - returns complex result for cos of val
c_acos(val) - returns complex result for arccos of val
c_tan(val) - returns complex result for tan of val
c_atan(val) - returns complex result for arctan of val
c_sqrt(val) - returns complex result for sqrt of val

shape(arr) - returns the shape of an arr
pow(val,n) - returns value raised to power 'n'

 --    CUSTOMS    --
  -    VECTORS    -
vec_check(v_list) - check if all vecs are the same length
vec3_check(v_list) - check if list only contains 3D vectors
det_2x2(m) - returns the determinant of a 2x2 matrix
vec_mult(const,v) - multiplies vec by a constant
vec_add(v0,v1) - adds two vectors element-wise
vec_sub(v0,v1) - subtracts first inp vec from the second element-wise
vec_dot(v0,v1) - returns dot product of two vectors
vec_cross(v0,v1) - returns cross product between two vectors
vec_dot2(v0) - returns my sq dot notation (dot vec with itself)
vec_dotL(v_list) - returns dot product of a list of vectors (my notation)
vec_dist(v0,v1) - returns the distance between two vectors
c_vec_dist(v0,v1) - returns complex valued distance between two vectors

 --     PLOTS     --

 --     DEBUG     --
notes() - print this output

'''

#---   GENERAL   ---#
#--    RELABEL    --#
#-     REAL FN     -#
#- mtw -#
def sin(x) : return ma.sin(x);
#- mtw -#
def asin(x) : return ma.asin(x);
#- mtw -#
def cos(x) : return ma.cos(x);
#- mtw -#
def acos(x) : return ma.acos(x);
#- mtw -#
def tan(x) : return ma.tan(x);
#- mtw -#
def atan(x) : return ma.atan(x);
#- mtw -#
def sqrt(x) : return ma.sqrt(x);

#-     COMP FN     -#
#- mtw -#
def c_sin(x) : return cma.sin(x);
#- mtw -#
def c_asin(x) : return cma.asin(x);
#- mtw -#
def c_cos(x) : return cma.cos(x);
#- mtw -#
def c_acos(x) : return cma.acos(x);
#- mtw -#
def c_tan(x) : return cma.tan(x);
#- mtw -#
def c_atan(x) : return cma.atan(x);
#- mtw -#
def c_sqrt(x) : return cma.sqrt(x);

#-      OTHER      -#
def pow(x,n) : return x**n;
# returns the shape of array as python list
def shape(arr) : 
	np_shp = np.asarray(arr).shape;
	py_shp = [i for i in np_shp];
	return py_shp;

#--    CUSTOMS    --#
#-     VECTORS     -#
#- mtw -#
def vec_check(v_list) :
	lens = set();
	lens.add(len(v_list[0]));
	for v in v_list :
		v_len = len(v);
		if v_len not in lens :
			return -1;
		else :
			lens.add(v_len);

	return 1;
#- mtw -#
def vec3_check(v_list) :
	for v in v_list :
		if len(v) != 3 :
			return -1;
	return 1;
#- mtw -#
def vec_mult(const,v) :
	v_len = len(v);
	i_list = range(0,v_len);
	return [const*v[i] for i in i_list];
#- mtw -#
def vec_add(v0,v1) :
	if vec_check([v0,v1]) == -1 :
		exit('VEC_ADD ERR - vector lengths not equal.');
	else :
		v_len = len(v0);
		i_list = range(0,v_len);
		return [v0[i] + v1[i] for i in i_list];
#- mtw -#
def vec_sub(v0,v1) :
	if vec_check([v0,v1]) == -1 :
		exit('VEC_MIN ERR - vector lengths not equal.');
	else :
		v_len = len(v0);
		i_list = range(0,v_len);
		return [v1[i] - v0[i] for i in i_list];
#- mtw -#
def vec_dot(v0,v1) :
	if vec_check([v0,v1]) == -1 :
		exit('VEC_DOT ERR - vector lengths not equal.');
	else :
		v_len = len(v0);
		i_list = range(0,v_len);
		return sum([v0[i]*v1[i] for i in i_list]);
#- mtw -#
def vec_dot2(v) :
	v_len = len(v);
	i_list = range(0,v_len);
	return sum([v[i]*v[i] for i in i_list]);
#- mtw -#
def vec_dotL(v_list) :
	if vec_check(v_list) == -1 :
		exit('VEC_DOT2 ERR - vector lengths not equal.');
	else :
		v_len = len(v_list[0]);
		list_len = len(v_list)
		n_list = range(0,list_len);
		i_list = range(0,v_len);
		outp = 0;
		for i in i_list :
			tmp = 1;
			for n in n_list :
				tmp *= v_list[n][i];
			outp += tmp;
		return outp;
#- mtw -#
def det_2x2(m) :
	if shape(m) != [2,2] :
		exit('DET_2X2 ERR - non 2x2 matrix input.');
	else :
		return ((m[0][0]*m[1][1]) - (m[0][1]*m[1][0]));
#- mtw -#
def vec_cross(v0,v1) :
	if vec3_check([v0,v1]) == -1 :
		exit('VEC_CROSS ERR - not all vectors are 3D.');
	else :
		m0 = [	[v0[1],v0[2]],
				[v1[1],v1[2]]];
		d0 = det_2x2(m0);

		m1 = [	[v0[0],v0[2]],
				[v1[0],v1[2]]];
		d1 = det_2x2(m1);

		m2 = [	[v0[0],v0[1]],
				[v1[0],v1[1]]];
		d2 = det_2x2(m2);

		return [d0,-d1,d2];
#- mtw -#
def vec_dist(v0,v1) : 
	if vec_check([v0,v1]) == -1 :
		exit('VEC_LEN ERR - vector lengths not equal.');
	else :
		v_len = len(v0);
		i_list = range(0,v_len);
		return sqrt(sum([pow((v1[i]-v0[i]),2) for i in i_list]));
#- mtw -#
def c_vec_dist(v0,v1) : 
	if vec_check([v0,v1]) == -1 :
		exit('VEC_LEN ERR - vector lengths not equal.');
	else :
		v_len = len(v0);
		i_list = range(0,v_len);
		return c_sqrt(sum([pow((v1[i]-v0[i]),2) for i in i_list]));

#--     PLOTS     --#

#--     DEBUG     --#
#- mtw -#
def notes() : print(LIB_NOTES);
