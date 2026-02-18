# LangGraph Demo + Cursor (Rules, Commands, Skills) & BugBot

Minimal LangGraph (Python) demo with **2–3 graph states**, an **LLM node**, **conditional routing**, and a **simple web UI**. Includes Cursor rules, custom commands, a custom skill, and a BugBot integration example.

## Project layout

```
.
├── app.py                # Streamlit UI (run with: streamlit run app.py)
├── langgraph_demo/
│   ├── src/
│   │   ├── __init__.py
│   │   ├── state.py      # Graph state (TypedDict)
│   │   ├── nodes.py      # input, process (LLM), output nodes
│   │   └── graph.py      # Build graph + conditional edges
│   ├── __init__.py
│   └── cli.py            # CLI entrypoint (optional)
├── .cursor/
│   ├── rules/            # Type hints, docstrings, modular, clean code
│   ├── commands/         # /explain-graph, /improve-code
│   └── skills/           # Skill: add new node to LangGraph
├── requirements.txt
├── .env.example
└── README.md
```

## Setup

1. **Go to the project root** (the folder that contains `langgraph_demo` and `.cursor`)
   ```bash
   cd \Test-bugbot-main
   ```
   Or use your full path (e.g. `d:\Test-bugbot-main`).

2. **Create a virtual environment (recommended)**
   ```bash
   python -m venv .venv
   .venv\Scripts\activate   # Windows
   # source .venv/bin/activate  # macOS/Linux
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure API key**
   - Copy `.env.example` to `.env`.
   - Set `OPENAI_API_KEY` in `.env` (you said you already have an API key configured; ensure it’s in `.env` or in your environment).

   ```bash
   copy .env.example .env   # Windows
   # cp .env.example .env   # macOS/Linux
   ```

   Then edit `.env` and set your key.

## Run the demo (UI)

From the **project root**:

```bash
streamlit run app.py
```

Open the URL in your browser (e.g. http://localhost:8501). Type text in the box and click **Run** to see the graph output.

**Flow:** Input → classify intent → optional LLM (process) → output. Empty input skips the LLM.

### Optional: CLI

```bash
python -m langgraph_demo.cli "What is 2 + 2?"
```

## Cursor: Rules, Commands, Skills

### 1. Cursor Rules (`.cursor/rules/`)

- **Type hints** and **docstrings** for all public functions and modules.
- **Modular structure**: one concern per module; graph, nodes, state in separate files.
- **Clean code**: clear names, small functions, no magic values in core logic.

Open a file in this repo and the rules apply when the globs match (or when `alwaysApply` is true).

### 2. Cursor Commands (`.cursor/commands/`)

- **`/explain-graph`** – Explains the LangGraph flow (states, nodes, conditional routing) in this project.
- **`/improve-code`** – Refactors the current file with best practices (type hints, docstrings, structure).

Use them by typing `/` in Cursor chat and choosing the command.

### 3. Cursor Skill (`.cursor/skills/`)

- **Add new node to LangGraph** – Step-by-step workflow to add a node: state updates, node function, edges, validation and testing.

The skill is in `.cursor/skills/langgraph-add-node/`. The agent can use it when you ask to add or change a node in the graph.

## BugBot integration (demo)

- An **intentional bug** is introduced in the codebase (see `docs/BUGBOT_DEMO.md`).
- **Creating a PR**: create a branch, commit the change, push, open a PR.
- **Triggering BugBot**: add **`@cursor review`** (or your org’s trigger) in the PR description or a comment so BugBot runs.
- **What BugBot does**: analyzes the PR, detects the issue, and comments with findings.

See **`docs/BUGBOT_DEMO.md`** for the exact bug, how to create the PR, and how BugBot detects and comments.

## License

MIT (or your choice).
