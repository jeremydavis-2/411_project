#!/usr/bin/python

import sys
import re
import string
import os
import subprocess
"""
Usage: qx_ea.py output_directory/
BUG: Does not work past the first level of a directory
"""
def main():
	Currdir = os.getcwd()+'/'+str(sys.argv[1])
	alps=[]
	print("L z 0 1 2 3 4 5")
	for item in os.listdir(Currdir):
		if os.path.isfile(os.path.join(Currdir,item)):
			sts = get_roots(Currdir,item)
			print(str(round(float(item[6:])**-2,4)),item[6:],*sts,sep=' ')
			#alps.append(float(item[6:]))
	
	
def get_roots(path, outfile):
    Es = []
    lines = readfile(path+'/'+outfile)
    for i, line in enumerate(lines):
        if "Electron-attached" in line:
                #print(lines[i+5]),
                Es.append(lines[i+5].split()[3])
    return(Es)

def readfile(filename):
    f = open(filename, 'r')
    lines = f.readlines()
    f.close()
    return lines

if __name__ == "__main__":
    main()
