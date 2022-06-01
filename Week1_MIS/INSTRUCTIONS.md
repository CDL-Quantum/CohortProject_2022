![CDL 2022 Cohort Project](../CDL_logo.jpg)
## Project 1: INSTRUCTIONS

A number of startup companies, including QuEra, Pasqal, and 2021 CDL Cohort graudates Bavarya QC,
are pursuing a novel architechture for quantum computing based on neutral ``Rydberg'' atom arrays.


### Modelling Rydberg atom arrays

Rydberg atoms need to be placed at a physical location.
We will strictly look at Rydberg atoms on a graph $G$ with vertices (physical Rydberg atom locations) and edges $V$ and $E$, respectively.
With this, we will look at a Rydberg Hamiltonian of the form
$$
    \hat{H} = -\sum_{i \in V} \hat{n}_i + \sum_{ i < j } \left( \frac{R_b}{r_{ij}} \right)^6 \hat{n}_i \hat{n}_j,
$$
where $\hat{n}_i = 1/2 \left( I - \hat{\sigma}_i^z \right) = \ketbra{1}{1}_i$ is called an {\it occupation operator}, $R_b$ is a parameter called the {\it blockade radius}, and $r_{ij}$ is the distance between Rydberg atoms located at vertices $i$ and $j$.
The computational basis we will be working in is the occupation basis: the eigenstates of $\hat{n}_i$,
$$
 \hat{n}_i \ket{0}_j =& 0 \qquad (\text{$\forall$ $i,j$}), \\
$$ and
$$
 \hat{n}_i \ket{1}_j =& \delta_{i,j}\ket{1}_j,
$$
where the state $\ket{0}$ ($\ket{1}$) represents the ground (excited) state of a Rydberg atom.

On observing the form of the Hamiltonian in Eq.~\ref{eq:rydberg_hamiltonian_Omega=0}, we can see that the first term (sum over $V$) favours all sites being occupied, while the interaction term penalizes occupied pairs.
