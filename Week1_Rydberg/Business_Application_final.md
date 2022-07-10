# Business Application for Cold Atoms Quantum Computing solving a Hubbard model Hamiltonian


# Technical problem

- Graphs

Full stack approach:

- Problem definition:
 Arrays of atoms have been used as simple toy model in spin systems. The simplest model is the well-know Heisenberg spin chain, which has been extended to one-dimensional Hubbard model (Hubbard chains). These toy models have been played an in describing lattice spin models and have also been employed in quantum computing, e.g. in quantum state (qubit) transfer in spin networks. Another system that has recently been of interest is the cold atom system (Rydberg atom). Arrays of Rydberg atom can be exited to their exited state using laser beam and revealed potential quantum computing application, e.g. in quantum enhanced sensing. Coherent coupling between such exited Rydberg states provides an avenue for realizing strongly interacting quantum systems.

- Hubbard model: The one-dimensional Fermi-Hubbard Hamiltonian reads

$$H = - \sum_{i, \sigma} t(\hat{c}_{i, \sigma}^{\dagger} \hat{c}_{i+1, \sigma} + \hat{c}_{i+1, \sigma}^{\dagger} \hat{c}_{i, \sigma}) + U \sum_{i} (\hat{n}_{i \uparrow} \hat{n}_{i \downarrow}) - \mu \sum_{i} (\hat{n}_{i \uparrow} + \hat{n}_{i \downarrow})$$

, where i enumerates the sites along the chain. The first term of the hamiltonian represents the hopping integrals for nearest neighbor interactions and the second term, represents the repulsive interaction between electrons on the same site. t denotes the hopping parameter, which describes how favorable it is for electrons to hop from site to site, U defines the strength of the electron repulsion, and mu is the chemical potential.

- Emulating the one-dimensional Fermi-Hubbard model on a neutral atom quantum computer:
  We propose that a neutral atom quantum computer could be used to perform an analog simulation of a Fermi Hubbard system. The first step is to recognize that the objects in the Fermi-Hubbard model are fermions, which have their charactestic anticommutation rules that must be taken into account. In contrast, a neutral-atom quantum computer is composed of qubits, which do not have these rules intrinsically encoded into them. To resolve this, we have to use a mapping, which is consistent with the rules, to represent fermions on qubits. The most well-known mapping is the Jordan-Wigner mapping, which transforms the Fermi-Hubbard model into [6]:

$$H = \sum_{i, \sigma} g^x(\hat{\sigma}_{i, \sigma}^{+} \hat{\sigma}_{i+1, \sigma}^{-} + \hat{\sigma}_{i+1, \sigma}^{+} \hat{\sigma}_{i, \sigma}^{-}) + g^z \sum_{i} (\hat{\sigma}_{i \uparrow}^z \hat{\sigma}_{i \downarrow}^z) + \frac{1}{2}\epsilon\sum_{i} (\hat{\sigma}_{i \uparrow}^z + \hat{\sigma}_{i \downarrow}^z)$$

  where we have introduced new parameters $\epsilon$, $g^{z}$ and $g^{x}$, which relate to the Hubbard model parameters with $\mu=-\epsilon+2g^{z}$, $U=4g^{z}$ and $t=-g^{x}$. Such a hamiltonian can be realized as a double chain of qubits, where each pair along the chain is representative of the two different spin species on each physical sight. Such a configuration is easily achievable with neutral atom arrays, as the platform has the capability to arrange the qubits into all kinds of 2D structures. Now all that is needed is a way to have a $\sigma^{z}$ interaction within each pair and a $\sigma^{\pm}$ interaction with the neighbouring pair. A method to create this has been proposed for superconducting qubits [6], but to our knowledge this has not been explored for neutral atoms yet. However, taking advantage of the finite range nature of the Rydberg blockade effect may be interesting to consider, beacuse it provides a way to differentiate between neighbouring qubits that differ by representative spin from those that differ by representative site. For example, the double chain can be constructed such that qubits which represent the same site are positioned close to each other so that thay experiance Rydberg blockade, whereas qubits of different sites are positioned on longer intervals, where this effect no longer dominates. 

