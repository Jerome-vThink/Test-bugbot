# Demo Test Plans

Step-by-step plans to demo **LangGraph**, **Cursor Rules**, **Cursor Commands**, and **Cursor Skills**.  
Run everything from the **project root** (folder that contains `langgraph_demo` and `.cursor`).

---

## Before you start

- [ ] Virtual environment: `python -m venv .venv` then activate it
- [ ] Dependencies: `pip install -r requirements.txt`
- [ ] API key: copy `.env.example` to `.env` and set `OPENAI_API_KEY`

---

## 1. LangGraph demo (UI)

**What you’re showing:** The graph runs in the browser: you type text → the app runs the graph → you see the result.

### How to run

```bash
streamlit run app.py
```

Then open the URL in your browser (e.g. http://localhost:8501).

### What to try

| Try this              | You should see |
|-----------------------|----------------|
| Leave input empty, click **Run** | “Please provide some input.” (no LLM call) |
| Type: `What is 2 + 2?` | An answer with a `[QUESTION]`-style prefix (after fixing the `outpt` bug: `[QUESTION]` + answer) |
| Type: `Python is a language.`  | A short summary with a `[SUMMARIZE]`-style prefix |
| Type: a long paragraph (no `?`) | Processed text with a `[PROCESS]`-style prefix |

### Pass

- [ ] Empty input shows a message and does not call the LLM
- [ ] Non-empty input shows LLM output (fix `outpt` → `output` in `nodes.py` if you see nothing)

---

## 2. Cursor Rules

**What you’re showing:** Cursor suggests and enforces type hints, docstrings, and clean structure when you edit code.

### What’s in the project

- **`.cursor/rules/python-standards.mdc`** — Type hints, docstrings (Google-style). Used for `**/*.py`.
- **`.cursor/rules/modular-clean-code.mdc`** — One concern per module, small functions. Always on.

### What to do

1. Open **`langgraph_demo/src/nodes.py`**.
2. In Cursor chat, ask: **“Review this file for project standards.”**
3. Check that the answer mentions type hints and docstrings.

**Optional:** Remove the type hints from one function and ask again — Cursor should suggest adding them back.

### Pass

- [ ] Cursor’s review mentions type hints and docstrings (and optionally modular/clean code).

---

## 3. Cursor Commands

**What you’re showing:** The custom commands `/explain-graph` and `/improve-code` work and give the right kind of result.

### `/explain-graph`

1. In Cursor chat, type **`/`** and choose **explain-graph**.
2. Send the message.
3. The reply should describe: **state** (`DemoState`), **nodes** (input, process, output), **edges** (START → input → process or output → output → END), and **routing** (`route_after_input`).

**Pass:** [ ] The explanation matches the real flow and is easy to follow.

### `/improve-code`

1. Open any Python file (e.g. `langgraph_demo/src/state.py`).
2. In chat, type **`/`** and choose **improve-code**.
3. Send. Cursor should suggest refactors: type hints, docstrings, structure — without changing behavior.

**Pass:** [ ] Suggestions match the command and don’t change what the code does.

---

## 4. Cursor Skills

**What you’re showing:** When you ask to add a node, Cursor follows the **langgraph-add-node** skill (state → node → graph → test).

### What’s in the project

- **`.cursor/skills/langgraph-add-node/SKILL.md`** — 4 steps: extend state → add node → add edges → validate.

### What to do

1. In Cursor chat, ask: **“How do I add a new node to this LangGraph project?”**
2. The answer should describe the 4 steps and point to `state.py`, `nodes.py`, `graph.py`.

**Optional:** Ask: **“Add a validation node that runs after input and before process.”**  
Check that the agent updates state, nodes, and graph in line with the skill.

### Pass

- [ ] “How do I add a node?” returns the 4-step workflow and the right files.
- [ ] (Optional) Actually adding a node follows that workflow and touches the right files.

---

## Quick demo order

1. **LangGraph** — Run `streamlit run app.py`, try empty and non-empty input in the UI.
2. **Rules** — Open `nodes.py`, ask Cursor to review for project standards.
3. **Commands** — Run `/explain-graph`, then `/improve-code` on a file.
4. **Skills** — Ask how to add a new node; optionally ask to add a validation node.

---

## One-line checklist

| Demo        | How to run / What to do                    | Pass |
|------------|---------------------------------------------|------|
| LangGraph  | `streamlit run app.py` → use the UI         | [ ]  |
| Rules      | Open `.py` file → “Review for project standards” | [ ]  |
| explain-graph | `/explain-graph` in chat                 | [ ]  |
| improve-code  | Open file → `/improve-code` in chat      | [ ]  |
| Skills     | “How do I add a new node?” (and optionally add one) | [ ]  |
