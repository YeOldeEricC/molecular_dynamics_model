import lib;
import prot_lib as prot;

lib.notes();
prot.notes();

x = lib.pts(-2,2,100);
y = [lib.pow(i,2) for i in x];
z = [lib.pow(i,3) for i in x];

lib.pl_init();
lib.pl_line('b.',x,y);
lib.pl_line('r-',x,z);
lib.pl_line('b_',y,z);
lib.pl_disp();