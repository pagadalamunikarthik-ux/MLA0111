import heapq

def gbfs(graph, h, start, goal):
    visited = set()
    pq = [(h[start], start)]  # (heuristic, node)

    while pq:
        _, node = heapq.heappop(pq)

        if node == goal:
            print("Reached Goal:", node)
            return

        if node in visited:
            continue
        visited.add(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                heapq.heappush(pq, (h[neighbor], neighbor))

graph = {
    'A': ['D', 'C', 'B'],
    'D': ['F'],
    'C': ['F', 'E'],
    'B': ['E'],
    'F': ['G'],
    'E': ['H'],
    'H': ['G'],
    'G': []
}

h = {
    'A': 40,
    'B': 32,
    'C': 25,
    'D': 35,
    'E': 19,
    'F': 17,
    'H': 10,
    'G': 0
}

gbfs(graph, h, 'A', 'G')
