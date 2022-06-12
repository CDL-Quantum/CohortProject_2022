![CDL 2022 Cohort Project](../CDL_logo.jpg)
# Project 1: INSTRUCTIONS

A new generation of programmable neutral atom quantum computer has recently matured enough that the technology has begun to transfer from academic labs to startup companies, including [QuEra](https://www.quera.com), [Pasqal](https://pasqal.io), and 2021 CDL Cohort graudates Bavarya QC. 
This technology, based on arrays of Rydberg (or highly-excited) atoms manipulated by optical tweezers, is capable of forming strongly interacting quantum systems that can be used for a variety of purposes, including the simulation of quantum matter and materials, and the solution to challenging combinatorial problems.

In this project, you will explore the ability of Rydberg atoms to prepare a variety of quantum target states.  After the introductory material below, you will be given a number of increasingly difficult *tasks*, as well as optional *challenges* to complete.

## Modelling Rydberg atom arrays
The foundation of today’s neutral-atom quantum computers is [Rydberg atoms](https://www.nature.com/articles/s41567-019-0733-z). Briefly, Rydberg atoms are highly-excited atoms (e.g. Rubidium or Strontium) that interact with each other on the scale of a few micrometres. A controlled laser pulse can excite an atom into a quantum state with a large principal quantum number (i.e. a Rydberg state) that is quasi-stable. The binary nature of a Rydberg atom’s ground and excited states defines a two-level system, and such atomic arrays can be used to build qubit-based quantum comptuters.

Rydberg atoms are held into a physical location by optical tweezers.
We will strictly look at Rydberg atoms on a graph $G$ with vertices (physical Rydberg atom locations) and edges $V$ and $E$, respectively.

The general Rydberg Hamiltonian has the form
$$H =  \frac{\Omega}{2} \sum_{i \in V}\sigma_i^x  - \delta \sum_{i \in V} n_i + \sum_{ i < j } V_{ij} n_i n_j$$
where $n_i = 1/2 \left({ I - \sigma_i^z }\right) = |r \rangle \langle r|_i$ is called an occupation operator. The interaction $V_{ij} =R_b/r_{ij}$, $R_b$ is a parameter called the it blockade radius, and the distance between atoms located at vertices $i$ and $j$ is $r$.

The computational basis we will be working in is the occupation basis, where $| g \rangle$ is the groundstate, and $| r \rangle$ is the excited or Rydberg state.
The eigenstates of the Rydberg occupation operator are $n_i | g \rangle_j = 0$ for all $i$ and $j$, and $n_i | r \rangle_j  = \delta_{i,j} |r \rangle_j$.
On observing the form of our Hamiltonian, we can see that the first term is off-diagonal, and analogous to a transverse field.  The second term favours all sites being occupied with an excitation, while the final (interaction) term penalizes occupied pairs. 

The goal of the simplest Rydberg atom quantum computer is to prepare the groundstate wavefunction of some target Hamiltonian, defined by the ratio $\delta/\Omega$ and the interaction $V_{ij}$ (which is in turn defined by the geometry of the optical tweezer lattice $r_{ij}$, and the blockade radius).  The computer can easiliy be prepared in its groundstate, where every single-atom state is $|0\rangle$.  Then, final (target) states are prepared by slowly tuning $\delta/\Omega$ using the adiabatic state preperation protocol.

Below are series of Tasks and optional Challenges for each team to attempt.

## Task 1: Adiabatic state preparation with Bloqade

To get us started, we will use the open-source simulation software [Bloqade](https://github.com/QuEraComputing/Bloqade.jl) to prepare an ordered ground states, motivated by recent experimental studies. Our target state will be the $Z_2$ state of a one-dimensional chain of 9 atoms.  In order to prepare this state, follow the Bloqade [tutorial](https://queracomputing.github.io/Bloqade.jl/dev/tutorials/2.adiabatic/main/#Preparation-of-Ordered-States-in-1D):
generate the pulse/detuning sequence, specify the atomic position, then starting in the ground state, simulate the time evolution of a quantum state under the Schrödinger equation.  Plot the occupation on each site as a function of time.  In addition to the tasks in the tutorial, calculate the expectation value of $\sigma^x_i$ and the entanglement entropy $S_A = - {\rm Tr}(\rho_A \log \rho_A)$ (for any spatial bipartition $A$ of interest).

## Task 2: Larger size arrays

What is the largest number of lattice sites that you can simulate with Bloqade?
