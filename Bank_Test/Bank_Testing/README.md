# Bank Testing

This folder is a small Python testing project. It contains two simple pieces
of application code and automated tests for them:

1. A `BankAccount` class that stores a balance and supports deposits and
   withdrawals.
2. A `letter_grade` function that converts a score into a letter grade.

The project is useful for beginners because the code is short, but the tests
demonstrate important software testing ideas such as assertions, boundary
values, exceptions, and independent tests.

## What you need

- Python 3.8 or newer
- `pytest`, the testing framework used by this project
- A terminal, such as PowerShell, Command Prompt, or the VS Code terminal

Install pytest on Windows with:

```powershell
py -m pip install pytest
```

If the `py` command is not available, try:

```powershell
python -m pip install pytest
```

The `py` command is the normal Python launcher on Windows. Running pytest as
`py -m pytest` makes sure that pytest uses the same Python installation.

## Folder contents

| File | Purpose |
|---|---|
| `bank.py` | Defines the `BankAccount` class. |
| `grade.py` | Defines the `letter_grade` function. |
| `test_bank.py` | Tests that a deposit increases an account balance. |
| `test_grades.py` | Tests grade boundaries and an invalid score. |
| `test_dependent.py` | Demonstrates two account tests written as separate functions. |
| `test_independent.py` | Demonstrates tests that each create their own fresh account. |
| `.gitignore` | Lists local folders and files that Git should ignore. |
| `README.md` | Explains this project and how to use it. |

## How to run the tests

Open a terminal in the `Bank_Testing` folder and run:

```powershell
py -m pytest -q
```

The `-q` option means "quiet" and prints a short summary. To see the name of
each test and more details, run:

```powershell
py -m pytest
```

You can run one test file at a time:

```powershell
py -m pytest test_bank.py -q
py -m pytest test_grades.py -q
py -m pytest test_dependent.py -q
py -m pytest test_independent.py -q
```

Pytest searches for files named `test_*.py` and functions whose names start
with `test_`. Each test uses Python's `assert` statement to compare the actual
result with the expected result.

## `bank.py`: the BankAccount class

### Creating an account

The `BankAccount` class stores the current balance in an attribute called
`balance`:

```python
from bank import BankAccount

account = BankAccount(100)
print(account.balance)  # 100
```

If no starting balance is provided, the default is zero:

```python
account = BankAccount()
print(account.balance)  # 0
```

### Depositing money

`deposit(amount)` adds money to the current balance and returns the new
balance:

```python
account = BankAccount(100)
new_balance = account.deposit(50)

print(new_balance)    # 150
print(account.balance)  # 150
```

The amount must be greater than zero. A zero or negative amount raises a
`ValueError`:

```python
account.deposit(0)     # ValueError: Deposit must be positive
account.deposit(-10)   # ValueError: Deposit must be positive
```

### Withdrawing money

`withdraw(amount)` subtracts money from the balance and returns the new
balance:

```python
account = BankAccount(100)
new_balance = account.withdraw(30)

print(new_balance)       # 70
print(account.balance)  # 70
```

The current implementation raises `ValueError` when the withdrawal is larger
than the balance:

```python
account = BankAccount(100)
account.withdraw(150)  # ValueError: Insufficient funds
```

The class does not currently reject a zero or negative withdrawal. The tests
and documentation should be updated if that behavior is meant to be changed.

### Bank account behavior summary

| Operation | Example | Result |
|---|---|---|
| Create with a balance | `BankAccount(100)` | Balance is `100` |
| Create without a balance | `BankAccount()` | Balance is `0` |
| Deposit | `deposit(50)` on `100` | Balance becomes `150` |
| Withdraw | `withdraw(30)` from `100` | Balance becomes `70` |
| Deposit zero or less | `deposit(0)` | Raises `ValueError` |
| Withdraw more than balance | `withdraw(150)` from `100` | Raises `ValueError` |

## `grade.py`: converting scores to grades

The `letter_grade(score)` function accepts a score from 0 through 100 and
returns a letter:

| Score range | Returned grade |
|---|---|
| 80 to 100 | `"A"` |
| 70 to 79 | `"B"` |
| 60 to 69 | `"C"` |
| 0 to 59 | `"F"` |

Examples:

```python
from grade import letter_grade

print(letter_grade(85))  # A
print(letter_grade(70))  # B
print(letter_grade(60))  # C
print(letter_grade(59))  # F
```

Scores below 0 or above 100 are invalid and raise `ValueError`:

```python
letter_grade(-1)   # ValueError: Score must be 0-100
letter_grade(101)  # ValueError: Score must be 0-100
```

## Understanding the tests

### `test_bank.py`

This file checks one basic behavior:

1. Create an account with a balance of 100.
2. Deposit 50.
3. Assert that the returned balance is 150.

An assertion is a statement that must be true for the test to pass:

```python
assert new_balance == 150
```

### `test_grades.py`

This file focuses on **boundary testing**. A boundary is the point where the
program changes from one result to another. The tests check both sides of the
important boundaries:

- 80 returns `A`, while 79 returns `B`.
- 60 returns `C`, while 59 returns `F`.
- 0 is the lowest valid score and returns `F`.
- 100 is the highest valid score and returns `A`.
- -1 is invalid and must raise `ValueError`.

The test uses `pytest.raises` to verify an expected error:

```python
with pytest.raises(ValueError):
	letter_grade(-1)
```

### `test_dependent.py` and `test_independent.py`

Both files test deposits and withdrawals. They are included to demonstrate
how test state should be handled.

Each test in `test_independent.py` creates a new `BankAccount`, performs one
operation, and checks the result. This is the preferred pattern because the
test does not depend on another test running first.

The functions in `test_dependent.py` also create their own account in the
current code, so they are independent in practice despite the filename. If a
test reused the same account object, the balance left by one test could change
the result of the next test. That would make failures harder to understand.

## Module names

The grading implementation is stored in `grade.py`, and the grading tests now
import it with the matching module name:

```python
from grade import letter_grade
```

There is no `grades.py` file in this folder. Keeping the filename and import
name the same prevents `ModuleNotFoundError` during pytest collection.

## Common problems

### `pytest` is not recognized

Use pytest through Python:

```powershell
py -m pytest -q
```

If pytest is missing, install it with:

```powershell
py -m pip install pytest
```

### Tests pass or fail depending on their order

Tests should create their own data and should not depend on values changed by
another test. Use the pattern shown in `test_independent.py`.

## Learning checklist

After studying this folder, a beginner should understand how to:

- Create and use a Python class.
- Change and read an object's state through methods and attributes.
- Write a function that maps input values to output values.
- Use `assert` to check expected results.
- Test the smallest and largest valid values.
- Test values just outside the valid range.
- Check that invalid input raises the correct exception.
- Keep automated tests independent from one another.
- Run a pytest test file from a terminal.

## Summary

This project uses simple bank and grading examples to demonstrate a complete
testing workflow: write small pieces of code, define the expected behavior,
test normal cases, test boundary cases, test invalid input, and run all tests
automatically with pytest.