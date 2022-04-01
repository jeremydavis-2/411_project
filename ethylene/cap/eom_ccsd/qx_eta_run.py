#!/usr/bin/python

import sys
import re
import string
import os
import subprocess
"""
Usage: qx_eta_run.py output_file
BUG: Does not work past the first level of a directory
"""
def main():
	outfile = os.getcwd()+'/'+str(sys.argv[1])
	alps=[]
	print("eta Re1 Im1 Re2 Im2 Re3 Im3 Re4 Im4 Re5 Im5")
	sts = eta_run(outfile)
	#print(str(round(float(item[6:])**-2,4)),item[6:],*sts,sep=' ')
	#alps.append(float(item[6:]))
	
	
def eta_run(outfile):
	data = []
	lines = readfile(outfile)
	for i, line in enumerate(lines):
		if "--- ETA =" in line: #find start of each ETA run --- index i
			print(lines[i].split()[3], end= ' ')
			for j,line_2 in enumerate(lines[i:]): # find the attachment energies of eta run --- index j lines from i
				if 'Attachment energies for CS/CAP-EOM-EA states' in line_2:
					k = i+j
					for l in range(5):
						print(lines[k+l+2].split()[1], end=' ')
						print(lines[k+l+2].split()[2], end=' ')
					print()
					break


	return(data)

def readfile(filename):
    f = open(filename, 'r')
    lines = f.readlines()
    f.close()
    return lines

if __name__ == "__main__":
    main()



'''
Attachment energies for CS/CAP-EOM-EA states (alpha = 1.00e+00 | theta = 0.00e+00| eta = 1.00e-03):
 State         Re(E)            Im(E)
   1      0.73896681      -0.30406473
   2      1.24032440      -1.45176723
   3      2.07385160      -0.29760237
   4      2.93881137      -0.61829713
   5      5.12624626      -0.55519856
'''
