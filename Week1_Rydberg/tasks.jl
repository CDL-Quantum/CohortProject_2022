using Bloqade
using PythonCall
using KrylovKit
using SparseArrays

plt = pyimport("matplotlib.pyplot");

# Task 1: Adiabatic state preparation with Bloqade

# generate the pulse/detuning sequence

total_time = 3.0;
Ω_max = 2π * 4;
Ω = piecewise_linear(clocks = [0.0, 0.1, 2.1, 2.2, total_time], values = [0.0, Ω_max, Ω_max, 0, 0]);

U1 = -2π * 10;
U2 = 2π * 10;
Δ = piecewise_linear(clocks = [0.0, 0.6, 2.1, total_time], values = [U1, U1, U2, U2]);

# specify the atomic position

nsites = 9
atoms = generate_sites(ChainLattice(), nsites, scale = 5.72)
h = rydberg_h(atoms; Δ, Ω)

# starting in the groundstate, simulate the time evolution of a quantum state under the Schrödinger equation.

reg = zero_state(9);
prob = SchrodingerProblem(reg, total_time, h);
integrator = init(prob, Vern8());

densities = []
for _ in TimeChoiceIterator(integrator, 0.0:1e-3:total_time)
    push!(densities, rydberg_density(reg))
end
D = hcat(densities...);

# plot the average occupation on each site as a function of time.

fig, ax = plt.subplots(figsize = (10, 4))
shw = ax.imshow(real(D), interpolation = "nearest", aspect = "auto", extent = [0, total_time, 0.5, nsites + 0.5])
ax.set_xlabel("time (μs)")
ax.set_ylabel("site")
ax.set_xticks(0:0.2:total_time)
ax.set_yticks(1:nsites)
bar = fig.colorbar(shw)
fig

# TUTORIAL CODE ENDS HERE, NEW CODE BELOW

# calculate the expectation value of <sigma^x_i>

#=
I think this means to:
1) Calculate the expectation value of sigma x for every i
2) Find the average value of those 9 results
=#

op = SumOfX(9, 1.0)
x_i = expect(op, reg) / 9
println(x_i)

# calculate the gap between the Rydberg Hamiltonian's groundstate and first excited state.

# retrieve the target hamiltonian at the end of the procuder
ht = h |> attime(total_time)
# convert the hamiltonian into a matrix
h_m = mat(ht)
# use an eigensolver to find the two lowest eigenvalues
vals, _, _ = KrylovKit.eigsolve(h_m, 2, :SR)
# calculate the gap from the difference of the eigenvalues
# Julia starts indexing from 1, not 0
gap = vals[2] - vals[1]
println(gap)

# What does the latter imply about the viability of the 
# adiabatic protocol for this type of quantum computer?
#=
The result was that the gap is around 55 Mhz * hbar. To be able to not accidentally
make that transition during the adiabatic evolution, the adiabatic protocol
must take at least as long as the inverse of the frequency of this gap, so to
successfully use this computer, the state preparation must take at least
1/55Mhz = 18 nanoseconds. The timescales used by this computer are on the order
of microseconds, so the performance of the computer is not limited by the size of
gap in this case.
=#

# Can you determine how it scales with increasing array size?
#=
We can wrap all of the previous code into a function that takes array size
as input and outputs the size of the gap
=#
function calculate_gap(nsites)
    atoms = generate_sites(ChainLattice(), nsites, scale = 5.72)
    h = rydberg_h(atoms; Δ, Ω)
    reg = zero_state(nsites);
    prob = SchrodingerProblem(reg, total_time, h);
    integrator = init(prob, Vern8());
    densities = []
    for _ in TimeChoiceIterator(integrator, 0.0:1e-3:total_time)
        push!(densities, rydberg_density(reg))
    end
    D = hcat(densities...);
    ht = h |> attime(total_time)
    h_m = mat(ht)
    vals, _, _ = KrylovKit.eigsolve(h_m, 2, :SR)
    gap = vals[2] - vals[1]
    return gap
end

for i in 1:3
    n = 5+i
    gap = calculate_gap(n)
    print(n)
    print(' ')
    println(gap)
end

#=
From inspecting the results for site numbers from 6 to 15, we can notice two patterns:
1) Even number of sites has a gap close to zero. This makes sense, because both alternating
configurations have equal energy in the even case.
2) As the number of sites is increased, the gap decreases, although less each time.
=#

# Task 2: Larger arrays with the Blockade Approximation

# What is the largest 1D array that you can simulate 
# for the full Rydberg Hamiltonian, with exact time evolution as above?

#=
If we want to extract the value of the gap, then the above function starts becoming
noticably slower at already 12 sites. On my laptop, it takes 28 seconds to execute
calculate_gap(15) and 70 seconds to execute calculate_gap(16)

If we don't care about the gap, but just want to retrieve the plot as the result
of the simulation, then we can call the following function
=#

function simulate_1D(nsites)
    atoms = generate_sites(ChainLattice(), nsites, scale = 5.72)
    h = rydberg_h(atoms; Δ, Ω)
    reg = zero_state(nsites);
    prob = SchrodingerProblem(reg, total_time, h);
    integrator = init(prob, Vern8());
    densities = []
    for _ in TimeChoiceIterator(integrator, 0.0:1e-3:total_time)
        push!(densities, rydberg_density(reg))
    end
    D = hcat(densities...);
    return D
end

#=
Executing the function simulate_1D takes equally long, beacuse evidently, the
computational bottleneck is the simulation, rather than the diagonalization.
=#

# What implications does this have for quantum advantage,
# particularly in light of the experiments mentioned above?

#=
Using this classical approach, the tasks seems to become quickly infeasible 
to simulate. In contrast, it does not seem infeasible to increase the number
of atoms in neutral atom quantum computers, so it is conceivable, that a
neutral atom quantum computer could outperform classical computers in this task.
From this simulation, it looks like tens of atoms are needed to outperform a laptop,
whereas probably a hundred or so could outperform a supercomputer (judging from the
way that the runtime increased with n_sites). The experimental work by Bernien et al.
suggests that employing hundreds of atoms in a quantum computer is possible in 
the near term.
=#