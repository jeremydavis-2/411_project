import numpy as np
import os

def infile(R):
	string = '''
#!/bin/bash

echo CFour on $HOSTNAME
export PATH=$PATH:/home/tsommerfeld/cfour-public-v2.1/bin
export OMP_NUM_THREADS=12

scr=aces.scratch
WorkDir=/src/jdavis/$scr
CurrDir=$PWD

if [ ! -d $WorkDir ]
then
	mkdir $WorkDir
else
	rm -rf $WorkDir/*
fi
cd $WorkDir

rm -rf $WorkDir/*
#cp ~thomas/AcesWork/basis_sets/AUG2.BASIS $WorkDir/GENBAS

cp $CurrDir/TZ $WorkDir/GENBAS

cat >> ZMAT << EOF
h_ethylene
C       0.000000      0.0   -0.664500
C       0.000000      0.0    0.664500
H       0.962348      0.0   -1.159080
H       0.962348      0.0    1.159080
H      -0.962348      0.0   -1.159080
H      -0.962348      0.0    1.159080
H      0.000000      '''+str(R)+'''      0.000000

*CFOUR(CALC=CCSD(T)
#EXCITE=EOMEE
#ESTATE_SYM=0/3/0/0
CC_PROG=VCC
CHARGE=-1
COORDINATES=CARTESIAN
BASIS=SPECIAL
REFERENCE=RHF
MEM_SIZE=90,MEM_UNIT=GB)

C:cc-pVTZ
C:cc-pVTZ
H:cc-pVTZ
H:cc-pVTZ
H:cc-pVTZ
H:cc-pVTZ
H:aug-cc-pVTZ

EOF


time xcfour
'''
	return string


for R in np.linspace(2, 10, num=121, endpoint=True):
	input = open("input"+str(round(R,6)),"w")
	input.write(infile(R))
	os.chmod("input"+str(round(R,6)), 0o775)
