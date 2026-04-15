def dfs(graph, node, visited):
    if node not in visited:
        print(node, end=" ")
        visited.add(node)

        for neighbor in graph[node]:
            dfs(graph, neighbor, visited)

graph = {
    '1': ['2', '7'],
    '2': ['3', '6'],
    '3': ['4', '5'],
    '4': [],
    '5': [],
    '6': [],
    '7': ['8', '10'],
    '8': ['9'],
    '9': [],
    '10': []
}

visited = set()

dfs(graph, '1', visited)
