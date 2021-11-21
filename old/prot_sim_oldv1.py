### protein simulation script in python as C is just too difficult for the time being.
## package imports
import math as ma, numpy as np, scipy as sp, random as rdm,time,os,sys,gc,warnings;warnings.filterwarnings('ignore');
from mpl_toolkits.mplot3d import Axes3D;
import matplotlib.pyplot as plt;

###############################################################################
###############################################################################

## pre loaded data
## path to project folder
fldr_path = '/home/ericc/spaces/extspace/prot_sim/';
struc_fldr = 'struc_arrays';
# structure load function
def struc_ld(fldr_path,fldr,prot_nm) : return np.loadtxt('%s%s/%s_struc.txt' % (fldr_path,fldr,prot_nm),delimiter=',',dtype=np.str);
## data arrays
symb0 = ['Ala','Arg','Asn','Asp','Cys','Glu','Gln','Gly','His','Ile','Leu','Lys','Met','Phe','Pro','Ser','Thr','Tyr','Val'];
symb1 = ['A'  ,'R'  ,'N'  ,'D'  ,'C'  ,'E'  ,'Q'  ,'G'  ,'H'  ,'I'  ,'L'  ,'K'  ,'M'  ,'F'  ,'P'  ,'S'  ,'T'  ,'Y'  ,'V'];
## structural arrays // loaded from files
Ala_struc = struc_ld(fldr_path,struc_fldr,'Ala');
Arg_struc = struc_ld(fldr_path,struc_fldr,'Arg');
Asn_struc = struc_ld(fldr_path,struc_fldr,'Asn');
Asp_struc = struc_ld(fldr_path,struc_fldr,'Asp');
Cys_struc = struc_ld(fldr_path,struc_fldr,'Cys');
Glu_struc = struc_ld(fldr_path,struc_fldr,'Glu');
Gln_struc = struc_ld(fldr_path,struc_fldr,'Gln');
Gly_struc = struc_ld(fldr_path,struc_fldr,'Gly');
His_struc = struc_ld(fldr_path,struc_fldr,'His');
Ile_struc = struc_ld(fldr_path,struc_fldr,'Ile');
Leu_struc = struc_ld(fldr_path,struc_fldr,'Leu');
Lys_struc = struc_ld(fldr_path,struc_fldr,'Lys');
Met_struc = struc_ld(fldr_path,struc_fldr,'Met');
Phe_struc = struc_ld(fldr_path,struc_fldr,'Phe');
Pro_struc = struc_ld(fldr_path,struc_fldr,'Pro');
Ser_struc = struc_ld(fldr_path,struc_fldr,'Ser');
Thr_struc = struc_ld(fldr_path,struc_fldr,'Thr');
Tyr_struc = struc_ld(fldr_path,struc_fldr,'Tyr');
Val_struc = struc_ld(fldr_path,struc_fldr,'Val');
## huge arr which may be used for bond linking
struc_list = [Ala_struc,Arg_struc,Asn_struc,Asp_struc,Cys_struc,Glu_struc,Gln_struc,Gly_struc,His_struc,Ile_struc,Leu_struc,Lys_struc,Met_struc,Phe_struc,Pro_struc,Ser_struc,Thr_struc,Tyr_struc,Val_struc];
struc_arr = [];
for i in range(0,len(symb1)) : struc_arr.append([symb1[i],struc_list[i]]);
## details of each atom || r_at(pm), r_vdw(pm), m_at(u), elec_neg, at_num
atom_det = [['C',70,170,12.0107,2.55,6],
			['H',53,120,1.00784,2.2,1],
			['O',60,152,15.999,3.44,8],
			['N',65,155,14.0067,3.04,7],
			['S',100,180,32.065,2.58,16]];

###############################################################################
###############################################################################

## some custom functions
# returning the shape/dimensions of an array
def shape(arr_in) : return np.asarray(arr_in).shape;

###############################################################################
###############################################################################

