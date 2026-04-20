---
description: 📝 【文件定位】這是一個命令（Command）定義檔案。此命令的功能：Comprehensive Kotlin code review for idiomatic patterns, null safety, coroutine safety, and security. Invokes the kotlin-reviewer agent.
---

# Kotlin Code Review
> 🇹🇼 命令指示

This command invokes the **kotlin-reviewer** agent for comprehensive Kotlin-specific code review.

## What This Command Does
> 🇹🇼 命令指示

1. **Identify Kotlin Changes**: Find modified `.kt` and `.kts` files via `git diff`
2. **Run Build & Static Analysis**: Execute `./gradlew build`, `detekt`, `ktlintCheck`
3. **Security Scan**: Check for SQL injection, command injection, hardcoded secrets
4. **Null Safety Review**: Analyze `!!` usage, platform type handling, unsafe casts
5. **Coroutine Review**: Check structured concurrency, dispatcher usage, cancellation
6. **Generate Report**: Categorize issues by severity

## When to Use
> 🇹🇼 命令指示

Use `/kotlin-review` when:
- After writing or modifying Kotlin code
- Before committing Kotlin changes
- Reviewing pull requests with Kotlin code
- Onboarding to a new Kotlin codebase
- Learning idiomatic Kotlin patterns

## Review Categories
> 🇹🇼 命令指示

### CRITICAL (Must Fix)
> 🇹🇼 命令指示
- SQL/Command injection vulnerabilities
- Force-unwrap `!!` without justification
- Platform type null safety violations
- GlobalScope usage (structured concurrency violation)
- Hardcoded credentials
- Unsafe deserialization

### HIGH (Should Fix)
> 🇹🇼 命令指示
- Mutable state where immutable suffices
- Blocking calls inside coroutine context
- Missing cancellation checks in long loops
- Non-exhaustive `when` on sealed types
- Large functions (>50 lines)
- Deep nesting (>4 levels)

### MEDIUM (Consider)
> 🇹🇼 命令指示
- Non-idiomatic Kotlin (Java-style patterns)
- Missing trailing commas
- Scope function misuse or nesting
- Missing sequence for large collection chains
- Redundant explicit types

## Automated Checks Run
> 🇹🇼 命令指示

```bash
# Build check
> 🇹🇼 命令指示
./gradlew build

# Static analysis
> 🇹🇼 命令指示
./gradlew detekt

# Formatting check
> 🇹🇼 命令指示
./gradlew ktlintCheck

# Tests
> 🇹🇼 命令指示
./gradlew test
```

## Example Usage
> 🇹🇼 命令指示

````text
User: /kotlin-review

Agent:
# Kotlin Code Review Report
> 🇹🇼 命令指示

## Files Reviewed
> 🇹🇼 命令指示
- src/main/kotlin/com/example/service/UserService.kt (modified)
- src/main/kotlin/com/example/routes/UserRoutes.kt (modified)

## Static Analysis Results
> 🇹🇼 命令指示
✓ Build: Successful
✓ detekt: No issues
WARNING: ktlint: 2 formatting warnings

## Issues Found
> 🇹🇼 命令指示

[CRITICAL] Force-Unwrap Null Safety
File: src/main/kotlin/com/example/service/UserService.kt:28
Issue: Using !! on nullable repository result
```kotlin
val user = repository.findById(id)!!  // NPE risk
```
Fix: Use safe call with error handling
```kotlin
val user = repository.findById(id)
    ?: throw UserNotFoundException("User $id not found")
```

[HIGH] GlobalScope Usage
File: src/main/kotlin/com/example/routes/UserRoutes.kt:45
Issue: Using GlobalScope breaks structured concurrency
```kotlin
GlobalScope.launch {
    notificationService.sendWelcome(user)
}
```
Fix: Use the call's coroutine scope
```kotlin
launch {
    notificationService.sendWelcome(user)
}
```

## Summary
> 🇹🇼 命令指示
- CRITICAL: 1
- HIGH: 1
- MEDIUM: 0

Recommendation: FAIL: Block merge until CRITICAL issue is fixed
````

## Approval Criteria
> 🇹🇼 命令指示

| Status | Condition |
|--------|-----------|
| PASS: Approve | No CRITICAL or HIGH issues |
| WARNING: Warning | Only MEDIUM issues (merge with caution) |
| FAIL: Block | CRITICAL or HIGH issues found |

## Integration with Other Commands
> 🇹🇼 命令指示

- Use `/kotlin-test` first to ensure tests pass
- Use `/kotlin-build` if build errors occur
- Use `/kotlin-review` before committing
- Use `/code-review` for non-Kotlin-specific concerns

## Related
> 🇹🇼 命令指示

- Agent: `agents/kotlin-reviewer.md`
- Skills: `skills/kotlin-patterns/`, `skills/kotlin-testing/`
