"""
visited = set()
def dfs(node):
    visited.add(node)
    print(node)
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(neighbor)
dfs("A")
"""
graph = {
    "a": ["b", "c", "d"],
    "b": ["g", "h"],
    "c": ["e", "f"],
    "d": ["i"],
    "f": ["m"],
    "g": ["j", "k"],
    "h": ["l"],
    "l": ["n"]
}
visited = set()
def dfs(node):
    visited.add(node)
    print(node)
    if node not in graph:
        return
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(neighbor)

dfs("a")
