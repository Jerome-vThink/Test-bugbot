"""Graph nodes: input handling, LLM processing, and output formatting."""

from langchain_openai import ChatOpenAI

from .state import DemoState


def input_node(state: DemoState) -> dict[str, str]:
    """Normalize and validate user input; set initial state.

    Args:
        state: Current graph state (must contain user_input).

    Returns:
        State updates: user_input (stripped), intent (for routing).
    """
    raw = (state.get("user_input") or "").strip()
    if not raw:
        return {"user_input": "", "intent": "empty"}

    # Simple intent: "summarize" if short, "question" if contains ?, else "process"
    if "?" in raw:
        intent = "question"
    elif len(raw) <= 100:
        intent = "summarize"
    else:
        intent = "process"

    return {"user_input": raw, "intent": intent}


def process_node(state: DemoState) -> dict[str, str]:
    """Call LLM to process user input based on intent.

    Args:
        state: Current state with user_input and intent.

    Returns:
        State update with 'processed' content.
    """
    user_input = state.get("user_input", "")
    intent = state.get("intent", "process")

    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.3)

    if intent == "empty":
        return {"processed": "(No input provided.)"}

    if intent == "summarize":
        prompt = f"Summarize this briefly in one or two sentences:\n\n{user_input}"
    elif intent == "question":
        prompt = f"Answer this question concisely:\n\n{user_input}"
    else:
        prompt = f"Process and clarify the following:\n\n{user_input}"

    response = llm.invoke(prompt)
    text = response.content if hasattr(response, "content") else str(response)
    return {"processed": text}


def output_node(state: DemoState) -> dict[str, str]:
    """Format processed content into final output.

    Args:
        state: State containing processed content.

    Returns:
        State update with 'output' string.
    """
    processed = state.get("processed", "")
    intent = state.get("intent", "process")
    user_input = state.get("user_input", "")

    if intent == "empty":
        output = "Please provide some input."
    else:
        output = f"[{intent.upper()}]\n\nQ: {user_input}\n\nA: {processed}"

    return {"output": output}
