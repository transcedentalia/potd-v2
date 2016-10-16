from collections import deque

__author__ = 'alina'


def print_bfs(graph_dict, start_node):
    queue = deque()
    queue.append(start_node)

    visited = [0] * (len(graph_dict) + 1)
    visited[start_node] = 1
    while queue:
        node = queue.popleft()
        print(node)
        for neigh in graph_dict[node]:
            if visited[neigh] == 0:
                queue.append(neigh)
                visited[neigh] = 1

def print_dfs(graph_dict, start_node, visited):
    current_neighbours = graph_dict[start_node]

    visited[start_node] = 1
    print(start_node, end=" ")
    for neigh in current_neighbours:
        if not visited[neigh]:
            print_dfs(graph_dict, neigh, visited)

def topological_sort_kahn(graph_dict):
    top_sort = []

    num_in_edges_per_node = [0] * (len(graph_dict) + 1)
    for node, neighbours in graph_dict.items():
        for neigh in neighbours:
            num_in_edges_per_node[neigh] += 1

    nodes_without_in_edges = []
    for i, num in enumerate(num_in_edges_per_node):
        if num == 0:
            nodes_without_in_edges.append(i)

    while nodes_without_in_edges:
        node = nodes_without_in_edges.pop()
        top_sort.append(node)

        for neigh in graph_dict[node]:
            num_in_edges_per_node[neigh] -= 1
            if num_in_edges_per_node[neigh]  == 0:
                nodes_without_in_edges.append(neigh)

    for num in num_in_edges_per_node:
        if num != 0:
            print("Graph has cycles!")
            return

    return top_sort

if __name__ == '__main__':
