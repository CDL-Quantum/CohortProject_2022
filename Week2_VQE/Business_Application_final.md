# Business Application for Co-design Approach applied to Superconducting Circuits and VQE

# Technical problem

## Layperson description:


Similar to soccer, hockey, and other shooting-ball-to-score-goal sports, spectator qubits can affect player qubits’ shooting in a quantum processor. A player influenced by spectators' unwanted interactions can make unwanted mistakes. In a quantum processor, even with a few qubits, there are always-on unwanted interactions between qubits. A quantum algorithm requires hundreds of perfect and fast interactions between qubits. Mixing these interactions with unwanted interactions makes optimization difficult. We may be able to reduce unwanted interactions on the hardware but will never get entirely rid of them. Facing this reality makes an opportunity to consider co-designing hardware and software, our key target. 

Co-designing quantum hardware and quantum algorithms is the critical link to making processors reliable for quantum algorithms, aiming at tailoring hardware and software as efficiently as possible. We can all relate to simple mental examples of companies such as Tesla, Porsche, Leica, Braun or Casio that have taken different approaches to co-design their products and the software layer. However, they are all approaching a unified model to maximize production efficiency by upgrading their software. 

Similar strategies have inspired us to develop a quantum hardware/software stack and to compete in the future against other market players; it will be essential to have identified an economically feasible approach to co-designing the elements in this stack while pursuing high-quality, novel and valuable tools for the end user.


## Hardware under study

Given that superconducting qubnits are the most scalable and tunable harware we use quantum computers based on superconducting circuits.

https://sites.google.com/site/mansari/home/research

## Technical/detailed description:

- Problem definition:

Standard gates between a pair of superconducting qubits are far from being perfect. This always act as a limiting factor in front of scaling up the number of qubits in a quantum processor; qubits talk to one another without our control on them. This affects the performance of quantum algorithms on a processor.    

- Hardware-efficient ansatz:

Unwanted interactions are not fixed values and they change under applying gates. Therefore we cannot ab intio measure and identify all unwanted interactions in the processor before applying algorithm on the processor.  However the presence of parasitic interactions affects gates, so that learning parastic interactions can be automated at the same time a quantum algorithm is implemented.  

- Variational Quantum Circuit implementation:

?

- Quantum Machine Learning (QML) aspect:

? (Josephine maybe?)

- Performance analysis:

?

# Real-world problems

Several co-design examples exist where research groups and companies have tailored the hardware to the specific mathematical problem to be solved. For example the company IQM studied the quantum simulation of nanoscale NMR with a co-design approach [Algaba et al., 2022]. Nanoscale NMR studies are important for medical applications such as improved detection of tissue malformations without the need of applying radiation (X-rays) to the human body.

# Potential customers

Customers who are looking for being able to have access to the whole hardware and software stack to tailor their problems in the most flexible way to the provided computational infrastructure.


# Video for customer value proposition



# References

[Algaba et al., 2022] Manuel G. Algaba, Mario Ponce-Martinez, Carlos Munuera-Javaloy, Vicente Pina-Canelles, Manish Thapa, Bruno G. Taketani, Martin Leib, Inés de Vega, Jorge Casanova, Hermanni Heimonen ;"Co-Design quantum simulation of nanoscale NMR"; https://arxiv.org/abs/2202.05792

[Ku et.al. 2020] Jaseung Ku, Xuexin Xu, Markus Brink, David C. McKay, Jared B. Hertzberg, Mohammad H. Ansari, B.L.T. Plourde, Suppression of Unwanted ZZ Interactions in a Hybrid Two-Qubit System, arXiv:2003.02775 , Phys. Rev. Lett. 125, 200504 (2020).

[Xu, et.al. 2021] Xuexin Xu and M.H. Ansari, ZZ freedom in two qubit gates, arXiv:2009.00485, Phys. Rev. Applied 15, 064074 (2021).

[]

[]

[]

[]
