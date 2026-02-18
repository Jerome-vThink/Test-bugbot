---
name: code-review
description: Reviews code for correctness, project standards (type hints, docstrings, modular structure), and clean code. Use when the user asks for a code review, review of a file or PR, or to check if code follows project rules.
---

# Code Review

Use this workflow when reviewing code in this project (current file, selected code, or a PR).

## Checklist

- [ ] Correctness and edge cases
- [ ] Project standards (type hints, docstrings)
- [ ] Structure and clean code
- [ ] Feedback format

---

## 1. Correctness and edge cases

- Logic is correct for the stated intent.
- Edge cases are handled (empty input, None, empty collections, boundary values).
- No obvious bugs (wrong condition, off-by-one, misuse of APIs).
- Error handling: explicit exceptions, no bare `except:`.

---

## 2. Project standards

Apply the project’s rules (see `.cursor/rules/`):

- **Type hints:** All function parameters and return types annotated. Prefer `list[str]`, `dict[str, str]`, etc.
- **Docstrings:** Every module and public function has a docstring. Use Google-style: summary, `Args:`, `Returns:`.
- **Exceptions:** Document raised exceptions in docstrings when they are part of the contract.

If the file is not Python, apply equivalent standards for that language.

---

## 3. Structure and clean code

- One clear concern per module; small, focused functions.
- Descriptive names; avoid magic strings/numbers in core logic.
- Prefer early returns and guard clauses over deep nesting.
- For LangGraph: state updates are returned as dicts; no in-place state mutation; routing functions are pure.

---

## 4. Feedback format

Structure feedback so the author can act on it:

- **Critical:** Must fix (bugs, broken behavior, security).
- **Suggestion:** Should fix for quality or project rules (e.g. missing types, docstrings).
- **Nice to have:** Optional improvements (naming, small refactors).

Give concrete snippets or line references where helpful. End with a short summary (what’s good, what to fix first).
