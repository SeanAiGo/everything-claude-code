---
description: 📝 【文件定位】這是一個命令（Command）定義檔案。此命令的功能：Legacy slash-entry shim for the prompt-optimizer skill. Prefer the skill directly.
---

# Prompt Optimize (Legacy Shim)
> 🇹🇼 命令指示

Use this only if you still invoke `/prompt-optimize`. The maintained workflow lives in `skills/prompt-optimizer/SKILL.md`.

## Canonical Surface
> 🇹🇼 命令指示

- Prefer the `prompt-optimizer` skill directly.
- Keep this file only as a compatibility entry point.

## Arguments
> 🇹🇼 命令指示

`$ARGUMENTS`

## Delegation
> 🇹🇼 命令指示

Apply the `prompt-optimizer` skill.
- Keep it advisory-only: optimize the prompt, do not execute the task.
- Return the recommended ECC components plus a ready-to-run prompt.
- If the user actually wants direct execution, say so and tell them to make a normal task request instead of staying inside the shim.
