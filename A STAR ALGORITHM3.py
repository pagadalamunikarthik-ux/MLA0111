import heapq

def astar(g, h, s, goal):
    pq = [(0, s)]
    cost = {s: 0}

    while pq:
        f, n = heapq.heappop(pq)

        if n == goal:
            print(cost[n])
            return

        for v, w in g[n]:
            new = cost[n] + w
            if v not in cost or new < cost[v]:
                cost[v] = new
                heapq.heappush(pq, (new + h[v], v))

g = {
    'S': [('A', 3), ('D', 2)],
    'A': [('B', 5)],
    'B': [('C', 2), ('D', 1), ('E', 1)],
    'C': [('G', 10)],
    'D': [('E', 4)],
    'E': [('G', 3)],
    'G': []
}

h = {'S': 7, 'A': 9, 'B': 4, 'C': 2, 'D': 5, 'E': 3, 'G': 0}

astar(g, h, 'S', 'G')
