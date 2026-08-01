# Java solutions

---

## Prerequisites

Java 11+ (Makefile uses single-file source launch). Tested against Java 23.

---

## Layout

```
java/
├── utilities/
│   └── DayTemplate.java
└── <year>/
    └── dayNN/
        └── Main.java
```

---

## Starting a new day

```bash
mkdir -p java/<year>/dayNN
cp java/utilities/DayTemplate.java java/<year>/dayNN/Main.java
```

Then in the new `Main.java`:
1. Rename `class DayTemplate` to `class Main`.
2. Set `INPUT_FILE` to `../../../inputs/<year>/<day>.txt`

---

## Running

```bash
make run LANG=java YEAR=<year> DAY=NN
```
