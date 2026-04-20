---
description: 📝 【文件定位】這是一個命令（Command）定義檔案。此命令的功能：Enforce TDD workflow for Kotlin. Write Kotest tests first, then implement. Verify 80%+ coverage with Kover.
---

# Kotlin TDD Command
> 🇹🇼 命令指示

This command enforces test-driven development methodology for Kotlin code using Kotest, MockK, and Kover.

## What This Command Does
> 🇹🇼 命令指示

1. **Define Types/Interfaces**: Scaffold function signatures first
2. **Write Kotest Tests**: Create comprehensive test specs (RED)
3. **Run Tests**: Verify tests fail for the right reason
4. **Implement Code**: Write minimal code to pass (GREEN)
5. **Refactor**: Improve while keeping tests green
6. **Check Coverage**: Ensure 80%+ coverage with Kover

## When to Use
> 🇹🇼 命令指示

Use `/kotlin-test` when:
- Implementing new Kotlin functions or classes
- Adding test coverage to existing Kotlin code
- Fixing bugs (write failing test first)
- Building critical business logic
- Learning TDD workflow in Kotlin

## TDD Cycle
> 🇹🇼 命令指示

```
RED     -> Write failing Kotest test
GREEN   -> Implement minimal code to pass
REFACTOR -> Improve code, tests stay green
REPEAT  -> Next test case
```

## Example Session
> 🇹🇼 命令指示

````text
User: /kotlin-test I need a function to validate user registration requests

Agent:
# TDD Session: Registration Validator
> 🇹🇼 命令指示

## Step 1: Define Interface
> 🇹🇼 命令指示

```kotlin
// validator/RegistrationValidator.kt
package com.example.validator

data class RegistrationRequest(
    val name: String,
    val email: String,
    val password: String,
)

sealed class ValidationResult {
    data object Valid : ValidationResult()
    data class Invalid(val errors: List<String>) : ValidationResult()
}

fun validateRegistration(request: RegistrationRequest): ValidationResult {
    TODO("not implemented")
}
```

## Step 2: Write Kotest Tests (RED)
> 🇹🇼 命令指示

```kotlin
// validator/RegistrationValidatorTest.kt
package com.example.validator

import io.kotest.core.spec.style.FunSpec
import io.kotest.matchers.shouldBe
import io.kotest.matchers.types.shouldBeInstanceOf

class RegistrationValidatorTest : FunSpec({
    test("valid registration returns Valid") {
        val request = RegistrationRequest(
            name = "Alice",
            email = "alice@example.com",
            password = "SecureP@ss1",
        )

        val result = validateRegistration(request)

        result.shouldBeInstanceOf<ValidationResult.Valid>()
    }

    test("blank name returns Invalid") {
        val request = RegistrationRequest(
            name = "",
            email = "alice@example.com",
            password = "SecureP@ss1",
        )

        val result = validateRegistration(request)

        val invalid = result.shouldBeInstanceOf<ValidationResult.Invalid>()
        invalid.errors shouldBe listOf("Name is required")
    }

    test("invalid email returns Invalid") {
        val request = RegistrationRequest(
            name = "Alice",
            email = "not-an-email",
            password = "SecureP@ss1",
        )

        val result = validateRegistration(request)

        val invalid = result.shouldBeInstanceOf<ValidationResult.Invalid>()
        invalid.errors shouldBe listOf("Invalid email format")
    }

    test("short password returns Invalid") {
        val request = RegistrationRequest(
            name = "Alice",
            email = "alice@example.com",
            password = "short",
        )

        val result = validateRegistration(request)

        val invalid = result.shouldBeInstanceOf<ValidationResult.Invalid>()
        invalid.errors shouldBe listOf("Password must be at least 8 characters")
    }

    test("multiple errors returns all errors") {
        val request = RegistrationRequest(
            name = "",
            email = "bad",
            password = "short",
        )

        val result = validateRegistration(request)

        val invalid = result.shouldBeInstanceOf<ValidationResult.Invalid>()
        invalid.errors.size shouldBe 3
    }
})
```

## Step 3: Run Tests - Verify FAIL
> 🇹🇼 命令指示

```bash
$ ./gradlew test

RegistrationValidatorTest > valid registration returns Valid FAILED
  kotlin.NotImplementedError: An operation is not implemented

FAILED (5 tests, 0 passed, 5 failed)
```

✓ Tests fail as expected (NotImplementedError).

