
# Automated Software Testing Examples

This project is a collection of small Python programs and `pytest` tests. It
is designed for learning how software is checked automatically instead of
being tested only by manually running a program and looking at the output.

The examples cover four important testing ideas:

1. **Assertions** - checking lists, dictionaries, sets, and decimal numbers.
2. **Bank testing** - testing a bank account class and a grading function.
3. **Positive and negative testing** - checking both accepted and rejected
	 input.
4. **Roman numeral testing** - validating and converting Roman numerals.

Each topic is kept in its own folder. The folders are independent examples,
so you can study or run one topic at a time.

## What you need

- Python 3.8 or newer
- `pytest`
- A terminal such as PowerShell, Command Prompt, or the VS Code terminal

There is currently no `requirements.txt` file. Install `pytest` with one of
these Windows commands:

```powershell
py -m pip install pytest
```

If the `py` command is not available, use:

```powershell
python -m pip install pytest
```

The `py` command is the usual Python launcher on Windows. The examples below
use `py -m pytest`; `python -m pytest` is an equivalent alternative when
`python` is configured on your PATH.

## Running the tests

Open a terminal in this project folder. Run tests from the folder that contains
the code and test files:

```powershell
cd Assertions_Testing
py -m pytest -q
```

Repeat the same process for the other folders:

```powershell
cd ..\Bank_Testing
py -m pytest -q

cd '..\Postive&Negative_Testing'
py -m pytest -q

cd ..\Roman_Testing
py -m pytest -q
```

The folder name `Postive&Negative_Testing` is intentionally kept as it exists
in this project. The word "Positive" is misspelled in the folder name, so use
the exact spelling when typing the command.

The `-q` option means "quiet": pytest prints a short summary. Remove `-q` if
you want more detail about each test.

To run every test from the project root, you can also use:

```powershell
py -m pytest -q Assertions_Testing Bank_Testing 'Postive&Negative_Testing' Roman_Testing
```

# Python Testing Practice Lab

This repository is a set of small, runnable examples for learning automated
testing with Python and `pytest`. Each directory focuses on a different kind
of behavior: comparing values, testing state changes, validating user input,
and checking a conversion algorithm.

## Quick start

The project does not include a dependency file. Install `pytest` with the
Python launcher available on your machine:

```powershell
py -m pip install pytest
```

Run the complete suite from the repository root:

```powershell
py -m pytest -q Assertions_Testing Bank_Testing 'Positive&Negative_Testing' Roman_Testing
```

The same command works with `python -m pytest` when `py` is unavailable. To
inspect one exercise, change into its directory and run `py -m pytest -q`.

## Exercises at a glance

| Directory | Main idea | Code under test |
| --- | --- | --- |
| `Assertions_Testing` | Equality, collection operations, and float tolerance | Tests only |
| `Bank_Testing` | Mutable account state, exceptions, score boundaries, and test isolation | `bank.py`, `grade.py` |
| `Positive&Negative_Testing` | Accepted input versus rejected input | `validators.py` |
| `Roman_Testing` | Strict parsing, conversion, and command-line interaction | `roman.py` |

## Assertions and numerical comparisons

`Assertions_Testing/test_collections.py` uses plain assertions with lists,
dictionaries, and sets. It demonstrates ordered list equality, comparing list
contents after sorting, dictionary equality regardless of key order, and set
intersection.

`Assertions_Testing/test_floats.py` highlights a common numerical testing
issue. The expression `0.1 + 0.2` is compared with `pytest.approx(0.3)` for a
tolerant assertion, while a separate test shows that exact binary floating-
point equality is not reliable for this calculation.

## Bank accounts, grades, and test independence

`Bank_Testing/bank.py` defines `BankAccount`:

```python
from bank import BankAccount

account = BankAccount(100)
account.deposit(50)   # returns 150; balance becomes 150
account.withdraw(30)  # returns 120; balance becomes 120
```

- The default starting balance is `0`.
- A deposit must be greater than zero or it raises `ValueError`.
- A withdrawal larger than the current balance raises `ValueError` with an
  insufficient-funds message.
- The current implementation allows zero or negative withdrawals; that is an
  important behavior to notice when extending the tests.

`Bank_Testing/grade.py` provides `letter_grade(score)`. Scores from `0` to
`100` are mapped as follows: `80-100` is `A`, `70-79` is `B`, `60-69` is `C`,
and `0-59` is `F`. Values outside that range raise `ValueError`.

The test files show several testing styles:

- `test_bank.py` checks a successful deposit.
- `test_grades.py` checks grade boundaries and an invalid score with
  `pytest.raises`.
- `test_dependent.py` contains separate deposit and withdrawal examples.
- `test_independent.py` creates a new account inside each test, so one test
  cannot change the starting state of another.

## Positive and negative validation

`Positive&Negative_Testing/validators.py` contains two validators:

```python
from validators import validate_email, validate_age

validate_email("user@example.com")  # True
validate_age(25)                    # True
```

`validate_email` accepts the project's regular-expression format: a username,
`@`, domain, dot, and a top-level domain of at least two letters. Invalid
values raise `ValueError`. The tests include a normal address and a
multi-level domain, as well as missing `@` and missing-domain cases.

`validate_age` accepts integers from `0` through `150`, inclusive. A value
outside that range raises `ValueError`; a non-integer raises `TypeError`. The
positive tests cover `0`, `25`, and `150`, while the negative tests cover `-5`
and the string `"twenty"`.

## Roman numeral conversion

`Roman_Testing/roman.py` exposes `roman_to_integer(roman)` and
`integer_to_roman(number)`. The parser accepts lowercase input by converting
it to uppercase, then checks the characters, repetition rules, allowed
subtractive pairs, numeric range, and canonical form.

Valid subtractive pairs are `IV`, `IX`, `XL`, `XC`, `CD`, and `CM`. Values must
represent an integer from `1` through `3999`. The parameterized tests cover
ordinary values, subtractive forms, lowercase input, and the upper boundary
`MMMCMXCIX` (`3999`). Invalid cases include empty input, repeated symbols,
unknown characters, illegal subtraction, non-canonical ordering, and values
above `3999`.

The module also has an interactive command-line mode:

```powershell
cd Roman_Testing
py roman.py
```

Enter a Roman numeral when prompted. The program prints the integer or an
error, then asks whether to continue with `yes`/`y` or stop with `no`/`n`.

## Repository map

```text
automated_software_testing/
|-- README.md
|-- Assertions_Testing/
|   |-- README.md
|   |-- test_collections.py
|   `-- test_floats.py
|-- Bank_Testing/
|   |-- README.md
|   |-- bank.py
|   |-- grade.py
|   |-- test_bank.py
|   |-- test_dependent.py
|   |-- test_grades.py
|   `-- test_independent.py
|-- Positive&Negative_Testing/
|   |-- README.md
|   |-- validators.py
|   |-- test_negativevalidators.py
|   `-- test_positivevalidators.py
`-- Roman_Testing/
    |-- README.md
    |-- roman.py
    `-- test_roman.py
```

The README in each directory gives a more focused explanation. This root
README is the index for running and comparing all four testing examples.
prove that code works for valid values, rejects invalid values, handles edge
cases, and remains understandable to future developers.
