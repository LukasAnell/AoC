# Python solutions

---

## Prerequisites

[uv](https://docs.astral.sh/uv/) - Handles the pinned Python version (see `.python-version`) and dependencies automatically, no separate install needed.

---

## Layout

```
python/
├── utilities/
│   ├── template.py
│   └── utils.py
└── <year>/
    └── dayNN.py
```

---

## Starting a new day

```bash
cp python/utilities/template.py python/<year>/dayNN.py
```

The template already imports `read_input_lines()` from `python/utilities/utils.py`, which infers the year/day from the file's own path.

---

## Running

```bash
make run LANG=python YEAR=<year> DAY=NN
```

or directly:

```bash
uv run python/<year>/dayNN.py
```

Both work from any working directory — `utils.py` locates the repo root via `Path(__file__)`.
