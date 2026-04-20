---
description: 📝 【文件定位】這是一個命令（Command）定義檔案。此命令的功能：Legacy slash-entry shim for the documentation-lookup skill. Prefer the skill directly.
---

# Docs Command (Legacy Shim)
> 🇹🇼 命令指示

Use this only if you still reach for `/docs`. The maintained workflow lives in `skills/documentation-lookup/SKILL.md`.

## Canonical Surface
> 🇹🇼 命令指示

- Prefer the `documentation-lookup` skill directly.
- Keep this file only as a compatibility entry point.

## Arguments
> 🇹🇼 命令指示

`$ARGUMENTS`

## Delegation
> 🇹🇼 命令指示

Apply the `documentation-lookup` skill.
- If the library or the question is missing, ask for the missing part.
- Use live documentation through Context7 instead of training data.
- Return only the current answer and the minimum code/example surface needed.
