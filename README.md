# Exercise 2: Test-Driven Development (TDD)

## Introduction

In this exercise, you'll practice **Test-Driven Development (TDD)** by writing tests *before* writing any code. This forces you to think about requirements and edge cases upfront.

## The TDD Cycle

Remember the cycle:

1. 🔴 **RED** - Write a failing test
2. 🟢 **GREEN** - Write minimal code to make it pass
3. 🔵 **REFACTOR** - Clean up your code (tests still passing)

**Important:** Commit after each green phase!

---

## Task 1: Password Strength Checker

### Function Signature
```python
def is_password_strong(password: str) -> bool:
    """
    Check if a password meets strength requirements.
    
    Args:
        password: The password string to validate
        
    Returns:
        True if password is strong, False otherwise
    """
    pass  # You'll implement this after writing tests
```

### Requirements (implement progressively)

Your password checker should validate:

1. **Minimum length** - choose a minimum length
2. **Contains uppercase** - At least one uppercase letter (A-Z)
3. **Contains lowercase** - At least one lowercase letter (a-z)
4. **Contains digit** - At least one number (0-9)
5. **Contains special character** - At least one of: `!@#$%^&*()-_+=`
6. **No Repeats ?** 

### TDD Approach

**Start simple, build incrementally:**

#### Step 1: Test minimum length
```python
# test_password_strength.py
from password_validator import is_password_strong

def test_password_too_short():
    assert is_password_strong("abc") is False

def test_password_minimum_length():
    assert is_password_strong("abcdefgh") is True  # Will fail on other rules later
```

**Now implement just enough code to pass these tests.**

#### Step 2: Add uppercase requirement


**Update your function to check for uppercase.**

#### Step 3: Continue adding requirements
- Add tests for lowercase (though most will already have it)
- Add tests for digits
- Add tests for special characters

#### Step 4: Comprehensive tests
```python
def test_password_all_requirements():
    assert is_password_strong("Abcd1234!") is True

def test_password_missing_digit():
    assert is_password_strong("Abcdefgh!") is False

def test_password_missing_special():
    assert is_password_strong("Abcd1234") is False
```

### Edge Cases to Consider

Write tests for:
- Empty string
- Very long password (max limit ?)
- Password with only special characters
- Password with spaces (decide: allow or reject?)
- Unicode characters (decide: allow or reject?)

### Bonus: Use Parametrize

Refactor your tests using `@pytest.mark.parametrize`:
```python
@pytest.mark.parametrize("password,expected", [
    ("abc", False),                    # Too short
    ("abcdefgh", False),               # No uppercase, digit, special
    ("Abcdefgh", False),               # No digit, special
    ("Abcd1234", False),               # No special
    ("Abcd1234!", True),               # Valid
    ("", False),                       # Empty
    ("P@ssw0rd", True),                # Valid
    ("MyP@ss123", True),               # Valid
])
def test_password_strength(password, expected):
    assert is_password_strong(password) == expected
```

---

## Task 2: Email Validator

### Function Signature
```python
def is_email_valid(email: str) -> bool:
    """
    Check if an email address is valid.
    
    Args:
        email: The email string to validate
        
    Returns:
        True if email is valid, False otherwise
    """
    pass  # You'll implement this after writing tests
```

### Requirements (implement progressively)

Your email validator should check:

1. **Contains '@'** - Must have exactly one @ symbol
2. **Has local part** - Text before @ (not empty)
3. **Has domain** - Text after @ (not empty)
4. **Domain has '.'** - Domain must contain at least one dot
5. **Valid characters** - Only alphanumeric, dots, underscores, hyphens
6. **Domain extension** - At least 2 characters after final dot


### Edge Cases to Consider

Write tests for:
- Empty string
- Only @ symbol
- Multiple dots in domain (`test@example..com`)
- Starting/ending with dot (`test@.example.com` or `test.@example.com`)
- Numbers in email (`user123@example.com`)
- Subdomains (`test@mail.example.com`)
- Special but valid characters in local part (`user+tag@example.com`)

### Valid Email Examples

These should return `True`:
- `user@example.com`
- `first.last@company.co.uk`
- `user_name@subdomain.example.com`
- `user+tag@example.org`
- `123@example.com`

### Invalid Email Examples

These should return `False`:
- `@example.com` (no local part)
- `user@` (no domain)
- `user@example` (no TLD)
- `user example@test.com` (space)
- `user@@example.com` (double @)
- `user@.com` (no domain name)

### Bonus: Use Parametrize
```python
@pytest.mark.parametrize("email,expected", [
    ("user@example.com", True),
    ("@example.com", False),
    ("user@", False),
    ("invalid", False),
    ("user@@example.com", False),
    ("first.last@company.co.uk", True),
    ("user@example", False),
    ("", False),
])
def test_email_validation(email, expected):
    assert is_email_valid(email) == expected
```

---

## Project Structure
```
tdd_exercise/
├── password_validator.py      # Your password checker implementation
├── email_validator.py         # Your email validator implementation
├── tests/
│   ├── __init__.py
│   ├── test_password_strength.py
│   └── test_email_validator.py
└── README.md
```

---

## Step-by-Step Workflow

For each requirement:

1. **Write the test first** (it will fail - RED 🔴)
```bash
   pytest tests/test_password_strength.py -v
```

2. **Write minimal code** to make test pass (GREEN 🟢)
```bash
   pytest tests/test_password_strength.py -v
```

3. **Refactor** if needed (tests still pass - REFACTOR 🔵)

4. **Commit** your changes
```bash
   git add .
   git commit -m "Add password length validation"
```

5. **Repeat** for next requirement

---





## Resources

- pytest documentation: https://docs.pytest.org/
- Python `re` module: https://docs.python.org/3/library/re.html
- Email RFC standards: https://datatracker.ietf.org/doc/html/rfc5322
- Password security best practices: https://pages.nist.gov/800-63-3/

Good luck! Remember: **RED → GREEN → REFACTOR**
