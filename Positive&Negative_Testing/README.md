# Positive and Negative Testing

This project demonstrates simple input validation using Python and test-driven positive/negative test cases.

The goal is to check that valid inputs are accepted and invalid inputs raise the correct errors.

## Project Files

- `validators.py` - Contains the validation functions
- `test_positivevalidators.py` - Tests valid inputs that should pass
- `test_negativevalidators.py` - Tests invalid inputs that should fail
- `README.md` - Project documentation

## Validators

### `validate_email(email)`
Validates whether a given email address matches a standard format.

Rules:
- Must contain a username and domain
- Must include an `@` symbol
- Must have a valid domain with a dot and a top-level domain
- Accepts letters, numbers, and common email characters such as `.`, `_`, `%`, `+`, and `-`

Example valid emails:
- `student@siam.ac.th`
- `user@mail.example.com`

If the email is invalid, the function raises a `ValueError`.

### `validate_age(age)`
Validates whether the age is an integer in a reasonable range.

Rules:
- Age must be an integer
- Age must be between `0` and `150` inclusive

If the value is not an integer, the function raises a `TypeError`.
If the age is outside the allowed range, it raises a `ValueError`.

## Positive Testing

The positive test file checks that valid values are accepted.

Examples:
- Valid email addresses are accepted
- Valid age values such as `0`, `25`, and `150` are accepted

## Negative Testing

The negative test file checks that invalid values are rejected.

Examples:
- Email without `@` is rejected
- Email without a domain is rejected
- Negative age is rejected
- Non-integer age input such as a string is rejected

## Running the Tests

Make sure you have Python and `pytest` installed.

Run the tests with:

```bash
pytest -q
```

This will execute both the positive and negative test files and confirm that the validator behavior matches the expected outcomes.

## Example Usage

```python
from validators import validate_email, validate_age

print(validate_email("user@example.com"))
print(validate_age(25))
```

Expected output:

```python
True
True
```

## Summary

This project is a simple example of automated software testing using both positive and negative cases to verify the correctness of validation logic.