## bonding rules for struc arrays, outputting the full list
# takes input string of 1 letter acid codes to make structure table
def bond_str(in_str) :
	## locally loaded arrays for the function // quick enough
	Ala_struc = struc_ld(fldr_path,struc_fldr,'Ala');
	Arg_struc = struc_ld(fldr_path,struc_fldr,'Arg');
	Asn_struc = struc_ld(fldr_path,struc_fldr,'Asn');
	Asp_struc = struc_ld(fldr_path,struc_fldr,'Asp');
	Cys_struc = struc_ld(fldr_path,struc_fldr,'Cys');
	Glu_struc = struc_ld(fldr_path,struc_fldr,'Glu');
	Gln_struc = struc_ld(fldr_path,struc_fldr,'Gln');
	Gly_struc = struc_ld(fldr_path,struc_fldr,'Gly');
	His_struc = struc_ld(fldr_path,struc_fldr,'His');
	Ile_struc = struc_ld(fldr_path,struc_fldr,'Ile');
	Leu_struc = struc_ld(fldr_path,struc_fldr,'Leu');
	Lys_struc = struc_ld(fldr_path,struc_fldr,'Lys');
	Met_struc = struc_ld(fldr_path,struc_fldr,'Met');
	Phe_struc = struc_ld(fldr_path,struc_fldr,'Phe');
	Pro_struc = struc_ld(fldr_path,struc_fldr,'Pro');
	Ser_struc = struc_ld(fldr_path,struc_fldr,'Ser');
	Thr_struc = struc_ld(fldr_path,struc_fldr,'Thr');
	Tyr_struc = struc_ld(fldr_path,struc_fldr,'Tyr');
	Val_struc = struc_ld(fldr_path,struc_fldr,'Val');
	## huge arr which may be used for bond linking
	struc_list = [Ala_struc,Arg_struc,Asn_struc,Asp_struc,Cys_struc,Glu_struc,Gln_struc,Gly_struc,His_struc,Ile_struc,Leu_struc,Lys_struc,Met_struc,Phe_struc,Pro_struc,Ser_struc,Thr_struc,Tyr_struc,Val_struc];
	struc_arr = [];
	for i in range(0,len(symb1)) : struc_arr.append([symb1[i],struc_list[i]]);
	## now to the actual purpose of this function, applying bonding rules to the above data
	bonded_struc = []; # output array
	for i in range(0,len(in_str)) :
		# check for matching character
		char = in_str[i]; # updating the current character
		for j in range(0,shape(struc_arr)[0]) :
			if char == struc_arr[j][0] : # comparing to see which acid the character refers to
				# making needed rows, then appending to outgoing new struc arr // going through arrays of each char
				for row in range(0,shape(struc_arr[j][1])[0]) : # going through acid array row by row // applying needed changes
					index_str = '{0}-'.format(str(i)) + struc_arr[j][1][row][0];
					ind0 = struc_arr[j][1][row][1]; # unaltered versions of the
					ind1 = struc_arr[j][1][row][2]; # original acid data
					ind2 = struc_arr[j][1][row][3];
					ind3 = struc_arr[j][1][row][4];
					ind4 = struc_arr[j][1][row][5];
					if i == range(0,len(in_str))[0] : # beginning acid case - only bonding below
						if struc_arr[j][1][row][0] == '04' : ind4 = struc_arr[j][1][row][5][0] + 'C';
					if i > range(0,len(in_str))[0] and i < range(0,len(in_str))[-1] : # middle acid case - bond above and below
						if struc_arr[j][1][row][0] == '02' : index_str = '{0}-'.format(str(i)) + struc_arr[j][1][row][0]; ind2 = struc_arr[j][1][row][3][0] + 'N';
						elif struc_arr[j][1][row][0] == '04' : ind4 = struc_arr[j][1][row][5][0] + 'C';
						elif struc_arr[j][1][row][0] == '022' : # technically redundant but good for book keeping
							ind0 = 'N'; ind1 = '-C'; ind2 = 'ee'; ind3 = '-C'; ind4 = '-H';
					if i == range(0,len(in_str))[-1] : # end acid case - only bond above
						if struc_arr[j][1][row][0] == '02' : ind2 = struc_arr[j][1][row][3][0] + 'N';
						elif struc_arr[j][1][row][0] == '022' : # redundant as the same as the bond below from prev acids
							ind0 = 'N'; ind1 = '-C'; ind2 = 'ee'; ind3 = '-C'; ind4 = '-H';
					bonded_struc.append([index_str,ind0,ind1,ind2,ind3,ind4]); # add altered & unaltered rows to the output array
	return bonded_struc; # output the huge array

###############################################################################
###############################################################################

print('\n');

