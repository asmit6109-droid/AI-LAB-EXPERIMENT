from itertools import permutations

cities = ['A', 'B', 'C', 'D']

distance = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

start = 0
best_cost = float('inf')
best_path = None

for order in permutations(range(1, len(cities))):
    path = (start,) + order + (start,)

    cost = sum(
        distance[path[i]][path[i + 1]]
        for i in range(len(path) - 1)
    )

    if cost < best_cost:
        best_cost = cost
        best_path = path

print("Travelling Salesman Problem")
print("Optimal tour:", " -> ".join(
    cities[i] for i in best_path
))
print("Minimum travel cost:", best_cost)