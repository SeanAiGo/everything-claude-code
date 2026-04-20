---
description: 📝 【文件定位】這是一個命令（Command）定義檔案。此命令的功能：Enforce TDD workflow for Rust. Write tests first, then implement. Verify 80%+ coverage with cargo-llvm-cov.
---

# Rust TDD Command
> 🇹🇼 命令指示

This command enforces test-driven development methodology for Rust code using `#[test]`, rstest, proptest, and mockall.

## What This Command Does
> 🇹🇼 命令指示

1. **Define Types/Traits**: Scaffold function signatures with `todo!()`
2. **Write Tests**: Create comprehensive test module (RED)
3. **Run Tests**: Verify tests fail for the right reason
4. **Implement Code**: Write minimal code to pass (GREEN)
5. **Refactor**: Improve while keeping tests green
6. **Check Coverage**: Ensure 80%+ coverage with cargo-llvm-cov

## When to Use
> 🇹🇼 命令指示

Use `/rust-test` when:
- Implementing new Rust functions, methods, or traits
- Adding test coverage to existing Rust code
- Fixing bugs (write failing test first)
- Building critical business logic
- Learning TDD workflow in Rust

## TDD Cycle
> 🇹🇼 命令指示

```
RED     -> Write failing test first
GREEN   -> Implement minimal code to pass
REFACTOR -> Improve code, tests stay green
REPEAT  -> Next test case
```

## Example Session
> 🇹🇼 命令指示

````text
User: /rust-test I need a function to validate user registration

Agent:
# TDD Session: Registration Validator
> 🇹🇼 命令指示

## Step 1: Define Interface
> 🇹🇼 命令指示

```rust
// src/validator.rs
pub struct RegistrationRequest {
    pub name: String,
    pub email: String,
    pub password: String,
}

pub enum ValidationResult {
    Valid,
    Invalid(Vec<String>),
}

pub fn validate_registration(request: &RegistrationRequest) -> ValidationResult {
    todo!()
}
```

## Step 2: Write Tests (RED)
> 🇹🇼 命令指示

```rust
#[cfg(test)]
> 🇹🇼 命令指示
mod tests {
    use super::*;

    #[test]
> 🇹🇼 命令指示
    fn valid_registration_returns_valid() {
        let request = RegistrationRequest {
            name: "Alice".into(),
            email: "alice@example.com".into(),
            password: "SecureP@ss1".into(),
        };
        assert!(matches!(validate_registration(&request), ValidationResult::Valid));
    }

    #[test]
> 🇹🇼 命令指示
    fn blank_name_returns_invalid() {
        let request = RegistrationRequest {
            name: "".into(),
            email: "alice@example.com".into(),
            password: "SecureP@ss1".into(),
        };
        match validate_registration(&request) {
            ValidationResult::Invalid(errors) => {
                assert!(errors.contains(&"Name is required".to_string()));
            }
            ValidationResult::Valid => panic!("expected Invalid"),
        }
    }

    #[test]
> 🇹🇼 命令指示
    fn invalid_email_returns_invalid() {
        let request = RegistrationRequest {
            name: "Alice".into(),
            email: "not-an-email".into(),
            password: "SecureP@ss1".into(),
        };
        assert!(matches!(
            validate_registration(&request),
            ValidationResult::Invalid(_)
        ));
    }

    #[test]
> 🇹🇼 命令指示
    fn short_password_returns_invalid() {
        let request = RegistrationRequest {
            name: "Alice".into(),
            email: "alice@example.com".into(),
            password: "short".into(),
        };
        assert!(matches!(
            validate_registration(&request),
            ValidationResult::Invalid(_)
        ));
    }
}
```

## Step 3: Run Tests — Verify FAIL
> 🇹🇼 命令指示

```bash
$ cargo test
running 4 tests
test tests::valid_registration_returns_valid ... FAILED (not yet implemented)
test tests::blank_name_returns_invalid ... FAILED
test tests::invalid_email_returns_invalid ... FAILED
test tests::short_password_returns_invalid ... FAILED
```

Tests fail as expected (todo! panic).

## Step 4: Implement Minimal Code (GREEN)
> 🇹🇼 命令指示

