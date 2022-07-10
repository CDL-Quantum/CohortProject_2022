![CDL 2022 Cohort Project](../CDL_logo.jpg)
# Project 1: INSTRUCTIONS

Contributed by Arunanghu Debnath on behalf of the working subgroup.


## Task 1: Adiabatic state preparation with Bloqade

The study was performed to study symmetric detuning range, higher Rabi pulse area. Predictably it prepares a site distribution and not site-specific state profiles.

## Task 2: Larger arrays with the Blockade Approximation

What is the largest 1D array that you can simulate for the full Rydberg Hamiltonian, with exact time evolution as above? 
What implications does this have for quantum advantage, particularly in light of the experiments mentioned above?

Next, in order to significantly reduce the size of the state space required to solve Rydberg problems, one can eliminate states that violate the blockade constraint (e.g. more than one atom being excited within $R_b$).  Implement the [blockade approximation](https://queracomputing.github.io/Bloqade.jl/dev/tutorials/2.adiabatic/main/#Emulation-in-the-Blockade-Subspace) and justify it; i.e. when do you expect it to be valid? You can find more detailed explaination about this approximation in [Rydberg Blockade](https://queracomputing.github.io/Bloqade.jl/dev/tutorials/1.blockade/main/) section.

Repeat your study of 1D arrays, and find the largest system for which you can adiabatically prepare the $\mathbb{Z}_2$ state.
What is the largest 2D array for which you can adiabatically prepare the checkerboard phase?  Has quantum advantage for 2D arrays already [been achieved](https://www.nature.com/articles/s41586-021-03582-4)?

## Task 3: MIS

Maximum Independent Set (MIS) is a combinatorial optimization problem that is naturally suited to implementation on a Rydberg atom quantum computer. Specifically, the Rydberg blockade implies that two atoms cannot be both excited to the Rydberg state $| r \rangle$ if they are close to each other. In MIS, the independent set constraint means that two vertices on a graph cannot be both in the independent set when they are connected by an edge. Thus, one can consider atoms in the Rydberg state as vertices in an independent set. Read more about the MIS problem [here](https://queracomputing.github.io/Bloqade.jl/dev/tutorials/4.MIS/main/#mis-tutorial).

Following the Bloqade tutorial [script](https://github.com/QuEraComputing/Bloqade.jl/blob/master/examples/4.MIS/main.jl), solve the $4 \times 4$ diagonal-connected unit-disk grid graphs (DUGG) problems using the adiabatic approach. How large of an array can Bloqade solve?  Attempt to solve for larger square DUGGs using your tensor network approach. Try different pulse parameterization and compare which is better, and explore how smoothing affects the performance.

## Task 4: Business applications

Finally, use your simulations to solve a groundstate encoding problem for an industrial application.  You may come up with your own, or look at one of the examples given in this recent [preprint](https://arxiv.org/abs/2205.08500): i.e. Portfolio optimization (example VI), Network immunization (example VII), or Task scheduling (example XII). Set up a problem, and solve it on as large a graph as possible using adiabatic state preparation protocols. Link this to your [Business Application](./Business_Application.md).

### Once you are comfortable with the above tasks, you may turn to one or more of the below optional **Challenges** for any time remaining in your project. 

## Challenge 1:
To push your classical simulations further, consider using a tensor-network based method (such as Matrix Product States), implemented in [iTensor](https://itensor.org) or [PastaQ](https://github.com/GTorlai/PastaQ.jl). To time-evolve a quantum state under the dynamics of the Rydberg Hamiltonian, the simplest method is to use "time evolving block decimation" (TEBD). This is the procedure of decomposing the time-evolution operator into a circuit of quantum gates (two-site unitaries) using the Trotter-Suzuki approximation and applying these gates to the tensor network state. See tutorials [here](https://docs.juliahub.com/ITensors/P3pqL/0.2.0/getting_started/Tutorials.html#Getting-Started-with-MPS-Time-Evolution-1).

Implement TEBD using the blockade approximation (see Task 2). Benchmark your tensor network against the results from Bloqade, then repeat for larger 1D arrays.  How large can you trust your results using tensor networks? How does this compare with current experimental capabilities?  Can you prepare a 2D state of size comparable to current experiments? If tensor networks are state-of-the-art, what do they imply about *quantum advantage* in Rydberg devices?

## Challenge 2:
In addition to adiabatic protocols, other state preparation protocols are currently being explored on quantum computing hardware.  A leading variational protocol is the Quantum Approximate Optimization Algorithm ([QAOA](https://queracomputing.github.io/Bloqade.jl/dev/tutorials/4.MIS/main/#QAOA-with-Piecewise-Constant-Pulses)), in which time evolution occurs via rapidly switching between a cost and mixer Hamiltonian.  For your problems above, particularly your Business Application, attempt a QAOA solution and compare your results to the adiabatic approach.

## Challenge 3:

As laid out in the [preprint](https://arxiv.org/abs/2205.08500), there are other applications of Rydberg atom arrays to industry problems, that may require quantum machine learning, quantum sampling algorithms, or other techniques. Explore one of these further applications using your numerical strategies above.

## Challenge 4:

Rydberg atom quantum computers are not the only hardware available to solve MIS and related problems. By employing a suitable mapping (e.g. to a QUBO Hamiltonian), solve any version of your problems using any available quantum hardware, e.g. D-Wave or IBM. Compare and contrast the quantum solutions to the classical simulations that you have employed above.





