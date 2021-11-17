import os;
import sys;
import time;
import math as ma;
import cmath as cma;
import numpy as np;
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

lib_notes = '''
--- SPECIAL FUNCTION LIBRARY ---

---     NOTES     ---
All functions listed below are the ones fully finished
and thus should be usable.

--- FUNCTION LIST ---
ld_struc(name) - loads table for amino acid structure
acid_3code() - returns list of 3-letter acid codes
acid_1code() - returns list of 1-letter acid codes

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
	FILE.close();
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

#--     DEBUG     --#
#- mtw -#
def notes() : print(lib_notes);
