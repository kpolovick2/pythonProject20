import timeit

# ------------- Timing with constraint C optimization --------------
# the concise implementation (which I will now refer to as optimized)
# 92.455% of the time of the naive implementation
# (8.16% speedup)
# over 100000 executions with 10 data items, 4 clusters, and 14 tags (4x14.txt)
#           94.825% in the second test
#           (5.46% speedup)
# 49.802% of the time over 5000 executions with 20 data items, 9 clusters, and 28 tags (9x28.txt)
#           (100.8% speedup)
# 10.795% of the time over 1000 executions with 38 data items, 16 clusters, and 56 tags (16x56.txt)
#           (826.3% speedup)
# negligible speedup for large values of n or N with small values of K
# 17735.92% speedup for 39_clusters.txt on a singular execution

filename = "test_txt_files/100n_7K_100N_15a_1b.txt"
test_count = 100

generalized_time = timeit.timeit(f'a.ILP(\"{filename}\")', setup="import ILP_gurobi_generalized as a", number=test_count)
concise_time = timeit.timeit(f'b.ILP_concise(\"{filename}\")',  setup="import ILP_gurobi_generalized_concise as b", number=test_count)
g_linearized_time = timeit.timeit(f'c.ILP_linear_g(\"{filename}\")', setup="import ILP_linear_g_optimized as c", number=test_count)
linearized_time = timeit.timeit(f'd.ILP_linear(\"{filename}\")', setup="import ILP_linear as d", number=test_count)

print(f"Generalized: {generalized_time} seconds")

print(f"Concise: {concise_time} seconds")
print(f"{generalized_time/concise_time} speedup factor")

print(f"Gurobi Linearized: {g_linearized_time} seconds")
print(f"{generalized_time/g_linearized_time} speedup factor")

print(f"Linearized: {linearized_time} seconds")
print(f"{generalized_time/linearized_time} speedup factor")