from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])

    visited.add(start)

    while queue:
        node = queue.popleft()
        print(node, end=" ")

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

graph = {
    '1': ['2', '7'],
    '2': ['3', '6'],
    '3': ['4', '5'],
    '4': [],
    '5': [],
    '6': [],
    '7': ['8', '9'],
    '8': ['9'],
    '9': [],
    '10': []
}

bfs(graph, '1')
