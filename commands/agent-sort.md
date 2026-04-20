---
description: 📝 【文件定位】這是一個命令（Command）定義檔案。此命令的功能：Legacy slash-entry shim for the agent-sort skill. Prefer the skill directly.
---

# Agent Sort (Legacy Shim)
> 🇹🇼 命令指示

Use this only if you still invoke `/agent-sort`. The maintained workflow lives in `skills/agent-sort/SKILL.md`.

## Canonical Surface
> 🇹🇼 命令指示

- Prefer the `agent-sort` skill directly.
- Keep this file only as a compatibility entry point.

## Arguments
> 🇹🇼 命令指示

`$ARGUMENTS`

## Delegation
> 🇹🇼 命令指示

Apply the `agent-sort` skill.
- Classify ECC surfaces with concrete repo evidence.
- Keep the result to DAILY vs LIBRARY.
- If an install change is needed afterward, hand off to `configure-ecc` instead of re-implementing install logic here.
