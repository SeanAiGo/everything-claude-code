---
description: 📝 【文件定位】這是一個命令（Command）定義檔案。此命令的功能：Fix Go build errors, go vet warnings, and linter issues incrementally. Invokes the go-build-resolver agent for minimal, surgical fixes.
---

# Go Build and Fix
> 🇹🇼 命令指示

This command invokes the **go-build-resolver** agent to incrementally fix Go build errors with minimal changes.

## What This Command Does
> 🇹🇼 命令指示

1. **Run Diagnostics**: Execute `go build`, `go vet`, `staticcheck`
2. **Parse Errors**: Group by file and sort by severity
3. **Fix Incrementally**: One error at a time
4. **Verify Each Fix**: Re-run build after each change
5. **Report Summary**: Show what was fixed and what remains

## When to Use
> 🇹🇼 命令指示

Use `/go-build` when:
- `go build ./...` fails with errors
- `go vet ./...` reports issues
- `golangci-lint run` shows warnings
- Module dependencies are broken
- After pulling changes that break the build

## Diagnostic Commands Run
> 🇹🇼 命令指示

```bash
# Primary build check
> 🇹🇼 命令指示
go build ./...

# Static analysis
> 🇹🇼 命令指示
go vet ./...

# Extended linting (if available)
> 🇹🇼 命令指示
staticcheck ./...
golangci-lint run

# Module issues
> 🇹🇼 命令指示
go mod verify
go mod tidy -v
```

## Example Session
> 🇹🇼 命令指示

```text
User: /go-build

Agent:
# Go Build Resolution
> 🇹🇼 命令指示

## Initial Diagnostics
> 🇹🇼 命令指示

```bash
$ go build ./...
internal/service/user.go:25:15: undefined: UserRepository
internal/handler/api.go:42:9: cannot use x (type string) as type int
internal/handler/api.go:58:2: missing return at end of function
```

Errors found: 3

## Fix 1: Undefined Identifier
> 🇹🇼 命令指示

File: internal/service/user.go:25
Error: undefined: UserRepository
Cause: Missing import

```go
// Added import
import "project/internal/repository"

// Changed
var repo UserRepository
// To
var repo repository.UserRepository
```

```bash
$ go build ./...
# 2 errors remaining
> 🇹🇼 命令指示
```

## Fix 2: Type Mismatch
> 🇹🇼 命令指示

File: internal/handler/api.go:42
Error: cannot use x (type string) as type int

```go
// Changed
count := params.Get("count")
// To
countStr := params.Get("count")
count, _ := strconv.Atoi(countStr)
```

```bash
$ go build ./...
# 1 error remaining
> 🇹🇼 命令指示
```

## Fix 3: Missing Return
> 🇹🇼 命令指示

File: internal/handler/api.go:58
Error: missing return at end of function

```go
func GetUser(id string) (*User, error) {
    if id == "" {
        return nil, ErrInvalidID
    }
    user := findUser(id)
    // Added missing return
    return user, nil
}
```

```bash
$ go build ./...
# Build successful!
> 🇹🇼 命令指示
```

## Final Verification
> 🇹🇼 命令指示

```bash
$ go vet ./...
# No issues
> 🇹🇼 命令指示

$ go test ./...
ok      project/internal/service   0.015s
ok      project/internal/handler   0.023s
```

## Summary
> 🇹🇼 命令指示

| Metric | Count |
|--------|-------|
| Build errors fixed | 3 |
| Vet warnings fixed | 0 |
| Files modified | 2 |
| Remaining issues | 0 |

Build Status: PASS: SUCCESS
```

## Common Errors Fixed
> 🇹🇼 命令指示

| Error | Typical Fix |
|-------|-------------|
| `undefined: X` | Add import or fix typo |
| `cannot use X as Y` | Type conversion or fix assignment |
| `missing return` | Add return statement |
| `X does not implement Y` | Add missing method |
| `import cycle` | Restructure packages |
| `declared but not used` | Remove or use variable |
| `cannot find package` | `go get` or `go mod tidy` |

## Fix Strategy
> 🇹🇼 命令指示

1. **Build errors first** - Code must compile
2. **Vet warnings second** - Fix suspicious constructs
3. **Lint warnings third** - Style and best practices
4. **One fix at a time** - Verify each change
5. **Minimal changes** - Don't refactor, just fix

## Stop Conditions
> 🇹🇼 命令指示

The agent will stop and report if:
- Same error persists after 3 attempts
- Fix introduces more errors
- Requires architectural changes
- Missing external dependencies

## Related Commands
> 🇹🇼 命令指示

- `/go-test` - Run tests after build succeeds
- `/go-review` - Review code quality
- `/verify` - Full verification loop

## Related
> 🇹🇼 命令指示

- Agent: `agents/go-build-resolver.md`
- Skill: `skills/golang-patterns/`
