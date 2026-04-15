def dfs(graph, node, visited):
    if node not in visited:
        print(node, end=" ")
        visited.add(node)

        for neighbor in graph[node]:
            dfs(graph, neighbor, visited)

graph = {
    '1': ['2', '3'],
    '2': ['5', '6'],
    '5': [],
    '6': [],
    '3': ['7', '4'],
    '7': ['8'],
    '4': ['8'],
    '8': []
}

visited = set()

dfs(graph, '1', visited)
