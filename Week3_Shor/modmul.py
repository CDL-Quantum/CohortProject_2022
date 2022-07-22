import numpy as np
from qiskit.extensions import UnitaryGate

def unitary_for_ax_mod_N(a, N):
    dim = int(2**(np.ceil(np.log2(N))))
    A = np.zeros([dim,dim])
    for x in range(dim):
        fx = (x*a)%N
        A[x][fx]=1
    #######
    # DOESNT WORK. NEEDS TO BE UNITARY.
    U = np.block([[np.zeros([dim,dim]),A],[A.T,np.zeros([dim,dim])]])
    #######
    return U

def gate_for_ax_mod_N(a,N):
    '''
    Creates gate for use on log2(N)+1 qubits. The first qubit is an ancilla qubit,
    always has the state |0>. The rest of the qubits are the binary representation
    of x.
    '''
    U = unitary_for_ax_mod_N(a, N)
    gate = UnitaryGate(U)
    return gate