import pytest

from pijp.utils.colors import ColorCycle


def test_singleton_instance():
    instance1 = ColorCycle()
    instance2 = ColorCycle()

    assert instance1 is instance2, "ColorCycle should be a singleton"


def test_next_color():
    cycle = ColorCycle()

    assert cycle.next_color() == "red", "First color should be red"
    assert cycle.next_color() == "green", "Second color should be green"
    assert cycle.next_color() == "blue", "Third color should be blue"


def test_color_wrap_around():
    cycle = ColorCycle()

    current_color = cycle.current_color()
    for _ in range(len(cycle.colors)):
        cycle.next_color()

    assert cycle.next_color() == current_color, "Should wrap around"


def test_index_reset():
    cycle = ColorCycle()
    cycle.reset()

    assert cycle.next_color() == "red", "Index should reset and return the first color"


def test_empty_color_list():
    cycle = ColorCycle()
    cycle.colors = []

    with pytest.raises(IndexError, match="list index out of range"):
        cycle.next_color()
