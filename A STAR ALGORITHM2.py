import heapq

def astar2():
    graph = {
        'A': [('B', 1), ('C', 4)],
        'B': [('D', 3), ('C', 2)],
        'C': [('E', 5)],
        'D': [('F', 2)],
        'E': [('G', 3)],
        'F': [('G', 1)],
        'G': []
    }

    h = {
        'A': 6, 'B': 6, 'C': 4,
        'D': 3, 'E': 3, 'F': 1, 'G': 0
    }

    pq = [(0, 'A')]
    g = {'A': 0}

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

astar2()
