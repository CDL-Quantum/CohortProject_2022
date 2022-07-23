![CDL 2022 Cohort Project](../CDL_logo.jpg)
# Quantum Cohort Project Business Application

For each weekly project, your team is asked to complete the below business application exercise.
To complement the technical tasks, please consdier the four questions below.
You are free to format your response to these four questions as you wish (with the final question done as a short recorded video), and to include
the content (or links to the content) on your forked repository.

## Step 1: Explain the technical problem you solved in this exercise

In this exercise, we explored public-key cryptography by using the RSA algorithm to distribute asymmetric keys, and we used those keys to encrypt and decrypt messages from plaintext to ciphertext and vice versa. We then implemented a simulation of Shor's algorithm and broke RSA for small numbers by prime factorization, demonstrating the threat that a fault-tolerant quantum computer presents to RSA (as well as to discrete logarithm- and elliptical curve discrete logarithm-based key distribution algorithms). The majority of Shor's algorithm is actually classical in nature, with the exception of one crucial step: order finding. The main differentiator between classical factorization methods and the quantum order-finding algorithm is that classical methods require brute-force solving for a multiplication factor, $d$, by trying the computation for each integer value, one-by-one, while the quantum order-finding algorithm exploits quantum superposition and entanglement to converge onto the correct value of $d$ using a single computation, with high probability.

We explored the quantum order-finding algorithm using Qiskit, and we showed that a classical implementation of the order-finding algorithm scales as $\mathcal{O}(2^n)$, where $n$ is the number of bits in the binary representation of the number, $N$, to be factorized. With efficient circuit design, the quantum order-finding algorithm can accomplish this same task in polynomial time, representing a superpolynomial speedup. We also computed the probability of failure of Shor's algorithm using classical order-finding techniques, and found that for bit-strings where $n \leq 8$, classical algorithms have a lower failure rate than the quantum order-finding algorithm. For $n \geq 9$, the quantum algorithm has a lower failure rate. Given that RSA using bitstrings with $n \geq 1024$, it is clear that the quantum algorithm run on quantum hardware has a much higher probability of success (in fact, it is so much higher that the classical methods are considered to be intractable, while the quantum method is considered to be a real threat to RSA).

We further explored implementing Shor's algorithm on quantum hardware, as well as factorization using other quantum algorithms designed to be used with NISQ hardware, such as VQE.  

## Step 2: Explain or provide examples of the types of real-world problems this solution can solve

Example: A courier has to deliver parcels to several locations and is looking to minimize its travel time. (e.g., “the travelling salesman problem”).

Example 1: Banks send sensitive financial information over networks on a regular basis. This information is encrypted using classical key distribution protocols such as RSA. An eavesdropper with access to a quantum computer runnning Shor's algorithm could decrypt the ciphertext into plaintext and steal the information.

Example 2: National defense organizations possess and transmit sensitive information that has a sensitivity timescale of tens of years or longer. Despite the fact that quantum hardware capable of executing Shor's algorithm is not yet available, a hostile entity could steal and store information in the form of ciphertext that was encrypted using RSA-generated keys, only to wait until quantum computation power enables the use of Shor's algorithm to decrypt into plaintext and steal the information that pertains to issues of national security.

Example 3: Telecommunications companies act as an information hub, transmitting the data and information belonging to clients across their networks. The use of Shor's algorithm to decrypt and access that information represents a major liability to the telecommunications company. Offering an invulnerable solution to this problem not only reduces the liability of the teleco, but also provides a value proposition that the teleco can offer to its clients.



## Step 3: Identify at least one potential customer for this solution - ie: a business who has this problem and would consider paying to have this problem solved

Examples: 
- Federal Express
- Canada Post

## Step 4: Prepare a 90 second video explaining the value proposition of your innovation to this potential customer in non-technical language

Example: By travelling to all destinations via the shortest route, a courier can generate the same revenue that it would have generated following any other route, but will minimize travel costs (e.g., fuel costs). By minimizing travel costs, the courier will be more profitable than it would have been had it travelled through any other route.

**Please store your video externally to the repo, and provide a link e.g. to Google Drive**
