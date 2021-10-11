import math as ma,cmath as cma,numpy as np,time,os,sys;
from matplotlib import pyplot as plt;

### obj - find the following functions/lengths
#	- set up parametric straight line in 3D
#	- set up function for sphere
#	- find intersections between line and sphere
#	- find length between intersections
###

## relabelling mathematical functions
def sin(x) : return ma.sin(x);
def arcsin(x) : return ma.arcsin(x);

def cos(x) : return ma.cos(x);
def arccos(x) : return ma.arccos(x);

def tan(x) : return ma.tan(x);
def arctan(x) : return ma.arctan(x);

def log(x) : return ma.log(x);
def sqrt(x) : return ma.sqrt(x);
def pow(x,n) : return x**n;

## conversion functions
def deg2rad(x) : return x*(ma.pi/180);
def rad2deg(x) : return x*(180/ma.pi);
# spherical to cartesian
def sph2car(rho,theta,phi) :
	x = rho*cos(theta)*sin(phi);
	y = rho*sin(theta)*sin(phi);
	z = rho*cos(phi);
	return [x,y,z]
# cartesian to spherical
def car2sph(x,y,z) :
	rho = sqrt(pow(x,2),pow(y,2)+popw(z,2));
	phi = arccos(z/rho);
	theta = arccos(x/(rho*sin(phi)));
	return [rho,theta,phi];

# parametrric straight line
def line3D(t,x_vars,y_vars,z_vars) :
	# vars should be vec : [d/dt,t0 constant]
	x = (x_vars[0]*t) + x_vars[1];
	y = (y_vars[0]*t) + y_vars[1];
	z = (z_vars[0]*t) + z_vars[1];
	# returns xyz vector of their positions
	return [x,y,z];

def sphere3D(rad,x,x0,y,y0,z,z0) :
	pow(rad,2) = pow((x-x0),2) + pow((y-y0),2) + pow((z-z0),2);
