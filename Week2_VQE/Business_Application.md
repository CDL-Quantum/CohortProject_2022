![CDL 2022 Cohort Project](../CDL_logo.jpg)
# Quantum Cohort Project Business Application

In this project, we use state-of-the-art techniques for solving electronic structure problems on NISQ computers and simulators.

## Step 1: Explain the technical problem you solved in this exercise

Beyond just finding the ground state energy for small molecules, one of the greatest feats that we had managed to achieve was the simulation of the bond-breaking for the nitrogen molecule, a much bigger molecule that requires a far more complex simulation than most current day simulators are able to handle. The simulation of N2 bond breaking was done on a proprietary software package that can go even bigger.  Among other things, the package was written to solve the wavefunctions of 2-electron dynamics (geminals) of small atoms/molecules in the gas phase.  However, adapting a Sums of Product (SOP) (i.e., simple tensor network) technology, in the context of a full configuration interaction (FCI) calculation, we found that summations of 5 groups of four qubits could successfully simulate N2 in the ground state, at two different nuclear separation distances: (a) near the global minimum geometry; (2) heading towards dissociation at 3 Angstroms. In comparison, CCSD(T) fails with regard to (2), because of the well-known challenges of breaking three three bonds.  Being able to achieve excited states at both radii with FCI quality is extremely useful.  Unlike a true FCI calculation, however,  we do not represent each Slater determinate as a separate mathematical object; instead we approximate the global sum of Slaters in the SOP representation.  The number of terms in this sum (i.e., the  canonical rank) of 4 qubits is proportional to the complexity of the wavefunction. We feel it is demonstrative of the capacity of this algorithm that we could solve these complex problems on a classical computer.  In the first  cohort challenge, for instance, we performed a 60-qubit simulation.  using the same c

The SOP representation effectively overcomes the "number of qubits" problem, and refocuses the complexity challenge to maintaining a global wave function via summations of products of, in this case, 4 qubit basis sets. We attacked this problem with full complexity to assure the answer found would be correct.  There are roughly 8000 2-body terms in the N2 Hamiltonian of the ground state and 15000 terms in the 3 Angstrom radius computation.  The terms are computed in pySCF.  All of these terms are acted on the basis via an algorithmic package that can construct arbitrary sums and products of ladder operators; other operators allowed include 1st quantization Kinetic and Coulombic terms.  The public release of the high level API, [Cepheus](https://github.com/Quantum-Galaxies-Corporation/Cepheus), is on Github.   


It is interesting to note that in first quantization, the number of terms in the same Hamiltonian would not exceed 100 or so, which may offer a huge advantage on quantum hardware. Traditional second-quantized methods are designed to minimize the basis size, which is the "rate limiting step" on classical computers. However, as we have seen, they give rise to a great many Hamiltonian terms, which on quantum computing implementations translates into a large number of quantum gates. This is certainly problematic, especially in the NISQ era, as quantum gates, not basis sizes, present the "rate limiting step" on quantum computers.  Thus, whereas the basis sizes required of first-quantized methods are enormous as compared to second quantized approaches, the far-fewer number of gates is highly attractive in a quantum computing setting. In any event, our proprietary code can perform both types of simulations on a classical computer, for a non-trivial number of qubits.

We could also have solved even more complex arrangements of atoms with perhaps a smaller number of interacting terms.  For instance, if we only retain terms above a milliHartree, the Hamiltonian size is more than halved. This SOP architecture is ideal for every kind of system we attempted so far.  It may be useful on quantum computing hardware to solve a non-Born Oppenheimer approximation via larger representations.  Its of particular interest that in SOP language, the communication between dimensional bundles, in this case 4 Qbits, is extremely limited, only passing scalars for very complex linear algebra procedures.  This may be an ideal way to reduce gates on large qbit actions.  

(Jonathan, please help fill this up! I think put down a brief description of how you were able to achieve it)

## Step 2: Explain or provide examples of the types of real-world problems this solution can solve

In this day and age, most of the ammonia that we get are by breaking the bonds of nitrogen we find in air. Most of the current industrial methods of doing so involve energy demanding processes, which drives up cost for businesses in the agricultural industry (due to ammonia being used in fertilizers), in manufacturing of plastics, textiles and other materials, and so many more. It is a versatile substance that is used extremely widely, so by being able to simulate the bond-breaking for the nitrogen molecule, we are able to study the processes required to manufacture ammonia much more easily.


(Jonathan, please help fill this up! Maybe write down how the bond breaking simulation helps us study ammonia production?)

## Step 3: Identify at least one potential customer for this solution - ie: a business who has this problem and would consider paying to have this problem solved

As the

Examples: 
- Federal Express
- Canada Post

## Step 4: Prepare a 90 second video explaining the value proposition of your innovation to this potential customer in non-technical language

Example: By travelling to all destinations via the shortest route, a courier can generate the same revenue that it would have generated following any other route, but will minimize travel costs (e.g., fuel costs). By minimizing travel costs, the courier will be more profitable than it would have been had it travelled through any other route.

**Please store your video externally to the repo, and provide a link e.g. to Google Drive**
