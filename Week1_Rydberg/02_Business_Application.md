![CDL 2022 Cohort Project](../CDL_logo.jpg)
# Quantum Cohort Project Business Application I

Contributed by Arunanghu Debnath on behanlf of the working subgroup.


## Step 1a: Motivation

Here we analyze another domain of application that is expected to
benefit immensely from the incorporation of MIS (maximum independent
set) based and related strategies. We focus on developing the operations
research-based decision-making framework which can leverage the
strengths of MIS and related optimization problems. In particular, we
focus on the acceleration of transport logistics in competitive,
underregulated markets. Such markets are usually less amenable to
quantitative modeling due to the overdetermined nature of the governing
equations. However, they often have a higher number of predictable
constraints owing to the fact that an evolving framework of regulations
conforms to the established robust, working ones.  


## Step 1b: Introduction

Logistics management is an undeniably essential component of the B2B and
B2C distribution processes in the manufacturing and retail sectors. The
long-term implications for strategic investments in this area with an
aim to build up optimization strategies of logistics management may
mitigate a wide range of concerns for the company. For example, the
improvement of accuracy of delivery, and increase in transparency of
transactions - all of which contribute to the robust functioning of the
company and streamline the pivoting capabilities in the face of
unexpected constraints.  
The recent macroeconomic drivers e.g., regulated globalization and
geopolitically motivated recalibration of the supply chain in the
manufacturing sector have shown early signs which reiterate the need for
such requirements. As the established companies try to find a way to
compete with the new disruptors in the sector, a common route is to
gradually veer away from the services to a platform-building business.
The latter reduces the need for logistics outsourcing but signals a
pressing need for investing in data-driven, technology solutions.
Furthermore, it is notable that the current shift in consumer demand is
dominantly governed by rapid urbanization, internet penetration, steady
increase in spending power linked to a higher tendency to consumption.
While the above-mentioned reasons and their consequences were predicted,
the involuntary migrations related to climate alterations, voluntary
economic migrations, and workforce realignments driven by global
political and strategic changes are yet to manifest themselves. It
points towards a demand for developing novel forecasting strategies.  
Together, they are expected to have a significant impact on the
optimized logistical models that are currently in use. Within this
broader context, we propose the construction of a minimal model and
describe a hybrid workflow that can leverage the power of quantum
information processing at the back-end.  


## Step 2: Proposed workflow