rdm_str = '';
for i in range(0,rdm.randint(1e2,1e3)) : rdm_str += str(symb1[rdm.randint(0,len(symb1)-1)]);

count_each = [[symb1[i],0] for i in range(0,len(symb1))];

for i in range(0,len(rdm_str)) :
	for j in range(0,len(symb1)) :
		if rdm_str[i] == symb1[j] : count_each[j][1] += 1;

for i in range(0,shape(count_each)[0]) : print(count_each[i]);

print('\n');
print('num of acids - %d' % len(rdm_str)); print('%s\n' % rdm_str);
rdm_str_bonded = bond_str(rdm_str);
print(shape(rdm_str_bonded)); print('\n');
# print out for checking that all is well
#for i in range(0,shape(rdm_str_bonded)[0]) : print(i,rdm_str_bonded[i]);

## set up default coordinate systems for each acid
# w/o loop -- Ala,Arg,Asp,Asn,Cys,Glu,Gln,Gly,Ile,Leu,Lys,Met,Ser,Thr,Val
# w/ loops -- His,Phe,Pro,Tyr

atom_rad = [['C',0.7],['H',0.53],['O',0.6],['N',0.65],['S',1]];
bond_lengths = [['C-C',1.54,1.40],['C-H',1.69],['C-N',1.47,1.34],['N-C',1.47,1.34],['N-H',0.99],['C-O',1.43],['O-C',1.43],['C=O',1.21],['O-H',0.98],['C=C',1.34],['C-S',1.82],['S-C',1.82],['S-H',1.34],['C=N',1.25],['N=C',1.25]];

tet_the = 120; # degrees
tet_phi = 109.5; # degrees
tri_the = 180; # degrees
tri_phi = 120; # degrees
ee_corr = -2.5; # degrees

# counting occurrences
def count(search_str,list_in) :
	count = 0; #print(len(list_in));
	for j in range(0,len(list_in)) :
		#print(j,list_in[j],search_str);
		if list_in[j] == search_str : count += 1;
	return count;
# make fn names shorter for laziness sake
def cos(x) : return ma.cos(x);
def sin(x) : return ma.sin(x);
# conversion functions
def d2r(deg) : return deg*ma.pi/180; # degrees to radians
def sph_x(sph) : return sph[0]*cos(sph[1])*sin(sph[2]);
def sph_y(sph) : return sph[0]*sin(sph[1])*sin(sph[2]);
def sph_z(sph) : return sph[0]*cos(sph[2]);
def ifeven(n) :
	if n/2 == int(n/2) : return True;
	else : return False;
# tet
def tet_rule(x0,y0,z0,row_in) :
	ee_corr = -2.5; # degrees
	tet_the = 120; # degrees
	tet_phi = 109.5 + (ee_corr*count('ee',row_in)); # degrees

	atom_rad = [['C',0.7],['H',0.53],['O',0.6],['N',0.65],['S',1]];
	bond_lengths = [['C-C',1.54,1.40],['C-H',1.69],['C-N',1.47,1.34],['N-C',1.47,1.34],['N-H',0.99],['C-O',1.43],['O-C',1.43],['C=O',1.21],['O-H',0.98],['C=C',1.34],['C-S',1.82],['S-C',1.82],['S-H',1.34],['C=N',1.25],['N=C',1.25]];

	r = [];
	for i in range(2,len(row_in)) :
		bond = row_in[1]+row_in[i];
		if row_in[i] != 'ee' :
			for j in range(0,len(bond_lengths)) :
				if bond == bond_lengths[j][0] :
					bond_len = bond_lengths[j][1];

		if row_in[i] == 'ee' :
			for j in range(0,len(atom_rad)) :
				if row_in[1] == atom_rad[j][0] :
					bond_len = atom_rad[j][1];

		#print(i-1,bond,bond_len);
		r.append(bond_len);

	tet0 = [0,0,0];
	tet1 = [r[0],0,0];
	tet2 = [r[1],0,d2r(tet_phi)];
	tet3 = [r[2],d2r(tet_the),d2r(tet_phi)];
	tet4 = [r[3],d2r(2*tet_the),d2r(tet_phi)];

	coord0 = [x0+sph_x(tet0),y0+sph_y(tet0),z0+sph_z(tet0)];
	coord1 = [x0+sph_x(tet1),y0+sph_y(tet1),z0+sph_z(tet1)];
	coord2 = [x0+sph_x(tet2),y0+sph_y(tet2),z0+sph_z(tet2)];
	coord3 = [x0+sph_x(tet3),y0+sph_y(tet3),z0+sph_z(tet3)];
	coord4 = [x0+sph_x(tet4),y0+sph_y(tet4),z0+sph_z(tet4)];

	return [coord0,coord1,coord2,coord3,coord4];

