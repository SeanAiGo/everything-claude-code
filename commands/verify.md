---
description: 📝 【文件定位】這是一個命令（Command）定義檔案。此命令的功能：Legacy slash-entry shim for the verification-loop skill. Prefer the skill directly.
---

# Verification Command (Legacy Shim)
> 🇹🇼 命令指示

Use this only if you still invoke `/verify`. The maintained workflow lives in `skills/verification-loop/SKILL.md`.

## Canonical Surface
> 🇹🇼 命令指示

- Prefer the `verification-loop` skill directly.
- Keep this file only as a compatibility entry point.

## Arguments
> 🇹🇼 命令指示

`$ARGUMENTS`

## Delegation
> 🇹🇼 命令指示

Apply the `verification-loop` skill.
- Choose the right verification depth for the user's requested mode.
- Run build, types, lint, tests, security/log checks, and diff review in the right order for the current repo.
- Report only the verdicts and blockers instead of maintaining a second verification checklist here.
