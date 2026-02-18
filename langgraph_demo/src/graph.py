"""Build and compile the LangGraph workflow with conditional routing."""

from langgraph.graph import END, START, StateGraph

from .nodes import input_node, output_node, process_node
from .state import DemoState


def route_after_input(state: DemoState) -> str:
    """Route from input_node: skip LLM for empty input, else go to process.

    Args:
        state: Current state with user_input and intent.

    Returns:
        Next node name: 'process' or 'output'.
    """
    if state.get("intent") == "empty":
        return "output"
    return "process"


def build_graph() -> StateGraph:
    """Build the demo graph: START → input → [process | output] → output → END.

    Returns:
        Compiled StateGraph ready for invocation.
    """
    graph_builder = StateGraph(DemoState)

    graph_builder.add_node("input", input_node)
    graph_builder.add_node("process", process_node)
    graph_builder.add_node("output", output_node)

    graph_builder.add_edge(START, "input")
    graph_builder.add_conditional_edges(
        "input",
        route_after_input,
        {"process": "process", "output": "output"},
    )
    graph_builder.add_edge("process", "output")
    graph_builder.add_edge("output", END)

    return graph_builder.compile()
