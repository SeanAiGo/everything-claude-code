---
paths:
  - "**/*.cpp"
  - "**/*.hpp"
  - "**/*.cc"
  - "**/*.hh"
  - "**/*.cxx"
  - "**/*.h"
  - "**/CMakeLists.txt"
---
# C++ Hooks
> 🇹🇼 規則說明與指示

> This file extends [common/hooks.md](../common/hooks.md) with C++ specific content.

## Build Hooks

Run these checks before committing C++ changes:

```bash
# Format check
> 🇹🇼 規則說明與指示
clang-format --dry-run --Werror src/*.cpp src/*.hpp

# Static analysis
> 🇹🇼 規則說明與指示
clang-tidy src/*.cpp -- -std=c++17

# Build
> 🇹🇼 規則說明與指示
cmake --build build

# Tests
> 🇹🇼 規則說明與指示
ctest --test-dir build --output-on-failure
```

## Recommended CI Pipeline

1. **clang-format** — formatting check
2. **clang-tidy** — static analysis
3. **cppcheck** — additional analysis
4. **cmake build** — compilation
5. **ctest** — test execution with sanitizers
