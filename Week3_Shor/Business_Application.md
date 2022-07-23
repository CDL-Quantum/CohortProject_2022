![CDL 2022 Cohort Project](../CDL_logo.jpg)
# Quantum Cohort Project Business Application

For each weekly project, your team is asked to complete the below business application exercise.
To complement the technical tasks, please consdier the four questions below.
You are free to format your response to these four questions as you wish (with the final question done as a short recorded video), and to include
the content (or links to the content) on your forked repository.

![Week3_Shor/Images/Logo-TM.png](https://github.com/Jordan-D-Smith/CohortProject_2022/blob/fece547b660c9cdd7933b57692318fe7e82bdfdd/Week3_Shor/Images/Logo-TM.png)

## Step 1: Explain the technical problem you solved in this exercise

In this exercise, we explored public-key cryptography by using the RSA algorithm to distribute asymmetric keys, and we used those keys to encrypt and decrypt messages from plaintext to ciphertext and vice versa. We then implemented a simulation of Shor's algorithm and broke RSA for small numbers by prime factorization, demonstrating the threat that a fault-tolerant quantum computer presents to RSA (as well as to discrete logarithm- and elliptical curve discrete logarithm-based key distribution algorithms). The majority of Shor's algorithm is actually classical in nature, with the exception of one crucial step: order finding. The main differentiator between classical factorization methods and the quantum order-finding algorithm is that classical methods require brute-force solving for a multiplication factor, $d$, by trying the computation for each integer value, one-by-one, while the quantum order-finding algorithm exploits quantum superposition and entanglement to converge onto the correct value of $d$ using a single computation, with high probability.

We explored the quantum order-finding algorithm using Qiskit, and we showed that a classical implementation of the order-finding algorithm scales as $\mathcal{O}(2^n)$, where $n$ is the number of bits in the binary representation of the number, $N$, to be factorized. With efficient circuit design, the quantum order-finding algorithm can accomplish this same task in polynomial time, representing a superpolynomial speedup. We also computed the probability of failure of Shor's algorithm using classical order-finding techniques, and found that for bit-strings where $n \leq 8$, classical algorithms have a lower failure rate than the quantum order-finding algorithm. For $n \geq 9$, the quantum algorithm has a lower failure rate. Given that RSA using bitstrings with $n \geq 1024$, it is clear that the quantum algorithm run on quantum hardware has a much higher probability of success (in fact, it is so much higher that the classical methods are considered to be intractable, while the quantum method is considered to be a real threat to RSA).

We further explored implementing Shor's algorithm on quantum hardware, as well as factorization using other quantum algorithms designed to be used with NISQ hardware, such as VQE.  

## Step 2: Explain or provide examples of the types of real-world problems this solution can solve

Example 1: Banks send sensitive financial information over networks on a regular basis. This information is encrypted using classical key distribution protocols such as RSA. An eavesdropper with access to a quantum computer runnning Shor's algorithm could decrypt the ciphertext into plaintext and steal the information.

Example 2: National defense organizations possess and transmit sensitive information that has a sensitivity timescale of tens of years or longer. Despite the fact that quantum hardware capable of executing Shor's algorithm is not yet available, a hostile entity could steal and store information in the form of ciphertext that was encrypted using RSA-generated keys, only to wait until quantum computation power enables the use of Shor's algorithm to decrypt into plaintext and steal the information that pertains to issues of national security.

Example 3: Telecommunications companies act as an information hub, transmitting the data and information belonging to clients across their networks. The use of Shor's algorithm to decrypt and access that information represents a major liability to the telecommunications company, and a potential loss of trust by its clients. Offering an invulnerable solution to this problem not only reduces the liability of the teleco, but also provides a value proposition that the teleco can offer to its clients.

As our solution to Task 4 of the Cohort Project, we have created a pitch deck to present to one of the potential clients listed in the above use-cases. We present from the perspective of a startup company founded by some of the members of our group, Quantized Technologies Inc. (QTI), and we assume a non-technical audience. QTI is working on solving exactly these sorts of problems, and will offer an initial solution called MDI-QKD (the future commercial product name has not yet been chosen). 

![Week3_Shor/Images/Slide%201.png](https://github.com/Jordan-D-Smith/CohortProject_2022/blob/fece547b660c9cdd7933b57692318fe7e82bdfdd/Week3_Shor/Images/Slide%201.png)

First, we explain the problem to the client. 

Sensitive information is currently kept secure by means of difficult math problems that would take eavesdroppers so long to solve (thousands of years) that it is impractical for them to try. The reason for this is that the computer has to try each possible "passcode" individually, one-by-one. Now, with the advent of quantum computation, an eavesdropper will be able to solve that math problem quickly by trying all possible "passcodes" simultaneously.

![Week3_Shor/Images/Slide%203.png](https://github.com/Jordan-D-Smith/CohortProject_2022/blob/fece547b660c9cdd7933b57692318fe7e82bdfdd/Week3_Shor/Images/Slide%203.png)

The ability of quantum computers to solve difficult math problems in seconds that would take a classical computer thousands of years has been demonstrated, and quantum computers that can break our encryption methods are projected to be created within the next 10 years. Not only should we start implementing systems that are safe against the hacking threat of quantum computers, but if we have information that will remain sensitive for 10 years or longer, we need to act immediately, since a bad actor could download our encrypted information right now, and decrypt it in a few years once capable quantum computers are available.

![Week3_Shor/Images/Slide%204.png](https://github.com/Jordan-D-Smith/CohortProject_2022/blob/fece547b660c9cdd7933b57692318fe7e82bdfdd/Week3_Shor/Images/Slide%204.png)

Now, the solution: quantum physics to the rescue! Given that math problems can potentially be solved with enough computing power, rather than using math problems to generate our encryption keys, we can use an entirely different approach and leverage the laws of quantum physics to create our keys. These quantum-based solutions are called "QKD" solutions. 

![Week3_Shor/Images/Slide%205.png](https://github.com/Jordan-D-Smith/CohortProject_2022/blob/fece547b660c9cdd7933b57692318fe7e82bdfdd/Week3_Shor/Images/Slide%205.png)

But there is a remaining problem. While no amount of computing power can break keys created using QKD, it is possible for an eavesdropper to obtain information about the key if they can access and manipulate the QKD hardware (specifically, the photodetectors). This type of hardware hack is the "Achilles heel" of current commercial QKD systems.

![Week3_Shor/Images/Slide%206a.png](https://github.com/Jordan-D-Smith/CohortProject_2022/blob/197551fd10d12ecfee0f937e62ee42cf8b4dac08/Week3_Shor/Images/Slide%206a.png)

Additional weaknesses of basic QKD solutions include detector cost (the most expensive component of the QKD hardware system, and basic QKD systems require about half of the users to possess a set of detectors), as well as distance limitations over which the systems can function.

![Week3_Shor/Images/Slide%207a.png](https://github.com/Jordan-D-Smith/CohortProject_2022/blob/197551fd10d12ecfee0f937e62ee42cf8b4dac08/Week3_Shor/Images/Slide%207a.png)

Now for the final solution: MDI-QKD. With our MDI-QKD solution, users in a network can obtain and share a secure key, and the security is not compromised even if an eavesdropper manipulates the system detectors. Further, the system is designed using a star-type topology, so only one set of detectors is needed, reducing the overall cost of the QKD network. Finally, MDI-QKD offers functionality over approximately twice the distance compared to basic QKD systems.

![Week3_Shor/Images/Slide%208a.png](https://github.com/Jordan-D-Smith/CohortProject_2022/blob/197551fd10d12ecfee0f937e62ee42cf8b4dac08/Week3_Shor/Images/Slide%208a.png)

A top-down market analysis reveals many national initiatives over the past few years, in which governments are committing larger and larger investments into quantum technologies. Some target market verticals for our solution include banking, finance, insurance, health care, national security, telecommunications, and quantum network testbeds. 

![Week3_Shor/Images/Slide%209.png](https://github.com/Jordan-D-Smith/CohortProject_2022/blob/fece547b660c9cdd7933b57692318fe7e82bdfdd/Week3_Shor/Images/Slide%209.png)

By 2027 the quantum cryptography market is projected to reach ~$13 billion in annual revenue, and our target market includes metropolitan, fibre-based use cases, which we estimate will represent approximately $10 billion. Given our marketing channels, access to regional markets, expected resources, and other factors, we estimate that we can capture 10% of the target market, which represents annual revenue of approximately $1 billion. 

![Week3_Shor/Images/Slide%2011.png](https://github.com/Jordan-D-Smith/CohortProject_2022/blob/fece547b660c9cdd7933b57692318fe7e82bdfdd/Week3_Shor/Images/Slide%2011.png)

While updated math-based solutions, referred to as post-quantum cryptographic (PQC) solutions, are more resiliant against quantum computing compared to the math-based methods of yesterday, it is never-the-less possible that with evolution in quantum algorithms and progression in quantum computing power, these solutions will also be threatened in the future by quantum computing. For this reason, these PQC solutions are software patch solutions that are quantum-resistant, not truly quantum-proof like QKD solutions are. 

![Week3_Shor/Images/Slide%2014.png](https://github.com/Jordan-D-Smith/CohortProject_2022/blob/fece547b660c9cdd7933b57692318fe7e82bdfdd/Week3_Shor/Images/Slide%2014.png)

While PQC and basic QKD solutions do address the threat that quantum computing represents to cybersecurity, we feel that our MDI-QKD solution offers certain competitive advantages. It offers unprecedented quantum-proof -- not just quantum-resistant -- security, cost-effectiveness for a multi-user QKD network, and large functional range compared to basic QKD systems.

![Week3_Shor/Images/Slide%2015a.png](https://github.com/Jordan-D-Smith/CohortProject_2022/blob/59a63e12b707b0fa9a672824216fd1e8803fd097/Week3_Shor/Images/Slide%2015a.png)

We hope to be able to find the right fit so that our MDI-QKD solution can reduce the pain-points experienced by your organization!

## Step 3: Identify at least one potential customer for this solution - ie: a business who has this problem and would consider paying to have this problem solved

- National Bank of Canada: Communication between metropolitan branches and headquarters involves sensitive information that would benefit from increased security.
- US Department of Defense: Communications involving information related to national security may be sent over optical fiber networks, and maximum security of this information would be worth paying for.
- AT&T: As a telecommunications company that provides data transmission services to many clients, security of the data transmitted is not only extremely important as a service provider, but its clients may also be interested in purchasing a solution for increases data security.

## Step 4: Prepare a 90 second video explaining the value proposition of your innovation to this potential customer in non-technical language

See [this](https://1drv.ms/u/s!Aly-26RuXWZBxWQlp3iW_NDQ4t6i) link for our value proposition video.

**Please store your video externally to the repo, and provide a link e.g. to Google Drive**
