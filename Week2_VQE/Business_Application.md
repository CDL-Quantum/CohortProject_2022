![CDL 2022 Cohort Project](../CDL_logo.jpg)
# Quantum Cohort Project Business Application

For each weekly project, your team is asked to complete the below business application exercise.
To complement the technical tasks, please consdier the four questions below.
You are free to format your response to these four questions as you wish (with the final question done as a short recorded video), and to include
the content (or links to the content) on your forked repository.

A brief example for each question is included for the 
[Traveling Salesman Problem.](https://en.wikipedia.org/wiki/Travelling_salesman_problem)

## Step 1: Explain the technical problem you solved in this exercise

Example: Finding a global minimum in settings where a classical approach may not be able to find a global minimum.

## Step 2: Explain or provide examples of the types of real-world problems this solution can solve

Example: A courier has to deliver parcels to several locations and is looking to minimize its travel time. (e.g., “the travelling salesman problem”).

## Step 3: Identify at least one potential customer for this solution - ie: a business who has this problem and would consider paying to have this problem solved

Examples: 
- Federal Express
- Canada Post

## Step 4: Prepare a 90 second video explaining the value proposition of your innovation to this potential customer in non-technical language

Example: By travelling to all destinations via the shortest route, a courier can generate the same revenue that it would have generated following any other route, but will minimize travel costs (e.g., fuel costs). By minimizing travel costs, the courier will be more profitable than it would have been had it travelled through any other route.

**Please store your video externally to the repo, and provide a link e.g. to Google Drive**



## Quantum chemical reaction with VQE
This is the technical section of the business application. We will  outline how the electronic structure Hamiltonian is used in the process to get an accurate description of the interaction. The electronic structure Hamiltonian for a geometry $x$ is defined

$$ H(x) = \sum_{pq} h_{pq}(x)c_p^\dagger c_q+\frac{1}{2}\sum_{pqrs}h_{pqrs}(x)c_p^\dagger c_q^\dagger c_rc_s.$$



   1. Generte an initial reaction path (geometry)  $x_0.$
   
   2. Generate a circuit for some parameters $\theta_0$, to get an ansatz state  
      $$|\psi(\theta_0)= U(\theta_0) |HF\rangle. $$
   
   3. Compute the expectation value of the Hamiltonian $$g(\theta_0, x_0)= \langle \psi(\theta_0)|H(x_0)|\psi(\theta_0)\rangle. $$
   
   4.  Optimize $\theta_0$ and $x_0,$ by computing the gradient  $$\nabla_{\theta_0}g(\theta_0, x_0) ;\nabla_{x_0}g(\theta_0, x_0).$$
    Repeat this step until you get optimal parameters  $\theta_{\text{opt}}$  and  $x_{\text{opt}}.$
   
   5. The optimized reaction path is then given to the neural network.  The activation energy $E_a$ is computed from the ground state $$\psi(\theta^*)\rangle $$ and the reaction path. From the activation energy, one can then compute the reaction rate. The data from the electronic structure Hamiltonian can be used to train neural-network and which can later predicct a chemical reaction with high acuracy. One of the challange in AI based leanred drug discovery is the lack of good data to train the model on. So, if the data is not good, what ever it preidcts is also not good. 
