from collections import deque

def water_jug_bfs(cap1, cap2, goal):
    visited = set()
    queue = deque([(0, 0)])

    while queue:
        x, y = queue.popleft()

        if x == goal or y == goal:
            print("Goal reached:", (x, y))
            return

        if (x, y) in visited:
            continue
        visited.add((x, y))

        next_states = [
            (cap1, y),
            (x, cap2),
            (0, y),
            (x, 0),
            (x - min(x, cap2 - y), y + min(x, cap2 - y)),
            (x + min(y, cap1 - x), y - min(y, cap1 - x))
        ]

        for state in next_states:
            if state not in visited:
                queue.append(state)

    print("No solution found")

water_jug_bfs(5, 3, 4)
