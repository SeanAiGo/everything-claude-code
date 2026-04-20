---
description: 📝 【文件定位】這是一個命令（Command）定義檔案。此命令的功能：Comprehensive Python code review for PEP 8 compliance, type hints, security, and Pythonic idioms. Invokes the python-reviewer agent.
---

# Python Code Review
> 🇹🇼 命令指示

This command invokes the **python-reviewer** agent for comprehensive Python-specific code review.

## What This Command Does
> 🇹🇼 命令指示

1. **Identify Python Changes**: Find modified `.py` files via `git diff`
2. **Run Static Analysis**: Execute `ruff`, `mypy`, `pylint`, `black --check`
3. **Security Scan**: Check for SQL injection, command injection, unsafe deserialization
4. **Type Safety Review**: Analyze type hints and mypy errors
5. **Pythonic Code Check**: Verify code follows PEP 8 and Python best practices
6. **Generate Report**: Categorize issues by severity

## When to Use
> 🇹🇼 命令指示

Use `/python-review` when:
- After writing or modifying Python code
- Before committing Python changes
- Reviewing pull requests with Python code
- Onboarding to a new Python codebase
- Learning Pythonic patterns and idioms

## Review Categories
> 🇹🇼 命令指示

### CRITICAL (Must Fix)
> 🇹🇼 命令指示
- SQL/Command injection vulnerabilities
- Unsafe eval/exec usage
- Pickle unsafe deserialization
- Hardcoded credentials
- YAML unsafe load
- Bare except clauses hiding errors

### HIGH (Should Fix)
> 🇹🇼 命令指示
- Missing type hints on public functions
- Mutable default arguments
- Swallowing exceptions silently
- Not using context managers for resources
- C-style looping instead of comprehensions
- Using type() instead of isinstance()
- Race conditions without locks

### MEDIUM (Consider)
> 🇹🇼 命令指示
- PEP 8 formatting violations
- Missing docstrings on public functions
- Print statements instead of logging
- Inefficient string operations
- Magic numbers without named constants
- Not using f-strings for formatting
- Unnecessary list creation

## Automated Checks Run
> 🇹🇼 命令指示

```bash
# Type checking
> 🇹🇼 命令指示
mypy .

# Linting and formatting
> 🇹🇼 命令指示
ruff check .
black --check .
isort --check-only .

# Security scanning
> 🇹🇼 命令指示
bandit -r .

# Dependency audit
> 🇹🇼 命令指示
pip-audit
safety check

# Testing
> 🇹🇼 命令指示
pytest --cov=app --cov-report=term-missing
```

## Example Usage
> 🇹🇼 命令指示

```text
User: /python-review

Agent:
# Python Code Review Report
> 🇹🇼 命令指示

## Files Reviewed
> 🇹🇼 命令指示
- app/routes/user.py (modified)
- app/services/auth.py (modified)

## Static Analysis Results
> 🇹🇼 命令指示
✓ ruff: No issues
✓ mypy: No errors
WARNING: black: 2 files need reformatting
✓ bandit: No security issues

## Issues Found
> 🇹🇼 命令指示

[CRITICAL] SQL Injection vulnerability
File: app/routes/user.py:42
Issue: User input directly interpolated into SQL query
```python
query = f"SELECT * FROM users WHERE id = {user_id}"  # Bad
```
Fix: Use parameterized query
```python
query = "SELECT * FROM users WHERE id = %s"  # Good
cursor.execute(query, (user_id,))
```

[HIGH] Mutable default argument
File: app/services/auth.py:18
Issue: Mutable default argument causes shared state
```python
def process_items(items=[]):  # Bad
    items.append("new")
    return items
```
Fix: Use None as default
```python
def process_items(items=None):  # Good
    if items is None:
        items = []
    items.append("new")
    return items
```

[MEDIUM] Missing type hints
File: app/services/auth.py:25
Issue: Public function without type annotations
```python
def get_user(user_id):  # Bad
    return db.find(user_id)
```
Fix: Add type hints
```python
def get_user(user_id: str) -> Optional[User]:  # Good
    return db.find(user_id)
```

[MEDIUM] Not using context manager
File: app/routes/user.py:55
Issue: File not closed on exception
```python
f = open("config.json")  # Bad
data = f.read()
f.close()
```
Fix: Use context manager
```python
with open("config.json") as f:  # Good
    data = f.read()
