![CDL 2022 Cohort Project](../CDL_logo.jpg)
## Project 1: MIS Optimization wth neutral atom arrays

This project will guide you through a novel quantum computing architechture pursued by a number of quantum startups, which trap neutral ``Rydberg'' atoms in an arbitrary array with optical tweezers.

Open [INSTRUCTIONS.md](./INSTRUCTIONS.md) to begin learning about your project for this week!


**Please edit this markdown file directly with links to your completed tasks and challenges.**

## Tasks include:
* Run this [Bloqade script](https://github.com/QuEraComputing/Bloqade.jl/blob/master/examples/2.adiabatic/main.jl) to prepare the Z2 state with 9 sites.
* What's the maximum number of atoms for which you can prepare the Z2 state with this adiabatic protocol.
* Repeat with PastaQ (Adiabatic or QAOA)
* Run this [Bloqade script](https://github.com/QuEraComputing/Bloqade.jl/blob/master/examples/4.MIS/main.jl) to find the solution for the MIS problem using the adiabatic approach.
* What is the maximum number of atoms for which you can define and solve the MIS problem with a random dropout graph?
* Repeat with PastaQ - compare the expectation values of the (classical) target Hamiltonian between the state found with Bloqade.

## Further Challenges:
* Use the [blockade approximation](https://queracomputing.github.io/Bloqade.jl/dev/subspace/) in the above problems, and discuss performance differences.
* Choose one of the industrial applications from [this paper](https://arxiv.org/abs/2205.08500) and solve it using your method of choice.

## Business Application
For each week, your team is asked to complete a Business Application. Questions you will be asked are:

* Explain to a layperson the technical problem you solved in this exercise.
* Explain or provide examples of the types of real-world problems this solution can solve.
* Identify at least one potential customer for this solution - ie: a business who has this problem and would consider paying to have this problem solved.
* Prepare a 90 second video explaining the value proposition of your innovation to this potential customer in non-technical language.

For more details refer to the [Business Application found here](./Business_Application.md)