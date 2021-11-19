import os;
import sys;
import time;
import math as ma;
import cmath as cma;
import numpy as np;
import random as rdm;
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
--- SPECIAL FUNCTION LIBRARY ---

---     NOTES     ---
This library is purely for functions or routines solely for this project.

All functions listed below are the ones fully finished
and thus should be usable.

--- FUNCTION LIST ---
ld_struc(name) - loads table for amino acid structure
acid_3code() - returns list of 3-letter acid codes
acid_1code() - returns list of 1-letter acid codes
atom_details() - returns details of atoms | r_at, r_vdw, m_at, elec_neg, at_num
rdm_sequence(length) - returns string of length of randomised codons

 --     DEBUG     --
notes() - print this output

'''
#---  FUNCTIONS  ---#
#- mtw -#
def ld_struc(name) :
	file = open('./struc_arrays/%s_struc.txt' % name, 'r');
	arr_out = [];
	while True :
		line = file.readline();
		if len(line) == 0 : break;
		line_lst = line.split(',');
		line_lst[-1] = line_lst[-1][:-1];
		arr_out.append(line_lst)
	file.close();
	return arr_out;
#- mtw -#
def acid_3code() :
	# 3 letter codes for the 20 amino acids
	three_letter = ['Ala','Arg','Asn','Asp','Cys','Gln','Glu','Gly','His','Ile','Leu','Lys','Met','Phe','Pro','Ser','Thr','Trp','Tyr','Val'];
	return three_letter;
#- mtw -#
def acid_1code() :
	# 1 letter codes for the 20 amino acids
	one_letter = ['A','R','N','D','C','Q','E','G','H','I','L','K','M','F','P','S','T','W','Y','V'];
	return one_letter;
#- mtw -#
def atom_details() :
	# details of each atom || r_at(pm), r_vdw(pm), m_at(u), elec_neg, at_num
	atom_det = [['C',70,170,12.0107,2.55,6],
				['H',53,120,1.00784,2.2,1],
				['O',60,152,15.999,3.44,8],
				['N',65,155,14.0067,3.04,7],
				['S',100,180,32.065,2.58,16]];
	return atom_det;
#- mtw -#
def rdm_sequence(length) :
	outp_str = '';
	code_list = acid_1code();
	i_list = range(0,length);
	for i in i_list :
		codon = rdm.choice(code_list);
		outp_str += codon;
	return outp_str;

#--     DEBUG     --#
#- mtw -#
def notes() : print(LIB_NOTES);
