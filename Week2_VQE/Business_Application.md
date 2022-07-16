![CDL 2022 Cohort Project](../CDL_logo.jpg)
# Quantum Cohort Project Business Application

In this project, we use state-of-the-art techniques for solving electronic structure problems on NISQ computers and simulators.

## Step 1: Explain the technical problem you solved in this exercise

Beyond just finding the ground state energy for small molecules, one of the greatest feats that we had managed to achieve was the simulation of the bond-breaking for the nitrogen molecule, a much bigger molecule that requires a far more complex simulation than most current day simulators are able to handle. The simulation of Nitrogen bond breaking was done on a proprietry software package that can go even bigger.  The package was written to solve the wavefunctions of 2-electron dynamics (geminals) of small atoms/molecules in gas phase.  However, adapting the Sums of Product (SOP) technology, we found summations of 5 groups of four qubits could successfully simulate the Nitrogen in the ground state and at a very difficult radius of 3 Angstroms.  CCSD(T) fails in particular in the breaking of the three bonds in diatomic nitrogen at the larger radius of 3 Angstroms.  Being able to achieve excited states at both radii with FCI quality is extremely useful.  Unlike FCI, we do not represent each Slater determinate as a separate mathematical object, instead we approximate the global sum of Slaters in the SOP representation.  The number of terms, Canonical ranks, in this sum of products of 4 Qbits is proportional to the complexity of the wavefunction. We feel it is demonstrative of the capacity of this algorithm that we could solve these complex problems.

The SOP representation effectively overcomes the Number of Qbit problem, and refocuses the complexity challenge to maintaining a global wave function via summations of products of, in this case, 4 qubit basis sets. We attacked this problem with full complexity to assure an answer found would be correct.  There are roughly 8000 2-body terms in the N2 Hamiltonian of the ground state and 15000 terms in the 3 Angstrom radius computation.  The terms are computed in pySCF.  All of these terms are acted on the basis via an algorithmic package that can construct arbitrary sums and products of ladder operators; other operators allowed include 1st quantization Kinetic and Coulombic terms.  The public release of the high level API, [Cepheus](https://github.com/Quantum-Galaxies-Corporation/Cepheus), is on Github.   


It is interesting to note that in first quantization, the number of terms in the same Hamiltonian would not exceed 100 or so, which may be an advantage in particular on a quantum hardware, where each term adds error to the summation.  Of course, we could have solved even more complex arrangements of atoms with perhaps a smaller number of interacting terms.  For instance, if we only retain terms above a milliHartree, the Hamiltonian size is more than halved. 



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
