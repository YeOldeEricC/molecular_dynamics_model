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
def arcsin(x) : return ma.asin(x);

def cos(x) : return ma.cos(x);
def arccos(x) : return ma.acos(x);

def tan(x) : return ma.tan(x);
def arctan(x) : return ma.atan(x);

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
	#print(t_now(t0)[1],'line2D: x=%1.3f  y=%1.3f' % (x,y),' vars=',x_vars);
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
		#print(t_now(t0)[1],'circle2D: ym=%1.3f  yp=%1.3f' % (ym,yp));
		return [ym,yp];
# calc pts of line intersecting the circle
def x_circ_intersects(grad,d_x,rad,centre) :
	phi_a = pow(grad,2) + 1;
	phi_b = centre[0] + (centre[1]*grad) + (d_x*pow(grad,2));
	phi_c = pow(centre[0],2) + pow(centre[1],2) - pow(rad,2) + pow((grad*d_x),2) + (2*grad*d_x*centre[1]);
	in_sqrt = pow(phi_b,2) - (phi_a*phi_c);
	#print('x_circ_intersects:\n    phi_a =\t%+1.3f\n    phi_b =\t%+1.3f\n    phi_c =\t%+1.3f\n    sqrt  =\t%+1.5f' % (phi_a,phi_b,phi_c,in_sqrt));
	if in_sqrt < 0 :
		print('x_circ_intersects ERR: -ve value in the sqrt. Setting to zero.');
		return [0,0];
	else :
		sqrt_pt = sqrt(in_sqrt);
		xp = (phi_b + pm(sqrt_pt)[0])/phi_a;
		xm = (phi_b + pm(sqrt_pt)[1])/phi_a;
		#print(t_now(t0)[1],'x_circ_intersects: xm=%1.3f  xp=%1.3f' % (xm,xp));
		return [xm,xp];
# can just use the line2D for y p/m
def y_circ_intersects(grad,d_x,rad,centre) :
	test = x_circ_intersects(grad,d_x,rad,centre);
	yp = grad*(test[1]-d_x);
	ym = grad*(test[0]-d_x);
	return [ym,yp];

# length between 2 points (lb2p)
def lb2p(x0,y0,x1,y1) :
	dy = y1-y0;
	dx = x1-x0;
	in_sqrt = pow(dy,2) + pow(dx,2);
	length = sqrt(in_sqrt);
	print(t_now(t0)[1],'lb2p: length=%1.5f' % (length));
	return length;
# maximum angle/gradient
def max_grad(d_x,rad,centre) :
	d = centre[0] - d_x;
	ang = arcsin(rad/d);
	max_m = tan(ang);
	return [max_m,ang];


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
num_pts = 5001;

## line params
# gradient
m = 0.25;
# x-intercept
d_x = -3;
# value lists
x_line = [i for i in np.linspace(-2,2,num_pts)];
y_line = [line2D(x,[m,d_x]) for x in x_line];

## circle params
rad = 0.6;
orig = [0.9,0];

# value lists
x_circ = [i for i in np.linspace(orig[0]-rad,orig[0]+rad,num_pts)];
y_pm = [circle2D(rad,x,orig) for x in x_circ];
yp_circ = [y_pm[i][1] for i in range(0,num_pts)];
ym_circ = [y_pm[i][0] for i in range(0,num_pts)];

## intersections
x_intersects = x_circ_intersects(m,d_x,rad,orig);
y_intersects = y_circ_intersects(m,d_x,rad,orig);
# len between them
length = lb2p(x_intersects[0],y_intersects[0],x_intersects[1],y_intersects[1]);

### panning gradient in 2D
num_pts = 2501;
epsilon = 1e-12;

max_m = max_grad(d_x,rad,orig)[0];

m_range = [i if i != 0 else 1e-12 for i in np.linspace(-max_m+epsilon,max_m-epsilon,num_pts)];
x_range = [i for i in [min([d_x,orig[0]+rad]),max([d_x,orig[0]+rad])]];
lines = [[line2D(x,[m,d_x]) for x in x_range] for m in m_range];

x_ints = [x_circ_intersects(m,d_x,rad,orig) for m in m_range];
y_ints = [y_circ_intersects(m,d_x,rad,orig) for m in m_range];

xp = [x_ints[i][1] for i in range(0,num_pts)];
xm = [x_ints[i][0] for i in range(0,num_pts)];
yp = [y_ints[i][1] for i in range(0,num_pts)];
ym = [y_ints[i][0] for i in range(0,num_pts)];

lengths = [lb2p(xm[i],ym[i],xp[i],yp[i]) for i in range(0,num_pts)];

for i in range(0,num_pts) :
	print('%+1.4f %+1.4f %+1.4f %+1.4f %+1.4f %+1.4f' % (m_range[i],xm[i],ym[i],xp[i],yp[i],lengths[i]));

### plot
plot0 = plt.figure();
plt.title('Testing fns that produce lines & intersections');
# line
#plt.plot(x_line,y_line,'k--');
for i in range(0,num_pts) :
	plt.plot(x_range,lines[i],'r:',alpha=0.05);
	plt.plot(xm[i],ym[i],'bo',alpha=0.05);
	plt.plot(xp[i],yp[i],'bo',alpha=0.05);

# circ upper
plt.plot(x_circ,yp_circ,'k');
# circ lower
plt.plot(x_circ,ym_circ,'k');
# intersections
#plt.plot(x_intersects[0],y_intersects[0],'bo');
#plt.plot(x_intersects[1],y_intersects[1],'bo');

plot1 = plt.figure();
plt.title('Looking at length between intersections, panning gradient');
plt.plot(m_range,lengths,'k-');
plt.ylabel('length');
plt.xlabel('gradient');

plt.show();



