using Graphs
using Bloqade
using Random
using GenericTensorNetworks
using Optim
using PythonCall

function MIS_adiabatic(n)
    Random.seed!(2)
    atoms = generate_sites(SquareLattice(), n, n; scale = 4.5) |> random_dropout(0.2)
    graph = BloqadeMIS.unit_disk_graph(atoms, 7.5)
    T_max = 0.6
    Ω_max = 2π * 4
    Ω = piecewise_linear(clocks = [0.0, 0.1, 0.5, T_max], values = [0.0, Ω_max, Ω_max, 0])
    Δ_start = -2π * 13
    Δ_end = 2π * 11
    Δ = piecewise_linear(clocks = [0.0, 0.1, 0.5, T_max], values = [Δ_start, Δ_start, Δ_end, Δ_end])
    hamiltonian = rydberg_h(atoms; Ω = Ω, Δ = Δ)
    prob = SchrodingerProblem(zero_state(nqubits(hamiltonian)), T_max, hamiltonian)
    emulate!(prob)
    best_bit_strings = most_probable(prob.reg, 2)
    all_optimal_configs = GenericTensorNetworks.solve(IndependentSet(graph), ConfigsMax())[]
    @assert all(bs -> GenericTensorNetworks.StaticBitVector([bs...]) ∈ all_optimal_configs.c, best_bit_strings)
    best5_bit_strings = most_probable(prob.reg, 3)
    fixed = mis_postprocessing(best5_bit_strings[3], graph)
    success = BloqadeMIS.is_independent_set(fixed, graph)
    return fixed, success
end
# Print the answer to the MIS problem and check it is valid
fixed, success = MIS_adiabatic(4)
print(fixed)
print(" ")
print(success)