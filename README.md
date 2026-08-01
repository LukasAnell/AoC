# AoC

My solutions to the [Advent of Code](https://adventofcode.com/) puzzles, organized by language and year.

---

## Layout

```
❯ tree --dirsfirst --gitignore
AoC/
├── inputs/<year>/<day>.txt   # puzzle inputs, gitignored, shared across all languages
├── python/                   # see python/README.md
├── java/                     # see java/README.md
├── tools/
│   └── fetch_inputs.py       # downloads puzzle inputs from adventofcode.com
├── Makefile                  # make run LANG=<lang> YEAR=YYYY DAY=NN
└── pyproject.toml / uv.lock  # Python deps, managed with uv
```

Adding a new language means adding a new top-level folder (e.g. `cpp/<year>/`) alongside
`python/` and `java/`, reusing the same shared `inputs/` tree, with its own dependency
management and its own README.

---

## Getting started

```bash
uv sync                                 # creates .venv and installs Python deps
cp .env.example .env                    # fill in AOC_SESSION_COOKIE
uv run tools/fetch_inputs.py
make run LANG=python YEAR=2015 DAY=01
```