- Performance analysis:
  To have a baseline calculation, which an implementation can be compared to, we present an auxiliary field quantum Monte Carlo (QMC) simulations for one-dimensional Hubbard model at low temperature regime. QMC algorithm is extensively employed for calculations of electronic structure of solids and molecules. Within the auxiliary field QMC the partition function is expressed as a multi-dimensional integral (calculated by Monte Carlo techniques) over a set of random auxiliary fields. The calculations are done for a 9-sites spin chain with nearest neighbor interaction and without periodic boundary conditions: the first and the last sites (antipodes) do not interact.


- Figures [1-3] show the calculated total energy (Kinetic + Potential) for a 9-sites spin chain with nearest neighbor interaction. The parameters U and beta are the Hubbard U and the inverse temperature, respectively. The larger beta=10 corresponds to the low temperature regime to depict the ground state of the system. As seen the lowest energy is obtained at chemical potential=0. The energy increases by increasing/decreasing the chemical potential, and the larger beta (lower temperature), the lower enrgy. The calculations show that the total energy for a relaxed system (at mu=0) changes by %10 upon changing beta from 3 to 10.

total density operator $\hat{n}_i = \hat{n}_{i \downarrow} + \hat{n}_{i \uparrow}$

Tight binding model


# Real-world problems

- Correlation clustering problem (undirected graph): Multiple-person pose estimation [Pishchulin et al., 2016]

- MAXAGREE on general graphs, weighted [Charikar et al., 2003], unweighted [Tan, 2007]; best approximation algorithm by [Swamy, 2004]: 

- Hubbard model for one-dimensional organic metals and conductivity of Bechgaard salts under pressure [Celebonovic, 2010]

- Hubbard model for two-dimensional systems by applying the Determinant Quantum Monte Carlo Method (DQMCM) [Celebonovic, 2010]

Solid material structures such as graphene, ferromagnetic lattices, Silicium square and cubic lattices.

# Potential customers

Potential customers of a simulation tool to predict the band structures of solid materials are photovoltaics companies. With quantum computing based simulations they may be able to predict structures in the future with greater accuracy and obtain the results faster. A high-throughput screening of novel materials with desired properties will help to improve the efficiency of photovoltaics.

In Copenhagen exist two start-up companies which build micro-reactors for nuclear (thorium) heat generation to generate electricity via steam. These two companies are Seaborg (https://seaborg.com) and Copenhagen Atomics (https://copenhagenatomics.com/). Crucial for these micro-reactors are liquid molten salts which act has the heat transport material between the micro-reactor and the water flow to be heated up.
https://aip.scitation.org/doi/10.1063/1.1324709
https://www.sciencedirect.com/science/article/abs/pii/S0378381216302394?via%3Dihub

Solid material structures such as graphene, ferromagnetic lattices, Silicium square and cubic lattices can also be simulated with the Hubbard model. Such materials can be found in a wide range of applications such as aviation composites, semi-conductors and specialized coatings.


# Video for customer value proposition


# References

[1] H. Bernien et al., Nature 551: 579-584 (2017).

[2] M.A. Jafarizadeh, R. Sufiani, S.F. Taghavi, and E. Barati, J. Phys. A: Math. Theor. 41, 475302 (2008).

[3] B.M. Rubenstein, Sh. Zhang, and D.R. Reichman, Phys. Rev. A 86, 053606 (2012).

[4] Sh. Zhang, Phys. Rev. Lett. 83, 2777 (1999).

[5] F.H.L. Essler, H. Frahm, F. Gohmann, V.E. Korepin, A. Klümper, "The one-dimensional Hubbard model", Cambridge University Press (2005).

[6] Reiner, Jan-Michael, et al. "Emulating the one-dimensional Fermi-Hubbard model by a double chain of qubits." Physical Review A 94.3 (2016): 032338.

[7]

[8]
