scores = {
    'A': 1,
    'B': 3,
    'C': 2,
    'D': 5,
    'E': 4
}

neighbors = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['A'],
    'D': ['B'],
    'E': ['B']
}

current = input("Enter starting state (A-E): ").upper()

if current not in scores:
    print("Invalid state")
else:
    print("Initial state:", current)

    while True:
        better = [
            n for n in neighbors[current]
            if scores[n] > scores[current]
        ]

        if not better:
            break

        current = max(better, key=lambda n: scores[n])
        print("Moving to:", current)

    print("Final state:", current)
    print("Maximum score:", scores[current])