```

## Summary
> 🇹🇼 命令指示
- CRITICAL: 1
- HIGH: 1
- MEDIUM: 2

Recommendation: FAIL: Block merge until CRITICAL issue is fixed

## Formatting Required
> 🇹🇼 命令指示
Run: `black app/routes/user.py app/services/auth.py`
```

## Approval Criteria
> 🇹🇼 命令指示

| Status | Condition |
|--------|-----------|
| PASS: Approve | No CRITICAL or HIGH issues |
| WARNING: Warning | Only MEDIUM issues (merge with caution) |
| FAIL: Block | CRITICAL or HIGH issues found |

## Integration with Other Commands
> 🇹🇼 命令指示

- Use `/tdd` first to ensure tests pass
- Use `/code-review` for non-Python specific concerns
- Use `/python-review` before committing
- Use `/build-fix` if static analysis tools fail

## Framework-Specific Reviews
> 🇹🇼 命令指示

### Django Projects
> 🇹🇼 命令指示
The reviewer checks for:
- N+1 query issues (use `select_related` and `prefetch_related`)
- Missing migrations for model changes
- Raw SQL usage when ORM could work
- Missing `transaction.atomic()` for multi-step operations

### FastAPI Projects
> 🇹🇼 命令指示
The reviewer checks for:
- CORS misconfiguration
- Pydantic models for request validation
- Response models correctness
- Proper async/await usage
- Dependency injection patterns

### Flask Projects
> 🇹🇼 命令指示
The reviewer checks for:
- Context management (app context, request context)
- Proper error handling
- Blueprint organization
- Configuration management

## Related
> 🇹🇼 命令指示

- Agent: `agents/python-reviewer.md`
- Skills: `skills/python-patterns/`, `skills/python-testing/`

## Common Fixes
> 🇹🇼 命令指示

### Add Type Hints
> 🇹🇼 命令指示
```python
# Before
> 🇹🇼 命令指示
def calculate(x, y):
    return x + y

# After
> 🇹🇼 命令指示
from typing import Union

def calculate(x: Union[int, float], y: Union[int, float]) -> Union[int, float]:
    return x + y
```

### Use Context Managers
> 🇹🇼 命令指示
```python
# Before
> 🇹🇼 命令指示
f = open("file.txt")
data = f.read()
f.close()

# After
> 🇹🇼 命令指示
with open("file.txt") as f:
    data = f.read()
```

### Use List Comprehensions
> 🇹🇼 命令指示
```python
# Before
> 🇹🇼 命令指示
result = []
for item in items:
    if item.active:
        result.append(item.name)

# After
> 🇹🇼 命令指示
result = [item.name for item in items if item.active]
```

### Fix Mutable Defaults
> 🇹🇼 命令指示
```python
# Before
> 🇹🇼 命令指示
def append(value, items=[]):
    items.append(value)
    return items

# After
> 🇹🇼 命令指示
def append(value, items=None):
    if items is None:
        items = []
    items.append(value)
    return items
```

### Use f-strings (Python 3.6+)
> 🇹🇼 命令指示
```python
# Before
> 🇹🇼 命令指示
name = "Alice"
greeting = "Hello, " + name + "!"
greeting2 = "Hello, {}".format(name)

# After
> 🇹🇼 命令指示
greeting = f"Hello, {name}!"
```

### Fix String Concatenation in Loops
> 🇹🇼 命令指示
```python
# Before
> 🇹🇼 命令指示
result = ""
for item in items:
    result += str(item)

# After
> 🇹🇼 命令指示
result = "".join(str(item) for item in items)
```

## Python Version Compatibility
> 🇹🇼 命令指示

The reviewer notes when code uses features from newer Python versions:

| Feature | Minimum Python |
|---------|----------------|
| Type hints | 3.5+ |
| f-strings | 3.6+ |
| Walrus operator (`:=`) | 3.8+ |
| Position-only parameters | 3.8+ |
| Match statements | 3.10+ |
| Type unions (&#96;x &#124; None&#96;) | 3.10+ |

Ensure your project's `pyproject.toml` or `setup.py` specifies the correct minimum Python version.
