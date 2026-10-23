from collections import deque

def water_jug(capacity_a, capacity_b, target):
    start = (0, 0)
    queue = deque([(start, [start])])
    visited = {start}

    while queue:
        (a, b), path = queue.popleft()

        if a == target or b == target:
            return path

        next_states = [
            (capacity_a, b),
            (a, capacity_b),
            (0, b),
            (a, 0),
            (a - min(a, capacity_b - b),
             b + min(a, capacity_b - b)),
            (a + min(b, capacity_a - a),
             b - min(b, capacity_a - a))
        ]

        for state in next_states:
            if state not in visited:
                visited.add(state)
                queue.append((state, path + [state]))

    return None

path = water_jug(4, 3, 2)

if path:
    print("Water Jug Solution:")
    for step, state in enumerate(path):
        print(f"Step {step}: Jug A = {state[0]}, Jug B = {state[1]}")
else:
    print("No solution found")