---
description: 📝 【文件定位】這是一個命令（Command）定義檔案。此命令的功能：Enable or disable hookify rules interactively
---

Interactively enable or disable existing hookify rules.

## Steps
> 🇹🇼 命令指示

1. Find all `.claude/hookify.*.local.md` files
2. Read the current state of each rule
3. Present the list with current enabled / disabled status
4. Ask which rules to toggle
5. Update the `enabled:` field in the selected rule files
6. Confirm the changes
