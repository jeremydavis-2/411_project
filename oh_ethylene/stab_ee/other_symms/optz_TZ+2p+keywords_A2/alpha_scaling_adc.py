#! /usr/bin/env python3
#ethylene geometry from CRC Handbook 102nd Edition

import string
import numpy as np
import subprocess
import sys
import os



job2 = '''$molecule
-1 1
C        -0.6645000000    0.0000000000    1.1619088658
C         0.6645000000    0.0000000000    1.1619088658
H        -1.1590800000    0.0000000000    0.1995598658
H         1.1590800000    0.0000000000    0.1995598658
H        -1.1590800000    0.0000000000    2.1242568658
H         1.1590800000    0.0000000000    2.1242568658
O         0.0000000000    0.0000000000   -1.5841414040
H         0.0000000000    0.0000000000   -2.5471307683
$end
$rem
   METHOD adc(2)
   BASIS gen
   PURECART 11
   EE_STATES [0,10,0,0]
   scf_convergence 8
   ADC_DAVIDSON_MAXITER 120
   ADC_DAVIDSON_MAXSUBSPACE 200
   adc_nguess_singles 100
   THRESH 14
   S2THRESH 14
   adc_davidson_conv 5
   adc_davidson_thresh 14
   THREADS 10
   MEM_TOTAL 95000
   STATE_ANALYSIS TRUE
$end'''


def basis(alp,gamma):
    bas ='''\n$basis
C     1
S    10   1.00
      8.236000D+03           5.310000D-04
      1.235000D+03           4.108000D-03
      2.808000D+02           2.108700D-02
      7.927000D+01           8.185300D-02
      2.559000D+01           2.348170D-01
      8.997000D+00           4.344010D-01
      3.319000D+00           3.461290D-01
      9.059000D-01           3.937800D-02
      3.643000D-01          -8.983000D-03
      1.285000D-01           2.385000D-03
S    1   1.00
      9.059000D-01           1.000000D+00
S    10   1.00
      8.236000D+03          -1.130000D-04
      1.235000D+03          -8.780000D-04
      2.808000D+02          -4.540000D-03
      7.927000D+01          -1.813300D-02
      2.559000D+01          -5.576000D-02
      8.997000D+00          -1.268950D-01
      3.319000D+00          -1.703520D-01
      9.059000D-01           1.403820D-01
      3.643000D-01           5.986840D-01
      1.285000D-01           3.953890D-01
S    1   1.00
      1.285000D-01           1.000000D+00
P    1   1.00
      3.827000D-01           1.000000D+00
P    5   1.00
      1.871000D+01           1.403100D-02
      4.133000D+00           8.686600D-02
      1.200000D+00           2.902160D-01
      3.827000D-01           5.010080D-01
      1.209000D-01           3.434060D-01
P    1   1.00
      1.209000D-01           1.000000D+00
P   1   1.00
      '''+str(round(0.1209/gamma*alp,7))+'''      1.0000000
P   1   1.00
      '''+str(round(0.1209/gamma/2*alp,7))+'''      1.0000000
D    1   1.00
      1.097000D+00           1.000000D+00
D    1   1.00
      3.180000D-01           1.000000D+00
F    1   1.00
      7.610000D-01           1.0000000
****
C     2
S    10   1.00
      8.236000D+03           5.310000D-04
      1.235000D+03           4.108000D-03
      2.808000D+02           2.108700D-02
      7.927000D+01           8.185300D-02
      2.559000D+01           2.348170D-01
      8.997000D+00           4.344010D-01
      3.319000D+00           3.461290D-01
      9.059000D-01           3.937800D-02
      3.643000D-01          -8.983000D-03
      1.285000D-01           2.385000D-03
S    1   1.00
      9.059000D-01           1.000000D+00
S    10   1.00
      8.236000D+03          -1.130000D-04
      1.235000D+03          -8.780000D-04
      2.808000D+02          -4.540000D-03
      7.927000D+01          -1.813300D-02
      2.559000D+01          -5.576000D-02
      8.997000D+00          -1.268950D-01
      3.319000D+00          -1.703520D-01
      9.059000D-01           1.403820D-01
      3.643000D-01           5.986840D-01
      1.285000D-01           3.953890D-01
S    1   1.00
      1.285000D-01           1.000000D+00
P    1   1.00
      3.827000D-01           1.000000D+00
P    5   1.00
      1.871000D+01           1.403100D-02
      4.133000D+00           8.686600D-02
      1.200000D+00           2.902160D-01
      3.827000D-01           5.010080D-01
      1.209000D-01           3.434060D-01
P    1   1.00
      1.209000D-01           1.000000D+00
P   1   1.00
      '''+str(round(0.1209/gamma*alp,7))+'''      1.0000000
P   1   1.00
      '''+str(round(0.1209/gamma/2*alp,7))+'''      1.0000000
D    1   1.00
      1.097000D+00           1.000000D+00
D    1   1.00
      3.180000D-01           1.000000D+00
F    1   1.00
      7.610000D-01           1.0000000
****
H 3
cc-pVTZ
****
H 4
cc-pVTZ
****
H 5
cc-pVTZ
****
H 6
cc-pVTZ
****
O 7
aug-cc-pVTZ
****
H 8
cc-pVTZ
****
$end'''
    return bas

gamma = 3.5
alpf = gamma/5.5 # default 4.5, 5.5 for extended alp range
alpi = gamma/1.5
num = 41
CurrDir = os.getcwd()
for alp in np.linspace(alpi, alpf, num=num, endpoint=True):
    input = open("input"+str(round(alp,6)),"w")
    #input.write(job1+basis(alp,gamma)+'\n@@@\n'+job2+basis(alp,gamma))
    input.write(job2+basis(alp,gamma))

    #output = open("output"+str(round(alp,6)),"w")
    #with open("output"+str(round(alp,6)),"w") as fout:
    #    subprocess.call(['qchem',str(CurrDir+'/'+input.name)],stdout=fout,shell=True)

    # output = open("output"+str(round(alp,6)),"w")
    # subprocess.call(['echo',input.name, '>', output.name])
    #subprocess.call('qchem tempfile >output-'+str(round(alp,4)))
