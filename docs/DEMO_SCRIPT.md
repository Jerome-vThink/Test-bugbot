# How to Demo: Rules, Commands, and Skills

Follow these steps in order. Use Cursor chat for all steps.

---

## Commands not showing when you type `/`?

Cursor only loads commands from the **workspace root** — the folder that **contains** `.cursor` must be the folder you opened in Cursor.

- **Do this:** **File → Open Folder** and open the folder that has **`.cursor`**, **`app.py`**, and **`langgraph_demo`** directly inside it (e.g. `Test-bugbot-main` — the *inner* one, not its parent).
- If you opened the *parent* folder, Cursor looks for `.cursor` there and won’t find your commands. Open the inner project folder and try `/` again.

---

## 1. Demo Rules

**What you’re showing:** Cursor uses project rules to enforce type hints, docstrings, and clean code.

### Step 1 – Show that rules exist

- In the file tree, open **`.cursor/rules/`**.
- Open **`python-standards.mdc`** and briefly show: “We require type hints and docstrings for all Python files.”
- Open **`modular-clean-code.mdc`** and show: “We require one concern per module and small functions.”

### Step 2 – Show rules in action

1. Open **`langgraph_demo/src/nodes.py`** (so the Rules apply to this file).
2. In **Cursor chat**, type exactly:
   ```text
   Review this file for project standards.
   ```
3. Send. Cursor should reply with a review that mentions **type hints**, **docstrings**, and possibly **modular structure** — i.e. it’s following the rules.

### Step 3 – Show rules “catching” a violation (optional)

1. In `nodes.py`, temporarily **delete the return type** of one function, e.g. change  
   `def input_node(state: DemoState) -> dict[str, str]:`  
   to  
   `def input_node(state: DemoState):`
2. In chat, ask:
   ```text
   Does this file follow the project rules?
   ```
3. Cursor should suggest adding the return type back (rule enforcement).
4. Undo your change when done.

**Script to say:**  
“We have Rules that require type hints and docstrings. When I ask Cursor to review this file, it follows those rules. If I break a rule, Cursor suggests fixing it.”

---

## 2. Demo Commands

**What you’re showing:** Custom commands give repeatable, one-click prompts for “explain graph” and “improve code.”

### Step 1 – Show where commands live

- In the file tree, open **`.cursor/commands/`**.
- Show **`explain-graph.md`** and **`improve-code.md`**: “These are the two commands we use in this project.”

### Step 2 – Demo `/explain-graph`

1. In **Cursor chat**, type **`/`** (slash).
2. Choose **`explain-graph`** from the list.
3. Send (you can send as-is, or add “please”).
4. Cursor should reply with:
   - **State** (e.g. `DemoState` in `state.py`)
   - **Nodes** (input, process, output in `nodes.py`)
   - **Edges** (START → input → process or output → output → END)
   - **Routing** (e.g. `route_after_input`)
   - How to run (UI or CLI)

**Script to say:**  
“When I type slash and pick ‘explain-graph’, Cursor runs a saved prompt that explains the whole LangGraph flow. No need to write that prompt every time.”

### Step 3 – Demo `/improve-code`

1. Open a Python file (e.g. **`langgraph_demo/src/state.py`**).
2. In chat, type **`/`** and choose **`improve-code`**.
3. Send.
4. Cursor should suggest changes: type hints, docstrings, structure — and say it won’t change behavior.

**Script to say:**  
“The improve-code command refactors the current file to match our rules — types, docstrings, clean structure — without changing what the code does.”

---

## 3. Demo Skills

**What you’re showing:** A Skill teaches Cursor a fixed workflow (here: how to add a new node to the graph).

### Step 1 – Show the skill file

- Open **`.cursor/skills/langgraph-add-node/SKILL.md`**.
- Briefly show the **4 steps**: extend state → implement node → register in graph → validate and test. Say: “This Skill tells Cursor exactly how we add a node in this project.”

### Step 2 – Demo “How do I add a node?”

1. In **Cursor chat**, type:
   ```text
   How do I add a new node to this LangGraph project?
   ```
2. Send. The answer should follow the Skill: **4 steps**, and mention **`state.py`**, **`nodes.py`**, **`graph.py`**, and **validation/testing**.

**Script to say:**  
“Our Skill defines a 4-step process for adding a node. When I ask how to add a node, Cursor follows that Skill and points to the right files and steps.”

### Step 3 – Demo “Add a node” (optional, longer)

1. In chat, type:
   ```text
   Add a validation node that runs after input and before process. It should check that user_input is not empty and set a validation_result in state.
   ```
2. Send. Cursor should:
   - Add a field to **`state.py`** (e.g. `validation_result`)
   - Add a **validation node** in **`nodes.py`**
   - Update **`graph.py`** so the flow is: input → validation → process or output
   - Mention testing/validation

**Script to say:**  
“When I ask to add a real node, Cursor follows the same Skill: state first, then the node, then the graph, then validation. That keeps changes consistent.”

---

## Quick reference

| Demo     | What to do |
|----------|------------|
| **Rules**   | Open `nodes.py` → chat: *“Review this file for project standards.”* (Optional: remove a type hint and ask *“Does this file follow the project rules?”*) |
| **Commands** | Type `/` → **explain-graph** (send). Then open a `.py` file → `/` → **improve-code** (send). |
| **Skills**   | Chat: *“How do I add a new node to this LangGraph project?”* (Optional: *“Add a validation node that runs after input and before process.”*) |

---

## Suggested demo order (5–10 minutes)

1. **Rules** — Open rules files, then “Review this file for project standards” on `nodes.py`.
2. **Commands** — `/explain-graph`, then `/improve-code` on `state.py`.
3. **Skills** — “How do I add a new node?” then optionally “Add a validation node…”.

That’s enough to show that Rules, Commands, and Skills are all working in this project.
