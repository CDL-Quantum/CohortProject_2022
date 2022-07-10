<script src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML" type="text/javascript"></script>


![CDL 2022 Cohort Project](../CDL_logo.jpg)
# Business Application : Oracle of assets

*Quantum in economics, it changes everything and we help you make your decisions!*



<center><img src="images/Oracle.png" width="200"></center>
<center>Figure 1. Logo for Oracle of assets. </center>



## Introduction

One of the challenges of computing is to solve problems with a large amount of data, but there are some problems due to their complexity that take a long time to solve, these are known as NP problems, and one of these is the Maximum Independent set (MIS), there are different proposals to solve but they fail to reduce its complexity as the greedy strategy. There is possible in  a graph $$G(n, m)$$ that contains $$n$$ vertices and $$m$$ edges, it is known that unless $$\mathrm{P}=\mathrm{NP}$$ no polynomial algorithm can find a $$O\left(n^{1-\epsilon}\right)$$ approximate solution in the worst case.


![Example of a Graph](images/graph.png)
<center>Figure 2. Example of a graph. </center>



One of the latest efforts in quantum computation research is to use a sizable quantum many-body system to solve non-deterministic polynomial-time (NP)-optimization problems. One proposal is the design of the Rydberg Blockade, one of the most important properties of neutral-atom quantum computing based on Rydberg states. It naturally encodes the independent set constraint. Other is using The Quantum Approximate Optimization Algorithm (QAOA), where a quantum state is created by a p-depth circuit specified by 2p variational parameters and using a classical optimizer to find the  best states. 



In the financial markets are complex environments that produce huge amounts of noisy data. Therefore, there are difficulties in dealing with these, one of the problems, online portfolio selection, aims to exploit data from different stocks to select asset portfolios in order to obtain positive investment results considering to decrease the different possible risks. One option is use the quantum advantage to improve this kind of  problems.



## Problem: Portfolio optimization 

By considering the above case, the portfolio optimization problem can be implemented. Where each stock has time-dependent returns, which may or may not be correlated with other stocks. For this, a graph must be considered where each vertex is a stock, and there is an edge between the vertices if the assets are correlated or not within a certain threshold. 




![Example of a Graph](images/graph_init.png)
<center>Figure 4. Example of a Graph for Portfolio optimization. </center>


To solve this problem can be based on the maximum clique problem, where this is represented in a graph is the largest subset of vertices that are completely connected. That is, each vertex is adjacent to all other vertices in the clique.  The natural complement to this problem is MIS. 





## What is Oracle Of Assets?


The oracle of assets is a tool for investors that identifies a subgroup of assets that minimize the risk to lose money. Using neutral atoms, we can identify such a subgroup using an algorithm known as Maximum Independent Set (MIS). The subgroup of assets will not share a correlation between them, therefore if the price in the market of one of the assets decreases it won't affect the price of the others. Our algorithm will ensure that the subgroup will have the greater variety of assets possible for an investor to invest in.


![Assets](images/assets.png)
<center>Figure 3. Eight stock prices. </center>


## Business

Any system that has multiple processes that are altered in the evolution of time, through certain factors that we cannot control, as is the case of the complex environment in which technology, media and telecommunications companies or investors who want to value their assets considering the risks and current situations of the companies of their interest. Where they are trying to drive growth by optimizing their asset portfolios. It consists of two phases, the quantitative finance problems, which is the prediction, and the decision-based optimization of these predictions. Therefore, covariance forecasting models are important, they are optimized with unique objectives and constraints based on the prediction. In the case of identifying the shares of a company, when investing it is important to consider the positions, the line of business and that some depend on another company for their relationships or that they are a block of a larger company, such as the shares of their CEOs. 


![Example of a Graph](images/cor.png)
<center>Figure 5. Example of covariance in a Conglomerate. </center>


Like the case Multiverse & BBVA mentioned in their news, we need to find a way that we can tell investors where to put their money. Where the best sequence of buying and selling is most accurate with our proposal. But this will depend on time with multiple conditions where the objective is to increase profits and decrease losses, being a rational being is what we are looking for.



![MIS solution of a Graph](images/graph_sol.png)
<center>Figure 6. Example of a Graph for Portfolio optimization using MIS. </center>


#### 



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
