# Expense Tracker (CLI, OOP)

A command-line expense tracker built in Python, using classes instead of plain dictionaries. Add, view, and total up expenses — all saved to a local file so your data persists between runs.

## Features

- **Add expenses** — record a name, amount, and category for each expense
- **View expenses** — see every recorded expense and its details
- **View total** — see the sum of all recorded expenses
- **Persistent storage** — expenses are saved to `expense.json` and automatically reloaded the next time the program runs

## How it works

Each expense is represented as an `Expense` object (not a plain dictionary), built from a custom class:

```python
class Expense:
    def __init__(self, name, amount, category):
        self.name = name
        self.amount = amount
        self.category = category
```

All expenses are stored in a list of `Expense` objects. Since Python's `json` module can't save custom objects directly, each object is converted to a dictionary (`to_dict()`) before saving, and converted back into a real `Expense` object when the program loads — so the objects still have their methods (like `.display()`) available after reloading, not just raw data.

On startup, the program tries to load existing expenses from `expense.json`. If the file doesn't exist yet (first run), it starts with an empty list instead of crashing.

## Running it

```bash
python expense.py
```

You'll see a menu:

```
1. Add expense
2. Show expenses
3. Show total
4. Exit
```

Enter a number to choose an action, and follow the prompts.

## What I learned building this

This was my second project, built right after a task tracker that used plain lists and dictionaries. This one pushed further into:

- **Classes and objects** — understanding `self`, constructors (`__init__`), and methods, and *why* a function needs to live inside a class versus outside it (does it act on one specific object, or a whole collection?)
- **Object serialization** — converting custom objects into JSON-safe dictionaries before saving, and rebuilding real objects from that data on load. This was the hardest new concept, since it's not something you hit with simple data types like plain lists/dicts.
- **Single-responsibility functions** — splitting logic that could have been combined (like showing expenses and calculating totals) into separate, focused functions instead
- **Git workflow** — creating a repo locally with `git init`, connecting it to GitHub with `git remote add`, and using `.gitignore` to keep generated data files (like `expense.json`) out of version control

## Possible future improvements

- Filtering expenses by category
- Monthly/date-based tracking
- Editing or deleting an existing expense
