import math as ma,cmath as cma,numpy as np,time,os,sys;
from matplotlib import pyplot as plt;

t0 = time.time();
def t_now(t0) :
	num = time.time()-t0;
	printout = 'Run time: %1.3fs' % num;
	return [num,printout];

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
def pow(x,n) : return (x)**(n);
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
	print(t_now(t0)[1],'line2D: x=%1.3f  y=%1.3f' % (x,y),' vars=',x_vars);
	return y;
def circle2D(rad,x,centre) :
	in_sqrt = pow(rad,2) - pow((x-centre[0]),2);
	if in_sqrt <= 0 :
		print('circle2D ERR: -ve value in the sqrt. Setting to zero.');
		return [0,0];
	else :
		sqrt_pt = sqrt(in_sqrt);
		yp = centre[1] + pm(sqrt_pt)[0];
		ym = centre[1] + pm(sqrt_pt)[1];
		print(t_now(t0)[1],'circle2D: ym=%1.3f  yp=%1.3f' % (ym,yp));
		return [ym,yp];
# calc pts of line intersecting the circle
def x_circ_intersects(grad,d_x,rad,centre) :
	phi_a = pow(grad,2) + 1;
	phi_b = centre[0] + (centre[1]*grad) + (d_x*pow(grad,2));
	phi_c = -(pow(rad,2) - pow(centre[0],2) - pow(centre[1],2) - pow((grad*d_x),2) - (2*grad*d_x*centre[1]));
	in_sqrt = pow(phi_b,2) - (phi_a*phi_c);
	print('x_circ_intersects:\n    phi_a =\t%+1.3f\n    phi_b =\t%+1.3f\n    phi_c =\t%+1.3f\n    sqrt  =\t%+1.5f' % (phi_a,phi_b,phi_c,in_sqrt));
	if in_sqrt < 0 :
		print('x_circ_intersects ERR: -ve value in the sqrt. Setting to zero.');
		return [0,0];
	else :
		sqrt_pt = sqrt(in_sqrt);
		xp = centre[0] + pm(sqrt_pt)[0];
		xm = centre[0] + pm(sqrt_pt)[1];
		print(t_now(t0)[1],'x_circ_intersects: xm=%1.3f  xp=%1.3f' % (xm,xp));
		return [xm,xp];

def y_circ_intersects(grad,d_x,rad,centre) :
	phi_a = pow(grad,-2) + 1;
	phi_b = centre[1] + (centre[0]/grad) + (d_x/m);
	phi_c = pow(centre[0],2) + pow(centre[1],2) + pow(d_x,2) - pow(rad,2) - (2*centre[0]*d_x);
	in_sqrt = pow(phi_b,2) - (phi_a*phi_c);
	print('y_circ_intersects:\n    phi_a =\t%+1.3f\n    phi_b =\t%+1.3f\n    phi_c =\t%+1.3f\n    sqrt  =\t%+1.5f' % (phi_a,phi_b,phi_c,in_sqrt));
	if in_sqrt < 0 :
		print('y_circ_intersects ERR: -ve value in the sqrt. Setting to zero.');
		return [0,0];
	else :
		sqrt_pt = sqrt(in_sqrt);
		yp = pm(sqrt_pt)[0];
		ym = pm(sqrt_pt)[1];
		print(t_now(t0)[1],'y_circ_intersects: ym=%1.3f  yp=%1.3f' % (ym,yp));
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

### testing the 2D functions
## general
num_pts = 201;
x_range = [i for i in np.linspace(-2,2,num_pts)];

## line params
# gradient
m = 0.25;
# x-intercept
d_x = -1;

y_line = [line2D(x,[m,d_x]) for x in x_range];

## circle params
rad = 1;
orig = [0.5,0];

y_pm = [circle2D(rad,x,orig) for x in x_range];

yp_circ = [y_pm[i][1] for i in range(0,num_pts)];
ym_circ = [y_pm[i][0] for i in range(0,num_pts)];

## intersections
x_intersections = x_circ_intersects(m,d_x,rad,orig);
y_intersections = y_circ_intersects(m,d_x,rad,orig);

## plot
plot0 = plt.figure();
# line
plt.plot(x_range,y_line,'k--');
# circ upper
plt.plot(x_range,yp_circ,'k');
# circ lower
plt.plot(x_range,ym_circ,'k');

plt.show();



