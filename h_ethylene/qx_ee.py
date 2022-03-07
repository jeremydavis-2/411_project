#!/usr/bin/python

import sys
import re
import string
import os
import subprocess
"""
Usage: qx_ea.py output_directory/ root_name
BUG: Does not work past the first level of a directory
"""
def main():
	Dir = str(sys.argv[1])
	rname = str(sys.argv[2])
	alps=[]
	print("L z 0 1 2 3 4 5")
	for item in os.listdir(Dir):
		path = os.path.join(Dir,item)
		if os.path.isfile(path) and rname in path:
			Es, e_size,h_size = get_roots(path)
			print(str(round(float(item[6:])**-2,4)),item[6:],*Es,sep=' ')
	
	
def get_roots(path):
    Es = []
    e_size = []
    h_size = []
    lines = readfile(path)
    for i, line in enumerate(lines):
        if "Excitation energy:" in line:
                #print(lines[i+5]),
                Es.append(lines[i].split()[2])
        if False:
            h_size.append(lines[i+58].split())
        #    e_size.append(lines[i+58].split()[3])
        
    return(Es,e_size, h_size)

def readfile(filename):
    f = open(filename, 'r')
    lines = f.readlines()
    f.close()
    return lines

if __name__ == "__main__":
    main()
