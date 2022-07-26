using Graphs
using Bloqade
using Random
using GenericTensorNetworks
using Optim
using PythonCall

function MIS_adiabatic(graph)
    T_max = 0.6
    Ω_max = 2π * 4
    Ω = piecewise_linear(clocks = [0.0, 0.1, 0.5, T_max], values = [0.0, Ω_max, Ω_max, 0])
    Δ_start = -2π * 13
    Δ_end = 2π * 11
    Δ = piecewise_linear(clocks = [0.0, 0.1, 0.5, T_max], values = [Δ_start, Δ_start, Δ_end, Δ_end])
    hamiltonian = rydberg_h(atoms; Ω = Ω, Δ = Δ)
    prob = SchrodingerProblem(zero_state(nqubits(hamiltonian)), T_max, hamiltonian)
    emulate!(prob)
    best_bit_string = most_probable(prob.reg, 1)[1]
    success = BloqadeMIS.is_independent_set(best_bit_string, graph)
    return best_bit_string, success
end

function MIS_tensor_network(graph)
    mis_solution = GenericTensorNetworks.solve(IndependentSet(graph), SingleConfigMax())[]
    bitstring = mis_solution.c.data
    return bitstring
end

# Following the Bloqade tutorial script, solve the  diagonal-connected unit-disk 
# grid graphs (DUGG) problems using the adiabatic approach.
# How large of an array can Bloqade solve?

n = 4
Random.seed!(2)
atoms = generate_sites(SquareLattice(), n, n; scale = 4.5) |> random_dropout(0.2)
graph = BloqadeMIS.unit_disk_graph(atoms, 7.5)

# Print the answer to the MIS problem and check it is valid

answer, success = MIS_adiabatic(graph)
print(answer)
print(" ")
print(success)

#=
From testing with the size of the graph, the largest graph that we managed to run is
a 5x5 square lattice, with 35% random dropout, resulting in a graph with 16 nodes.
With 20% dropout, the largest square is 4x4
=#

#Attempt to solve for larger square DUGGs using your tensor network approach.

n = 18
Random.seed!(2)
atoms = generate_sites(SquareLattice(), n, n; scale = 4.5) |> random_dropout(0.2)
graph = BloqadeMIS.unit_disk_graph(atoms, 7.5)

answer = MIS_tensor_network(graph)
print(answer)

#=
The tensor network can solve significantly higher graphs, up to 18x18 with 20% dropout
=#