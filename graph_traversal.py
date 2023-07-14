# Implement a graph traversal algorithm, such as depth-first search (DFS) or breadth-first search (BFS).
from collections import defaultdict


def bfs(graph, start_node):
    visited = set()
    queue = [start_node]  # Using a list as a queue

    while queue:
        node = queue.pop(0)
        if node not in visited:
            print(f"Visiting node: {node}")
            visited.add(node)

            # Add unvisited neighboring nodes to the queue
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)
                    print(f"Adding neighbor {neighbor} to the queue")


def dfs(graph, start_node):
    visited = set()
    stack = [start_node]  # Using a list as a stack

    while stack:
        node = stack.pop()
        if node not in visited:
            print(f"Visiting node: {node}")
            visited.add(node)

            # Add unvisited neighboring nodes to the stack
            for neighbor in graph[node]:
                if neighbor not in visited:
                    stack.append(neighbor)
                    print(f"Adding neighbor {neighbor} to the stack")


# Test Case
graph = defaultdict(list)
graph['A'] = ['B', 'C']
graph['B'] = ['D', 'E']
graph['C'] = ['F']
graph['D'] = []
graph['E'] = []
graph['F'] = ['G']
graph['G'] = []

print("Running BFS:")
bfs(graph, 'A')
print()

print("Running DFS:")
dfs(graph, 'A')
