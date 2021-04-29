from typing import Dict, List

class Node:
    def __init__(self, val):
        self.val = val

    def __repr__(self):
        return str(self.val)

def get_length_of_shortest_path(graph: Dict[Node, List[Node]], A: Node, B: Node) -> int:
    queue = [(A, 0)]
    visited = {}
    paths = {}
    cur_level = 0
    while queue:
        node, cur_level = queue.pop(0)
        visited[node] = True
        if node == B:
            return cur_level
        for move in graph[node]:
            if move in visited:
                continue
            queue.append((move, cur_level+1))
    return None

if __name__ == "__main__":
    n = int(input())
    nodes = { i:  Node(i) for i in range(n) }
    graph = { nodes[i]: [] for i in range(n) }
    for i in range(n):
        graph[nodes[i]] = [nodes[int(j)] for j in input().split()]
    A = nodes[int(input())]
    B = nodes[int(input())]
    print('Shortest path from A to B are', get_length_of_shortest_path(graph, A, B), 'steps')
