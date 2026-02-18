"""Graph state definitions for the LangGraph demo."""

from typing import TypedDict


class DemoState(TypedDict, total=False):
    """Shared state flowing through the graph.

    Attributes:
        user_input: Raw text from the user.
        intent: Classified intent used for routing (e.g. 'summarize', 'question').
        processed: LLM output or processed content.
        output: Final formatted response for the user.
    """

    user_input: str
    intent: str
    processed: str
    output: str
