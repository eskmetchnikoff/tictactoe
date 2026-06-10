# tictactoe

A terminal-based two-player tic-tac-toe game in Python. Single file: `tictactoe.py`.

## Project purpose

This is Sam's (sckadoodle) learning project. The primary goal is practicing Git workflows and software testing — using a real codebase as the vehicle. The game itself is secondary.

Sam is a field applications scientist at a genomics company. The long-term goal is for her to use Claude to define requirements as tests, then have Claude write code that satisfies them — applied to scientific computing workflows.

## Collaborators

- **Sam Kalla** (sckadoodle) — owner, learning Git and terminal basics
- **Andrew Widdowson** (widdowson) — collaborator, more experienced, teaching Sam Git

## How to run

```
python3 tictactoe.py
```

When prompted for Player 2, type `c` to play against the computer.

## Current features

- Two human players, or human vs computer (random move AI)
- Players enter their names at the start of each game
- Type `?` during your turn to print the position reference grid
- Positions 1–9 numbered left-to-right, top-to-bottom

## Git learning progress

Sam has practiced the following through hands-on exercises in this repo:

- `git diff` / `git status` — inspecting state before acting
- `git checkout -b` — creating and switching branches
- `git add` / `git commit` — the staging and commit loop
- `git log --oneline --all --graph` — reading history
- `git merge` — fast-forward merges and conflict resolution
- `git push` / `git branch -d` — publishing and cleanup

**Next topic:** `git blame` and `git show` — reading history at the line and commit level.

## Testing learning plan

Testing is taught via pytest. To run tests:

```
pytest test_tictactoe.py -v
pytest test_tictactoe.py -v --cov=tictactoe --cov-report=term-missing
```

Milestones (pick up at the first incomplete one):

1. **Coverage completion** — Tests for all easily-testable pure functions (`is_full` ✅, `check_winner`, `computer_move`). Discuss what not to test (`print_board`, `get_move` involve stdout/input). Commit when coverage is satisfying.
2. **Test-driven bug finding** — Write a test that should pass per spec, watch it fail, identify the bug.
3. **Fix the bug** — Red → understand → fix → green. The core feedback loop.
4. **New feature + tests in lockstep** — Sam writes a feature, Claude writes the matching test (or vice versa).
5. **Refactor / changing features** — Tests as safety net; understand the difference between "implementation changed" and "behavior changed."

... (Andrew checks in here and may define further milestones) ...

N. **Regression testing** — How do you know a change didn't silently break something? Especially relevant for genomics pipelines.

## Teaching notes

Sam is a terminal beginner. When teaching:

- Explain each command before she runs it, including what each flag does
- Have her run commands herself via the `!` prefix — she stays in the driver's seat
- Correct typos clearly and explain why they broke things (spacing in shell commands is a common stumble)
- Interactive programs (like `python3 tictactoe.py`) must be run with `!` in her terminal, not via Claude's Bash tool
- Andrew (widdowson) co-pilots from a second keyboard/mouse in the same room; he may address Claude directly to coordinate before handing back to Sam
