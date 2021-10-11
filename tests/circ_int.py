import math as ma,cmath as cma,numpy as np,time,os,sys;
from matplotlib import pyplot as plt;

### obj - find the following functions/lengths
#	- set up functions to relabel libraries			DONE
#	- set up straight line in 2D					DONE
#	- set up circle in 2D							DONE
#	- set up parametric straight line in 3D			DONE
#	- set up function for sphere in 3D
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
def pm(x) : return [+x,-x];

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

## 2D functions
def line2D(x,x_vars) :
	# vars = [grad,x intercept]
	y = x_vars[0]*(x-x_vars[1]);
	return y;
def circle2D(rad,x,centre) :
	in_sqrt = pow(rad,2) - pow((x-centre[0]),2);
	if in_sqrt < 0 : return 0;
	else :
		sqrt_pt = sqrt(in_sqrt);
		yp = centre + pm(sqrt_pt)[0];
		ym = centre + pm(sqrt_pt)[1];
		return [ym,yp];


## 3D functions
# parametrric straight line
def line3D(t,x_vars,y_vars,z_vars) :
	# vars should be vec : [d/dt,t0 constant]
	x = (x_vars[0]*t) + x_vars[1];
	y = (y_vars[0]*t) + y_vars[1];
	z = (z_vars[0]*t) + z_vars[1];
	# returns xyz vector of their positions
	return [x,y,z];

def sphere3D(rad,x,x0,y,y0,z,z0) :
	#pow(rad,2) = pow((x-x0),2) + pow((y-y0),2) + pow((z-z0),2);
	return 0;
