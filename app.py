"""Simple Streamlit UI for the LangGraph demo."""

import sys
from pathlib import Path

# Ensure project root is on path when running: streamlit run app.py
_root = Path(__file__).resolve().parent
if str(_root) not in sys.path:
    sys.path.insert(0, str(_root))

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

import streamlit as st

from langgraph_demo.src.graph import build_graph


def run_graph(user_input: str) -> str:
    """Run the graph and return the output text."""
    graph = build_graph()
    result = graph.invoke({"user_input": user_input or ""})
    # Support both correct key and intentional bug key for demo
    return result.get("output") or result.get("outpt", "")


st.set_page_config(page_title="LangGraph Demo", page_icon="🔄")
st.title("LangGraph Demo")
st.caption("Type text below. The graph will classify intent and run the LLM when needed.")

user_input = st.text_area("Input", placeholder="e.g. What is 2 + 2?", height=100)

if st.button("Run"):
    if not user_input.strip():
        user_input = ""
    with st.spinner("Running graph…"):
        output = run_graph(user_input.strip())
    st.divider()
    st.subheader("Output")
    st.text(output if output else "(No output — check the outpt/output bug in nodes.py if you expect text)")
