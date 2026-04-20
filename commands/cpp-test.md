---
description: 📝 【文件定位】這是一個命令（Command）定義檔案。此命令的功能：Enforce TDD workflow for C++. Write GoogleTest tests first, then implement. Verify coverage with gcov/lcov.
---

# C++ TDD Command
> 🇹🇼 命令指示

This command enforces test-driven development methodology for C++ code using GoogleTest/GoogleMock with CMake/CTest.

## What This Command Does
> 🇹🇼 命令指示

1. **Define Interfaces**: Scaffold class/function signatures first
2. **Write Tests**: Create comprehensive GoogleTest test cases (RED)
3. **Run Tests**: Verify tests fail for the right reason
4. **Implement Code**: Write minimal code to pass (GREEN)
5. **Refactor**: Improve while keeping tests green
6. **Check Coverage**: Ensure 80%+ coverage

## When to Use
> 🇹🇼 命令指示

Use `/cpp-test` when:
- Implementing new C++ functions or classes
- Adding test coverage to existing code
- Fixing bugs (write failing test first)
- Building critical business logic
- Learning TDD workflow in C++

## TDD Cycle
> 🇹🇼 命令指示

```
RED     → Write failing GoogleTest test
GREEN   → Implement minimal code to pass
REFACTOR → Improve code, tests stay green
REPEAT  → Next test case
```

## Example Session
> 🇹🇼 命令指示

````
User: /cpp-test I need a function to validate email addresses

Agent:
# TDD Session: Email Validator
> 🇹🇼 命令指示

## Step 1: Define Interface
> 🇹🇼 命令指示

```cpp
// validator/email.hpp
#pragma once
> 🇹🇼 命令指示
#include <string>
> 🇹🇼 命令指示
#include <expected>
> 🇹🇼 命令指示

enum class EmailError {
    Empty,
    InvalidFormat
};

std::expected<void, EmailError> validate_email(const std::string& email);
```

## Step 2: Write Tests (RED)
> 🇹🇼 命令指示

```cpp
// validator/email_test.cpp
#include <gtest/gtest.h>
> 🇹🇼 命令指示
#include "email.hpp"
> 🇹🇼 命令指示

TEST(ValidateEmail, AcceptsSimpleEmail) {
    auto result = validate_email("user@example.com");
    EXPECT_TRUE(result.has_value());
}

TEST(ValidateEmail, AcceptsSubdomain) {
    EXPECT_TRUE(validate_email("user@mail.example.com").has_value());
}

TEST(ValidateEmail, AcceptsPlus) {
    EXPECT_TRUE(validate_email("user+tag@example.com").has_value());
}

TEST(ValidateEmail, RejectsEmpty) {
    auto result = validate_email("");
    ASSERT_FALSE(result.has_value());
    EXPECT_EQ(result.error(), EmailError::Empty);
}

TEST(ValidateEmail, RejectsNoAtSign) {
    EXPECT_FALSE(validate_email("userexample.com").has_value());
}

TEST(ValidateEmail, RejectsNoDomain) {
    EXPECT_FALSE(validate_email("user@").has_value());
}

TEST(ValidateEmail, RejectsNoLocalPart) {
    EXPECT_FALSE(validate_email("@example.com").has_value());
}
```

## Step 3: Run Tests - Verify FAIL
> 🇹🇼 命令指示

```bash
$ cmake --build build && ctest --test-dir build --output-on-failure

1/1 Test #1: email_validator_test .....***Failed
    --- undefined reference to `validate_email`

FAIL
```

✓ Tests fail as expected (unimplemented).

## Step 4: Implement Minimal Code (GREEN)
> 🇹🇼 命令指示

```cpp
// validator/email.cpp
#include "email.hpp"
> 🇹🇼 命令指示
#include <regex>
> 🇹🇼 命令指示

std::expected<void, EmailError> validate_email(const std::string& email) {
    if (email.empty()) {
        return std::unexpected(EmailError::Empty);
    }
    static const std::regex pattern(R"([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,})");
    if (!std::regex_match(email, pattern)) {
        return std::unexpected(EmailError::InvalidFormat);
    }
    return {};
}
```

## Step 5: Run Tests - Verify PASS
> 🇹🇼 命令指示

```bash
$ cmake --build build && ctest --test-dir build --output-on-failure

1/1 Test #1: email_validator_test .....   Passed    0.01 sec

100% tests passed.
```

✓ All tests passing!

## Step 6: Check Coverage
> 🇹🇼 命令指示

```bash
$ cmake -DCMAKE_CXX_FLAGS="--coverage" -B build && cmake --build build
$ ctest --test-dir build
$ lcov --capture --directory build --output-file coverage.info
$ lcov --list coverage.info

validator/email.cpp     | 100%
```

✓ Coverage: 100%

## TDD Complete!
> 🇹🇼 命令指示
````

## Test Patterns
> 🇹🇼 命令指示

### Basic Tests
> 🇹🇼 命令指示
```cpp
TEST(SuiteName, TestName) {
    EXPECT_EQ(add(2, 3), 5);
    EXPECT_NE(result, nullptr);
    EXPECT_TRUE(is_valid);
    EXPECT_THROW(func(), std::invalid_argument);
}
```

### Fixtures
> 🇹🇼 命令指示
```cpp
class DatabaseTest : public ::testing::Test {
protected:
    void SetUp() override { db_ = create_test_db(); }
    void TearDown() override { db_.reset(); }
    std::unique_ptr<Database> db_;
};

TEST_F(DatabaseTest, InsertsRecord) {
    db_->insert("key", "value");
    EXPECT_EQ(db_->get("key"), "value");
}
```

### Parameterized Tests
> 🇹🇼 命令指示
```cpp
class PrimeTest : public ::testing::TestWithParam<std::pair<int, bool>> {};

TEST_P(PrimeTest, ChecksPrimality) {
    auto [input, expected] = GetParam();
    EXPECT_EQ(is_prime(input), expected);
}

INSTANTIATE_TEST_SUITE_P(Primes, PrimeTest, ::testing::Values(
    std::make_pair(2, true),
    std::make_pair(4, false),
    std::make_pair(7, true)
));
```

## Coverage Commands
> 🇹🇼 命令指示

```bash
# Build with coverage
> 🇹🇼 命令指示
cmake -DCMAKE_CXX_FLAGS="--coverage" -DCMAKE_EXE_LINKER_FLAGS="--coverage" -B build

# Run tests
> 🇹🇼 命令指示
cmake --build build && ctest --test-dir build

# Generate coverage report
> 🇹🇼 命令指示
lcov --capture --directory build --output-file coverage.info
lcov --remove coverage.info '/usr/*' --output-file coverage.info
genhtml coverage.info --output-directory coverage_html
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
- Use `EXPECT_*` (continues) over `ASSERT_*` (stops) when appropriate
- Test behavior, not implementation details
- Include edge cases (empty, null, max values, boundary conditions)

**DON'T:**
- Write implementation before tests
- Skip the RED phase
- Test private methods directly (test through public API)
- Use `sleep` in tests
- Ignore flaky tests

## Related Commands
> 🇹🇼 命令指示

- `/cpp-build` - Fix build errors
- `/cpp-review` - Review code after implementation
- `/verify` - Run full verification loop

## Related
> 🇹🇼 命令指示

- Skill: `skills/cpp-testing/`
- Skill: `skills/tdd-workflow/`
