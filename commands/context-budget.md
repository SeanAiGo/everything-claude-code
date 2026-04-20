---
description: 📝 【文件定位】這是一個命令（Command）定義檔案。此命令的功能：Legacy slash-entry shim for the context-budget skill. Prefer the skill directly.
---

# Context Budget Optimizer (Legacy Shim)
> 🇹🇼 命令指示

Use this only if you still invoke `/context-budget`. The maintained workflow lives in `skills/context-budget/SKILL.md`.

## Canonical Surface
> 🇹🇼 命令指示

- Prefer the `context-budget` skill directly.
- Keep this file only as a compatibility entry point.

## Arguments
> 🇹🇼 命令指示

$ARGUMENTS

## Delegation
> 🇹🇼 命令指示

Apply the `context-budget` skill.
- Pass through `--verbose` if the user supplied it.
- Assume a 200K context window unless the user specified otherwise.
- Return the skill's inventory, issue detection, and prioritized savings report without re-implementing the scan here.
