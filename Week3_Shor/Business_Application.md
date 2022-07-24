![CDL 2022 Cohort Project](../CDL_logo.jpg)
# Quantum Cohort Project Business Application

In this business application, we present a scoring system for quantum hardware. This neutral, transparent, and understandable benchmarking system is based on Shor's algorithm. It allows all actors on the quantum computing scene to communicate with a common knowledge of the devices, thereby building a bridge between the expert and laymen communities at play.

## Step 1: Explain the technical problem you solved in this exercise

#### Non-technical explanation
What can a quantum computer actually compute? When does it become a threat for your security system? How to convince investors of the utility of your quantum device without falling into the trap of false promises? At QTrust, we provide an independent evaluation service based on Shor’s algorithm to assess existing quantum devices. Our scoring system aims at transparency, clarity, and accessibility for all its users, experts or laymen. Thanks to our score, we build a data bank of quantum devices to follow the evolution of quantum computing towards universal quantum machines. We conduct detailed evaluations both for universal programming and particular tasks to analyze the strengths and weaknesses of devices and help the hardware designers to improve their platform. We provide a simple and understandable score for actors looking for the platform that suits best their application. In addition, our data bank gives visibility to both hardware companies and their users by making their performance public. 

 #### Technical explanation
The problem of benchmarking lies at the center of the development of quantum computing. Goals of a benchmark encompass evaluating the capability of a device to perform particular or universal tasks, understanding the mechanisms behind information losses, such as coherent and incoherent noise. In addition, the results of the benchmark guide users in the zoo of existing platforms: it helps end users to select the right device for their needs and helps tracking their evolution to ensure strategic fundings and investments based on trust. 
Building a comprehensive measure for benchmarking is a difficult task in itself.
- A benchmark can only become meaningful if it is widely adopted by the community and performed under the same conditions for each hardware. Only then can different devices be compared in a fair way. Therefore, we propose to create a data bank to make benchmarking results public in a safe and protected way. The score is evaluated thanks to Shor’s algorithm by our members, in an independent manner. 
- The measures it involves must be performed in an efficient and scalable way. Many methods used up to this day involve the classical simulation of random quantum circuits,  as in the Quantum Volume (Cross et al. 2018) and the Binned Output Generator method (Kim et al. 2021), in order to compare the ideal and real outputs of the circuit. However, this approach is not scalable as the circuit sizes increase. To cope with this problem, we use Shor’s algorithm that is known to have an advantageous scaling on a quantum computer. Applying it to numbers of increasing sizes enables us to make it scalable to larger platforms. The number that can be factorized with high probability is in itself a good indication of how many qubits can be used to perform universal computations.
- The score must contribute to progress: the criteria taken into account set goals for the evolution of quantum hardware and future research. Our experts developed a set of indicators that can be evaluated efficiently to reflect the status of a quantum computer:
  - The number that can be factorized provides indication on the circuit size that can be implemented;
  - The probability of getting a right answer provides insights on the gate fidelity and reliability of the hardware;
  - The time it takes to execute the algorithm reflects the realization of a quantum advantage. This indicator must also differentiate between the time required for quantum operations, and the efficiency of quantum-classical operations;
  - To identify information loss causes, we  implement a measure to detect losses in purity. In the short term, we use the negativity measure $\eta = Tr(\rho^T)-1$ (Kendon and Munro 2006) to circumvent memory issues. In the intermediate term, measures such a Von Neumann entropy $S_{VN}(\rho) = -Tr[\rho \log(\rho)]$ or second order Rényi entropy $S^{(2)}(\rho) = - \log(Tr(\rho^2))$ can be computed at strategic steps of the algorithm. The protocol proposed in (Uzdin 2021) will eventually enable us to quantify explicitly the information loss by building the expectation value of the dissipator. We will ultimately be able to seperate coherent and incoherent errors in our measure, while keeping the test scalable.
- The score can be adapted to perform a holistic or specialized assessment of the hardware. For example, Shor's algorithm can be used for the former, while its variational translation (Anschuetz et al. 2018) quantifies whether the device already has the resources necessary for variational algorithms.

The code for the noisy simulations can be found [here](./NoisyFactorization.ipynb).


## Step 2: Explain or provide examples of the types of real-world problems this solution can solve

