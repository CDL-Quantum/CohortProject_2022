![CDL 2022 Cohort Project](../CDL_logo.jpg)

## Project 2: VQE: Constructing potential energy surfaces for small molecules

This project will guide you through the state-of-the-art techniques for solving electronic structure problems on NISQ computers.


## Task 1: Generating PES using classical methods

PESs were generated for all of the model diatomic systems (H$_2$, LiH, H$_2$O$, N$_2$, H$_4$), using all of the suggested classical electronic structure methods, i.e.: Hartree-Fock (HF); configuration interaction singles and doubles (CISD); coupled cluster singles and doubles (CCSD); full configuration interaction (FCI). All of these calculations were performed using a minimal STO-3G basis set. In that sense, the FCI calculations are of course still far from "exact", in that we are still very far from the complete basis set limit. Nevertheless, these will serve as illustrative examples. 

Below we present the computed PESs using all methods for all systems, separated into strongly correlated and weakly correlated categories. Please consult the notebook [S1-sol.ipynb](https://github.com/FoggyBrain/CohortProject_2022/blob/main/Week2_VQE/S1-sol.ipynb), where the work was actually performed. 

### PES for weakly correlated systems (H$_2$, LiH)

![fig1](https://github.com/FoggyBrain/CohortProject_2022/blob/main/Week2_VQE/h2PES.png)
![fig2](https://github.com/FoggyBrain/CohortProject_2022/blob/main/Week2_VQE/lihPES.png)

### PES for strongly correlated systems (H$_2$O$, N$_2$, H$_4$)

![fig3](https://github.com/FoggyBrain/CohortProject_2022/blob/main/Week2_VQE/h2oPES.png)
![fig4](https://github.com/FoggyBrain/CohortProject_2022/blob/main/Week2_VQE/n2PES.png)
![fig5](https://github.com/FoggyBrain/CohortProject_2022/blob/main/Week2_VQE/h4PES.png)

The results are as expected. In particular, only FCI performs well as the molecules dissociate, in the case of the strongly correlated systems. Also, the CCSD method, being a coupled-pair theory, is clearly seen to be non-variational, as evidenced by computed energy values that are below the FCI values. All other methods are "variational" however (although that does not really mean much in the case of HF), in the sense that the results are larger than the FCI values. Also, HF always fails completely as one approaches the dissociation limit, even for the weakly correlated systems. This is primarily because restricted HF is being used, whose restrictive assumption is appropriate for chemical bonding but entirely inappropriate in bond-breaking situations.  Actually, this can be fruitfully thought of in symmetry terms, as will be discussed more later in the size consistency section.  

### (1) The variational approach and its advantages

Among the classical methods introduced, HF, FCI, and truncated CI such as CISD are variational, while CCSD is not. The main advantage of the variational approach is that any energy calculated from it is never less than the true energy of the electronic state and system in question, i.e. the calculated energy is an upper bound to the true energy. Energies can be lowered systematically by increasing the size of the basis set, and the variational behavior serves as a helpful guide to the quality of the trial wavefunction $-$ the lower the energy the better the ansatz.

The argument for a using a non-variational technique such as CCSD over, say, CISD is self-consistency (energy of n widely-separated atoms/molecules of the same species is the same as n times the energy of one of them; see below), which is a physical condition that should be met whenever possible. CCSD is also generally more accurate as it captures more of the correlation energy than CISD. CC methods also exhibit fast convergence to the FCI  solution.

All of that said, the best approach is clearly always FCI. It is conceptually simplest, most accurate, size-consistent, AND variational. Of course, the main difficulty with FCI is that the computational complexity scales exponentially with problem size.  Coming from the quantum dynamics community, rather than the electronic structure community, our philosophy is that, rather than tinker with different approximations that have their various pros and cons in terms of desirable (really essential) features that one has to give up, it is better to address the exponential scaling problem head on. In particularly, we have developed a methodology and proprietary code, Andromeda, that to date have been applied to FCI calculations with up to 10$^{18}$ basis functions. As part of this cohort challenge, we have used Andromeda to compute FCI calculations for the most challenging of the above systems (N$_2$) as will be reported on elsewhere in this document.  

### (2) Size-consistency of HF, CISD, and CCSD

<div align="center">

| Method | $2E_{H_2}$ | $E_{H_2+H_2}$ | $E_{H_2+H_2}-2E_{H_2}$ | Size-consistent |
| --- | --- | --- | :---: | :---: |
| HF   | -2.23341227 | -2.23341227 | $2.35189646*10^{-12}$ | Y |
| CCSD | -2.27454914 | -2.27454907 | $7.57789431*10^{-8}$  | Y |
| CISD | -2.27454881 | -2.27403870 | $5.10108724*10^{-4}$  | N |
     
</div>

The table above shows the difference between the energy (in units of Hartree) calculated using different methods, for the H$_2$ dimer (with the two H$_2$'s separated by a large distance of 100 $\unicode{x212B}$) vs. twice that of a single H$_2$. Physically, when separation tends to infinity, identical molecules would not affect each other, and the energy of the whole should be the sum of each individual molecule. This exercise is thus a simple test of size consistency, as described above. From this calculation, we see that HF and CCSD reproduce this behavior to a very high accuracy, and are thus ***size-consistent***, whereas CISD is not. 

The reason why CISD is not size-consistent is because of the basis set truncation that it applies. In particular, it includes only configurations/basis functions with single and double excitations. While these are naturally the most important (besides the ground configuration) for computing the ground electronic state, this truncation of the FCI basis set introduces a type of "basis truncation correlation" that does not properly respect the symmetry of the separated fragments. Note that the fragment symmetry is different from, and greater than, the symmetry of the combined molecule itself. To be sure, all HF and post-HF methods automatically respect the symmetry of the molecule itself (e.g. in the calculation of HF molecular orbitals), but not necessarily that of the fragments. In technical  terms, a proper understanding of the fragment symmetry in relation to that of the molecule is achieved through the use of group theory correlation tables.  Note that the greater symmetry of the fragments always leads to increased degeneracy of energy levels. It is for this reason that different PES curves often correlate to the same value asymptotically $-$ at least in principle, when a suitable computational method is employed.

CCSD, in contrast, being a coupled-pair theory, is size-consistent by design. So not surprisingly, it achieves size-consistency in the above exercise to better than $10^{-7}$ Hartree $-$ i.e., a full four orders of magnitude better than CISD. What is perhaps at first glance remarkable is that HF is by far the best at achieving size consistency $-$ all the way down to $10^{-12}$ Hartree! This can be understood based on two properties. First, from a purely mathematical standpoint, the fact that there is only one basis function implies that we do not have any correlated basis truncation. Second, as more of a technical point, we are actually using restricted HF rather than unrestricted. So this means we have to be very careful in terms of the examples we consider. For example, as seen in part 1 above, we know full well that restricted HF is not "size consistent" when applied to the dissociation of the H$_2$ molecule into two H atom fragments! That is because the H atom fragments themselves are clearly open-shell species. In order to observe size-consistency with restricted HF, it is necessary to apply the method to a system for which all of the fragments are themselves closed-shell systems $-$ which is no doubt the reason why H$_2$ dimer was chosen for this particular exercise...

### (3) Convergence to the exact non-relativistic electronic energies

<div align="center">
     
| Basis | sto3g | cc-pVDZ | cc-pVTZ | cc-pVQZ | cc-pV5Z |
| --- | --- | --- | --- | --- | --- |
| $E_{HF}$      | -1.11670614 | -1.12871101 | -1.13295914 | -1.13345751 | -1.13360663 |
| $E_{CISD}$    | -1.13727441 | -1.16340296 | -1.17233494 | -1.17379598 | -1.17422279 |
| $E_{CCSD}$    | -1.13727457 | -1.16340297 | -1.1723349  | -1.17379598 | -1.17422279 |
| $E_{CCSD(T)}$ | -1.13727457 | -1.16340297 | -1.1723349  | -1.17379598 | -1.17422279 |
| $E_{FCI}$     | -1.13727441 | -1.16340296 | -1.17233494 | -1.17379598 | -1.17422279 |

</div>

The table above shows the energy (in unit of Hartree) of H$_2$ calculated using different methods and basis sets. We see that for a given basis, the more electronic correlation is accounted for by a method, the closer it gets to the FCI value (note that for H$_2$ CISD gives the FCI value). While for a given method, the larger the basis the lower the calculated energy. Note that all post-HF methods using the cc-pVQZ and cc-pV5Z basis sets are within $10^{-3}$ Hartree to the experimental value of -1.17377 Hartree.

In principle, one would expect the FCI calculation with the largest basis set (i.e. closest to complete basis set limit) to be closest to experiment. However, we must recall that we are also running into the limits of the Born-Oppenheimer approximation; in reality, non-Born-Oppenheimer transitions and nuclear quantum effects also play a role in any experimental measurement. 


## Task 2: Generating the qubit Hamiltonian

Please see [S5_circuit_qec.ipynb](https://github.com/FoggyBrain/CohortProject_2022/blob/main/Week2_VQE/S5_circuit_qec.ipynb) for examples of generating qubit Hamiltonians. In particular, we have used the Jordan-Wigner mapping in the full CI space, i.e. without using any qubit tapering. Additional discussion may be found in the Task 5 section, as well.

### (1) Requirements for a function of qubit operators to be a valid mapping for fermionic operators

For a mapping from fermionic operators to qubits operators to be valid, it becomes necessary and sufficient to find a way to represent annihilation and creation operators from the Fock space as spin operators on the qubit space. In particular, the anti-commuting fermionic operator relationships must be properly satisfied in the qubit or spin-based representation.  In practice, this means introducing a kind of "non-locality", in that creation and annihilation of occupation for a specific configuration, i, is accompanied with a phase change that depends on the values of other configurations, j.  The precise manner in which this happens depends on the particular mapping used. For Jordan-Wigner, it is the occupations of the j<i that govern the phase shift. For Bravyi-Kitaev, the phase change is designed to be more local.  

### (2) Consequences of a real electronic Hamiltonian on the qubit Hamiltonian after the Jordan-Wigner transformation

All Hamiltonians in quantum mechanics are necessarily Hermitian operators, representable as Hermitian matrices.  If, however, the Hamiltonian also satisfies time-reversal symmetry, then it can be shown that it is always possible to represent the Hamiltonian as a real-valued matrix--which, given the further condition of Hermiticity, implies a real symmetric matrix. Given that the Jordan-Wigner transformation replaces creation and annihilation operators with tensor products of spin operators on the multi-qubit space, it becomes clear that each spin-product term or "Pauli word" in the Hamiltonian should be expressible using an $even$ number of $y$ spin (i.e. $\hat\sigma_y$) operators. Otherwise, there would have to be imaginary contributions to the matrix elements.

### (3) Pros and cons of Bravyi-Kitaev (BK) compared to Jordan-Wigner (JW) encoding

***Pros***: BK gives rise to more local qubit Hamiltonians than does JW. In particular, JW mapping requires a non-local mapping across essentially the entire lattice (i.e., for all j < i, which implies the entire lattice if i adopts the maximal value). The hope is that this would somehow translate into a reduction of gate count on a quantum computer, especially for entangled or two-qubit gates.   

***Cons***: In practice, BK appears to offer no real computational advantage on quantum computers within the context of the most popular eigensolver, VQE. Whatever advantage the locality of BK provides may be somewhat undermined by Trotterization. Also, BK makes a sacrifice on the locality of occupation number operator, in favor of increasing locality for processing parity information. In JW, the occupation number of a spin orbital is stored locally and the parity nonlocally; but in BK, the orbitals store partial sums of occupation numbers. The qubit operators are also considerably more complicated in BK than in JW.   

***Further Question***: on quantum computing architectures with limited topologies, where not every pair of qubits can be directly coupled together in a two-qubit gate: would BK with VQE possibly present an advantage in this context?

## Task 3: Unitary transformations

Again, for coding examples where we have used unitary transformations to simulate VQE solution on a quantum computer, please consult the notebook [S5_circuit_qec.ipynb](https://github.com/FoggyBrain/CohortProject_2022/blob/main/Week2_VQE/S5_circuit_qec.ipynb).


### (1) Standard symmetries of the Hamiltonian preserved in (a) UCC and (b) QCC

(a) In principle, UCC preserves time-reversal $\mathcal{T}$, particle number $\hat{N}_e$, and spin projection $\hat{S}_z$. It should also be possible, working in a spin-symmetry adapted basis, to preserve total spin symmetry, $\hat{S}^2$ as well. As for point-group symmetry, this should be automatically satisfied by the underlying Fock operator solutions, used to define the molecular orbitals of the calculation. If you have, for example, two MOs that are doubly-degenerate by point-group symmetry, then both should be included in the MO set, and both will be singly or doubly excited in the same manner. So UCC should preserve point group symmetry as well. 

(b) QCC certainly preserves $\mathcal{T}$. For this approach, the way that individual Pauli words are chosen is based on the magnitude of the commutator of a given Pauli word operator with the Hamiltonian.  If this is sufficiently large, then that particular Pauli word operator is retained. Since it is directly based on energy, then degenerate MOs will be treated identically in this framework, and therefore again, point group symmetry should be respected. Beyond that, QCC respects the remaining symmetries less well than UCC. In principle, they might be conserved, but unlike UCC the QCC implementation makes no attempt to ensure that symmetry is in fact preserved. The advantage, however, is that QCC requires fewer quantum gates.  

### (2) Why symmetries are helpful

For a given symmetry, a unitary operator can be constructed to rotate the initial state to the particular symmetry eigenstate. Symmetries thus restrict the Hilbert space to a smaller subspace that conforms with them, thereby reducing the complexity of the problem, making computation easier to perform. Symmetries are also useful as a "check" on such transformations, after the fact. 

### (3) Ways to restore symmetries broken by a unitary transformation

For restorimg broken symmetries there are at least two options:

(i) Construct and apply symmetry projectors to move into subspaces preserving the symmetries in question, or

(ii) Incorporate the symmetries as constraints in a variational formulation.

There is also a simple way to mitigate errors based on symmetry, that can be applied post-measurement, as discussed in Task 5.

## Task 4: Hamiltonian measurements

Again, the splitting of the Hamiltonian terms into a minimal number of measurement groups has been applied in the notebook
[S5_circuit_qec.ipynb](https://github.com/FoggyBrain/CohortProject_2022/blob/main/Week2_VQE/S5_circuit_qec.ipynb). Please see also additional discussion in the Task 5 section.

### (1) Optimal splitting of the total number of measurements between Hamiltonian fragments

With the total error of the Hamiltonian estimator bounded above by 
$|\langle\Psi|\hat{H}|\Psi\rangle - \bar{H}|^2 \leq \sum_n\frac{\sigma_{H_n}^2}{N_n}$ subject to the constraint $\sum_n N_n = N_T$ , the minimal bound is found by minimizing the function $L(\{N_n\},\lambda) = \sum_n\frac{\sigma_{H_n}^2}{N_n} + \lambda(\sum_n N_n - N_T)$ where $\lambda$ is the Lagrangian multiplier. Solving $\nabla L = 0$ to find the minimum, we have $\partial_{N_n}L = -\frac{\sigma_{H_n}^2}{N_n^2} + \lambda = 0 \implies N_n = \sqrt{\frac{\sigma_{H_n}^2}{\lambda}}$ for each n. The constraint equation then gives $\sqrt{\lambda} = \sum_n\sqrt{\sigma_{H_n}^2}/N_T$ , and with this we obtain

(i) the optimal splitting: $N_n/N_T = \sqrt{\sigma_{H_n}^2}/\sum_n\sqrt{\sigma_{H_n}^2}$ ,

(ii) the minimal error bound: $|\langle\Psi|\hat{H}|\Psi\rangle - \bar{H}| \leq \sum_n\sqrt{\sigma_{H_n}^2}/\sqrt{N_T}$ .

### (2) Achieving $10^{-3}E_h$ accuracy for qubit-wise and full commuting partitionings

From the minimal error bound above, the total number of measurements need to achieve a given error tolerance, $\epsilon_T$, is

<p align="center">
$N_T = \left(\sum_n\sqrt{\sigma_{H_n}^2}\right)^2 / \epsilon_T$. 
</p>

To calculate $N_T$, we also need to know the fragment variances, $\sigma_{H_n}$, which we can estimate using the wavefunction obtained by classical methods. In [S4-sol.ipynb](https://github.com/FoggyBrain/CohortProject_2022/blob/main/Week2_VQE/S4-sol.ipynb), we carried out the calculation for the H$_2$ molecular using both QWC and FC partitionings. We find for H$_2$ at equilibrium ($r_0 = 0.741\unicode{x212B}$), an error tolerance of 
$\epsilon_T = 10^{-3}E_h$ requires the following number of measurements:

<div align="center">
     
| H$_2$ | QWC | FC |
| --- | --- | --- |
| $N_T$ | 31208 | 32929 |
     
</div>

Note that for FC, there are two measurement groupings: the first corresponding to all $z$ spin operations (thus, the original basis representation suffices for measurement and no transformation is required), and the second consisting of all $x$ and $y$ spin operations. But in the STO-3G basis, there are are only four such terms in the second grouping.  As it happens, none of these terms has the same spin (or no) operations for all qubits. This means that each individual term comprises its own QWC grouping. In contrast, the first grouping from FC also satisfies qubit-wise commutativity. Thus, the QWC calculation involves five groupings in all: four from the second FC grouping, plus the first FC grouping. 

### (3) Achieving $10^{-3}E_h$ accuracy measuring $\hat{H}$ as a single operator

Suppose we can prepare without error an exact energy eigenstate to the Hamiltonian $|\psi\rangle$ such that $H|\psi\rangle = E|\psi\rangle$, then

<p align="center">
$\sigma_H^2 = \langle\psi|\hat{H}^2|\psi\rangle - \langle\psi|\hat{H}|\psi\rangle^2 = E^2 - E^2 = 0$ ,
</p>

and so $N_T = 1$ would suffice.

## Task 5: Use of quantum hardware

### (1) Implementing the post-processing protocol

#### Introduction

For this question, we were tasked to implement an error mitigation protocol that is based on removing measurement results corresponding to the wrong number of electrons, as described in the reference below:

Ilya G. Ryabinkin, Scott N. Genin, and Artur F. Izmaylov. Constrained variational quantum eigensolver: Quantum computer search engine in the Fock space. J. Chem. Theory Comput. 2019, 15(1), 249 - 255.

Our full implementation using the code can be found in the notebook 
[S5_circuit_qec.ipynb](https://github.com/FoggyBrain/CohortProject_2022/blob/main/Week2_VQE/S5_circuit_qec.ipynb), so please view it for full details. We use the hydrogen molecule as an example to test the error mitigation protocol, and to see the effects of the error mitigation, we want to see three different results: firstly, the correct expectation value; secondly, the expectation value without the post processing error mitigation protocol; and thirdly, the expectation value after implementing said protocol. As we had learnt previously in the last few steps, we can easily find the correct expectation value using tequila:

```
print("The correct expectation value is: ", tq.simulate(E, variables=vars))
```

```
The correct expectation value is: -0.9486411121761621
```

#### Split Hamiltonians by Measurement Groups

To implement the error mitigation protocol, we are going to need to see the measurement results of the sample directly. As we had learnt in step 4, we split it up into measurement groups (which in this case there are 2), and use that as the measurement protocol to view the measurement results.

```
binary_H = BinaryHamiltonian.init_from_qubit_hamiltonian(H)
commuting_parts = binary_H.commuting_groups()
print(The first group is: ", commuting_parts[0].to_qubit_hamiltonian())
print(The second group is: ", commuting_parts[1].to_qubit_hamiltonian())
```

```
The first group is: -0.5339+0.0673Z(0)+0.0673Z(1)+0.0067Z(2)+0.0067Z(3)+0.1274Z(0)Z(1)+0.0650Z(0)Z(2)+0.1298Z(0)Z(3)+0.1298Z(1)Z(2)+0.0650Z(1)Z(3)+0.1337Z(2)Z(3)

The second group is: -0.0648X(0)X(1)Y(2)Y(3)+0.0648X(0)Y(1)Y(2)X(3)+0.0648Y(0)X(1)X(2)Y(3)-0.0648Y(0)Y(1)X(2)X(3)

```

To measure each group independently, we implemented a function to split the Hamiltonians by measurement group, which also introduced different measurement protocols. We can see the different circuits that will be implemented for each measurement group:

```
circ_0 = tq.circuit.compiler.compile_exponential_pauli_gate(U + U_0)
tq.draw(circ_0, backend="qiskit")
```

```
     ┌────────────────────┐┌─────────────────────┐┌──────────┐               »
q_0: ┤ Rx(f((beta_0,))_0) ├┤ Rz(f((gamma_0,))_1) ├┤ Ry(-π/2) ├──■────────────»
     ├────────────────────┤├─────────────────────┤├─────────┬┘┌─┴─┐          »
q_1: ┤ Rx(f((beta_1,))_2) ├┤ Rz(f((gamma_1,))_3) ├┤ Rx(π/2) ├─┤ X ├──■───────»
     ├────────────────────┤├─────────────────────┤├─────────┴┐└───┘┌─┴─┐     »
q_2: ┤ Rx(f((beta_2,))_4) ├┤ Rz(f((gamma_2,))_5) ├┤ Ry(-π/2) ├─────┤ X ├──■──»
     ├────────────────────┤├─────────────────────┤├──────────┤     └───┘┌─┴─┐»
q_3: ┤ Rx(f((beta_3,))_6) ├┤ Rz(f((gamma_3,))_7) ├┤ Ry(-π/2) ├──────────┤ X ├»
     └────────────────────┘└─────────────────────┘└──────────┘          └───┘»
c: 4/════════════════════════════════════════════════════════════════════════»
                                                                             »
«                                                     ┌─────────┐ 
«q_0: ──────────────────────────────────────────■─────┤ Ry(π/2) ├─
«                                             ┌─┴─┐   ├─────────┴┐
«q_1: ───────────────────────────────■────────┤ X ├───┤ Rx(-π/2) ├
«                                  ┌─┴─┐   ┌──┴───┴──┐└──────────┘
«q_2: ───────────────────────■─────┤ X ├───┤ Ry(π/2) ├────────────
«     ┌───────────────────┐┌─┴─┐┌──┴───┴──┐└─────────┘            
«q_3: ┤ Rz(f((tau_0,))_8) ├┤ X ├┤ Ry(π/2) ├───────────────────────
«     └───────────────────┘└───┘└─────────┘                       
«c: 4/════════════════════════════════════════════════════════════
«
```

The first measurement group basically has nothing to change the measurement basis since it is all in the Z basis.

```
circ_1 = tq.circuit.compiler.compile_exponential_pauli_gate(U + U_1)
tq.draw(circ_1, backend="qiskit")
```
```
q_0: ┤ Rx(f((beta_0,))_0) ├┤ Rz(f((gamma_0,))_1) ├┤ Ry(-π/2) ├──■────────────»
     ├────────────────────┤├─────────────────────┤├─────────┬┘┌─┴─┐          »
q_1: ┤ Rx(f((beta_1,))_2) ├┤ Rz(f((gamma_1,))_3) ├┤ Rx(π/2) ├─┤ X ├──■───────»
     ├────────────────────┤├─────────────────────┤├─────────┴┐└───┘┌─┴─┐     »
q_2: ┤ Rx(f((beta_2,))_4) ├┤ Rz(f((gamma_2,))_5) ├┤ Ry(-π/2) ├─────┤ X ├──■──»
     ├────────────────────┤├─────────────────────┤├──────────┤     └───┘┌─┴─┐»
q_3: ┤ Rx(f((beta_3,))_6) ├┤ Rz(f((gamma_3,))_7) ├┤ Ry(-π/2) ├──────────┤ X ├»
     └────────────────────┘└─────────────────────┘└──────────┘          └───┘»
c: 4/════════════════════════════════════════════════════════════════════════»
                                                                             »
«                                                     ┌─────────┐      »
«q_0: ──────────────────────────────────────────■─────┤ Ry(π/2) ├───■──»
«                                             ┌─┴─┐   ├─────────┴┐  │  »
«q_1: ───────────────────────────────■────────┤ X ├───┤ Rx(-π/2) ├──┼──»
«                                  ┌─┴─┐   ┌──┴───┴──┐└──────────┘  │  »
«q_2: ───────────────────────■─────┤ X ├───┤ Ry(π/2) ├──────────────┼──»
«     ┌───────────────────┐┌─┴─┐┌──┴───┴──┐└─────────┘            ┌─┴─┐»
«q_3: ┤ Rz(f((tau_0,))_8) ├┤ X ├┤ Ry(π/2) ├───────────────────────┤ X ├»
«     └───────────────────┘└───┘└─────────┘                       └───┘»
«c: 4/═════════════════════════════════════════════════════════════════»
«                                                                      »
«                      ┌──────────┐                      ┌──────────┐»
«q_0: ──────────────■──┤ Rx(-π/2) ├──■────────────────■──┤ Ry(-π/2) ├»
«                   │  └──────────┘  │                │  └──────────┘»
«q_1: ──────────────┼────────────────┼────────────────┼───────■──────»
«                   │                │                │       │      »
«q_2: ──────────────┼────────────────┼────────────────┼───────┼──────»
«     ┌──────────┐┌─┴─┐            ┌─┴─┐┌──────────┐┌─┴─┐   ┌─┴─┐    »
«q_3: ┤ Rz(-π/2) ├┤ X ├────────────┤ X ├┤ Rz(-π/2) ├┤ X ├───┤ X ├────»
«     └──────────┘└───┘            └───┘└──────────┘└───┘   └───┘    »
«c: 4/═══════════════════════════════════════════════════════════════»
«                                                                    »
«                                                                    »
«q_0: ───────────────────────────────────────────────────────────────»
«                      ┌──────────┐                      ┌──────────┐»
«q_1: ──────────────■──┤ Rx(-π/2) ├──■────────────────■──┤ Ry(-π/2) ├»
«                   │  └──────────┘  │                │  └──────────┘»
«q_2: ──────────────┼────────────────┼────────────────┼───────■──────»
«     ┌──────────┐┌─┴─┐            ┌─┴─┐┌──────────┐┌─┴─┐   ┌─┴─┐    »
«q_3: ┤ Rz(-π/2) ├┤ X ├────────────┤ X ├┤ Rz(-π/2) ├┤ X ├───┤ X ├────»
«     └──────────┘└───┘            └───┘└──────────┘└───┘   └───┘    »
«c: 4/═══════════════════════════════════════════════════════════════»
«                                                                    »
«                                                                              »
«q_0: ─────■───────────────────────────────────────────────────────────────────»
«        ┌─┴─┐                                                                 »
«q_1: ───┤ X ├─────────────────────────────────────────────────────────■───────»
«        └───┘         ┌──────────┐                      ┌──────────┐┌─┴─┐     »
«q_2: ──────────────■──┤ Rx(-π/2) ├──■────────────────■──┤ Ry(-π/2) ├┤ X ├──■──»
«     ┌──────────┐┌─┴─┐└──────────┘┌─┴─┐┌──────────┐┌─┴─┐├──────────┤└───┘┌─┴─┐»
«q_3: ┤ Rz(-π/2) ├┤ X ├────────────┤ X ├┤ Rz(-π/2) ├┤ X ├┤ Ry(-π/2) ├─────┤ X ├»
«     └──────────┘└───┘            └───┘└──────────┘└───┘└──────────┘     └───┘»
«c: 4/═════════════════════════════════════════════════════════════════════════»
«                                                                              »
«                                             ┌─────────┐ ┌──────────┐     »
«q_0: ─────────────────────────────────■──────┤ Ry(π/2) ├─┤ Ry(-π/2) ├──■──»
«                                    ┌─┴─┐    ├─────────┤ ├──────────┤┌─┴─┐»
«q_1: ──────────────────────■────────┤ X ├────┤ Ry(π/2) ├─┤ Ry(-π/2) ├┤ X ├»
«                         ┌─┴─┐   ┌──┴───┴──┐ ├─────────┴┐└──────────┘└───┘»
«q_2: ──────────────■─────┤ X ├───┤ Ry(π/2) ├─┤ Ry(-π/2) ├─────────────────»
«     ┌──────────┐┌─┴─┐┌──┴───┴──┐├─────────┴┐├──────────┤                 »
«q_3: ┤ Rz(-π/2) ├┤ X ├┤ Ry(π/2) ├┤ Rz(-π/2) ├┤ Ry(-π/2) ├─────────────────»
«     └──────────┘└───┘└─────────┘└──────────┘└──────────┘                 »
«c: 4/═════════════════════════════════════════════════════════════════════»
«                                                                          »
«                                                      ┌─────────┐ ┌──────────┐»
«q_0: ───────────────────────────────────────────■─────┤ Ry(π/2) ├─┤ Rz(-π/2) ├»
«                                              ┌─┴─┐   ├─────────┤ ├──────────┤»
«q_1: ──■─────────────────────────────■────────┤ X ├───┤ Ry(π/2) ├─┤ Rz(-π/2) ├»
«     ┌─┴─┐                         ┌─┴─┐   ┌──┴───┴──┐├─────────┴┐├──────────┤»
«q_2: ┤ X ├──■────────────────■─────┤ X ├───┤ Ry(π/2) ├┤ Rz(-π/2) ├┤ Rx(-π/2) ├»
«     └───┘┌─┴─┐┌──────────┐┌─┴─┐┌──┴───┴──┐└─────────┘└──────────┘└──────────┘»
«q_3: ─────┤ X ├┤ Rz(-π/2) ├┤ X ├┤ Ry(π/2) ├───────────────────────────────────»
«          └───┘└──────────┘└───┘└─────────┘                                   »
«c: 4/═════════════════════════════════════════════════════════════════════════»
«                                                                              »
«     ┌──────────┐┌──────────┐
«q_0: ┤ Rx(-π/2) ├┤ Rz(-π/2) ├
«     ├──────────┤├──────────┤
«q_1: ┤ Rx(-π/2) ├┤ Rz(-π/2) ├
«     ├──────────┤└──────────┘
«q_2: ┤ Rz(-π/2) ├────────────
«     └──────────┘            
«q_3: ────────────────────────
«                             
«c: 4/════════════════════════
«                             
```

On the other hand, the second measurement group has to have quite a long circuit appended to the end, to change the measurement basis to fit the measurement group.  

Using the classical simulation route, 100,000 trials were used for each measurement group. The following number of measurements were obtained for each outcome:

first measurement group: 		+28837.0000|0011> +71163.0000|1100>
second measurement group:		+4709.0000|1100> +95291.0000|1101> 

Before moving on to the quantum computation, some further discussion here is in order, as it is relevant for what follows. First off, it is important for our purposes that there are only two measurement groups, and not more. Second, it is quite a remarkable fact that the minimal clique approach in this case is even able to reduce things down to just two groups, or fully connected subgraphs. As discussed in the references, this implies a set of commuting operators--but not necessarily qubit-wise commuting. This distinction turns out to be extremely important. Of course, for the first measurement group, comprised of just z operators across various qubit combinations, it is obvious that they must form a commuting set. As mentioned, these operators are all diagonal in the default Z representation, so there is no need even to change the representation in order to perform a measurement.  Equally importantly, assuming that the default representation is indeed the requested  Wigner-Jordan-mapped qubit representation, then these basis functions must respect both particle number symmetry and Sz symmetry (where Sz refers to the spins of the individual electrons).  

Actually, as an aside, we point out that there is some evidence to suggest that in fact, we are not working directly with a basis of Slater determinants of spin-up and spin-down sigma and sigma* orbitals, as would be implied for a true Wigner-Jordan STO-3G basis as requested in our code. Rather, it seems that we may somehow be working with a spin-symmetry-adapted version of said basis, for which the overall Shat^2 spin symmetry (i.e., singlet or triplet, but in this case triplet) is also respected. This is evidenced by the fact that if the lowest-lying configuration is |1100>, as indicated by the first measurement group results above (the second group cannot be relied on for this analysis, for reasons given below), then the next-highest-amplitude contributing Slater determinants should be |1001> and |0110>, with equal weights, corresponding to the singly-excited singlet state.  Instead, only |0011> appears in the expansion, which would correspond to the doubly-excited singlet state. It therefore seems likely that in fact, |0011> by itself, refers to the symmetry-adapted linear combination corresponding to the singly-excited singlet state.

In any event, what matters most for our purposes is that the transformation from STO-3G to spin-symmetry-adapted basis (if indeed, such a transformation has been applied without our knowledge) itself respects particle number symmetry. Consequently, in either basis, it is the set of qubit basis functions with two zeros and two ones, that presumably corresponds to the actual two-electron system of interest. There are six such basis functions/Slater Determinants in all, i.e. |0011>, |1100>, |0101>, |0110>, |1010>, and |1001>.  

Now we consider the second measurement group, consisting of various combinations of z and y operators, again across various qubit combinations. This set clearly does not satisfy qubit-wise commutativity. Nevertheless, it is remarkable that it satisfies commutativity as a whole. This can be easily verified by observing that the four "Pauli words"--i.e., xxyy, xyyx, yxxy, and yyxx (where the order of characters in each word refers to the order of the qubits, 0123)---all differ from each other by an even number of qubits, either 2 or 4. Of course, it is necessary to transform to a new representation in terms of which these take the form of z operators, prior to measurement. As  discussed, this leads to the extended circuit described above. Unfortunately, the unitary transform necessary to implement this change of basis is quite complicated and difficult to follow. Also, it does not treat all four qubits equally, as the final q3 qubit has many more gates than the others. We understand there is a "method to the madness" involving Clifford gates and such, as described in the literature provided, e.g. Refs [12], [13], and [16].  However, we did not have the time to read through this carefully and figure out EXACTLY what transformation is being applied here. Besides, we are using Jordan-Wigner whereas much of the discussion/videos pertains to Bravyi-Kitaev mapping. Finally, as mentioned, it is not 100% clear to us that the initial basis is not spin-symmetry-adapted.

Now, let's address the symmetry of the basis-transformed second measurement group. Here is where the fact that there are only two measurement groups comes into play. Because we know that the full Hamiltonian commutes with both the electron number operator N and the electron z spin operators Sz, and we know that this is also true of the first measurement group, it must necessarily also be true of the second measurement group. In addition, since the unitary basis transformation essentially serves to diagonalize the second measurement group contribution to the total Hamiltonian, then the new basis functions must themselves also respect electron number symmetry. This is useful, and comforting, information.  On the other hand, since the actual transformation itself involves many z-component-mixing operations, we can no longer assume that it is the basis functions with two zeros and two ones that correspond to two electrons. To be sure, SOME set of six basis functions are the ones we want, but we do not know which ones those are--and cannot know, without a lot more research...Indeed, as evidence attesting to this fact, we note that the exact simulation as presented above includes a |1101> contribution, i.e. a basis function with three 1's and one 0, even though it corresponds to only two electrons.  


#### Running on IBMQ

We ran these two circuits on an IBMQ device (imbq_quito, chosen as the queue time was the shortest) with a sameple size of 2000, and got the following measurement results. NOTE! you must use the slider below to see all data; consult also S5_circuit_qec.ipynb.
```
res_0_test = tq.simulate(circ_0, variables=vars, samples = no_samples, backend="qiskit", device='ibmq_quito')
res_0_test
```
```
+57.0000|0000> +123.0000|1000> +109.0000|0100> +1020.0000|1100> +48.0000|0010> +26.0000|1010> +23.0000|0110> +33.0000|1110> +27.0000|0001> +18.0000|1001> +16.0000|0101> +45.0000|1101> +400.0000|0011> +18.0000|1011> +26.0000|0111> +11.0000|1111> 
```
```
res_1_test = tq.simulate(circ_1, variables=vars, samples = no_samples, backend="qiskit", device='ibmq_quito')
res_1_test
```
```
+121.0000|0000> +102.0000|1000> +90.0000|0100> +233.0000|1100> +69.0000|0010> +51.0000|1010> +52.0000|0110> +82.0000|1110> +151.0000|0001> +97.0000|1001> +101.0000|0101> +560.0000|1101> +85.0000|0011> +68.0000|1011> +35.0000|0111> +103.0000|1111> 
```

#### Without Post-processing Error Mitigation

Now that we have the measurement results by running the two circuits, we can calculate the expectation value using the measurement results. To describe the process briefly (to see the full code, please check the notebook), we first convert the measurement results into a state-vector form, and then use a tequila function to compute the expectation value. We calculate the expectation value for each Hamiltonian (split by measurement group) separately, and then add them to gether to get the expectation value from the run.

The expectation value we got from the first measurement group was:
```
base_E_0 = base_res_0.compute_expectationvalue(H_0)
base_E_0
```
```
-0.6467700690869538
```

The expectation value we got from the second measurement group was:
```
base_E_1 = base_res_1.compute_expectationvalue(H_1)
base_E_1
```
```
-0.04457181767954178
```

And so combined together, we got the expectation value of:
```
base_E = base_E_0 + base_E_1
```
```
-0.6913418867664956
```

As you can tell, this expectation value is very different from the actual expectation value that we were hoping to get. On the other hand, it is also very clear that there is a lot of noise across all basis functions--including those basis functions that correspond to the wrong number of electrons, whose identity we can at least confirm for the first measurement group, as discussed.  


#### With Post-processing Error Mitigation

Now, we attempt to implement the error mitigation protocol. To implement it, we remove all the measurement results for the 10 out of 16 basis functions that DO NOT correspond to two electrons. This would be easily enough achieved in the case of the first measurement group---i.e., we would throw away all results except those for the six measurement outcomes, |0011>, |1100>, |0101>, |0110>, |1010>, and |1001>.  However, if you have been following the preceding discussion, you immediately recognize the problem we encounter with this approach--which is that FOR THE SECOND MEASUREMENT GROUP, WE DO NOT KNOW THE ALLOWED SET OF SIX BASIS FUNCTIONS (though we do know that it exists...). So, we cannot consistently apply this procedure to both parts of the Hamiltonian. 

Of course, this is not a fundamental limitation. More research into the methodology would reveal this information. Also, we could have implemented the number operator, transform it, and apply it to the individual transformed second-group basis functions, to identify the requisite six. Time limits restricted us from actually doing any of this. However, we have a simpler and very effective approach that we can also justify, as described above. 

Consider that in the exact calculation, we discovered that each measurement group in fact receives an exact contribution from just two basis functions.  In the case of the first measurement group, these are |1100> and |0011>, both of which are seen to belong the aforementioned group of six. In the case of the second measurement group, these are |1100> and |1101>. So we know that at least these two transformed basis functions belong to the correct group of six, but we have no means of identifying the other four. 

All of that being the case, the best we can do here in terms of applying the proposed error-mitigation scheme, in a way that is consistent across both groups, is to throw away all data 
in each group, EXCEPT for that from the two basis functions from each group that are identified above. So this is the scheme that we have implemented, and provide data for below. Of course, this
is ``cheating'' a little bit, because we are using information from the exact result that in principle we would not know, to throw away more data than the true method would allow based on symmetry. Nevertheless, it is still an excellent approximation to the true method, as we can 
justify from the first group quantum calculation as follows.  

In particular, by examining the first group data above, we see that the |1100> and |0011> outcomes received the most measurements by far, which is exactly as expected.  However, the important question then becomes, of the remaining outcomes, which receive more measurements the two-electron outcomes, or the others? Remarkably, the non-included two-electron outcomes received FAR FEWER measurements than the others. Therefore, excluding them from the calculation, in addition to the others, will not skew the results too unduly. 

Applying the above procedure, we were left with the following total number of measurements from each measurement group:

```
The total number of samples for first measurement group remaining is: 1420
```
```
The total number of samples for second measurement group remaining is: 793
```

These numbers make sense, as we expect errors to be introduced when we apply gates and apply the measurement readout. The second group definitely lost many more samples (through the protocol) due to the sheer number of gates that we had to use to implement the measurement. Now, we check the expectation value post implementation of protocol:


The expectation value we got from the first measurement group was:
```
post_E_0 = post_res_0.compute_expectationvalue(H_0)
post_E_0
```
```
-0.7154794048100186
```

The expectation value we got from the second measurement group was:
```
post_E_1 = post_res_1.compute_expectationvalue(H_1)
post_E_1
```
```
-0.10685785786394145
```

And so combined together, we got the expectation value of:
```
post_E = post_E_0 + post_E_1
post_E
```
```
-0.82233726267396
```

While still different from the correct value, this expectation value is very much closer to the actual expectation value! As we can see, much of deviance came from the second measurement group, which is to be expected due to the error induced by the long circuit.

It is worth mentioning that the error mitigation of this approach must in some sense be related to the fraction of $2^M$ configurations (where $M$ is the total number of orbitals) that correspond to the desired number of electrons N. If N=M/2, as is often the case and is definitely the case here, then this fraction is the largest, and larger than one might like--e.g., 6/16 in this case. In principle, this will not lead to tremendous reduction, assuming that error is spread uniformly across all basis functions. However, we have seen that this is not really the case.  In particular, the error associated with the two-electron basis functions, for whatever reason, appears to be SMALLER than the others. This means that the method will work better than expected.   

### (2) Can the error-mitigation protocol in Ref. [14] be used for more complicated symmetries like $\hat{S}^2$?

The answer here is absolutely yes! Indeed, as discussed, there is some evidence to suggest that we are already working in a spin-symmetry-adapted basis, in terms of the numerical results reported above. There are, however, some caveats. To begin with, for this to work, then ALL measurement groups must respect all desired symmetries--meaning that the operators corresponding to each group $H_n$ must individually commute with all desired symmetry operations. Even if it is known that the total H does so, it is not necessarily that case that the individual $H_n$ will also do so. 

With regard to the "Pauli word" (x/y/z tensor product) contributions to the Hamiltonian that emerge in say, the UCC and QCC schemes, to the extent that these procedures can be symmetry adapted in principle (which is in any event clearly not always the case in practice, according to the youtube videos),  it is not immediately obvious (at least to me) that the associated minimal clique groupings necessarily also satisfy the same symmetry requirements, nor exactly what kind of symmetries this may be expected to be the case for.  However, at least in cases where one grouping is found to consist of pure z tensor products, and there is only one other grouping with all of the x's and y's, as is the case here, then the necessary condition described above is clearly  satisfied, at least with respect to $\hat N$ and $S_z$ symmetry.

### (3) An error-mitigation protocol if the right wavefunction is known to be an eigenstate of a certain multi-qubit operator $\hat{A}$ with eigenvalue a.

This challenge is a little bit oddly worded. Is $\hat A$ the Hamiltonian operator whose expectation value we are seeking, or is it the symmetry operation for which the eigenvalue a corresponds to the desired irrep (irreducible representation)? Is |$\Psi$> presumed to be an eigenstate of the Hamiltonian? Either way, I suppose, |$\Psi$> must be an eigenstate of $\hat A$, at least in principle. 

So, one could try following a similar procedure to that described
above. If $\hat A$ were not first decomposed into pieces, one would
first transform unitarily to a diagonalizing representaton, and then
make measurements. All measurements corresponding to basis functions
NOT associated with the desired eigenvalue a would be ignored. But
then of course, we already know a priori that the result will be a, 
so this seem a bit useless, unless we actually are seeking the expectation
value for some other operator (unclear from the way the problem is written).

One could also try to decompose $\hat A$ into as small a sum as possible
of x/y/z tensor products across individual qubits.  Then, apply a minimal
clique analysis to divide these terms into the fewest number of maximally
commuting groups. Then, ensure that each such group also satisfies 
the desired symmetry---i.e., commutes with the desired symmetry operations.
Here though, one would have to have sorted out in advance which eigenvalue
(really irrep) contributions from each piece give rise to the desired final
value of a, once they are all combined together.  
 
Other options would be to apply constraint penalty within the variational
algorithm, or to apply an (approximate unitary) projection operator. 

-> All questions from the instructions pdf have been answered in this pdf document: https://github.com/MQS-mark/CohortProject_2022/blob/main/Week2_VQE/CDL_week_2_answers.pdf

## Further Challenges:

- How to obtain excited electronic states of the same or different symmetry?
For different symmetry it is straightforward; one can apply an error mitigation scheme as discussed above, or introduce a symmetry constraint into the variational optimization. For excited states of different symmetry, it is generally more challenging (at least on classical computers). However, in principle, one can introduce a constraint based on overlap with the known ground state, say, to compute the first excited state. However, this approach becomes difficult if a number of excited states are desired--as new constraints must be added for each such lower-lying state. 

Of course, this is all in the context of quantum computing with VQE. Using our FCI-based proprietary code, we can compute excited electronic states--quite many of them, actually--on classical computers. 

- Partitioning in the fermionic operator space.
As discussed in the provided references, this can be a real challenge. For UCC for instance, symmetry is generally (better) conserved, but many terms (and therefore quantum gates) are needed. For QCC, it is the opposite; the number of gates is minimized, but at the expense of preserving symmetry. Perhaps better methods could be developed that provide the "best of both worlds"?  Doubtful, unless better representations were first discovered.  In particular, there must be ways to nontrivially transform the initial basis, such that in the new representation, far fewer terms are needed to represent the desired operators.  

- Applying unitary transformations on the Hamiltonian.
This has been discussed in many contexts. The challenge is to limit not only the number of quantum gates needed, but also to keep them as local as possible. That said, it appears locality is not always all it is cracked up to be--with Bravyi-Kitaev vs. Jordan-Wigner mappings being a case in point. 

- Compress larger basis sets into smaller number of qubits.
Of course, spin symmetry provides one way to do this. There are other techniques discussed in the references, e.g. "qubit tapering". 

-> All questions from the instructions pdf have been answered in this pdf document: https://github.com/MQS-mark/CohortProject_2022/blob/main/Week2_VQE/CDL_week_2_answers.pdf

## Business Application

For each week, your team is asked to complete a Business Application. Questions you will be asked are:

- Explain to a layperson the technical problem you solved in this exercise.
- Explain or provide examples of the types of real-world problems this solution can solve.
- Identify at least one potential customer for this solution - ie: a business who has this problem and would consider paying to have this problem solved.
- Prepare a 90 second video explaining the value proposition of your innovation to this potential customer in non-technical language.

For more details refer to the [Business Application found here](./Business_Application.md)

-> The business application can be found here: https://github.com/MQS-mark/CohortProject_2022/blob/main/Week2_VQE/Business_Application_final.md