## Step 4: Implement Minimal Code (GREEN)
> 🇹🇼 命令指示

```kotlin
// validator/RegistrationValidator.kt
package com.example.validator

private val EMAIL_REGEX = Regex("^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,}$")
private const val MIN_PASSWORD_LENGTH = 8

fun validateRegistration(request: RegistrationRequest): ValidationResult {
    val errors = buildList {
        if (request.name.isBlank()) add("Name is required")
        if (!EMAIL_REGEX.matches(request.email)) add("Invalid email format")
        if (request.password.length < MIN_PASSWORD_LENGTH) add("Password must be at least $MIN_PASSWORD_LENGTH characters")
    }

    return if (errors.isEmpty()) ValidationResult.Valid
    else ValidationResult.Invalid(errors)
}
```

## Step 5: Run Tests - Verify PASS
> 🇹🇼 命令指示

```bash
$ ./gradlew test

RegistrationValidatorTest > valid registration returns Valid PASSED
RegistrationValidatorTest > blank name returns Invalid PASSED
RegistrationValidatorTest > invalid email returns Invalid PASSED
RegistrationValidatorTest > short password returns Invalid PASSED
RegistrationValidatorTest > multiple errors returns all errors PASSED

PASSED (5 tests, 5 passed, 0 failed)
```

✓ All tests passing!

## Step 6: Check Coverage
> 🇹🇼 命令指示

```bash
$ ./gradlew koverHtmlReport

Coverage: 100.0% of statements
```

✓ Coverage: 100%

## TDD Complete!
> 🇹🇼 命令指示
````

## Test Patterns
> 🇹🇼 命令指示

### StringSpec (Simplest)
> 🇹🇼 命令指示

```kotlin
class CalculatorTest : StringSpec({
    "add two positive numbers" {
        Calculator.add(2, 3) shouldBe 5
    }
})
```

### BehaviorSpec (BDD)
> 🇹🇼 命令指示

```kotlin
class OrderServiceTest : BehaviorSpec({
    Given("a valid order") {
        When("placed") {
            Then("should be confirmed") { /* ... */ }
        }
    }
})
```

### Data-Driven Tests
> 🇹🇼 命令指示

```kotlin
class ParserTest : FunSpec({
    context("valid inputs") {
        withData("2026-01-15", "2026-12-31", "2000-01-01") { input ->
            parseDate(input).shouldNotBeNull()
        }
    }
})
```

### Coroutine Testing
> 🇹🇼 命令指示

```kotlin
class AsyncServiceTest : FunSpec({
    test("concurrent fetch completes") {
        runTest {
            val result = service.fetchAll()
            result.shouldNotBeEmpty()
        }
    }
})
```

## Coverage Commands
> 🇹🇼 命令指示

```bash
# Run tests with coverage
> 🇹🇼 命令指示
./gradlew koverHtmlReport

# Verify coverage thresholds
> 🇹🇼 命令指示
./gradlew koverVerify

# XML report for CI
> 🇹🇼 命令指示
./gradlew koverXmlReport

# Open HTML report
> 🇹🇼 命令指示
open build/reports/kover/html/index.html

# Run specific test class
> 🇹🇼 命令指示
./gradlew test --tests "com.example.UserServiceTest"

# Run with verbose output
> 🇹🇼 命令指示
./gradlew test --info
```

## Coverage Targets
> 🇹🇼 命令指示

| Code Type | Target |
|-----------|--------|
| Critical business logic | 100% |
| Public APIs | 90%+ |
| General code | 80%+ |
| Generated code | Exclude |

## TDD Best Practices
> 🇹🇼 命令指示

**DO:**
- Write test FIRST, before any implementation
- Run tests after each change
- Use Kotest matchers for expressive assertions
- Use MockK's `coEvery`/`coVerify` for suspend functions
- Test behavior, not implementation details
- Include edge cases (empty, null, max values)

**DON'T:**
- Write implementation before tests
- Skip the RED phase
- Test private functions directly
- Use `Thread.sleep()` in coroutine tests
- Ignore flaky tests

## Related Commands
> 🇹🇼 命令指示

- `/kotlin-build` - Fix build errors
- `/kotlin-review` - Review code after implementation
- `/verify` - Run full verification loop

## Related
> 🇹🇼 命令指示

- Skill: `skills/kotlin-testing/`
- Skill: `skills/tdd-workflow/`
