![CDL 2022 Cohort Project](../CDL_logo.jpg)
## Project 3: Shor's algorithm

Team 7: Madhava Syamlal, Shinibali Bhattacharyya, Sultana Hadi, Shan Zhong, Ruolan Xue

The security of many encryption algorithms, such as RSA, relies on the presumed difficulty of the semiprime factorization problem using classical computers, i.e, for a given large semiprime $N$, how to find the prime numbers $p$ and $q$ that gives $p*q=N$?

This project is an exploration of the quantum gate-model implmentation of Shor's algorithm and its scaling for semiprime factorization. Quantum computer promises polynomial scaling in time required for factorizing an $n$-bit semiprime number, compared to exponential scaling in classical computers.

## Solutions:
* Encrypt and decrypt a message using RSA: [Task 1 Solution](./Task_1.ipynb) 
* Research and implement the quantum algorithm for order finding for factorizing $N=91$: [Task 2 Solution](./shor_task2.ipynb)
* Use Shor's algorithm to factor increasingly large sequences: [Task 3 Solution](./Task_3.ipynb)
* Discuss a new quantum-safe protocol as part of your Business Application: [Business Application](https://youtu.be/-fg8Jq4fE98)

## Further Challenges:
* Implementation of Shor's algorithm on IBM quantum hardware [Challenge 1 Solution](./Challenge_1.ipynb)

## Business Application

## The technical problem you solved

Using the power of quantum simulations, we were able to factorize semiprime numbers upto $N=91$, which is $7$-bits large, within 9 hours CPU time on our local machine, i.e. Apple Macbook with M1 chip & 16 GB RAM. Our current algorithm adapted from [Buearegard 2003](https://dl.acm.org/doi/10.5555/2011517.2011525) uses $0(n^3lg(n))$ elementary quantum gates in a depth of $0(n^3)$ quantum circuit. The number of qubits required scales as $2n+3$ for a $n$-bits semiprime number. With more efficient algorithmsn in the future, even lesser number of qubits can be used.

## Explain or provide examples of the types of real-world problems this solution can solve

The strength of many encryption algorithms that use large semiprime number $N$ ($2048-4096$-bits) in their public keys, is based on the fact that such large $N$ cannot be factorized on classical computers using current state-of-the-art algorithms. This is due to the gigantic amount of time ($\approx 1000$ years) and resources required for such algorithms, even if they are executed in the world's fastest computers. The highest RSA number factored on a classical computer was [RSA-768](https://phys.org/news/2014-11-largest-factored-quantum-device.html#:~:text=%22The%20highest%20RSA%20number%20factored,with%20exactly%20two%20prime%20factors.), which has $768$-bits and took two years to compute (from 2007 to 2009). With the arrival of fault-tolerant quantum computing era with 10000+ qubits, this basic assumption about the difficulty of semiprime number factorization will no longer hold true. It could take only a few seconds for anyone with access to an actual fault-tolerant quantum computer to factorize $2048$-bits or larger numbers.

Secured digital payments worth US $\$ 8.5 $ trillion and around $1$ Exabyte of end-to-end encrypted data is [exchanged daily around the world](https://www.statista.com/outlook/dmo/fintech/digital-payments/worldwide). All it takes is a machine capable of factorizing large semiprime numbers, and hence, breaking the very notion of security on which such RSA-like encryption algorithms are based. This will allow the hacker to have access to any cyber information with digital footprint of their public keys from the past; and steal data and wealth worth more than $\$ 100$ trillion dollars till date! That is greater than $2.5$ times the combined current GDP of USA, Canada and Europe! Such technology, if falls into the wrong hands, could potentially set the stqge for the next *WeltKrieg*!

Our quantum-safe cryptography protocol works around the above-mentioned problem by bypassing the RSA logistics. Instead, it leverages quantum correlation, quantum random generator, and is based on erasable quantum memory, to generate unhackable key-pairs. More resources are required and further research needs to be done to convert our protocol into a user-friendly, scalable premium software product. For more details, please follow our [video](https://youtu.be/-fg8Jq4fE98), and the corresponding [transcript](./Business_Application.md).

## Identify at least one potential customer for this solution - ie: a business who has this problem and would consider paying to have this problem solved

- Government and Defense industry
- Banking and finance sector
- B2C communication platforms like Signal, WhatsApp, etc.
- Any organisation/company with digital footprint that requires privacy of their information exchange (healthcare, telecom, energy and utilities, logistics, automotive, education)

## Prepare a 90 second video explaining the value proposition of your innovation to this potential customer in non-technical language

Link to the science-fiction story, of a conversation taking place in the backdrop of High Park, Toronto: [Business Application found here](./Business_Application.md)
Link to the video trailer highlighting snippets of the conversation: [Bussiness Application video](https://youtu.be/-fg8Jq4fE98)