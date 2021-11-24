import os;
import sys;
import time;
import math as ma;
import cmath as cma;
import numpy as np;
from matplotlib import pyplot as plt;
import inspect as insp;

### TEXT COLOURS ###
RED = '0;31;1';
BLUE = '0;34;1';
CYAN = '0;36;1';
MAGENTA = '0;35;1';
GREEN = '0;32;1';
YELLOW = '0;33;1';
WHITE = '0;37;1';

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
--- GENERAL FUNCTION LIBRARY ---

---     NOTES     ---
All functions listed below are the ones fully finished
and thus should be usable.

--- FUNCTION LIST ---
 --     DEBUG     --
notes() - print this output
term_colour_fmt() - prints table of coloured print outs
col_txt(col,txt) - returns string of coloured text
err_inf() - prints code and func source files and linenumbers
err_msg(fname,msg) - exits with error message for function
err_log(fname,msg) - prints error message for function w/o exit


 --    RELABEL    --
sin(val) - returns sin of val
asin(val) - returns arcsin of val
cos(val) - returns cos of val
acos(val) - returns arccos of val
tan(val) - returns tan of val
atan(val) - returns arctan of val
sqrt(val) - returns sqrt of val

c_sin(val) - returns complex result for sin of val
c_asin(val) - returns complex result for arcsin of val
c_cos(val) - returns complex result for cos of val
c_acos(val) - returns complex result for arccos of val
c_tan(val) - returns complex result for tan of val
c_atan(val) - returns complex result for arctan of val
c_sqrt(val) - returns complex result for sqrt of val

shape(arr) - returns the shape of an arr
pow(val,n) - returns value raised to power 'n'
pts(llim,ulim,num) - returns evenly spaced points between two limits

 --    CUSTOMS    --
  -    VECTORS    -
vec_check(v_list) - check if all vecs are the same length
vec3_check(v_list) - check if list only contains 3D vectors
det_2x2(m) - returns the determinant of a 2x2 matrix
vec_mult(const,v) - multiplies vec by a constant
vec_add(v0,v1) - adds two vectors element-wise
vec_sub(v0,v1) - subtracts first inp vec from the second element-wise
vec_dot(v0,v1) - returns dot product of two vectors
vec_cross(v0,v1) - returns cross product between two vectors
vec_dot2(v0) - returns my sq dot notation (dot vec with itself)
vec_dotL(v_list) - returns dot product of a list of vectors (my notation)
vec_dist(v0,v1) - returns the distance between two vectors
c_vec_dist(v0,v1) - returns complex valued distance between two vectors

 --     PLOTS     --
  -    FMT_STR    -
The format string is just a set of characters which describe how the outp plot
looks. 

For 'pl_lineL' order of fmt string: '[c][s]' :
	c - colour
	s - style, ex. == _ (solid), - (dashed), . (dotted)

For 'pl_lineF' order of fmt string: '[c][s]w[int]a[flt]' :
	c - colour
	s - style, ex. == _ (solid), - (dashed), . (dotted)
	w - linewidth
	a - alpha, float: 'a' elem of [0,1]

For 'pl_label' order of fmt string: 'T[y/n]s[int]w[str]L[y/n]s[int]p[b/pc]' :
	T - title section
	L - legend section
	y/n - yes or no
	s - font size
	w - font weight
	p - legend position, b (best) or pc (position code) in pl_pc(posc)

  -   FUNCTIONS   -
pl_init() - relabel of plt.figure()
pl_disp() - display plot
pl_font(name) - set font to specific 'name', or Times if 'def'
pl_label(title,xlab,ylab,legend) - overall plot labels
pl_lineL(fmt,x,y) - simple line plot with [L]ittle formatting
pl_lineF(fmt,title,x,y) - simple line plot with [F]ull formatting
pl_fw(fwc) - returns string for fontweight for title formatting
pl_pc(posc) - returns position string for the legend for position code

