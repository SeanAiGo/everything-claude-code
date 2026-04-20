---
description: 📝 【文件定位】這是一個命令（Command）定義檔案。此命令的功能：Comprehensive Go code review for idiomatic patterns, concurrency safety, error handling, and security. Invokes the go-reviewer agent.
---

# Go Code Review
> 🇹🇼 命令指示

This command invokes the **go-reviewer** agent for comprehensive Go-specific code review.

## What This Command Does
> 🇹🇼 命令指示

1. **Identify Go Changes**: Find modified `.go` files via `git diff`
2. **Run Static Analysis**: Execute `go vet`, `staticcheck`, and `golangci-lint`
3. **Security Scan**: Check for SQL injection, command injection, race conditions
4. **Concurrency Review**: Analyze goroutine safety, channel usage, mutex patterns
5. **Idiomatic Go Check**: Verify code follows Go conventions and best practices
6. **Generate Report**: Categorize issues by severity

## When to Use
> 🇹🇼 命令指示

Use `/go-review` when:
- After writing or modifying Go code
- Before committing Go changes
- Reviewing pull requests with Go code
- Onboarding to a new Go codebase
- Learning idiomatic Go patterns

## Review Categories
> 🇹🇼 命令指示

### CRITICAL (Must Fix)
> 🇹🇼 命令指示
- SQL/Command injection vulnerabilities
- Race conditions without synchronization
- Goroutine leaks
- Hardcoded credentials
- Unsafe pointer usage
- Ignored errors in critical paths

### HIGH (Should Fix)
> 🇹🇼 命令指示
- Missing error wrapping with context
- Panic instead of error returns
- Context not propagated
- Unbuffered channels causing deadlocks
- Interface not satisfied errors
- Missing mutex protection

### MEDIUM (Consider)
> 🇹🇼 命令指示
- Non-idiomatic code patterns
- Missing godoc comments on exports
- Inefficient string concatenation
- Slice not preallocated
- Table-driven tests not used

## Automated Checks Run
> 🇹🇼 命令指示

```bash
# Static analysis
> 🇹🇼 命令指示
go vet ./...

# Advanced checks (if installed)
> 🇹🇼 命令指示
staticcheck ./...
golangci-lint run

# Race detection
> 🇹🇼 命令指示
go build -race ./...

# Security vulnerabilities
> 🇹🇼 命令指示
govulncheck ./...
```

## Example Usage
> 🇹🇼 命令指示

```text
User: /go-review

Agent:
# Go Code Review Report
> 🇹🇼 命令指示

## Files Reviewed
> 🇹🇼 命令指示
- internal/handler/user.go (modified)
- internal/service/auth.go (modified)

## Static Analysis Results
> 🇹🇼 命令指示
✓ go vet: No issues
✓ staticcheck: No issues

## Issues Found
> 🇹🇼 命令指示

[CRITICAL] Race Condition
File: internal/service/auth.go:45
Issue: Shared map accessed without synchronization
```go
var cache = map[string]*Session{}  // Concurrent access!

func GetSession(id string) *Session {
    return cache[id]  // Race condition
}
```
Fix: Use sync.RWMutex or sync.Map
```go
var (
    cache   = map[string]*Session{}
    cacheMu sync.RWMutex
)

func GetSession(id string) *Session {
    cacheMu.RLock()
    defer cacheMu.RUnlock()
    return cache[id]
}
```

[HIGH] Missing Error Context
File: internal/handler/user.go:28
Issue: Error returned without context
```go
return err  // No context
```
Fix: Wrap with context
```go
return fmt.Errorf("get user %s: %w", userID, err)
```

## Summary
> 🇹🇼 命令指示
- CRITICAL: 1
- HIGH: 1
- MEDIUM: 0

Recommendation: FAIL: Block merge until CRITICAL issue is fixed
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

- Use `/go-test` first to ensure tests pass
- Use `/go-build` if build errors occur
- Use `/go-review` before committing
- Use `/code-review` for non-Go specific concerns

## Related
> 🇹🇼 命令指示

- Agent: `agents/go-reviewer.md`
- Skills: `skills/golang-patterns/`, `skills/golang-testing/`
