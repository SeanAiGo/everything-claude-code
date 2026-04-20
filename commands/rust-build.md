---
description: 📝 【文件定位】這是一個命令（Command）定義檔案。此命令的功能：Fix Rust build errors, borrow checker issues, and dependency problems incrementally. Invokes the rust-build-resolver agent for minimal, surgical fixes.
---

# Rust Build and Fix
> 🇹🇼 命令指示

This command invokes the **rust-build-resolver** agent to incrementally fix Rust build errors with minimal changes.

## What This Command Does
> 🇹🇼 命令指示

1. **Run Diagnostics**: Execute `cargo check`, `cargo clippy`, `cargo fmt --check`
2. **Parse Errors**: Identify error codes and affected files
3. **Fix Incrementally**: One error at a time
4. **Verify Each Fix**: Re-run `cargo check` after each change
5. **Report Summary**: Show what was fixed and what remains

## When to Use
> 🇹🇼 命令指示

Use `/rust-build` when:
- `cargo build` or `cargo check` fails with errors
- `cargo clippy` reports warnings
- Borrow checker or lifetime errors block compilation
- Cargo dependency resolution fails
- After pulling changes that break the build

## Diagnostic Commands Run
> 🇹🇼 命令指示

```bash
# Primary build check
> 🇹🇼 命令指示
cargo check 2>&1

# Lints and suggestions
> 🇹🇼 命令指示
cargo clippy -- -D warnings 2>&1

# Formatting check
> 🇹🇼 命令指示
cargo fmt --check 2>&1

# Dependency issues
> 🇹🇼 命令指示
cargo tree --duplicates

# Security audit (if available)
> 🇹🇼 命令指示
if command -v cargo-audit >/dev/null; then cargo audit; else echo "cargo-audit not installed"; fi
```

## Example Session
> 🇹🇼 命令指示

````text
User: /rust-build

Agent:
# Rust Build Resolution
> 🇹🇼 命令指示

## Initial Diagnostics
> 🇹🇼 命令指示

```bash
$ cargo check
error[E0502]: cannot borrow `map` as mutable because it is also borrowed as immutable
  --> src/service/cache.rs:25:5
error[E0308]: mismatched types
  --> src/handler/api.rs:42:12
error[E0425]: cannot find value `db` in this scope
  --> src/handler/api.rs:58:9
```

Errors found: 3

## Fix 1: Borrow Checker Error
> 🇹🇼 命令指示

File: src/service/cache.rs:25
Error: E0502 — cannot borrow `map` as mutable because also borrowed as immutable
Cause: Immutable borrow still active during mutable insert

```rust
// Changed: restructured to end immutable borrow before mutable access
if !map.contains_key("key") {
    map.insert("key".into(), default);
}
```

```bash
$ cargo check
# 2 errors remaining
> 🇹🇼 命令指示
```

## Fix 2: Type Mismatch
> 🇹🇼 命令指示

File: src/handler/api.rs:42
Error: E0308 — mismatched types: expected `usize`, found `&str`

```rust
// Changed
let count = params.get("count");
// To
let count: usize = params.get("count")
    .and_then(|s| s.parse().ok())
    .unwrap_or(0);
```

```bash
$ cargo check
# 1 error remaining
> 🇹🇼 命令指示
```

## Fix 3: Unresolved Name
> 🇹🇼 命令指示

File: src/handler/api.rs:58
Error: E0425 — cannot find value `db` in this scope
Cause: Missing import

```rust
// Added
use crate::db;
```

```bash
$ cargo check
# Build successful!
> 🇹🇼 命令指示
```

## Final Verification
> 🇹🇼 命令指示

```bash
$ cargo clippy -- -D warnings
# No warnings
> 🇹🇼 命令指示

$ cargo test
running 6 tests
test service::cache::tests::test_insert ... ok
test service::cache::tests::test_get ... ok
test handler::api::tests::test_parse_count ... ok
test handler::api::tests::test_missing_count ... ok
test handler::api::tests::test_db_import ... ok
test handler::api::tests::test_response ... ok

test result: ok. 6 passed; 0 failed; 0 ignored
```

## Summary
> 🇹🇼 命令指示

| Metric | Count |
|--------|-------|
| Build errors fixed | 3 |
| Clippy warnings fixed | 0 |
| Files modified | 2 |
| Remaining issues | 0 |

Build Status: SUCCESS
````

## Common Errors Fixed
> 🇹🇼 命令指示

| Error | Typical Fix |
|-------|-------------|
| `cannot borrow as mutable` | Restructure to end immutable borrow first; clone only if justified |
| `does not live long enough` | Use owned type or add lifetime annotation |
| `cannot move out of` | Restructure to take ownership; clone only as last resort |
| `mismatched types` | Add `.into()`, `as`, or explicit conversion |
| `trait X not implemented` | Add `#[derive(Trait)]` or implement manually |
| `unresolved import` | Add to Cargo.toml or fix `use` path |
| `cannot find value` | Add import or fix path |

## Fix Strategy
> 🇹🇼 命令指示

1. **Build errors first** - Code must compile
2. **Clippy warnings second** - Fix suspicious constructs
3. **Formatting third** - `cargo fmt` compliance
4. **One fix at a time** - Verify each change
5. **Minimal changes** - Don't refactor, just fix

## Stop Conditions
> 🇹🇼 命令指示

The agent will stop and report if:
- Same error persists after 3 attempts
- Fix introduces more errors
- Requires architectural changes
- Borrow checker error requires redesigning data ownership

## Related Commands
> 🇹🇼 命令指示

- `/rust-test` - Run tests after build succeeds
- `/rust-review` - Review code quality
- `/verify` - Full verification loop

## Related
> 🇹🇼 命令指示

- Agent: `agents/rust-build-resolver.md`
- Skill: `skills/rust-patterns/`
