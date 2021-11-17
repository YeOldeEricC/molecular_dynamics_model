###
'''

In here is a test for plotting vector fields with elec field as example for
point sources in a arrangement. Effectively need matrices for x, y and the
magnitudes for each component.

'''
###

import time,os,sys,math as ma,cmath as cma, numpy as np;
from matplotlib import pyplot as plt;
from mpl_toolkits.mplot3d import Axes3D;

def pow(x,n) : return x**n;
def sqrt(x) : return ma.sqrt(x);

# coulomb const
kq = 1;
# number of electrons
num_elec = 8;
# radius
rad = [0.25,0.4,0.5,0.55,0.6];
# atom centres
centre = [[0,0]];

# pos and charge arrs
r = []; q = [];
for k in range(0,len(centre)) :
	for j in range(0,len(rad)) :
		for i in range(0,num_elec) :
			ang = 2*ma.pi*(num_elec-i)/num_elec;
			q.append(-1);
			r.append([(rad[j]*ma.cos(ang))+centre[k][0],(rad[j]*ma.sin(ang))+centre[k][1]]);

	r.append([centre[k][0],centre[k][1]]);
	q.append(num_elec);

num_charges = len(q);

grid_sz = 400;
x_lim = [-1,1];
y_lim = [-1,1];
scale = 1e-3;

# used to replace np.meshgrid
x = [[j for j in np.linspace(x_lim[0],x_lim[1],grid_sz)] for i in range(0,grid_sz)];
y = [[i for j in range(0,grid_sz)] for i in np.linspace(y_lim[0],y_lim[1],grid_sz)];

def Ex(kq,q,r,x,y,grid_sz,scale) : return [[scale*kq*q*(x[i][j]-r[0])/pow(sqrt(pow((x[i][j]-r[0]),2) + pow((y[i][j]-r[1]),2)),3) for j in range(0,grid_sz)] for i in range(0,grid_sz)];

def Ey(kq,q,r,x,y,grid_sz,scale) : return [[scale*kq*q*(y[i][j]-r[1])/pow(sqrt(pow((x[i][j]-r[0]),2) + pow((y[i][j]-r[1]),2)),3) for j in range(0,grid_sz)] for i in range(0,grid_sz)];

Exs = [Ex(kq,q[i],r[i],x,y,grid_sz,scale) for i in range(0,num_charges)];
Eys = [Ey(kq,q[i],r[i],x,y,grid_sz,scale) for i in range(0,num_charges)];

# effectively the u and v below
Ex_T = [[sum([Exs[n][i][j] for n in range(0,num_charges)]) for j in range(0,grid_sz)] for i in range(0,grid_sz)];
Ey_T = [[sum([Eys[n][i][j] for n in range(0,num_charges)]) for j in range(0,grid_sz)] for i in range(0,grid_sz)];




plot = plt.figure();
plt.quiver(x,y,Ex_T,Ey_T,width=1e-3,alpha=0.6);

for i in range(0,num_charges) :
	if q[i] > 0 :
		plt.plot(r[i][0],r[i][1],'ro',linewidth=1,alpha=0.5);
	if q[i] < 0 :
		plt.plot(r[i][0],r[i][1],'bo',linewidth=1,alpha=0.5);
plt.gca().set_aspect('equal', adjustable='box')
plt.show();


# u = x/np.sqrt(x**2 + y**2)
# v = y/np.sqrt(x**2 + y**2)

# plt.quiver(x,y,u,v)
# plt.show()