```rust
pub fn validate_registration(request: &RegistrationRequest) -> ValidationResult {
    let mut errors = Vec::new();

    if request.name.trim().is_empty() {
        errors.push("Name is required".into());
    }
    if !request.email.contains('@') {
        errors.push("Invalid email format".into());
    }
    if request.password.len() < 8 {
        errors.push("Password must be at least 8 characters".into());
    }

    if errors.is_empty() {
        ValidationResult::Valid
    } else {
        ValidationResult::Invalid(errors)
    }
}
```

## Step 5: Run Tests — Verify PASS
> 🇹🇼 命令指示

```bash
$ cargo test
running 4 tests
test tests::valid_registration_returns_valid ... ok
test tests::blank_name_returns_invalid ... ok
test tests::invalid_email_returns_invalid ... ok
test tests::short_password_returns_invalid ... ok

test result: ok. 4 passed; 0 failed
```

All tests passing!

## Step 6: Check Coverage
> 🇹🇼 命令指示

```bash
$ cargo llvm-cov
Coverage: 100.0% of lines
```

Coverage: 100%

## TDD Complete!
> 🇹🇼 命令指示
````

## Test Patterns
> 🇹🇼 命令指示

### Unit Tests
> 🇹🇼 命令指示

```rust
#[cfg(test)]
> 🇹🇼 命令指示
mod tests {
    use super::*;

    #[test]
> 🇹🇼 命令指示
    fn adds_two_numbers() {
        assert_eq!(add(2, 3), 5);
    }

    #[test]
> 🇹🇼 命令指示
    fn handles_error() -> Result<(), Box<dyn std::error::Error>> {
        let result = parse_config(r#"port = 8080"#)?;
        assert_eq!(result.port, 8080);
        Ok(())
    }
}
```

### Parameterized Tests with rstest
> 🇹🇼 命令指示

```rust
use rstest::{rstest, fixture};

#[rstest]
> 🇹🇼 命令指示
#[case("hello", 5)]
> 🇹🇼 命令指示
#[case("", 0)]
> 🇹🇼 命令指示
#[case("rust", 4)]
> 🇹🇼 命令指示
fn test_string_length(#[case] input: &str, #[case] expected: usize) {
    assert_eq!(input.len(), expected);
}
```

### Async Tests
> 🇹🇼 命令指示

```rust
#[tokio::test]
> 🇹🇼 命令指示
async fn fetches_data_successfully() {
    let client = TestClient::new().await;
    let result = client.get("/data").await;
    assert!(result.is_ok());
}
```

### Property-Based Tests
> 🇹🇼 命令指示

```rust
use proptest::prelude::*;

proptest! {
    #[test]
> 🇹🇼 命令指示
    fn encode_decode_roundtrip(input in ".*") {
        let encoded = encode(&input);
        let decoded = decode(&encoded).unwrap();
        assert_eq!(input, decoded);
    }
}
```

## Coverage Commands
> 🇹🇼 命令指示

```bash
# Summary report
> 🇹🇼 命令指示
cargo llvm-cov

# HTML report
> 🇹🇼 命令指示
cargo llvm-cov --html

# Fail if below threshold
> 🇹🇼 命令指示
cargo llvm-cov --fail-under-lines 80

# Run specific test
> 🇹🇼 命令指示
cargo test test_name

# Run with output
> 🇹🇼 命令指示
cargo test -- --nocapture

# Run without stopping on first failure
> 🇹🇼 命令指示
cargo test --no-fail-fast
```

## Coverage Targets
> 🇹🇼 命令指示

| Code Type | Target |
|-----------|--------|
| Critical business logic | 100% |
| Public API | 90%+ |
| General code | 80%+ |
| Generated / FFI bindings | Exclude |

## TDD Best Practices
> 🇹🇼 命令指示

**DO:**
- Write test FIRST, before any implementation
- Run tests after each change
- Use `assert_eq!` over `assert!` for better error messages
- Use `?` in tests that return `Result` for cleaner output
- Test behavior, not implementation
- Include edge cases (empty, boundary, error paths)

**DON'T:**
- Write implementation before tests
- Skip the RED phase
- Use `#[should_panic]` when `Result::is_err()` works
- Use `sleep()` in tests — use channels or `tokio::time::pause()`
- Mock everything — prefer integration tests when feasible

## Related Commands
> 🇹🇼 命令指示

- `/rust-build` - Fix build errors
- `/rust-review` - Review code after implementation
- `/verify` - Run full verification loop

## Related
> 🇹🇼 命令指示

- Skill: `skills/rust-testing/`
- Skill: `skills/rust-patterns/`
