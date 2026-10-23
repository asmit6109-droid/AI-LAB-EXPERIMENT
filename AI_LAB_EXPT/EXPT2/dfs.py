graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

def dfs(node, visited):
    visited.add(node)
    print(node, end=" ")

    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(neighbor, visited)

start = input("Enter starting node (A-F): ").upper()

if start not in graph:
    print("Invalid starting node")
else:
    print("DFS Traversal:", end=" ")
    dfs(start, set())
    print()