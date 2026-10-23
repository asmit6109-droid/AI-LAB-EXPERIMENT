import heapq

graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'D': 2, 'E': 5},
    'C': {'E': 1},
    'D': {'G': 5},
    'E': {'G': 3},
    'G': {}
}

heuristic = {
    'A': 7, 'B': 6, 'C': 4,
    'D': 4, 'E': 2, 'G': 0
}

def a_star(start, goal):
    queue = [(heuristic[start], 0, start, [start])]
    best_cost = {start: 0}

    while queue:
        f, cost, node, path = heapq.heappop(queue)

        if cost != best_cost.get(node):
            continue

        if node == goal:
            return path, cost

        for neighbor, weight in graph[node].items():
            new_cost = cost + weight

            if new_cost < best_cost.get(neighbor, float('inf')):
                best_cost[neighbor] = new_cost
                priority = new_cost + heuristic[neighbor]
                heapq.heappush(
                    queue,
                    (priority, new_cost, neighbor,
                     path + [neighbor])
                )

    return None, None

start = input("Enter start node: ").upper()
goal = input("Enter goal node: ").upper()

if start not in graph or goal not in graph:
    print("Invalid node")
else:
    path, cost = a_star(start, goal)

    if path:
        print("Optimal path:", " -> ".join(path))
        print("Total cost:", cost)
    else:
        print("No path found")