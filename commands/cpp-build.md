---
description: 📝 【文件定位】這是一個命令（Command）定義檔案。此命令的功能：Fix C++ build errors, CMake issues, and linker problems incrementally. Invokes the cpp-build-resolver agent for minimal, surgical fixes.
---

# C++ Build and Fix
> 🇹🇼 命令指示

This command invokes the **cpp-build-resolver** agent to incrementally fix C++ build errors with minimal changes.

## What This Command Does
> 🇹🇼 命令指示

1. **Run Diagnostics**: Execute `cmake --build`, `clang-tidy`, `cppcheck`
2. **Parse Errors**: Group by file and sort by severity
3. **Fix Incrementally**: One error at a time
4. **Verify Each Fix**: Re-run build after each change
5. **Report Summary**: Show what was fixed and what remains

## When to Use
> 🇹🇼 命令指示

Use `/cpp-build` when:
- `cmake --build build` fails with errors
- Linker errors (undefined references, multiple definitions)
- Template instantiation failures
- Include/dependency issues
- After pulling changes that break the build

## Diagnostic Commands Run
> 🇹🇼 命令指示

```bash
# CMake configure
> 🇹🇼 命令指示
cmake -B build -S .

# Build
> 🇹🇼 命令指示
cmake --build build 2>&1 | head -100

# Static analysis (if available)
> 🇹🇼 命令指示
clang-tidy src/*.cpp -- -std=c++17
cppcheck --enable=all src/
```

## Example Session
> 🇹🇼 命令指示

```text
User: /cpp-build

Agent:
# C++ Build Resolution
> 🇹🇼 命令指示

## Initial Diagnostics
> 🇹🇼 命令指示

```bash
$ cmake --build build
src/service/user.cpp:25:15: error: use of undeclared identifier 'UserRepository'
src/handler/api.cpp:42:9: error: no matching function for call to 'process'
src/handler/api.cpp:58:1: error: non-void function does not return a value
```

Errors found: 3

## Fix 1: Undeclared Identifier
> 🇹🇼 命令指示

File: src/service/user.cpp:25
Error: use of undeclared identifier 'UserRepository'
Cause: Missing include

```cpp
// Added include
#include "repository/user_repository.hpp"
> 🇹🇼 命令指示
```

```bash
$ cmake --build build
# 2 errors remaining
> 🇹🇼 命令指示
```

## Fix 2: No Matching Function
> 🇹🇼 命令指示

File: src/handler/api.cpp:42
Error: no matching function for call to 'process'

```cpp
// Changed
process(params.get("count"));
// To
process(std::stoi(params.get("count")));
```

```bash
$ cmake --build build
# 1 error remaining
> 🇹🇼 命令指示
```

## Fix 3: Missing Return
> 🇹🇼 命令指示

File: src/handler/api.cpp:58
Error: non-void function does not return a value

```cpp
std::optional<User> getUser(const std::string& id) {
    if (id.empty()) {
        return std::nullopt;
    }
    auto user = findUser(id);
    // Added missing return
    return user;
}
```

```bash
$ cmake --build build
# Build successful!
> 🇹🇼 命令指示
```

## Final Verification
> 🇹🇼 命令指示

```bash
$ ctest --test-dir build --output-on-failure
Test project build
    1/5 Test #1: unit_tests ........   Passed    0.02 sec
    2/5 Test #2: integration_tests    Passed    0.15 sec
All tests passed.
```

## Summary
> 🇹🇼 命令指示

| Metric | Count |
|--------|-------|
| Build errors fixed | 3 |
| Linker errors fixed | 0 |
| Files modified | 2 |
| Remaining issues | 0 |

Build Status: PASS: SUCCESS
```

## Common Errors Fixed
> 🇹🇼 命令指示

| Error | Typical Fix |
|-------|-------------|
| `undeclared identifier` | Add `#include` or fix typo |
| `no matching function` | Fix argument types or add overload |
| `undefined reference` | Link library or add implementation |
| `multiple definition` | Use `inline` or move to .cpp |
| `incomplete type` | Replace forward decl with `#include` |
| `no member named X` | Fix member name or include |
| `cannot convert X to Y` | Add appropriate cast |
| `CMake Error` | Fix CMakeLists.txt configuration |

## Fix Strategy
> 🇹🇼 命令指示

1. **Compilation errors first** - Code must compile
2. **Linker errors second** - Resolve undefined references
3. **Warnings third** - Fix with `-Wall -Wextra`
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

- `/cpp-test` - Run tests after build succeeds
- `/cpp-review` - Review code quality
- `/verify` - Full verification loop

## Related
> 🇹🇼 命令指示

- Agent: `agents/cpp-build-resolver.md`
- Skill: `skills/cpp-coding-standards/`
