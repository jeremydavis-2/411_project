import psi4
import numpy as np

psi4.core.set_num_threads(4)
psi4.set_memory(int(10e9))
psi4.core.set_output_file('pes_output', True)


psi4.set_options({'reference':'RHF',
                  'basis':'cc-pvdz',
                  'roots_per_irrep':'[0,0,3,0]'})

psi4.basis_helper('''
        assign H cc-pvdz
        assign C cc-pvdz
        assign H7 aug-cc-pvdz''')

rs = np.linspace(0.2, 5, num=5, endpoint=True)
Es = []
for i, r in enumerate(rs):
    mol=psi4.geometry('''
        -1 1
        C       0.000000      0.0   -0.664500
        C       0.000000      0.0    0.664500
        H       0.962348      0.0   -1.159080
        H       0.962348      0.0    1.159080
        H      -0.962348      0.0   -1.159080
        H      -0.962348      0.0    1.159080
        H7       0.000000     '''+str(r)+'''    0.000000
        ''')

    psi4.core.clean()
    E, wfn = psi4.energy('ccsd', return_wfn=True)
    print(i,end=' ')
    Es.append(E)

print('\nRs')
for r in rs:
	print(r,end=',')

print('\nEs')
for E in Es:
	print(E,end=',')
