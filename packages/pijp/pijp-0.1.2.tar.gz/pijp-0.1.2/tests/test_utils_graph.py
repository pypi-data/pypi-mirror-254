import pytest

from pijp.utils.graph import Graph


def test_add_vertex():
    graph = Graph()
    graph.add_vertex("A")

    assert "A" in graph.adjacency_list
    assert graph.adjacency_list["A"] == set()


def test_adding_duplicate_vertex():
    graph = Graph()
    graph.add_vertex("A")
    graph.add_vertex("A")

    assert len(graph.adjacency_list) == 1


def test_add_edge():
    graph = Graph()
    graph.add_edge("A", "B")

    assert "A" in graph.adjacency_list
    assert "B" in graph.adjacency_list
    assert "B" in graph.adjacency_list["A"]


def test_adding_duplicate_edge():
    graph = Graph()
    graph.add_edge("A", "B")
    graph.add_edge("A", "B")

    assert len(graph.adjacency_list["A"]) == 1


def test_get_vertices():
    graph = Graph()
    graph.add_vertex("A")
    graph.add_vertex("B")

    assert set(graph.get_vertices()) == {"A", "B"}


def test_topological_sort():
    graph = Graph()
    graph.add_edge("A", "B")
    graph.add_edge("A", "C")

    assert graph.topological_sort() == [["B", "C"], ["A"]]


def test_topological_sort_empty_graph():
    graph = Graph()

    assert not graph.topological_sort()


def test_topological_sort_with_cycle():
    graph = Graph()
    graph.add_edge("A", "B")
    graph.add_edge("B", "A")

    with pytest.raises(ValueError, match="Graph has a cycle!"):
        graph.topological_sort()


def test_topological_sort_no_edges():
    graph = Graph()
    graph.add_vertex("A")
    graph.add_vertex("B")

    assert graph.topological_sort() == [["A", "B"]]


def test_graph_with_isolated_vertex():
    graph = Graph()
    graph.add_vertex("A")
    graph.add_edge("B", "C")

    assert set(graph.get_vertices()) == {"A", "B", "C"}
