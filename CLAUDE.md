# tictactoe

A terminal-based two-player tic-tac-toe game in Python. Single file: `tictactoe.py`.

## Project purpose

This is Sam's (sckadoodle) learning project. The primary goal is practicing Git workflows — branching, committing, merging, conflict resolution — using a real codebase as the vehicle. The game itself is secondary.

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

## Teaching notes

Sam is a terminal beginner. When continuing the Git tutorial:

- Explain each command before she runs it, including what each flag does
- Have her run commands herself via the `!` prefix — she stays in the driver's seat
- Correct typos clearly and explain why they broke things (spacing in shell commands is a common stumble)
- Interactive programs (like `python3 tictactoe.py`) must be run with `!` in her terminal, not via Claude's Bash tool
