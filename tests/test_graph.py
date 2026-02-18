"""Unit tests for langgraph_demo.src.graph."""

from langgraph_demo.src.graph import build_graph, route_after_input


def test_route_after_input_empty_goes_to_output() -> None:
    """When intent is 'empty', route to 'output' (skip LLM)."""
    assert route_after_input({"intent": "empty"}) == "output"


def test_route_after_input_non_empty_goes_to_process() -> None:
    """When intent is not empty, route to 'process'."""
    assert route_after_input({"intent": "question"}) == "process"


def test_graph_invoke_empty_input_returns_message() -> None:
    """Empty input must return 'Please provide some input.' without calling LLM."""
    graph = build_graph()
    result = graph.invoke({"user_input": ""})
    assert result.get("intent") == "empty"
    assert "Please provide some input." in result.get("output", "")
