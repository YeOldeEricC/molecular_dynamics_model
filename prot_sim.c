#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#include <complex.h>
#include <string.h>

int main()
{
	FILE *fptr;
	char contents;
	char file_path[] = "/home/ericc/spaces/extspace/prot_sim/struc_arrays/Gly_struc.txt";
	

	fptr = fopen(file_path,"r");
	
	contents = fgetc(fptr);
	while (contents != EOF)
	{
		printf("%c",contents);
		contents = fgetc(fptr);

	}

	fclose(fptr);

	return 0;
}