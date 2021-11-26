import lib;
import prot_lib as prot;

lib.notes();
prot.notes();

# lib.term_colour_fmt();

x = lib.pts(-2,2,100);
y = [lib.pow(i,2) for i in x];
z = [lib.pow(i,3) for i in x];

# lib.pl_init();
# lib.pl_font('def');
# lib.pl_lineL('b.',x,y);
# lib.pl_lineL('r-',x,z);
# lib.pl_lineF('b_w4a0.75',y,z,r'$\varphi$');
# lib.pl_label('Tys10wbLys8pb','Title',r'$x$',r'$y$');
# lib.pl_disp();