import time,os,sys,math as ma,cmath as cma, numpy as np;
from matplotlib import pyplot as plt;

def vec_dot(v0,v1) :
	if len(v0) != len(v1) :
		exit('ERR: VEC_DOT - vectors not the same length');
	else :
		vlen = len(v0);
		outp = 0;
		for i in range(0,vlen) :
			outp += (v0[i]*v1[i]);

		return outp;

def vec_add(v0,v1) :
	if len(v0) != len(v1) :
		exit('ERR: VEC_ADD - vectors not the same length');
	else :
		vlen = len(v0);
		outp = [];
		for i in range(0,vlen) :
			tmp = v0[i] + v1[i];
			outp.append(tmp);
		
		return outp;