Given the Cohort project which involves the preparation of specific
states in Rydberg atomic aggregates via manipulation of inter-site
interactions, and externally induced detunings, we focus on a simple
extension that involves state-to-state amplitude transfer.  
We identify the logistical ports of interest as the nodes of a weighted
graph. The assignment of these weights (referred to as intrinsic
weights) can be obtained from the values representing rates of transport
in-flow and out-flow. This simple exercise completes the mapping of the
logistical transport problem to a weighted graph.  
Subsequently, we define a control objective as sum of weights (assigned
to edges of the constructed graph) which are further multiplied by
extrinsic weights
*J*<sub>1</sub> = ∑<sub>*i*, *j*</sub>∑<sub>*k*</sub>*w*<sub>*i**j*</sub><sup>(*k*)</sup>*t*<sub>*i**j*</sub><sup>(*k*)</sup>.
We note that the control objective is a generalizable one. We may also
define the objective as a quantity that describes deviation from a
predefined objective as,
*J*<sub>2</sub> = (*J*<sub>1</sub>−*J*<sub>goal</sub>)<sup>2</sup>.
Thereafter, the state-to-state amplitude transfer problem can be
reformulated as finding a set of weights which minimizes the above
mentioned control objective via a reformulation of optimal control
algorithms. We seek the MIS problem to be implemented in a quantum
variational hardware and offer us the identification of the independent
sets of nodes. The resultant independent sets are assigned to matrix
elements which are then utilized in a classical finite-time optimal
control problem using Hamilton-Jacobi-Bellman formulation i.e.
∂*J*<sub>*m*</sub>({**r**(*t*)},*t*)/*d**t* = max<sub>*u*</sub>*H*(*u*).
Here *H*(*u*) is may be specified as, $\\begin{pmatrix}
\\partial J\_{m}(r_1, t)/dt & \\partial J\_{m}(r_2, t)/dt & \\cdots\\\\
\\end{pmatrix}^T \\times \\begin{pmatrix}
-k_1 & t\_{12} & \\cdots\\\\
t\_{21} & -k_2 & \\cdots \\\\
\\vdots &  \\vdots    & \\ddots
\\end{pmatrix} \\times \\begin{pmatrix}
r_1 & r_2 & \\cdots\\\\
\\end{pmatrix}$. Here we look for the maximum attainable
*r*<sub>val</sub>(*T*) for all initialized ({**r**}) for a finite time
*T*. The maximum or the optimal return function is denoted as
*J*<sub>*m*</sub>({**r**},*t*). Such a description incorporates the
problem of finding MIS integrated within a broader logistics control
problem. It is important to note that such a hybrid framework is
particularly advantageous because of its ability to include several
dissipative terms within the classical control part of the framework.
The latter can be used to model adversities of different nature.  

## Step 3: Remarks

Although the present description presents a minimal workflow for the
formulation of the problem, this has larger applicability. The solutions
remain adaptable to include industry-specific and consumer
sentiment-driven control objectives. We note that a particular use case
of minimal-time delivery of essential consumer requirements by FedEx
Corporation could be an ideal test ground for such analysis. Given the
competition it faces from the recent decision by companies such as
Amazon to enter this space, they will be an ideal customer for testing
and implementing such a solution framework.  
Additionally, for a company, it may offer better adaptation to GDP
fluctuations and evolving trade agreements and multilateral treaties. If
multiple locally optimized outcomes are identified apriori and the local
dissipative causes are incorporated, it can help the company cope with
the amplified consequences of relatively smaller fluctuations of
constraints.  


## References

-   https://www.bcg.com/publications/2021/building-resilience-strategies-to-improve-supply-chain-resilience

-   https://www.accenture.com/us-en/services/supply-chain-operations/resilient-supply-chain

-   https://www.mckinsey.com/business-functions/strategy-and-corporate-finance/our-insights/lessons-from-growth-outperformers-in-logistics

-   https://www.bcg.com/capabilities/operations/digital-supply-chain

-   https://www.mckinsey.com/industries/travel-logistics-and-infrastructure/our-insights/startup-funding-in-logistics-focused-investment-in-a-growing-industry



# Quantum Cohort Business application project II

Contributed by Sultana Hadi on behalf of the working subgroup


## Step 1 & 2: Motivation and problem formulation 

For industrial application, one can also look at Protein-folding.
Protein is a sequence of amino-acid. In the protein folding problem, one
is given a sequence on 1D, unfolded protein, based on its interactions
with each other and outside, one has to find how it becomes functions
and folds to a 3D shape. Protein folding is crucial for designing new
therapeutics. In general, protein folding is NP-hard. Quantum promises
to provide speedup for an optimization problem. Protein folding is an
optimization problem, and we expect that quantum computers can speed up
the process. There has been ongoing work to experimentally show speed
for useful application of quantum speed up for the optimization is one
of them. There has been some work on designing Quantum algorithms for
protein folding problems, that has indicated speed up on quantum
computers. We can write the problem Hamiltonian
\[\[1\]\[2\]\[3\]\](https://arxiv.org/abs/1811.00713,https://www.nature.com/articles/srep00571.pdf,https://arxiv.org/pdf/2205.06084.pdf)
as
*H*<sub>*I*</sub> = *H*<sub>pair</sub> + *H*<sub>penalty</sub>
where *H*<sub>pair</sub> encodes the interaction between different
acids, valid interaction, and *H*<sub>penalty</sub> penalizes the
unwanted amino-acid fold, and the the full Hamiltonian is the sum of a
non-interacting and the interacting part
*H* = *H*<sub>free</sub> + *H*<sub>pair</sub> + *H*<sub>penalty</sub>.
The ground state of *H* gives us the string with valid protein folds. To
solve this problem with Rydberg-Hamiltonian, we have to map it that
Hamiltonian. The Rydberg-Hamiltonian is
$$H= \\frac{\\Omega}{2}\\sum\_{i\\in V}\\sigma_i^x-\\delta\\sum\_{i\\in V}n_i+\\sum\_{i\>j}V\_{ij}n_in_j.$$
We map
*H*<sub>free</sub> →  − *δ*∑<sub>*i* ∈ *V*</sub>*n*<sub>*i*</sub>,
*H*<sub>pair</sub> + *H*<sub>penalty</sub> → ∑<sub>*i* \> *j*</sub>*V*<sub>*i**j*</sub>*n*<sub>*i*</sub>*n*<sub>*j*</sub>.
The problem is to start in the ground-state of
∑<sub>*i* ∈ *V*</sub>*σ*<sub>*i*</sub><sup>*x*</sup>,
\|*ψ*<sub>0</sub>⟩
, and then addibaitcally go the ground sate of the full Hamiltonain
$$\|\\psi_g\\rangle= e^{-i\\int\_{t_0}^{t_f}\\left(\\frac{\\Omega}{2}f(t)\\sum\_{i\\in V}\\sigma_i^x-g(t)(\\delta\\sum\_{i\\in V}n_i+\\sum\_{i\>j}V\_{ij}n_in_j)\\right)dt}\|\\psi_0\\rangle.$$
The function f(t) and g(t), for the adibatic protocoal, is define such
that at *t*<sub>*i*</sub> the state \|*ψ*<sub>0</sub>⟩, and at time
*t*<sub>*f*</sub>, one gets \|*ψ*<sub>*g*</sub>⟩. Note
$e^{-i\\int\_{t_0}^{t_f}\\left(\\frac{\\Omega}{2}f(t)\\sum\_{i\\in V}\\sigma_i^x-g(t)(\\delta\\sum\_{i\\in V}n_i+\\sum\_{i\>j}V\_{ij}n_in_j)\\right)dt}$
can be discretized. The state \|*ψ*<sub>*g*</sub>⟩ is populated with
different protein folds and the one with high probability is considered
the stable folds. It is multi-objective optimization and solves for a
solution space in a multivariate setup. We can also encode molecular
docking as an optimization in the Ryberg-Hamiltonian.
