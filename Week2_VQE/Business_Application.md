![CDL 2022 Cohort Project](../CDL_logo.jpg)
# Quantum Cohort Project Business Application

In this project, we use state-of-the-art techniques for solving electronic structure problems on NISQ computers and simulators.

## Step 1: Explain the technical problem you solved in this exercise

### Introduction

The technical problem that we were tasked to focus on for this exercise was to explore using variational methods to solve the electronic structure problem. For the many sub-parts of the exercise, we were using state-of-the-art techniques to solve for many small molecules like the H2 molecule or the LiH molecule. However, beyond just finding the ground state energy for small molecules, one of the greatest feats that we had managed to achieve was the simulation of the bond-breaking for the nitrogen molecule, a much bigger molecule that requires a far more complex simulation than most current day simulators are able to handle. We achieved this by using a proprietary software package that can go even bigger than most simulators.

### How we did it

Among other things, the package was written to solve the wavefunctions of 2-electron dynamics (geminals) of small atoms/molecules in the gas phase.  However, adapting a Sums of Product (SOP) (i.e., simple tensor network) technology, in the context of a full configuration interaction (FCI) calculation, we found that summations of 5 groups of four qubits could successfully simulate N2 in the ground state, at two different nuclear separation distances: (a) near the global minimum geometry; (2) heading towards dissociation at 3 Angstroms. In comparison, CCSD(T) fails with regard to (2), because of the well-known challenges of breaking three three bonds.  Being able to achieve excited states at both radii with FCI quality is extremely useful.  Unlike a true FCI calculation, however, we do not represent each Slater determinate as a separate mathematical object; instead we approximate the global sum of Slaters in the SOP representation.  The number of terms in this sum (i.e., the  canonical rank) of 4 qubits is proportional to the complexity of the wavefunction. We feel it is demonstrative of the capacity of this algorithm that we could solve these complex problems on a classical computer.  In the first cohort challenge, for instance, we performed a 60-qubit simulation, using the same proprietary code.

The SOP representation effectively overcomes the "number of qubits" problem, and refocuses the complexity challenge to maintaining a global wave function via summations of products of, in this case, 4 qubit basis sets. We attacked this problem with full complexity to assure the answer found would be correct.  There are roughly 8000 2-body terms in the N2 Hamiltonian of the ground state and 15000 terms in the 3 Angstrom radius computation.  The terms are computed in pySCF.  All of these terms are acted on the basis via an algorithmic package that can construct arbitrary sums and products of ladder operators; other operators allowed include 1st quantization Kinetic and Coulombic terms.  The public release of the high level API, [Cepheus](https://github.com/Quantum-Galaxies-Corporation/Cepheus), is on Github. 

It is interesting to note that in first quantization, the number of terms in the same Hamiltonian would not exceed 100 or so, which may offer a huge advantage on quantum hardware. Traditional second-quantized methods are designed to minimize the basis size, which is the "rate limiting step" on classical computers. However, as we have seen, they give rise to a great many Hamiltonian terms, which on quantum computing implementations translates into a large number of quantum gates. This is certainly problematic, especially in the NISQ era, as quantum gates, not basis sizes, present the "rate limiting step" on quantum computers.  Thus, whereas the basis sizes required of first-quantized methods are enormous as compared to second quantized approaches, the far-fewer number of gates is highly attractive in a quantum computing setting. In any event, our proprietary code can perform both types of simulations on a classical computer, for a non-trivial number of qubits.

We could also have solved even more complex arrangements of atoms with perhaps a smaller number of interacting terms.  For instance, if we only retain terms above a milliHartree, the Hamiltonian size is more than halved. This SOP architecture is ideal for every kind of system we attempted so far.  It may be useful on quantum computing hardware to solve a non-Born Oppenheimer approximation via larger representations.  Its of particular interest that in SOP language, the communication between dimensional bundles, in this case 4 qubits, is extremely limited, only passing scalars for very complex linear algebra procedures.  This may be an ideal way to reduce gates on large qubit actions.  

## Step 2: Explain or provide examples of the types of real-world problems this solution can solve

Being able to simulate the bond-breaking of the nitrogen molecule is extremely significant for many industries, particularly the agricultural industry. In this day and age, most of the ammonia that we get are by breaking the bonds of nitrogen we find in air. Most of the current industrial methods of doing so involve energy demanding processes, so much so that 1 to 2% of worldwide energy is being used to create ammonia just for use in fertilizers. Most obviously, this drives up cost for many businesses in the agricultural industry since 80% of produced ammonia is used for fertilizers, but beyond that, ammonia is also being used in many other industries, for example in the manufacturing of plastics, textiles and fuels. A successful simulation of the bond breaking for the nitrogen molecule is key to the computational development of studying and discovering new ways to produce ammonia, making ammonia production not only a less energy expensive (and hence also literally less expensive) process, but a greener one too.

## Step 3: Identify at least one potential customer for this solution - ie: a business who has this problem and would consider paying to have this problem solved

As our main success lies in being able to simulate the bond-breaking of nitrogen, the most obvious customers would then be businesses who are heavily invested in ammonia production. Many countries are heavily invested in ammonia production, like China, USA and India. With good research, one might be able to break into their markets:

In the USA:
https://www.statista.com/statistics/1266394/ammonia-capacities-by-company-united-states/
Examples in the top 3 in USA: 
- CF Industries
- Nutrien
- LSB Industries

Examples in other countries:
- Matix Fertilisers & Chemicals Panagarh Ammonia Plant (India)
- Mitsui and Ube (Japan)

Many of these companies by nature would be interested in research for lowering costs for ammonia production. Furthermore, a more specific target that we would want sell to would be those that are heavily invested in green ammonia production, since this is an important step in making ammonia production more environmentally friendly:

https://www.marketsandmarkets.com/Market-Reports/green-ammonia-market-118396942.html

Companies that are interested in this are generally in the European region:
- Siemens (Germany)
- NEL Hydrogen (Norway)
- ITM Power (UK)

## Step 4: Prepare a 90 second video explaining the value proposition of your innovation to this potential customer in non-technical language

Transcript link - https://docs.google.com/document/d/10Nneqw6CnNDhuYWJcCd2aDLhHG-YPvmjv_cykZrAW9c/edit?usp=sharing

Slides link - https://docs.google.com/presentation/d/1j8aARAxIkn6I1lqRPOBKmFBGS6xGRzOflEeMl0q8MEY/edit?usp=sharing

Video link -

**Please store your video externally to the repo, and provide a link e.g. to Google Drive**
