import lib;
import prot_lib as prot;

#lib.notes();
#prot.notes();

lc = 0;
while lc < 25 :
	test = prot.rdm_sequence(25);
	print(test);

	lc += 1;

