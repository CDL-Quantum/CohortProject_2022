# Business Application for Co-design Approach applied to Superconducting Circuits, VQE and Solvation Calculations

# Technical problem

## Layperson description:


Similar to soccer, hockey, and other shooting-ball-to-score-goal sports, spectator qubits can affect player qubits’ shooting in a quantum processor. A player influenced by spectators' unwanted interactions can make unwanted mistakes. In a quantum processor, even with a few qubits, there are always unwanted interactions between qubits. A quantum algorithm requires hundreds of perfect and fast interactions between qubits. Mixing these interactions with unwanted interactions makes optimization difficult. We may be able to reduce unwanted interactions on the hardware but will never get entirely rid of them. Facing this reality makes an opportunity to consider co-designing hardware and software, our key target.

Co-designing quantum hardware and quantum algorithms is the critical link to making processors reliable for quantum algorithms, aiming at tailoring hardware and software as efficiently as possible. We can all relate to simple mental examples of companies such as Tesla, Porsche, Leica, Braun or Casio that have taken different approaches to co-design their products and the software layer. However, they are all approaching an unified model to maximize production efficiency by upgrading their software. 

Similar strategies have inspired us to develop a quantum hardware/software stack and to compete in the future against other market players; it will be essential to have identified an economically feasible approach to co-designing the elements in this stack while pursuing high-quality, novel and valuable tools for the end user.


## Hardware under study

Numerous physical quantum hardware technologies exist to leverage the extended state space with qubits to compile quantum algorithms.

<!--
The following table give an overview of some of the selected hardware technologies:

| Aspect                        | Superconducting circuits                                               | Trapped ion                                                 | Photonic                                          | Cold atoms |
|-------------------------------|------------------------------------------------------------------------|-------------------------------------------------------------|---------------------------------------------------|------------|
| Qubit lifetime                | Short period (50-100 µs) and susceptible to noises [Hazra2021]         | Minutes and more [Wang2021]                                 | 150 microseconds, but destroyed by measurement [Gerbert2018] |            |
| Gate speed                    | 10-100 ns []                                                           | 20 microseconds []                                          | ~ 1 ns []                                         |            |
| Connectivity & entanglement   | Poor connectivity to other qubits (only nearest and few neighbours) [] | all to all []                                               | Easy to generate entanglement []                  |            |
| Reproducibility & scalability | No significant obstacles to reproduce and control qubits []            | No significant obstacles to reproduce and control qubits [] | Scalable architectures are possible []            |            |
| Operation conditions          | Near absolute zero temperature to operate (20 mK), no vacuum []        | No near absolute zero temperature needed; vacuum needed []  | Possible room temperature []                      |            |
| Maturity [Gerbert2018]        | The furthest developed technology []                                   | Similar to superconducting circuit technology []            | Early stage development (TRL 3) []                |            |
-->

Given that superconducting qubits are the most mature and numerous companies have provided access to their superconducting qubit hardware (IBM, Rigetti, Quantum Inspire) we study VQE quantum computers based on superconducting circuits.

<!--
References

[Hazra2021] S. Hazra, A. Bhattacharjee, M. Chand, K. V. Salunkhe, S. Gopalakrishnan, M. P. Patankar, R. Vijay;
Ring-resonator-based coupling architecture for enhanced connectivity in a superconducting multiqubit
network, Phys. Rev. Applied 16 (2021); https://doi:10.1103/PhysRevApplied.16.024018

[Wang2021] P. Wang, C. Luan, M. Qiao; Single ion qubit with estimated coherence time exceeding one
hour, Nature Communications 12 (1) (2021) 233; https://doi.org/10.1038/s41467-020-20330-w

[Gerbert2018] P. Gerbert, F. Ruess; The Next Decade in Quantum Computing—and How to Play; https://www.bcg.com/publications/2018/next-decade-quantum-computing-how-play

[Shaw2020] David Shaw; "The quantum computing landscape has been transformed by a surge of commercial startups pursuing very different technical paths. Investors and pioneers must prepare themselves for a challenging journey ahead.", 2020; https://www.factbasedinsight.com/quantum-hardware-into-the-quantum-jungle/
-->

## Technical/detailed description:

- Problem definition:

Standard gates between a pair of superconducting qubits are far from being perfect. This always acts as a limiting factor in scaling up the number of qubits in a quantum processor; qubits affect each other without our control on them. This affects the performance of quantum algorithms on a processor.

- Hardware-efficient ansatz:

Unwanted interactions are not fixed values and they change under applying gates. Therefore we cannot ab intio measure and identify all unwanted interactions in the processor before applying algorithm on the processor.  However the presence of parasitic interactions affects gates, so that learning parastic interactions can be automated at the same time a quantum algorithm is implemented.

- Variational Quantum Circuits

Variational quantum circuits allow to prepare a state on a parameterized composition of gates. The iterative classical-quantum approach to optimize these parameters allow to solve for example for the ground state energy of a molecule.

- Machine Learning + VQE

An interesting research paper has just been published to calculate the potential energy surface (PES) of molecules with a simple deep neural network in combination with a VQE algorithm. [Tao2022]


- Performance analysis

In the upcoming Hackathon we are going to implement various approaches to calculate PES and solvation effects with VQE. This business case application can be seen as the rough outline of the Hackathon project and the performance analysis of implemented algorithm will assess how well our implementation compares to fully classical calculation methods.

After this first analysis the co-design approach will taken into account to see if certain kind of gate compositions or hardware schemes might benefit the evaluation of solvation models.

# Real-world problems

Several co-design examples exist where research groups and companies have tailored the hardware to the specific mathematical problem to be solved. For example the company IQM studied the quantum simulation of nanoscale NMR with a co-design approach [Algaba et al., 2022]. Nanoscale NMR studies are important for medical applications such as improved detection of tissue malformations without the need of applying radiation (X-rays) to the human body.

# Potential customers

- Customers who are looking for being able to have access to the whole hardware and software stack to tailor their problems in the most flexible way to the provided computational infrastructure.

- Pharma, biotech and chemical companies which are make use of solvents in their manufacturing processes or product compositions.


# Video for customer value proposition

https://www.loom.com/share/fc5a5969fb104adb906b6e9074e74383

# References

[Algaba et al., 2022] Manuel G. Algaba, Mario Ponce-Martinez, Carlos Munuera-Javaloy, Vicente Pina-Canelles, Manish Thapa, Bruno G. Taketani, Martin Leib, Inés de Vega, Jorge Casanova, Hermanni Heimonen ;"Co-Design quantum simulation of nanoscale NMR"; https://arxiv.org/abs/2202.05792

[Ku et.al. 2020] Jaseung Ku, Xuexin Xu, Markus Brink, David C. McKay, Jared B. Hertzberg, Mohammad H. Ansari, B.L.T. Plourde, Suppression of Unwanted ZZ Interactions in a Hybrid Two-Qubit System, arXiv:2003.02775 , Phys. Rev. Lett. 125, 200504 (2020).

[Xu et.al. 2021] Xuexin Xu and M.H. Ansari, ZZ freedom in two qubit gates, arXiv:2009.00485, Phys. Rev. Applied 15, 064074 (2021).

[Tao et al. 2022]     Yanxian Tao, Xiongzhi Zeng, Yi Fan, Jie Liu, Zhenyu Li, and Jinlong Yang; "Exploring Accurate Potential Energy Surfaces via Integrating Variational Quantum Eigensolver with Machine Learning", 2022; https://doi.org/10.1021/acs.jpclett.2c01738
