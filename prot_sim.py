### Towards Molecular Dynamics Model for Natural/Proteingenic Amino Acids - Eric C.
## obj - at least have the string analysis portion done in this script.
##		--	would've done this in C, but python for str processing is
##			far easier on the brain.

import os,sys,time,numpy as np,warnings;
warnings.filterwarnings('ignore');
t_0 = time.time();

# end program at specific place 
def end(t) : return exit('-- RUN TIME %1.3f --' % (time.time()-t));
# folder path
#fldr_path = '/home/ericc/spaces/extspace/prot_sim';
fldr_path = '/Users/ericc/Desktop/molec_dyn/molecular_dynamics_model';
# 3 letter codes for the 20 amino acids
name_arr = ['Ala','Arg','Asn','Asp','Cys','Gln','Glu','Gly','His','Ile','Leu','Lys','Met','Phe','Pro','Ser','Thr','Trp','Tyr','Val'];
# 1 letter codes for the 20 amino acids
letter_lst = ['A','R','N','D','C','Q','E','G','H','I','L','K','M','F','P','S','T','W','Y','V'];
# details of each atom || r_at(pm), r_vdw(pm), m_at(u), elec_neg, at_num
atom_det = [['C',70,170,12.0107,2.55,6],
			['H',53,120,1.00784,2.2,1],
			['O',60,152,15.999,3.44,8],
			['N',65,155,14.0067,3.04,7],
			['S',100,180,32.065,2.58,16]];

# shape of array
def shape(arr_in) : 
	np_shp = np.asarray(arr_in).shape;
	py_shp = [i for i in np_shp];
	return py_shp;

# loading txt file structure into python array
def ld_struc(name,fldr_path) :
	FILE = open('%s/struc_arrays/%s_struc.txt' % (fldr_path,name),'r');
	arr_out = [];
	while True :
		line = FILE.readline();
		if len(line) == 0 : break;
		line_lst = line.split(',');
		line_lst[-1] = line_lst[-1][:-1];
		arr_out.append(line_lst);
	FILE.close();
	return arr_out;

# bonding rules for struc arrays, outputting the full list
# takes input string of 1 letter acid codes to make structure table
def bond_str(in_str) :
	# lists of codes
	symb0 = ['Ala','Arg','Asn','Asp','Cys','Glu','Gln','Gly','His','Ile','Leu','Lys','Met','Phe','Pro','Ser','Thr','Trp','Tyr','Val'];
	symb1 = ['A'  ,'R'  ,'N'  ,'D'  ,'C'  ,'E'  ,'Q'  ,'G'  ,'H'  ,'I'  ,'L'  ,'K'  ,'M'  ,'F'  ,'P'  ,'S'  ,'T'  ,'W'	,'Y'  ,'V'];
	# locally loaded arrays for the function // quick enough
	Ala_struc = ld_struc('Ala',fldr_path);
	Arg_struc = ld_struc('Arg',fldr_path);
	Asn_struc = ld_struc('Asn',fldr_path);
	Asp_struc = ld_struc('Asp',fldr_path);
	Cys_struc = ld_struc('Cys',fldr_path);
	Glu_struc = ld_struc('Glu',fldr_path);
	Gln_struc = ld_struc('Gln',fldr_path);
	Gly_struc = ld_struc('Gly',fldr_path);
	His_struc = ld_struc('His',fldr_path);
	Ile_struc = ld_struc('Ile',fldr_path);
	Leu_struc = ld_struc('Leu',fldr_path);
	Lys_struc = ld_struc('Lys',fldr_path);
	Met_struc = ld_struc('Met',fldr_path);
	Phe_struc = ld_struc('Phe',fldr_path);
	Pro_struc = ld_struc('Pro',fldr_path);
	Ser_struc = ld_struc('Ser',fldr_path);
	Thr_struc = ld_struc('Thr',fldr_path);
	Trp_struc = ld_struc('Trp',fldr_path);
	Tyr_struc = ld_struc('Tyr',fldr_path);
	Val_struc = ld_struc('Val',fldr_path);
	# huge arr which may be used for bond linking
	struc_list = [Ala_struc,Arg_struc,Asn_struc,Asp_struc,Cys_struc,Glu_struc,Gln_struc,Gly_struc,His_struc,Ile_struc,Leu_struc,Lys_struc,Met_struc,Phe_struc,Pro_struc,Ser_struc,Thr_struc,Trp_struc,Tyr_struc,Val_struc];
	struc_arr = [];
	for i in range(0,len(symb1)) : struc_arr.append([symb1[i],struc_list[i]]);
	# now to the actual purpose of this function, applying bonding rules to the above data
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
						if struc_arr[j][1][row][0] == '04' :
							ind4 = struc_arr[j][1][row][5][0] + 'C';
					if i > range(0,len(in_str))[0] and i < range(0,len(in_str))[-1] : # middle acid case - bond above and below
						if struc_arr[j][1][row][0] == '02' :
							index_str = '{0}-'.format(str(i)) + struc_arr[j][1][row][0];
							ind2 = struc_arr[j][1][row][3][0] + 'N';
						elif struc_arr[j][1][row][0] == '04' :
							ind4 = struc_arr[j][1][row][5][0] + 'C';
						elif struc_arr[j][1][row][0] == '022' : # technically redundant but good for book keeping
							ind0 = 'N';
							ind1 = '-H';
							ind2 = '-C';
							ind3 = 'ee';
							ind4 = '-C';
					if i == range(0,len(in_str))[-1] : # end acid case - only bond above
						if struc_arr[j][1][row][0] == '02' :
							ind2 = struc_arr[j][1][row][3][0] + 'N';
						elif struc_arr[j][1][row][0] == '022' : # redundant as the same as the bond below from prev acids
							ind0 = 'N';
							ind1 = '-H';
							ind2 = '-C';
							ind3 = 'ee';
							ind4 = '-C';
					bonded_struc.append([index_str,ind0,ind1,ind2,ind3,ind4]); # add altered & unaltered rows to the output array
	return bonded_struc; # output the huge array

###############################################################################
###############################################################################

test = 'APA';
arr = bond_str(test);

for i in arr : print(i);












end(t_0);