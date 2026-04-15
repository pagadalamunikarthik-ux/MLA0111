import heapq

def astar():
    graph = {
        'S': [('A', 3), ('D', 4)],
        'A': [('B', 4)],
        'B': [('C', 4), ('E', 5)],
        'C': [],
        'D': [('E', 2)],
        'E': [('F', 4)],
        'F': [('G', 9.5)],
        'G': []
    }

    h = {
        'S': 11.5, 'A': 10.1, 'B': 5.8, 'C': 3.4,
        'D': 9.2, 'E': 7.1, 'F': 3.5, 'G': 0
    }

    pq = [(0, 'S')]
    g = {'S': 0}

    while pq:
        f, node = heapq.heappop(pq)

        if node == 'G':
            print("Cost:", g[node])
            return

        for n, cost in graph[node]:
            new_g = g[node] + cost
            if n not in g or new_g < g[n]:
                g[n] = new_g
                heapq.heappush(pq, (new_g + h[n], n))

astar()
