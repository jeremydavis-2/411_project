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
C 1
S   9   1.00
      6.665000D+03           6.920000D-04
      1.000000D+03           5.329000D-03
      2.280000D+02           2.707700D-02
      6.471000D+01           1.017180D-01
      2.106000D+01           2.747400D-01
      7.495000D+00           4.485640D-01
      2.797000D+00           2.850740D-01
      5.215000D-01           1.520400D-02
      1.596000D-01          -3.191000D-03
S   9   1.00
      6.665000D+03          -1.460000D-04
      1.000000D+03          -1.154000D-03
      2.280000D+02          -5.725000D-03
      6.471000D+01          -2.331200D-02
      2.106000D+01          -6.395500D-02
      7.495000D+00          -1.499810D-01
      2.797000D+00          -1.272620D-01
      5.215000D-01           5.445290D-01
      1.596000D-01           5.804960D-01
S   1   1.00
      1.596000D-01           1.000000D+00
S   1   1.00
      0.0469000              1.0000000
P   4   1.00
      9.439000D+00           3.810900D-02
      2.002000D+00           2.094800D-01
      5.456000D-01           5.085570D-01
      1.517000D-01           4.688420D-01
P   1   1.00
      1.517000D-01           1.000000D+00
P   1   1.00
      '''+str(round(0.1517/gamma*alp,7))+'''      1.0000000
P   1   1.00
      '''+str(round(0.1517/gamma/2*alp,7))+'''      1.0000000
D   1   1.00
      5.500000D-01           1.0000000
****
C 2
S   9   1.00
      6.665000D+03           6.920000D-04
      1.000000D+03           5.329000D-03
      2.280000D+02           2.707700D-02
      6.471000D+01           1.017180D-01
      2.106000D+01           2.747400D-01
      7.495000D+00           4.485640D-01
      2.797000D+00           2.850740D-01
      5.215000D-01           1.520400D-02
      1.596000D-01          -3.191000D-03
S   9   1.00
      6.665000D+03          -1.460000D-04
      1.000000D+03          -1.154000D-03
      2.280000D+02          -5.725000D-03
      6.471000D+01          -2.331200D-02
      2.106000D+01          -6.395500D-02
      7.495000D+00          -1.499810D-01
      2.797000D+00          -1.272620D-01
      5.215000D-01           5.445290D-01
      1.596000D-01           5.804960D-01
S   1   1.00
      1.596000D-01           1.000000D+00
S   1   1.00
      0.0469000              1.0000000
P   4   1.00
      9.439000D+00           3.810900D-02
      2.002000D+00           2.094800D-01
      5.456000D-01           5.085570D-01
      1.517000D-01           4.688420D-01
P   1   1.00
      1.517000D-01           1.000000D+00
P   1   1.00
      '''+str(round(0.1517/gamma*alp,7))+'''      1.0000000
P   1   1.00
      '''+str(round(0.1517/gamma/2*alp,7))+'''      1.0000000
D   1   1.00
      5.500000D-01           1.0000000
****
H 3
cc-pVDZ
****
H 4
cc-pVDZ
****
H 5
cc-pVDZ
****
H 6
cc-pVDZ
****
O 7
aug-cc-pVDZ
****
H 8
cc-pVDZ
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
