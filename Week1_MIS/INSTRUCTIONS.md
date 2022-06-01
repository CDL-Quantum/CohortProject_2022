![CDL 2022 Cohort Project](../CDL_logo.jpg)
## Project 1: INSTRUCTIONS

A number of startup companies, including 
[QuEra](https://www.quera.com), [Pasqal](https://pasqal.io), and 2021 CDL Cohort graudates Bavarya QC, are pursuing a novel architechture for quantum computing based on neutral "Rydberg" atom arrays.


### Modelling Rydberg atom arrays

Rydberg atoms need to be placed at a physical location.
We will strictly look at Rydberg atoms on a graph $G$ with vertices (physical Rydberg atom locations) and edges $V$ and $E$, respectively.

With this, we will look at a Rydberg Hamiltonian of the form
$$H = -\sum_{i \in V} n_i + \sum_{ i < j } \left({ \frac{R_b}{r_{ij}} }\right)^6 n_i n_j$$
where $n_i = 1/2 \left({ I - \sigma_i^z }\right) = |1 \rangle \langle 1|_i$ is called an occupation operator, $R_b$ is a parameter called the it blockade radius, and the distance between atoms located at vertices $i$ and $j$ is $r$.

The computational basis we will be working in is the occupation basis, where $| 0 \rangle$ is the groundstate, and $| 1 \rangle$ is the excited or Rydberg state.

the eigenstates of which are $n_i | 0 \rangle_j = 0$ for all $i$ and $j$, and $n_i | 1 \rangle_j  = \delta_{i,j} |1 \rangle_j$.