# tri coord calc
def tri_rule(x0,y0,z0,row_in) :
	row_ind = row_in[0];
	#if ifeven(len(row_ind)) == True
	ee_corr = -2.5; # degrees
	tri_the = 180; # degrees
	tri_phi = 120 + (ee_corr*count('ee',row_in)); # degrees

	atom_rad = [['C',0.7],['H',0.53],['O',0.6],['N',0.65],['S',1]];
	bond_lengths = [['C-C',1.54,1.40],['C-H',1.69],['C-N',1.47,1.34],['N-C',1.47,1.34],['N-H',0.99],['C-O',1.43],['O-C',1.43],['C=O',1.21],['O-H',0.98],['C=C',1.34],['C-S',1.82],['S-C',1.82],['S-H',1.34],['C=N',1.25],['N=C',1.25]];

	r = [];
	for i in range(2,len(row_in)-1) :
		bond = row_in[1]+row_in[i];

		if row_in[i] != 'ee' :
			for j in range(0,len(bond_lengths)) :
				if bond == bond_lengths[j][0] :
					bond_len = bond_lengths[j][1];

		if row_in[i] == 'ee' :
			for j in range(0,len(atom_rad)) :
				if row_in[1] == atom_rad[j][0] :
					bond_len = atom_rad[j][1];

		#print(i-1,bond,bond_len);
		r.append(bond_len);

	tri0 = [0,0,0];
	tri1 = [r[0],0,0];
	tri2 = [r[1],0,d2r(tri_phi)];
	tri3 = [r[2],d2r(tri_the),d2r(tri_phi)];

	coord0 = [x0+sph_x(tri0),y0+sph_y(tri0),z0+sph_z(tri0)];
	coord1 = [x0+sph_x(tri1),y0+sph_y(tri1),z0+sph_z(tri1)];
	coord2 = [x0+sph_x(tri2),y0+sph_y(tri2),z0+sph_z(tri2)];
	coord3 = [x0+sph_x(tri3),y0+sph_y(tri3),z0+sph_z(tri3)];

	return [coord0,coord1,coord2,coord3];

def row_type(row_in) :
	if count('X',row_in) == 0 :
		str_out = 'tet';
	if count('X',row_in) == 1 :
		str_out = 'tri';
	#print(count('X',row_in),count('ee',row_in),109.5 + (ee_corr*count('ee',row_in)),'%s' % str_out);
	return str_out

tmp_arr = Gly_struc;
tmp_coord = [];
x0 = 0; y0 = 0; z0 = 0;
for i in range(0,shape(tmp_arr)[0]) :
	row = tmp_arr[i];
	#print(row);
	typ = row_type(row);
	row_index = row[0];
	bond_index = row_index[-1];
	#print(row_index,bond_index)

	#if row[0] != '0' : x0 = 0; y0 = 0; z0 = 0;

	if typ == 'tet' : coord = tet_rule(x0,y0,z0,row);
	if typ == 'tri' : coord = tri_rule(x0,y0,z0,row);
	tmp_coord.append(coord);

	if i > 0 :
		for j in range(0,len(tmp_coord[0])) :
			if str(j) == bond_index :
				prev_coord = tmp_coord[0][j];
				#print('coord0: j=',j,x0,y0,z0);
				x0 = prev_coord[0];
				y0 = prev_coord[1];
				z0 = prev_coord[2];

	#for j in range(0,len(tmp_coord[i])) :
		#print(j,tmp_coord[i][j]);

	#print('\n');

#print(shape(tmp_coord));

#plot = plt.figure();
#ax = Axes3D(plot);
#col = ['black','blue','green','red'];
#for i in range(0,len(tmp_coord)) :
#	for j in range(0,len(tmp_coord[i])) :
#		ax.scatter(tmp_coord[i][j][0],tmp_coord[i][j][1],tmp_coord[i][j][2],color=col[i]);
#plt.show();
