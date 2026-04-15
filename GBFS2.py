import heapq

def gbfs(graph, h, start, goal):
    visited = set()
    pq = [(h[start], start)]

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
    'P': ['R', 'C', 'A'],
    'R': ['E'],
    'C': ['R', 'G', 'M'],
    'A': ['M'],
    'M': ['U', 'G'],
    'U': ['N'],
    'N': ['S'],
    'E': ['G', 'S'],
    'G': ['S', 'N'],
    'S': []
}

h = {
    'P': 10,
    'R': 8,
    'C': 6,
    'A': 11,
    'M': 9,
    'U': 9,
    'N': 6,
    'E': 3,
    'G': 4,
    'S': 0
}

gbfs(graph, h, 'P', 'S')
