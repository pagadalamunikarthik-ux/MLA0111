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
    'A': [('D', 4)],
    'D': [('H', 2), ('I', 1)],
    'H': [('M', 3)],
    'I': [],
    'M': []
}

ucs(graph, 'A', 'M')
