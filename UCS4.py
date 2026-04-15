import heapq

def ucs(graph, start, goal):
    visited = set()
    pq = [(0, start)]

    while pq:
        cost, node = heapq.heappop(pq)

        if node == goal:
            print("Cost:", cost)
            return

        if node in visited:
            continue
        visited.add(node)

        for neighbor, weight in graph[node]:
            if neighbor not in visited:
                heapq.heappush(pq, (cost + weight, neighbor))

graph = {
    'S': [('A', 3), ('B', 3), ('C', 7)],
    'A': [('D', 3), ('E', 8), ('G', 15)],
    'B': [('G', 20)],
    'C': [('G', 6)],
    'D': [],
    'E': [],
    'G': []
}

ucs(graph, 'S', 'G')
