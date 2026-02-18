"""Simple CLI to run the LangGraph demo."""

import sys

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

from langgraph_demo.src.graph import build_graph


def main() -> int:
    """Read input from stdin or args, run graph, print output.

    Returns:
        Exit code: 0 on success, 1 on error.
    """
    if len(sys.argv) > 1:
        user_input = " ".join(sys.argv[1:])
    else:
        print("Enter text (or pipe stdin). Ctrl+Z then Enter to finish on Windows.", flush=True)
        user_input = sys.stdin.read().strip()

    graph = build_graph()
    initial = {"user_input": user_input}
    result = graph.invoke(initial)

    output = result.get("output", "")
    print(output, flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
