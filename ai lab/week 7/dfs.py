# DFS implementation using recursion

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

visited = set()   # to keep track of visited nodes

def dfs(node):
    if node not in visited:
        print(node, end="")   # process the node
        visited.add(node)
        for neighbour in graph[node]:
            dfs(neighbour)

# Run DFS starting from A
print("DFS Traversal starting from A:")
dfs('A')
