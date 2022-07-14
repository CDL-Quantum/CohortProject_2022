![CDL 2022 Cohort Project](../CDL_logo.jpg)

## Project 2: VQE: Constructing potential energy surfaces for small molecules

This project will guide you through the state-of-the-art techniques for solving electronic structure problems on NISQ computers.


## Task 1: Generating PES using classical methods

[ Plots comparing accuracy of PES generated for different chemical species using different methods ]

### The variational approach and its advantages
Among the classical methods introduced, HF, FCI, and truncated CI such as CISD are variational, while CCSD is not. The main advantage of the variational approach is that any energy calculated from it is never less than the true energy of the electronic state and system in question, i.e. the calculated energy forms and upper bound to the true energy. Energies can be lowered systematically by increasing the size of the basis set, and the variational behavior serves as a helpful guide to the quality of the trial wavefunction $-$ the lower the energy the better the ansatz.

### Separability/size-consistency of HF, CISD, and CCSD

[ Table comparing $E_{H_2 + H_2}$ with $2E_{H_2}$ for each of HF, CISD, and CCSD ]

### Convergence to the exact non-relativistic electronic energies

[ Table of $E_{method} - E_{FCI}$ for a given basis set and different methods and $E_{basis}$ for a given method ]

## Task 2: Generating the qubit Hamiltonian

### Requirements for a function of qubit operators to be a valid mapping from the fermionic operators

### Consequences of the time-reversal symmetry on the qubit Hamiltonian Jordan-Wigner transformed from the electronic Hamiltonian

### Pros and cons of Bravyi-Kitaev vs Jordan-Wigner

## Task 3: Unitary transformations

## Task 4: Hamiltonian measurements

## Task 5: Use of quantum hardware

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
