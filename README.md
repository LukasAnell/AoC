# AoC

My solutions to the [Advent of Code](https://adventofcode.com/) puzzles, organized by language
and year.

## Layout

```
AoC/
├── inputs/<year>/<day>.txt   # puzzle inputs, gitignored, shared across all languages
├── python/
│   ├── <year>/dayNN.py       # one file per solved day
│   ├── utilities/            # shared helpers + template for new days
│   └── requirements.txt
└── tools/
    └── fetch_inputs.py       # downloads puzzle inputs from adventofcode.com
```

Adding a new language means adding a new top-level folder (e.g. `rust/<year>/`) alongside
`python/`, reusing the same shared `inputs/` tree.
