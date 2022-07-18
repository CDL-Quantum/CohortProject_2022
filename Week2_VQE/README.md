![CDL 2022 Cohort Project](../CDL_logo.jpg)

## Project 2: VQE: Constructing potential energy surfaces for small molecules

This project will guide you through the state-of-the-art techniques for solving electronic structure problems on NISQ computers.

Open up [instructions.pdf](./Instructions.pdf) to begin learning about your tasks for this week!

**Please edit this markdown file directly with links to your completed tasks and challenges.**

## Tasks include:

### Generating PES using classical methods.

*Hartree-Fock (HF), Configuration Interaction Singles and Doubles (CISD), Coupled Cluster Singles and Doubles (CCSD), and the exact answer within the chosen basis Full Configuration Interaction (FCI) [2]. All these methods can easily be used for all molecules in minimal atomic basis, STO-3G. Comparing accuracy of PES generated for different species using different methods you can see the difference between weakly correlated $\left(\mathrm{H}_{2}, \mathrm{LiH}\right)$ and strongly correlated $\left(\mathrm{H}_{4}, \mathrm{H}_{2} \mathrm{O}, \mathrm{N}_{2}\right)$ systems. Even though the FCI method provides the exact answer it scales exponentially with the number of basis functions and thus cannot be used for larger systems (system size can be either correlated with the number of electrons or number of basis functions). All approximated methods (HF, CISD, CCSD) scale polynomially with the system size but fail to deliver chemical accuracy along PESs.*

**1) Among classical methods, there are techniques based on the variational approach and those that are not. Identify variational methods among those that were used and explain advantages of the variational approach. Are there any arguments for using non-variational techniques?**


For this work, the methods and proposals offered in resources [1](https://www.youtube.com/user/AAA22254/videos) and [2](./S1_Classical_Methods.ipynb) were addressed; in the latst, the techniques were presented : 

- [The Hartree-Fock](https://en.wikipedia.org/wiki/Hartree%E2%80%93Fock_method) (HF), 
- [Configuration Interaction Singles and Doubles](https://en.wikipedia.org/wiki/Configuration_interaction) (CISD) 
- [Full Configuration Interaction](https://en.wikipedia.org/wiki/Configuration_interaction) (FCI) 
- [Coupled Cluster Singles and Doubles](https://en.wikipedia.org/wiki/Coupled_cluster) (CCSD) 


of these from the state of the art we can conclude that  


|Variational Method      | No Variational Method| 
|----------------------- | -------------------- | 
| Hartree-Fock           | CCSD                 | 
| CISD			         | 				        | 
| FCI                    | 				        | 


CISD and FCI are "post-Hartree–Fock linear variational method for solving the nonrelativistic Schrödinger equation within the Born–Oppenheimer approximation for a quantum chemical multi-electron system".


### Generating the qubit Hamiltonian.


*To proceed to VQE one needs to generate the qubit Hamiltonian, the easiest path is via first generating the electronic Hamiltonian in the second quantized form and then transform it into the qubit form using one of the fermion-to-qubit transformations: Jordan-Wigner or Bravyi-Kitaev [3]. Next, some qubit operators can be substituted by numbers $(\pm 1)$ because their states are stationary for the specific electronic state (e.g. ground state). This reduction is very useful for fitting larger problem in a fewer qubit description and is based on Hamiltonian symmetries, which are discussed in Refs. $[4,5,6]$*

**1) What are the requirements for a function of qubit operators to be a valid mapping for the fermionic operators?**


Following the ref [Lecture 3: Fermion-qubit mappings](https://www.youtube.com/watch?v=W8SW3qp3RzY), they explain that

Electronic structure problem needs to be translated to qubits, this requires to transfer both wavefunction and operators (Hamiltonian).

$$
\begin{gathered}
\hat{H}_{e}(\mathbf{R})\left|\Phi_{j}(\mathbf{R})\right\rangle=E_{j}(\mathbf{R})\left|\Phi_{j}(\mathbf{R})\right\rangle \\
\hat{H}_{e}=\sum_{p q} h_{p q} \hat{a}_{p}^{\dagger} \hat{a}_{q}+\sum_{p q r s} g_{p q, r s} \hat{a}_{p}^{\dagger} \hat{a}_{q}^{\dagger} \hat{a}_{r} \hat{a}_{s}
\end{gathered}
$$
Fermions:
$$
\begin{aligned}
\left\{\hat{a}_{i}^{\dagger}, \hat{a}_{j}\right\} &=\delta_{i j} \quad\left\{\hat{a}_{i}, \hat{a}_{j}\right\}=\left\{\hat{a}_{i}^{\dagger}, \hat{a}_{j}^{\dagger}\right\}=0 \\
\left|\Phi_{j}(\mathbf{R})\right\rangle &=\sum_{\bar{n}} C_{\bar{n}, j}\left|n_{1}, n_{2}, \ldots n_{N_{o}}\right\rangle, n_{i}=\{0,1\}
\end{aligned}
$$
Qubits: $\quad\left[\hat{\sigma}_{x}, \hat{\sigma}_{y}\right]=i \hat{\sigma}_{z}$


i.e., it must be fulfilled that the function is anticomponent with respect to the operators, since fermionic operators are anticomponent.


**2) The electronic Hamiltonian is real (due to time-reversal symmetry), what consequences does that have on the terms in the qubit Hamiltonian after the Jordan-Wigner transformation?**


### Unitary transformations.


### Hamiltonian measurements.


### Use of quantum hardware.








## Further Challenges:

- How to obtain excited electronic states of the same or different symmetry?
- Partitioning in the fermionic operator space.
- Applying unitary transformations on the Hamiltonian.
- Compress larger basis sets into smaller number of qubits.

## The ansatzer - your ansatz distributor - Business Application

- Different techniques have been proposed for generating ansatz for finding ground states in VQE problems. Our method gives you the ansatz that best adapts to your specific problem. We have distributed ansatz for different molecules that improve performance in terms of convergence and required less number of parameters. We are specialized in big molecules using Tree Tensor Networks (TTN). Give us your molecule and we will tailor the best performance ansatz for it!

<center><img src="./Images/theAnsatzer.png" width="400"></center>

### Our Solution for different molecules 

In this section, we show the solution of VQE with our special ansatz for two different cases H<sub>2 and BeH<sub>2. The TTN is compared against a strongly correlating layer ansatz STL. Here, it can be seen that our model improves the results for the STL ansatz. 

| **H<sub>2**| **BeH<sub>2**    |
| ------------ | ------------------------ |
| ![image](Images/H2.png) | ![image](Images/BeH2.png) |
| ![image](Images/H2_TTNvsSEL.png) | ![image](Images/TTNvsSEL.png) |


### Potential Customers

BASF SE is a German multinational chemical company and the largest chemical producer in the world. For this chemical company, quantum-computing will improve the modeling quantum-mechanical systems capabilities in molecules and polymers. Identifying the most effective molecular design or structures to achieve required effects—before synthesizing molecules in the lab.
