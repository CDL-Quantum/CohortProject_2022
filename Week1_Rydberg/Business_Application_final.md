# Business Application for Cold Atoms Quantum Computing solving a Hubbard model Hamiltonian

# Technical problem

## Layperson description:

Companies producing new advanced materials are performing many experiments in the laboratory to find new structures and chemicals. This is a very tedious endeveaour which costs time, the needed experimental equipment and human expert knowledge. Software tools based on quantum physics allow to calculate the properties of materials and can guide the researcher to do the important experiments in the lab. Such kind of software simulation tools help the researcher to find the needle in the haystack: a novel, valuable and potential commercial product material.

In this exercise we investigated a specific quantum physical model which can be applied to such material discovery simulations. Solving this kind of simulation model on a quantum computer could lead to improvements with respect to the accuracy of the results and the speed obtaining them.

## Technical/detailed description:

- Problem definition:

Arrays of atoms have been used as simple toy model in spin systems. The simplest model is the well-know Heisenberg spin chain, which has been extended to one-dimensional Hubbard model (Hubbard chains). These toy models have been played a pivotal role in describing lattice spin models and have also been employed in quantum computing, e.g. in quantum state (qubit) transfer in spin networks. Another system that has recently been of interest is the cold atom system (Rydberg atom). Arrays of Rydberg atom can be exited to their exited state using laser beam and revealed potential quantum computing application, e.g. in quantum enhanced sensing. Coherent coupling between such exited Rydberg states provides an avenue for realizing strongly interacting quantum systems. It has been shown that appropriate configuration of Rydberg atoms into a system of itinerant electrons and phonons can be described by Hubbard model.


- Hubbard model: The Fermi-Hubbard Hamiltonian reads

$$
H=-\sum_{\langle i,j \rangle,\sigma}t (\hat{c_{i\sigma}}^{\dagger} \hat{c_{j\sigma}}+h.c.) +U\sum_{i}(\hat{n_{i \uparrow}}\hat{n_{i\downarrow}})
-\mu \sum_{i}(\hat{n_{i\uparrow}}+\hat{n}_{i\downarrow}), 
$$

where $\sigma$
stands for spin, and i and j enumerate the interacting sites along the chain. The first term of the hamiltonian represents the hopping integrals for nearest neighbor interactions and the second term, represents the repulsive interaction between electrons on the same site. t denotes the hopping parameter, which describes how favorable it is for electrons to hop from site to site, U defines the strength of the electron repulsion, and $\mu$ is the chemical potential.


- Emulating the one-dimensional Fermi-Hubbard model on a neutral atom quantum computer:

We propose that a neutral atom quantum computer could be used to perform an analog simulation of a Fermi Hubbard system. The first step is to recognize that the objects in the Fermi-Hubbard model are fermions, which have their charactestic anticommutation rules that must be taken into account. In contrast, a neutral-atom quantum computer is composed of qubits, which do not have these rules intrinsically encoded into them. To resolve this, we have to use a mapping, which is consistent with the rules, to represent fermions on qubits. The most well-known mapping is the Jordan-Wigner mapping, which transforms the Fermi-Hubbard model into [6]:

$$H = \sum_{i, \sigma} g^x(\hat{\sigma}_{i, \sigma}^{+} \hat{\sigma}_{i+1, \sigma}^{-} + \hat{\sigma}_{i+1, \sigma}^{+} \hat{\sigma}_{i, \sigma}^{-}) + g^z \sum_{i} (\hat{\sigma}_{i \uparrow}^z \hat{\sigma}_{i \downarrow}^z) + \frac{1}{2}\epsilon\sum_{i} (\hat{\sigma}_{i \uparrow}^z + \hat{\sigma}_{i \downarrow}^z)$$

where we have introduced new parameters $\epsilon$, $g^{z}$, and $g^{x}$, 
which relate to the Hubbard model parameters with $\mu=-\epsilon+2g^{z}$, $U=4g^{z}$ and $t=-g^{x}$. 
Such a hamiltonian can be realized as a double chain of qubits, where each pair along the chain is representative of the two different spin species on each physical sight. Such a configuration is easily achievable with neutral atom arrays, as the platform has the capability to arrange the qubits into all kinds of 2D structures. Now all that is needed is a way to have a $\sigma^{z}$
interaction within each pair and a $\sigma^{\pm}$
interaction with the neighbouring pair. A method to create this has been proposed for superconducting qubits [6], but to our knowledge this has not been explored for neutral atoms yet. However, taking advantage of the finite range nature of the Rydberg blockade effect may be interesting to consider, beacuse it provides a way to differentiate between neighbouring qubits that differ by representative spin from those that differ by representative site. For example, the double chain can be constructed such that qubits which represent the same site are positioned close to each other so that thay experiance Rydberg blockade, whereas qubits of different sites are positioned on longer intervals, where this effect no longer dominates. 


- Performance analysis:

To have a baseline calculation, which an implementation can be compared to, we present an auxiliary field quantum Monte Carlo (QMC) simulations for one-dimensional Hubbard model at low temperature regime. QMC algorithm is extensively employed for calculations of electronic structure of solids and molecules. Within the auxiliary field QMC the partition function is expressed as a multi-dimensional integral (calculated by Monte Carlo techniques) over a set of random auxiliary fields. The calculations are done for a 9-sites spin chain with nearest neighbor interaction and without periodic boundary conditions: the first and the last sites (antipodes) do not interact.