###### For security companies and governments:
- The use of Shor's algorithm as a benchmark gives clear predictions on the threat that each quantum computer represents for data encrypted with the RSA scheme. Among our benchmarking indices, we take into account the largest number that can be factorized on each machine using the most efficient implementation of Shor’s algorithm (gate-based, variational (Anschuetz et al. 2018)). This provides a clear timeline to design encryption schemes that resist quantum hacking.
- Does a company or a government need to make quantum technologies a priority to protect its data and that of its clients/population? Our score can help in the decision-making process by giving prognostics that are anchored in the latest real technological achievements in this field.
- The hardware data bank can contribute to orient the efforts to the most relevant platform for the desired application.

###### For investors:
- It is not always clear what can be achieved or not on a quantum computer and why it is promising to invest in quantum technologies. By giving scores that are easy to understand, providing an extensive encyclopedia of quantum computing to educate the public about quantum information and by issuing certificates with authentic grades, we facilitate trust building between companies and their investors.

###### For quantum software companies:
- Working with a particular type of algorithm does not necessarily require a universal quantum computer. We propose a wide range of evaluation protocols that are both targeting universal and specialized tasks so that software companies can easily identify the most suitable platform for their application. By helping companies navigating in the zoo of quantum platforms, we shorten the delay to the proof of a quantum advantage.
- The detailed analysis of each software can contribute to the co-design of algorithms and platforms for an application of choice.

###### For quantum hardware experts:
- Once a quantum device for computing is built, characterization is a long and expensive step. We use Shor’s algorithm to begin with to achieve this in an impartial manner. We provide indicators for gate speed, output fidelity, purity loss and entanglement creation within the device. These cast light onto the successes and points to improve in their device.
- To get out of the hype surrounding quantum computing, our measure is based on an algorithm shown to provide a quantum advantage. Assessing how big of a number it can factorize and the success probability can clarify the current status of quantum computing.
- The certification of your hardware guarantees visibility in the relevant markets by appearing in the data bank, but also by participating to conferences and event as partners, contributing to the quantum computing encyclopedia...


## Step 3: Identify at least one potential customer for this solution - ie: a business who has this problem and would consider paying to have this problem solved

Our service can be attractive both for:
- quantum technology experts
  - in the academia, eg. university labs 
  -  private research institutions such as IBM, Xanadu, IonQ, Google (and other start-ups to be formed at the CDL)
-  investors in the quantum field
-  banking institutions: Credit Suisse, JPMorgan Chase & Co
-  Governements, in particular the military and any department requiring data protection, but also the ministry in charge of research to allocate fundings.  

For the experts, young quantum hardware companies are given the opportunity to compete on an equal footing with the largest companies and quantum developpers are offered access to the data bank to choose the most suitable platform for their application. On the other hand, the score strengthens trust to attract potential investments: a clear report is provided to distinguish rumors and real achievements. Any institution dealing with sensitive data, such as banks or governments, must keep an eye on the evolution of quantum technologies to protect them: to make this process easier, we provide access to our certified data base and encyclopedia for a rapid grasp of the technological evolution.

## References
- Anschuetz, Eric R., Jonathan P. Olson, Alan Aspuru-Guzik, and Yudong Cao. 2018. “Variational Quantum Factoring.” ArXiv, 08 27, 2018, arxiv.1808.08927. https://arxiv.org/abs/1808.08927.
- Cross, Andrew, Lev Bishop, Sarah Sheldon, and Paul Nation. 2018. “Validating quantum computers using randomized model circuits.” PRA, 09 20, 2018, 032328. https://journals.aps.org/pra/abstract/10.1103/PhysRevA.100.032328.
- Kendon, Vivien, and William Munro. 2006. Entanglement and its role in Shor's algorithm. https://arxiv.org/abs/quant-ph/0412140.
- Kim, Jin-Sung, Lev S. Bishop, Antonio D. Corcoles, Seth Merkel, John A. Smolin, and Sarah Sheldon. 2021. “Hardware-efficient random circuits to classify noise in a multiqubit system.” Physical Review A, 08 1, 2021, 022609. https://doi.org/10.1103%2Fphysreva.104.022609.
- Uzdin, Raam. 2021. “Methods for measuring noise, purity changes, and entanglement entropy in quantum devices and systems.” ArXiv, 12 1, 2021, arXiv:2112.00546. https://arxiv.org/abs/2112.00546.

## Step 4: Prepare a 90 second video explaining the value proposition of your innovation to this potential customer in non-technical language

link to the slides: https://docs.google.com/presentation/d/1P6UYxQ1xh4E1AhxwI4ynlWlgVs7XNjeMEnK-kQHldD4/edit?usp=sharing

