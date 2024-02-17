class Graph:
    adjacency_list: dict[str, set[str]]

    def __init__(self) -> None:
        self.adjacency_list = {}

    def add_vertex(self, name: str) -> None:
        if name not in self.adjacency_list:
            self.adjacency_list[name] = set()

    def add_edge(self, from_vertex: str, to_vertex: str) -> None:
        self.add_vertex(from_vertex)
        self.add_vertex(to_vertex)
        self.adjacency_list[from_vertex].add(to_vertex)

    def get_vertices(self) -> list[str]:
        return list(self.adjacency_list.keys())

    def topological_sort(self) -> list[list[str]]:
        in_degree: dict[str, int] = {vertex: 0 for vertex in self.adjacency_list}
        for neighbors in self.adjacency_list.values():
            for neighbor in neighbors:
                in_degree[neighbor] += 1

        zero_in_degree = [vertex for vertex, degree in in_degree.items() if degree == 0]
        result: list[list[str]] = []

        while zero_in_degree:
            current_zero_in_degree = sorted(zero_in_degree)
            result.insert(0, current_zero_in_degree)

            next_zero_in_degree = []
            for vertex in current_zero_in_degree:
                del in_degree[vertex]
                for neighbor in self.adjacency_list[vertex]:
                    in_degree[neighbor] -= 1
                    if in_degree[neighbor] == 0:
                        next_zero_in_degree.append(neighbor)

            zero_in_degree = next_zero_in_degree

        if in_degree:
            raise ValueError("Graph has a cycle!")

        return result
