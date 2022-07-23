![CDL 2022 Cohort Project](../CDL_logo.jpg)
## Project 3: Shor's algorithm

Team 2 - Week 3: Mykola Maksymenko, Jordan Smith, Sourav Sen Choudhury, Ezad Shojaee, Kenneth Sharman

## Task 1: Privacy is key

...

## Task 2: Everything is in order

Please see [task2_3_calculations.ipynb](./Calculations/task2_3_calculations.ipynb) for the calculation details associated with task #2 and #3.

![task2.1](./Images/task2.1.PNG)

![task2.2](./Images/task2.2.PNG)

![task2.3](./Images/task2.3.PNG)

Our first attempt at implementing the quantum order finding algorithm was following the $\texttt{QISKIT}$ tutorial found [here](https://qiskit.org/textbook/ch-algorithms/shor.html). Unfortunately, we were unable to determine how to implement the modular exponentiation function for $N=91$. The quantum circuit is supposed to be constructed on the single-gate level, and we were unsure how to decompose the modular exponentiation function into $\texttt{SWAP}$ gates.

Our next attempt to implement the quantum order finding algorithm was by using another $\texttt{QISKIT}$ tutorial found [here](https://qiskit.org/documentation/tutorials/algorithms/08_factorizers.html#:~:text=Shor's%20Factoring%20algorithm%C2%B6,N%20%3D%2015%20backend%20%3D%20Aer.). This approach was much simpler computationally, as the functions required to implement the entire algorithm are included in the library package- including the modular exponentiation. Again, our attempts to use this package for the case of $N=91$ failed due to insufficient memory to execute the code. Note that we also experimented with different values of $a$, with no success. Additionally, we verified that the memory issue was not a Jupyter Notebook issue, and found that running the relevant code from the command line also produced the memory error.

![qiskit_memory](./Images/qiskit_memory.PNG)

We decided to implement a classical algorithm to solve the order finding problem. This was not the ideal solution, but it was a method to move forward on this task. For the curious reader, please see [task2_3_calculations.ipynb](./Calculations/task2_3_calculations.ipynb) for the code we used to implement the algorithm.

For $N = 91$, our code calculates the factors to be (p,q) = (13,7). Since 13x7=91 and we know that 13 and 7 are both prime, the code produces the correct result. Further, the values of a = 2 and r = 12 yield 2^12 % 91 = 1, which is the desired result.

Our analysis shows that even using a classical order finding method, breaking RSA which uses 7 bit number (91 = 0b1011011) is very easy. It only takes ~15 microseconds to run the (rather unoptimized) code. That's just a 7 bit number though- we should expect that this will get much tougher for larger numbers.

## Task 3: Are we running Shor-t on time?

Please see [task2_3_calculations.ipynb](./Calculations/task2_3_calculations.ipynb) for the calculation details associated with task #2 and #3.

You will likely have noticed in Task 2 that Shor's algorithm is not guaranteed to find a solution. In fact, there are few potential points of failure. How often does your implementation succeed? How does this depend on the size of ?

Further to this point, now that you have an implementation, let's stress test it. Use Shor's algorithm to factor a sequence of increasingly large . How large of a number can you reliably factor with your computer? As you are increasing , take the opportunity to perform an analysis of:

- Run time (wall time)
- Number of qubits required
- Number of quantum gates required

Present your results graphically and use this to infer the scaling of these resources with the size of the problem instance.

After, consider the following: how does the size of your largest solved instance compare with the size of RSA keys in use today? Can you estimate the quantum resources that would be needed to factor numbers of this size, and when we might have a device capable of doing so? Consider the qubit count and gate count in your estimate. To take things further, you could even estimate a rough wall time by looking at circuit depth, and gate operation speeds of present-day hardware.

To investigate the runtime and failure rate associated with Shor's algorithm, we utilize the code as implemented in task #2 ([task2_3_calculations.ipynb](./Calculations/task2_3_calculations.ipynb)). Recall that instead of stimulating the quantum order finding algorithm, we execute a classical version. Thus, our analysis here can be veiwed as an upperbound to the runtime associated with Shor's algorithm which utilizes quantum order finding.

![shor_comp](./Images/shor_comp.PNG)

The plot on the left shows how the runtime, i.e., the number of operations, of the modular exponential function scales with the number of input bits. $N$ is the divisor and $n$ is the number of bits when $N$ is represented as a binary. The red data points correspond to the runtime of the modular exponential function as implemented classically in task 2 (there are so many data points that map to a particular number of bits that when plotted, they appear as a vertical line). We see that in the worst case, the algorithm scales as $O(2^n)$, i.e., it is exponential. With quantum modular exponentiation, on the other hand, the number of operations scales as $O(n^3)$ when the quantum circuit has been efficiently implemented [1].

The plot on the right shows the average numer of failures when Shor's algorithm is implemented using the classical order finding algorithm. The classical implementation has relatively few failures for inputs that are one byte in size or less. The problem is that the number of failures explodes for lager $N$. Thus, attempting to break an input key of length 2048 bits is a formidable task and classical computers have no chance. The largest number our code could factor in a reasonably short amount of time was $N = 4294967297 = 2^{32} + 1$ which takes approximately 1.6 seconds. Unfortunately, this is nowhere near a 1024 or 2048 bit number. RSA has therefore been considered an excellent cryposystem since it was first proposed in 1977, but quantum computers threaten the long-term success of this protocol.

## Task 4

Please see our [business application](./Business_Application.md)

## Challenge 1

Try running your implementation of Shor's algorithm on real quantum hardware. How large of a number can you successfully (and reliably) factor?

## Challenge 2

As you will have discovered in Task 3 (and Challenge 1), Shor's algorithm is not going to be running at scale on NISQ devices any time soon. However, given that NISQ devices are particularly suited to variational algorithms, researchers have investigated whether factoring can be recast into this framework. For this challenge, explore and implement variational quantum factoring. Compare its resource usage and solution quality to that of your initial approach. How large of a number can you successfully factor?

### The Variational Quantum Factoring Algorithm 

The aim ofthe algorithim is given a number $m$ find $p$, $q$ such that $m = p \times q$. Both $p, q$ are primes. 


### Factoring as binary optimization:

- We want to set this factoring problem up as a optimization problem. So what are we to  optimize ? In the paper [variational quantum factoring](https://arxiv.org/abs/1808.08927) the optimization is set up as the following 

![challenge2.1](./Images/challenge2.1.PNG)

From the binary multiplication $m=p\times q$ we get the following equation [factoring as optimization](https://www.microsoft.com/en-us/research/publication/factoring-as-optimization/),

![challenge2.2](./Images/challenge2.2.PNG)

### Classical preprocessing:

After this the the above equations  are simplified (i.e truncating the summation of of the final term in equation (2) above)  by applying some  classical preprocessing rules ( see [variational quantum factoring](https://arxiv.org/abs/1808.08927))

### Constructing the Ising Hamiltonian

![challenge2.3](./Images/challenge2.3.PNG)

### VQF Algorithim

- Step 1: Feed the mixing hamiltonian and the cost Hamiltonian to the QAOA circuit

- Step 2: Obtain a set of good initial parameters (both for mixing and cost hamiltonians) from output of step 1. (quantum optimization)

- Step 3: Feed the paprametrs of step 2 to the BFGS optimizer

- Step 4:  Repeat step 2 with the optimized parameters from the output of step 3. (classical optimization)

- Step 5: Repeat steps 2,3,4 until some convergence criteria is satisfied.

- step 6: Measure quantum state to obtain results

Therefore there are essentials four blocks  in the VQFT implementation.

1. Preprocessing
2. Hamiltonian creation
3. Parameter initialization (this is where quantum optimization happens )
4. Classical optimization

### Results of Implementation


Looking at the original paper ([variational quantum factoring](https://arxiv.org/abs/1808.08927)) and the experiments performed by [mstechly](https://github.com/mstechly/vqf) we find the following- 

1. As $m$ gets bigger the the number of qubits needed to factor $m = p \times q$ icreases rapidly without classical preprocessing. With classical preprocessing however the number of qubits increases much more slowly.

2. Further elaborating on the above if we don't know the length of $p, q$ the qubit scaling (with classical preprocessing)  in advance is worse that compared to the case when the  length of $p, q$ is known.

3. The closeness of the VQF results tothe exact result crucially depends of the choice of $m$. For certain numbers the VQF results are very close to the exact one, whereas for others its very bad (see FIG. 2. in [variational quantum factoring](https://arxiv.org/abs/1808.08927)).   

4. The number of BFGS function evaluations increases withthe number of circuit layers (see FIG. 3. in [variational quantum factoring](https://arxiv.org/abs/1808.08927)). (The scaling is approximately linear.) 

5. [mstechly](https://github.com/mstechly/vqf) also found that for certain numbers no matter how hard you try, you cannot find the exact solution with just one QAOA layer.

## Challenge 3

Researchers have also explored how to factor using quantum annealers. Try implementing the method described in this paper. Consider a solution that uses simulated classical annealing, i.e. classical Monte Carlo. Again, compare its resources and solution quality to your initial implementation, and that of Challenge 2 if you completed it.

## References

[1] Van Meter, Rodney, and Kohei M. Itoh. "Fast quantum modular exponentiation." Physical Review A 71.5 (2005): 052320.
