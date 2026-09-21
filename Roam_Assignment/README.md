# Roman Numeral Converter

A simple Python project that converts Roman numerals into standard Arabic numbers, such as `IV` to `4` and `MMXXVI` to `2026`.

This project is designed to be easy to understand, even for someone who is new to programming. It shows how a real software program can validate input, follow rules, and test for correctness.

## Project purpose

Roman numerals were used in ancient Rome and are still seen today in clocks, book chapters, movie titles, and historical documents. This project helps convert them into numbers in a reliable and safe way.

The program checks whether a Roman numeral is valid before converting it. For example, inputs like `IV`, `IX`, and `XVI` are accepted, while invalid values like `IIII`, `VX`, or `ABC` are rejected.

## What the program does

- Converts Roman numerals to integers
- Accepts uppercase and lowercase input
- Rejects invalid Roman numeral formats
- Validates common Roman numeral rules
- Provides a command-line interface for user input

## Project files

- `roman.py` — contains the conversion and validation logic
- `test_roman.py` — contains automated tests to check valid and invalid examples
- `README.md` — explains the project in plain English

## Roman numeral rules used by this project

The code follows the standard Roman numeral rules:

- Roman numerals use these symbols: `I`, `V`, `X`, `L`, `C`, `D`, `M`
- `V`, `L`, and `D` cannot repeat
- `I`, `X`, `C`, and `M` cannot repeat more than three times in a row
- Some smaller numbers before larger ones are allowed as subtractive pairs, such as:
  - `IV` = 4
  - `IX` = 9
  - `XL` = 40
  - `XC` = 90
  - `CD` = 400
  - `CM` = 900
- The final number must be between 1 and 3999

## How to run the project

1. Open a terminal or command prompt.
2. Go to the project folder.
3. Run the following command:

```bash
python roman.py
```

On Windows PowerShell, you may also use:

```powershell
python .\roman.py
```

Then the program will ask:

```text
Enter a Roman numeral:
```

You can type a value such as:

- `XIV`
- `MCMXCIV`
- `mmxxvi`

The program will output the equivalent number.

## Example

```text
Enter a Roman numeral: XIV
Integer: 14
```

```text
Enter a Roman numeral: VX
Invalid input: Invalid subtraction: VX
```

## Running the tests

This project includes automated tests to check both correct and incorrect inputs.

To run the tests, use:

```bash
pytest
```

If the tests pass, the program is behaving as expected.

## Why this is useful

This project is a good example of:

- data validation
- input checking
- testing software behavior
- converting between number systems
- building a simple command-line application

It is also a practical introduction to automated software testing, because the project includes tests that confirm the program works correctly.

## Beginner-friendly summary

In simple terms, the program does this:

1. Reads the Roman numeral entered by the user
2. Checks whether it follows the Roman numeral rules
3. Converts it to a number
4. Prints the result
5. Rejects invalid values instead of producing a wrong answer

## Conclusion

This project demonstrates how software can take human-readable text, validate it, and convert it into a correct numeric result. It is a small but professional example of input handling and testing in Python.

For a student project or learning exercise, it is a clear and effective example of how real-world software logic is built and checked.
