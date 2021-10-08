import math as ma,cmath as cma,numpy as np,time,os,sys;
from matplotlib import pyplot as plt;

# circle stuff
def circ_func(x_in,r,x0,y0) :
	tmp0 = (r**2) - ((x_in-x0)**2);
	if tmp0 < 0 : return [0,0];
	tmp = ma.sqrt(tmp0);
	out0 = y0-tmp;
	out1 = y0+tmp;
	return [out0,out1];

r = 1;
x0 = 1/2;
y0 = 0;

# straight line
def line_func(x_in,m,b) :
	return m*(x_in-b);

m = 1/4;
b = -1;

# intersections
def intersect(m,b,x0,y0,r) :
	a = 1 + (m**2);
	b = + (m*m*b) + x0 + (y0*m);
	c = (x0**2) + (y0**2) - (r**2) + ((m**2)*(b**2)) + (2*y0*m*b);
	tmp0 = (b**2) - (a*c);
	if tmp0 < 0 : return [[0,0],[0,0]];
	tmp = ma.sqrt(tmp0);

	outx0 = (b-tmp)/a;
	outx1 = (b+tmp)/a;
	outy0 = line_func(outx0,m,b);
	outy1 = line_func(outx1,m,b);

	return [[outx0,outy0],[outx1,outy1]];

# l_tilde from diagram
def l_tilde(x0,y0,x1,y1) :
	if x0 == 0 and y0 == 0 and x1 == 0 and y1 == 0 : return 0;
	out = ma.sqrt(((y1-y0)**2) + ((x1-x0)**2));
	return out;

#m = [i for i in np.linspace(-1,1,401)];
l_t = [];

# circle lines;
x_range = [i for i in np.linspace(-2,2,401)];
y_circ0 = [circ_func(i,r,x0,y0)[0] for i in x_range];
y_circ1 = [circ_func(i,r,x0,y0)[1] for i in x_range];
y_line = [line_func(i,m,b) for i in x_range];


plot = plt.figure();
plt.plot(x_range,y_circ0,'k-');
plt.plot(x_range,y_circ1,'k-');
plt.plot(x_range,y_line,'k--');
#for i in m :
#	tmp = intersect(i,b,x0,y0,r);
#	tmp_l = l_tilde(tmp[0][0],tmp[0][1],tmp[1][0],tmp[1][1]);
#	l_t.append(tmp_l)
#	print(i,tmp_l);
#	if tmp_l > 0 :
#		plt.plot(tmp[0][0],tmp[0][1],'kx');
#		plt.plot(tmp[1][0],tmp[1][1],'ko');
#
#plt.plot(m,l_t,'k-');
plt.xlabel(r'$x$');
plt.ylabel(r'$y$');
plt.show();


