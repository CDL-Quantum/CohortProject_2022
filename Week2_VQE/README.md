![CDL 2022 Cohort Project](../CDL_logo.jpg)

## Project 2: VQE: Constructing potential energy surfaces for small molecules

This project will guide you through the state-of-the-art techniques for solving electronic structure problems on NISQ computers.


## Task 1: Generating PES using classical methods

[ Plots comparing accuracy of PES generated for different chemical species using different methods ]

### (1) The variational approach and its advantages

Among the classical methods introduced, HF, FCI, and truncated CI such as CISD are variational, while CCSD is not. The main advantage of the variational approach is that any energy calculated from it is never less than the true energy of the electronic state and system in question, i.e. the calculated energy is an upper bound to the true energy. Energies can be lowered systematically by increasing the size of the basis set, and the variational behavior serves as a helpful guide to the quality of the trial wavefunction $-$ the lower the energy the better the ansatz.

The arugument for a non-variational technique such as CCSD over, say, CISD is self-consistency (energy of n widely-separated atoms/molecules of the same species is the same as n times the energy of one of them; see below), which is a physical condition that should be met whenever possible. CCSD is also more accurate as it captures more of the correlation energy than CISD. CC methods also exhibit fast convergence to the (exact) FCI solution.

### (2) Separability/size-consistency of HF, CISD, and CCSD

[ Table comparing $E_{H_2 + H_2}$ with $2E_{H_2}$ for each of HF, CISD, and CCSD ]

### (3) Convergence to the exact non-relativistic electronic energies

[ Table of $E_{method} - E_{FCI}$ for a given basis set and different methods and $E_{basis}$ for a given method ]

## Task 2: Generating the qubit Hamiltonian

### (1) Requirements for a function of qubit operators to be a valid mapping for fermionic operators

For a mapping from fermionic operators to qubits operators to be valid, the way anti-commuting fermionic operators act on the fermion Fock space must be reproduced by the qubit operators acting on the qubit space. Furthermore, the anti-commutation relations that fermionic operators satisfy must also hold for the qubit operators.

### (2) Consequences of a real electronic Hamiltonian on the qubit Hamiltonian after the Jordan-Wigner transformation

### (3) Pros and cons of Bravyi-Kitaev vs Jordan-Wigner

## Task 3: Unitary transformations

### (1) Standard symmetries of the Hamiltonian preserved in (a) UCC and (b) QCC

(a) UCC preserves time-reversal $\mathcal{T}$, particle number $\hat{N}_e$, and spin projection $\hat{S}_z$. Total spin $\hat{S}$ and point-group symmetry (?)

(b) QCC preserves only $\mathcal{T}$.

### (2) Why symmetries are helpful

For a given symmetry, a unitary operator can be constructed to rotate the initial state to the particular symmetry eigenstate. Symmetries thus restrict the Hilbert space to a smaller subspace that conforms with them, thereby reducing the complexity of the porblem, making computation easier to perform.

### (3) Ways to restore symmetries broken by a unitary transformation

There are two ways to restore broken symmetries:

(i) Incorporate them as constraints in a variational estimator.

(ii) Use symmetry projectors to project into the appropriate symmetry subspaces.

## Task 4: Hamiltonian measurements

### (1) Optimal splitting of the total number of measurements between Hamiltonian fragments

With the total error of the Hamiltonian estimator bounded above by 
$|\langle\Psi|\hat{H}|\Psi\rangle - \bar{H}|^2 \leq \sum_n\frac{\sigma_{H_n}^2}{N_n}$ subject to the constraint $\sum_n N_n = N_T$ , the minimal bound is found by minimizing the function $L(\{N_n\},\lambda) = \sum_n\frac{\sigma_{H_n}^2}{N_n} + \lambda(\sum_n N_n - N_T)$ where $\lambda$ is the Lagrangian multiplier. Solving $\nabla L = 0$ to find the minimum, we have $\partial_{N_n}L = -\frac{\sigma_{H_n}^2}{N_n^2} + \lambda = 0 \implies N_n = \sqrt{\frac{\sigma_{H_n}^2}{\lambda}}$ for each n. The constraint equation then gives $\sqrt{\lambda} = \sum_n\sqrt{\sigma_{H_n}^2}/N_T$ , and we obtain:

(i) the optimal splitting: $N_n/N_T = \sqrt{\sigma_{H_n}^2}/\sum_n\sqrt{\sigma_{H_n}^2}$ ,

(ii) the minimal error bound: $|\langle\Psi|\hat{H}|\Psi\rangle - \bar{H}| \leq \sum_n\sqrt{\sigma_{H_n}^2}/\sqrt{N_T}$ .


### (2) Achieving 1 mHa accuracy for qubit-wise and full commuting partitionings

### (3) Achieving 1 mHa accuracy measuring $\hat{H}$ as a single operator

## Task 5: Use of quantum hardware

```
circ_0 = tq.circuit.compiler.compile_exponential_pauli_gate(U + U_0)
tq.draw(circ_0, backend="qiskit")
```

```
circ_1 = tq.circuit.compiler.compile_exponential_pauli_gate(U + U_1)
tq.draw(circ_1, backend="qiskit")
```

```
base_E = base_E_0 + base_E_1
```
```
-0.6913418867664956
```

```
post_E_1 = post_res_1.compute_expectationvalue(H_1)
```
```
-0.10685785786394145
```

## Further Challenges:

- How to obtain excited electronic states of the same or different symmetry?
- Partitioning in the fermionic operator space.
- Applying unitary transformations on the Hamiltonian.
- Compress larger basis sets into smaller number of qubits.

## Business Application

For each week, your team is asked to complete a Business Application. Questions you will be asked are:

- Explain to a layperson the technical problem you solved in this exercise.
- Explain or provide examples of the types of real-world problems this solution can solve.
- Identify at least one potential customer for this solution - ie: a business who has this problem and would consider paying to have this problem solved.
- Prepare a 90 second video explaining the value proposition of your innovation to this potential customer in non-technical language.

For more details refer to the [Business Application found here](./Business_Application.md)
