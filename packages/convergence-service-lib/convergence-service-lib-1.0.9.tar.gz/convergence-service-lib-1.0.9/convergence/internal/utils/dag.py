from typing import List


class DirectedAcyclicGraph:
    def __init__(self, steps: List):
        self.node_count = len(steps)
        self.adj_matrix = self.create_adj_matrix()
        self.nodes = steps

        name_to_node_map = {n.name: n for n in steps}
        for node in steps:
            dependencies = node.get_dependencies()
            for dep in dependencies:
                self.add_edge(steps.index(name_to_node_map[dep]), steps.index(node))

    def create_adj_matrix(self):
        result = [None] * self.node_count

        for i in range(self.node_count):
            result[i] = [False] * self.node_count

        return result

    def topological_sort(self):
        stack = []
        visited = [False] * len(self.nodes)

        for i in range(self.node_count):
            if not visited[i]:
                self.topological_sort_utils(i, visited, stack)

        result = []
        for i in stack:
            result.append(self.nodes[i])

        return result

    def add_edge(self, node, dependent_node):
        self.adj_matrix[dependent_node][node] = True

    def topological_sort_utils(self, v, visited, stack):
        visited[v] = True

        for index in range(self.node_count):
            if self.adj_matrix[v][index]:
                if not visited[index]:
                    self.topological_sort_utils(index, visited, stack)

        stack.append(v)
