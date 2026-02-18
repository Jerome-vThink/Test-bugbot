"""Unit tests for langgraph_demo.src.nodes."""

from unittest.mock import MagicMock, patch

from langgraph_demo.src.nodes import input_node, output_node, process_node


def test_input_node_empty() -> None:
    """Empty or whitespace input must set intent to 'empty'."""
    assert input_node({"user_input": ""}) == {"user_input": "", "intent": "empty"}
    assert input_node({"user_input": "   "}) == {"user_input": "", "intent": "empty"}
    assert input_node({}) == {"user_input": "", "intent": "empty"}


def test_input_node_question() -> None:
    """Input containing '?' is classified as question."""
    result = input_node({"user_input": "What is 2+2?"})
    assert result["intent"] == "question"
    assert result["user_input"] == "What is 2+2?"


def test_input_node_summarize() -> None:
    """Short input (<=100 chars, no '?') is summarize."""
    short = "Python is a language."
    result = input_node({"user_input": short})
    assert result["intent"] == "summarize"
    assert result["user_input"] == short


def test_input_node_process() -> None:
    """Long input (>100 chars, no '?') is process."""
    long_input = "x" * 101
    result = input_node({"user_input": long_input})
    assert result["intent"] == "process"
    assert result["user_input"] == long_input


def test_output_node_empty_intent() -> None:
    """Empty intent produces 'Please provide some input.'."""
    result = output_node({"intent": "empty"})
    assert result["output"] == "Please provide some input."


@patch("langgraph_demo.src.nodes.ChatOpenAI")
def test_process_node_empty_intent(mock_chat: MagicMock) -> None:
    """Empty intent returns without calling LLM."""
    result = process_node({"intent": "empty", "user_input": ""})
    assert result["processed"] == "(No input provided.)"
    mock_chat.return_value.invoke.assert_not_called()
