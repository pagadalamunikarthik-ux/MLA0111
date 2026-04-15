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
    'A': [('B', 9), ('C', 4)],
    'B': [('D', 7), ('C', 2), ('E', 3)],
    'C': [('D', 1), ('E', 6)],
    'D': [('E', 4), ('F', 8)],
    'E': [('F', 2)],
    'F': []
}

ucs(graph, 'A', 'F')
