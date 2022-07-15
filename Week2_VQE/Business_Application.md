![CDL 2022 Cohort Project](../CDL_logo.jpg)
# Quantum Cohort Project Business Application

For each weekly project, your team is asked to complete the below business application exercise.
To complement the technical tasks, please consdier the four questions below.
You are free to format your response to these four questions as you wish (with the final question done as a short recorded video), and to include
the content (or links to the content) on your forked repository.

## Step 1: Explain the technical problem you solved in this exercise

In this exercise, we used various methods to calculate the potential energy surfaces (PESs), electronic orbital structures, and other properties that can be obtained by solving the Shrödinger equation of a given quantum system. As the Hilbert space of a system grows, classical approximation and exact analytical solution methods require exponentially more computational resources. By using the variational quantum eigensolver (VQE) method on quantum computing hardware, one can produce solutions in super-polynomial time which may be advantageous for analyzing large quantum systems. By modelling molecular orbital structures and calculationg bond lengths, molecular formation energies, and other quantities of interest, molecular engineering and design can be used to solve many pain-points in industry. Of specific commercial relevance, here we used density functional theory (DFT) to analyze the molecular orbital structure of a $N_2O-O_2^{ .-}$ system and gain some insight about the potential applicability of $N_2O$ within a proposed mechanism for general anesthesia that was recently published [1].

[1] Smith, Jordan, et al. "Radical pairs may play a role in xenon-induced general anesthesia." Scientific Reports 11.1 (2021): 1-13.

## Step 2: Explain or provide examples of the types of real-world problems this solution can solve

Here we provide several examples of real-world problems that precise and computationally resource-efficient molecular characterization and design would help solve:

First, molecular design is an ongoing challenge in improving battery technology which may help pave the way for future clean energy storage technology.

Second, the past two years have shown us that molecular engineering and synthesis is an important problem to solve in the design of vaccines and other drugs and pharmaceuticals.

Third, understanding molecular structures can help solve the global energy production problem by enabling the production of more efficient materials for energy transformation and harnessing (solar, wind, hydro, etc).

Finally, in the field of medicine, general anesthesia is a poorly understood phenomenon that has significant health risk for the patient, including death. The global anaesthesia drugs market is expected to reach $11.8bn in 2024 and is estimated to grow at a CAGR of 3.9% from 2019-2024[2]. The design and creation of safer, more efficient, and more cost-effective anesthetic agents would present a meaningful solution to an enormous world-wide medical challenge. The mechanism by which general anesthesia takes places remains an open question, although recent work[1] has proposed one explanation for xenon-induced general anesthsia. One particular family of general anesthetics, including xenon, $N_2O$, and cyclopropane, is thought to act on the NMDA receptor of central-nervous-system neurons. The proposed mechanism which explains this behaviour requires the creation of radical pairs in the neuronal biological environment. It is suggested that the quantum effects inherent in the radical-pair mechanism may play a role in a loss of consciousness.

While the recent study analyzed xenon as an anesthetic agent, we used DFT to model a similar quantum system using $N_2O$, another member of the same anesthetic family, instead of xenon, and found that the molecular orbital including the radical electron density extends to the $N_2O$ molecule, indicating that it may also fit within the same mechanism proposed to explain xenon-induced general anesthesia.

This result highlights that classical approximation methods, such as DFT, can be used to model and design molecules that have particularly desirable properties as anesthetic agents, and VQE on quantum hardware can enable similar modelling and design of much larger molecules in significantly less time, enabling the synthesis and production of safer and more cost-effective anesthetics.

[2] https://www.visiongain.com/report/top-25-anaesthesia-drugs-manufacturers-2020/#:~:text=Novartis%2C%20Mylan%2C%20Teva%2C%20Merck%20and%20Other%20Companies&text=The%20global%20anaesthesia%20drugs%20market,anaesthesia%20drugs%20market%20in%202018. Accessed July 14, 2022

## Step 3: Identify at least one potential customer for this solution - ie: a business who has this problem and would consider paying to have this problem solved

Pharmaceutical companies that manufacturer anesthetic agents face this problem and would likely pay to have it solved. These companies include:

- AstraZeneca
- Johnson & Johnson
- Novartis
- Mylan
- Teva
- Merck

## Step 4: Prepare a 90 second video explaining the value proposition of your innovation to this potential customer in non-technical language

Example: By travelling to all destinations via the shortest route, a courier can generate the same revenue that it would have generated following any other route, but will minimize travel costs (e.g., fuel costs). By minimizing travel costs, the courier will be more profitable than it would have been had it travelled through any other route.

**Please store your video externally to the repo, and provide a link e.g. to Google Drive**