- Figures [1-3] show the calculated total energy (Kinetic + Potential) for a 9-sites spin chain with nearest neighbor interaction. The parameters U and $\beta$
 are the Hubbard U and the inverse temperature, respectively. The larger $\beta=10$
 corresponds to the low temperature regime to depict the ground state of the system. As seen the Kinetic/potential energy decreases/increases with increasing the chemical potential. The lowest total energy is obtained at chemical potential $\mu=0$. 
 The total energy increases by increasing/decreasing the chemical potential, and the larger $\beta$
 (lower temperature), the lower enrgy. The calculations show that the total energy for a relaxed system (at $\mu=0$) changes by %10 upon changing $\beta$ from 3 to 10. Please note that while the calculations are reported for the Hubbard parameters, they can be applied to the Rydberg atom system by appropriate scaling.

![Figure 1](images/beta3new.png)

![Figure 2](images/beta3_10new.png)

![Figure 3](images/beta10new.png)

# Real-world problems

Different real-world applications exist to apply cold atoms quantum computers such as:

- Correlation clustering problem (undirected graph): Multiple-person pose estimation [Pishchulin et al., 2015; https://arxiv.org/abs/1511.06645]

- MAXAGREE on general graphs, weighted [Charikar et al., 2003; https://ieeexplore.ieee.org/document/1238225], unweighted [Tan, 2007; https://ui.adsabs.harvard.edu/abs/2007arXiv0704.2092T/abstract]; best approximation algorithm by [Swamy, 2004; https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwio6OPMne_4AhUIwAIHHZlNBUYQFnoECAYQAQ&url=https%3A%2F%2Fwww.math.uwaterloo.ca%2F~cswamy%2Fpapers%2Fmaxclstrsoda.pdf&usg=AOvVaw1bYH4sqh8JGXMHX95MoQCj]: 

- Hubbard model for one-dimensional organic metals and conductivity of Bechgaard salts under pressure [Celebonovic, 2011; https://arxiv.org/abs/1101.0363]

- Hubbard model for two-dimensional systems by applying the Determinant Quantum Monte Carlo Method (DQMCM) [Celebonovic, 2011; https://arxiv.org/abs/1101.0363]

As a computational chemistry company we focus on solving use-case applications for material design problems and therefore investigating how to solve the Hubbard model with a cold atoms quantum computer has been chosen as a valuable problem to tackle.

The lesson learned from this project is:

- The hamiltonian has some terms which are not present in the Rydberg Hamiltonian, so we can not straightforwardly use the code from the bloqade Julia package. To do a physical implementation, there needs to be further research into how the necessary interactions could be realized. To do a computer simulation, a custom hamiltonian would has to be built, which we have not (yet) managed to implement with bloqade.

# Potential customers

Potential customers of a simulation tool to predict the band structures of solid materials are photovoltaics companies. With quantum computing based simulations they may be able to predict structures in the future with greater accuracy and obtain the results faster. A high-throughput screening of novel materials with desired properties will help to improve the efficiency of photovoltaics.

In Copenhagen exist two start-up companies which build micro-reactors for nuclear (thorium) heat generation to generate electricity via steam. These two companies are Seaborg (https://seaborg.com) and Copenhagen Atomics (https://copenhagenatomics.com/). Crucial for these micro-reactors are liquid molten salts which act has the heat transport material between the micro-reactor and the water flow to be heated up. [https://aip.scitation.org/doi/10.1063/1.1324709, https://www.sciencedirect.com/science/article/abs/pii/S0378381216302394?via%3Dihub]

Solid material structures such as graphene, ferromagnetic lattices, Silicium square and cubic lattices can also be simulated with the Hubbard model. Such materials can be found in a wide range of applications such as aviation composites, semi-conductors and specialized coatings.


# Video for customer value proposition

https://www.loom.com/share/ff77cd7f199c4208889f6308379f9c30

# References

[Bernien et al., 2017] H. Bernien et al., Nature 551: 579-584 (2017).

[Jafarizadeh, 2008] M.A. Jafarizadeh, R. Sufiani, S.F. Taghavi, and E. Barati, J. Phys. A: Math. Theor. 41, 475302 (2008).

[Rubenstein, 2012] B.M. Rubenstein, Sh. Zhang, and D.R. Reichman, Phys. Rev. A 86, 053606 (2012).

[Zhang, 1999] Sh. Zhang, Phys. Rev. Lett. 83, 2777 (1999).

[Essler, 2005] F.H.L. Essler, H. Frahm, F. Gohmann, V.E. Korepin, A. Klümper, "The one-dimensional Hubbard model", Cambridge University Press (2005).

[Reiner, 2016] Reiner, Jan-Michael, et al. "Emulating the one-dimensional Fermi-Hubbard model by a double chain of qubits." Physical Review A 94.3 (2016): 032338.

[Hague-2014] J.P. Hague, S. Downes, C. MacCormick, et al., J Supercond Nov Magn 27, 937–940 (2014).
