![CDL 2022 Cohort Project](../CDL_logo.jpg)
## Project 1: INSTRUCTIONS

A number of startup companies, including 
[QuEra](https://www.quera.com), [Pasqal](https://pasqal.io), and 2021 CDL Cohort graudates Bavarya QC, are pursuing a novel architechture for quantum computing based on neutral "Rydberg" atom arrays.


### Modelling Rydberg atom arrays

Rydberg atoms need to be placed at a physical location.
We will strictly look at Rydberg atoms on a graph $G$ with vertices (physical Rydberg atom locations) and edges $V$ and $E$, respectively.

With this, we will look at a Rydberg Hamiltonian of the form
$$H = -\sum_{i \in V} n_i + \sum_{ i < j } \left({ \frac{R_b}{r_{ij}} }\right)^6 n_i n_j$$