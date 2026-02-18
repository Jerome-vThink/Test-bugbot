# BugBot Integration Demo

This doc describes the **intentional bug** in the repo, how to **create a PR**, and how **BugBot** (via `@cursor review`) detects and comments on issues.

## The intentional bug

**Location**: `langgraph_demo/src/nodes.py` — in `output_node`.

**Bug**: The return dictionary uses a typo: `"outpt"` instead of `"output"`. The graph state type and the CLI expect the key `"output"`. So when the user provides non-empty input:

- The graph runs and the node returns `{"outpt": ...}`.
- The final state has no `"output"` key.
- The CLI does `result.get("output", "")` and prints nothing (or only the default empty string).

**How to verify**: Run `python -m langgraph_demo.cli "Hello"` — you should see no response body, while with the fix (return `{"output": output}`) you see the formatted LLM response.

**Fix**: Change `return {"outpt": output}` to `return {"output": output}` in `output_node`.

---

## Creating a PR (for the demo)

1. Create a branch (e.g. `fix/output-typo` or keep the bug on a `demo/bugbot` branch for the demo).
2. Commit the change that introduces the bug (or leave it as-is if the bug is already in `main`).
3. Push and open a **Pull Request** against your default branch (e.g. `main`).
4. In the PR description or in a comment, add **`@cursor review`** (or your organization’s trigger for BugBot) to request an automated review.

---

## How BugBot detects and comments

- **Trigger**: When someone adds `@cursor review` (or the configured trigger) in the PR, BugBot runs on the PR diff.
- **Detection**: BugBot analyzes the changed (and relevant) code and can flag:
  - Wrong or inconsistent dictionary keys (e.g. `"outpt"` vs `"output"` expected by the rest of the codebase).
  - Missing or incorrect state keys that downstream code (e.g. CLI) relies on.
- **Comment**: BugBot posts a comment on the PR describing the issue and, where applicable, suggests a fix (e.g. renaming `outpt` to `output`).

After the fix is applied, the CLI again prints the model output correctly.

---

## Summary

| Item | Details |
|------|--------|
| **Bug** | Typo in `output_node`: `"outpt"` instead of `"output"`. |
| **File** | `langgraph_demo/src/nodes.py`. |
| **Create PR** | Branch → commit → push → open PR. |
| **Trigger BugBot** | Add `@cursor review` in the PR. |
| **Outcome** | BugBot detects the wrong key and comments; fix by using `"output"`. |