'''

#---   GENERAL   ---#
#--     DEBUG     --#
#- mtw -#
def notes() : print(LIB_NOTES);
#- mtw -#
def term_colour_fmt():
	# prints table of formatted text format options
	# ref: https://stackoverflow.com/questions/287871/
	#	how-to-print-colored-text-to-the-terminal 
	# dat: [23/11/2021]
	s_list = range(0,8);
	fg_list = range(30,38);
	bg_list = range(40,48);
	for style in s_list :
		for fg in fg_list :
			outp_str = ''
			for bg in bg_list :
				# bg = 1 for coloured text on normal bg
				fmt = '%d;%d;%d' % (style,fg,bg);
				outp_str += '\x1b[%sm %s \x1b[0m' % (fmt, fmt);
			print(outp_str);
	print('\n');
#- mtw -#
def col_txt(col,txt) : return '\x1b[%sm%s\x1b[0m' % (col,txt);
#- mtw -#
def err_inf() :
	info = insp.stack();
	info_prs = [];
	err_info = col_txt(RED,'##');
	for i in info :
		fil = ''; typ = ''; # typ = type: C (code), F (func)
		if 'molecular_dynamics_model/' in str(i.filename) :
			# case if function is from lib (as should be)
			fil = str(i.filename).split('molecular_dynamics_model/')[1];
			typ = 'F';
		else :
			fil = i.filename;
			typ = 'C';
		if str(i.function) != 'err_inf' :
			txt0 = col_txt(MAGENTA,typ);
			txt1 = col_txt(CYAN,'src: ');
			txt2 = col_txt(WHITE,fil);
			txt3 = col_txt(CYAN,'line: ');
			txt4 = col_txt(WHITE,str(i.lineno));
			txt_inst = ' %s%s%s, %s%s ' % (txt0,txt1,txt2,txt3,txt4);
			err_info += col_txt(CYAN,txt_inst);
			err_info += col_txt(RED,'##');
	print(err_info);
#- mtw -#
def err_msg(fname,msg) :
	name_pt = col_txt(RED,'%s ERR - ' % fname);
	msg_pt = col_txt(CYAN, '%s.' % msg)
	exit_str = name_pt + msg_pt;
	exit(exit_str);
#- mtw -#
def err_log(fname,msg) :
	name_pt = col_txt(RED,'%s ERR - ' % fname);
	msg_pt = col_txt(CYAN, '%s.' % msg)
	exit_str = name_pt + msg_pt;
	print(exit_str);

#--    RELABEL    --#
#-     REAL FN     -#
#- mtw -#
def sin(x) : return ma.sin(x);
#- mtw -#
def asin(x) : return ma.asin(x);
#- mtw -#
def cos(x) : return ma.cos(x);
#- mtw -#
def acos(x) : return ma.acos(x);
#- mtw -#
def tan(x) : return ma.tan(x);
#- mtw -#
def atan(x) : return ma.atan(x);
#- mtw -#
def sqrt(x) : return ma.sqrt(x);

#-     COMP FN     -#
#- mtw -#
def c_sin(x) : return cma.sin(x);
#- mtw -#
def c_asin(x) : return cma.asin(x);
#- mtw -#
def c_cos(x) : return cma.cos(x);
#- mtw -#
def c_acos(x) : return cma.acos(x);
#- mtw -#
def c_tan(x) : return cma.tan(x);
#- mtw -#
def c_atan(x) : return cma.atan(x);
#- mtw -#
def c_sqrt(x) : return cma.sqrt(x);

#-      OTHER      -#
#- mtw -#
def pow(x,n) : return x**n;
#- mtw -#
def shape(arr) : 
	np_shp = np.asarray(arr).shape;
	py_shp = [i for i in np_shp];
	return py_shp;
#- mtw -#
def pts(llim,ulim,num) : return [i for i in np.linspace(llim,ulim,num)];

#--    CUSTOMS    --#
#-     VECTORS     -#
#- mtw -#
def vec_check(v_list) :
	lens = set();
	lens.add(len(v_list[0]));
	for v in v_list :
		v_len = len(v);
		if v_len not in lens :
			return -1;
		else :
			lens.add(v_len);

	return 1;
#- mtw -#
def vec3_check(v_list) :
	for v in v_list :
		if len(v) != 3 :
			return -1;
	return 1;
#- mtw -#
def vec_mult(const,v) :
	v_len = len(v);
	i_list = range(0,v_len);
	return [const*v[i] for i in i_list];
#- mtw -#
def vec_add(v0,v1) :
	if vec_check([v0,v1]) == -1 :
		err_inf();
		err_msg('VEC_ADD','vector lengths not equal');
	else :
		v_len = len(v0);
		i_list = range(0,v_len);
		return [v0[i] + v1[i] for i in i_list];
#- mtw -#
def vec_sub(v0,v1) :
	if vec_check([v0,v1]) == -1 :
		err_inf();
		err_msg('VEC_MIN ERR','vector lengths not equal');
	else :
		v_len = len(v0);
		i_list = range(0,v_len);
		return [v1[i] - v0[i] for i in i_list];
#- mtw -#
def vec_dot(v0,v1) :
	if vec_check([v0,v1]) == -1 :
		err_inf()
		err_msg('VEC_DOT ERR','vector lengths not equal');
	else :
		v_len = len(v0);
		i_list = range(0,v_len);
		return sum([v0[i]*v1[i] for i in i_list]);
#- mtw -#
def vec_dot2(v) :
	v_len = len(v);
	i_list = range(0,v_len);
	return sum([v[i]*v[i] for i in i_list]);
#- mtw -#
def vec_dotL(v_list) :
	if vec_check(v_list) == -1 :
		err_inf();
		err_msg('VEC_DOT2 ERR','vector lengths not equal');
	else :
		v_len = len(v_list[0]);
		list_len = len(v_list)
		n_list = range(0,list_len);
		i_list = range(0,v_len);
		outp = 0;
		for i in i_list :
			tmp = 1;
			for n in n_list :
				tmp *= v_list[n][i];
			outp += tmp;
		return outp;
#- mtw -#
def det_2x2(m) :
	if shape(m) != [2,2] :
		err_msg();
		err_msg('DET_2X2 ERR','non 2x2 matrix input');
	else :
		return ((m[0][0]*m[1][1]) - (m[0][1]*m[1][0]));
#- mtw -#
def vec_cross(v0,v1) :
	if vec3_check([v0,v1]) == -1 :
		err_inf();
		err_msg('VEC_CROSS ERR','not all vectors are 3D');
	else :
		m0 = [	[v0[1],v0[2]],
				[v1[1],v1[2]]];
		d0 = det_2x2(m0);

		m1 = [	[v0[0],v0[2]],
				[v1[0],v1[2]]];
		d1 = det_2x2(m1);

		m2 = [	[v0[0],v0[1]],
				[v1[0],v1[1]]];
		d2 = det_2x2(m2);

		return [d0,-d1,d2];
#- mtw -#
def vec_dist(v0,v1) : 
	if vec_check([v0,v1]) == -1 :
		err_inf();
		err_msg('VEC_LEN ERR','vector lengths not equal');
	else :
		v_len = len(v0);
		i_list = range(0,v_len);
		return sqrt(sum([pow((v1[i]-v0[i]),2) for i in i_list]));
#- mtw -#
def c_vec_dist(v0,v1) : 
	if vec_check([v0,v1]) == -1 :
		err_inf();
		err_msg('VEC_LEN ERR','vector lengths not equal');
	else :
		v_len = len(v0);
		i_list = range(0,v_len);
		return c_sqrt(sum([pow((v1[i]-v0[i]),2) for i in i_list]));

#--     PLOTS     --#
#- mtw -#
def pl_init() : plt.figure();
#- mtw -#
def pl_disp() : plt.show();
#- mtw -#
def pl_fw(fwc) :
	# due to using 'L' for 'legend', using 'w' for 'light' aka 'weak'
	if fwc == 'd' : return 'normal';
	if fwc == 'b' : return 'bold';
	if fwc == 'h' : return 'heavy';
	if fwc == 'w' : return 'light';
	if fwc == 'B' : return 'ultrabold';
	if fwc == 'W' : return 'ultralight';
	# in the case that no above cases have been satisfied
	else :
		err_inf();
		err_log('PL_FW ERR','no known code used, setting to default');
		err_log('MSG','continuing..');
		print('\n');
		return 'normal';
#- mtw -#
def pl_pc(posc) :
	pos = '';
	if posc == 'b' :
		pos = 'best';
	else :
		pos_pt1 = '';
		pos_pt2 = '';
		if posc[0] == 'u' : pos_pt1 = 'upper';
		if posc[0] == 'c' : pos_pt1 = 'center';
		if posc[0] == 'l' : pos_pt1 = 'lower';
		if posc[1] == 'r' : pos_pt2 = 'right';
		if posc[1] == 'c' : pos_pt2 = 'center';
		if posc[1] == 'l' : pos_pt2 = 'left';
		pos = '%s %s' % (pos_pt1,pos_pt2);
	return pos;
#- mtw -#
def pl_font(name) :
	font = 'Times New Roman' if name == 'def' else name;
	plt.rcParams['font.family'] = font;
#- mtw -#
def pl_lineL(fmt,x,y) :
	# format sorting - only style needs actual work
	style = '';
	if fmt[1] == '_' : style = '-';
	if fmt[1] == '-' : style = '--';
	if fmt[1] == '.' : style = ':';
	line_style = '%s%s' % (fmt[0],style);
	plt.plot(x,y,line_style);
#- mtw -#
def pl_lineF(fmt,x,y,lab) :
	# extract line style
	style = '';
	if fmt[1] == '_' : style = '-';
	if fmt[1] == '-' : style = '--';
	if fmt[1] == '.' : style = ':';
	line_style = '%s%s' % (fmt[0],style);
	# extract line width and alpha
	tmp = fmt.split('w')[1].split('a');
	lw = int(tmp[0]);
	al = float(tmp[1]);
	plt.plot(x,y,line_style,linewidth=lw,alpha=al,label=lab);
#- mtw -#
def pl_label(fmt,title,xlab,ylab) :
	tmp = fmt.split('T')[1].split('L');
	fmt_T = tmp[0];
	fmt_L = tmp[1];
	# extracting title formatting
	if fmt_T[0] != 'n' :
		tmp0 = fmt_T.split('s')[1].split('w');
		s = int(tmp0[0]);
		w = pl_fw(str(tmp0[1]));
		plt.title(title,fontsize=s,fontweight=w);
	# extracting legend formatting
	if fmt_L[0] != 'n' :
		tmp1 = fmt_L.split('s')[1].split('p');
		s = int(tmp1[0]);
		p = pl_pc(tmp1[1]);
		plt.legend(fontsize=s,loc=p);
	plt.xlabel(xlab);
	plt.ylabel(ylab);
	



