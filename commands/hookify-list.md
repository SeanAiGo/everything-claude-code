---
description: 📝 【文件定位】這是一個命令（Command）定義檔案。此命令的功能：List all configured hookify rules
---

Find and display all hookify rules in a formatted table.

## Steps
> 🇹🇼 命令指示

1. Find all `.claude/hookify.*.local.md` files
2. Read each file's frontmatter:
   - `name`
   - `enabled`
   - `event`
   - `action`
   - `pattern`
3. Display them as a table:

| Rule | Enabled | Event | Pattern | File |
|------|---------|-------|---------|------|

4. Show the rule count and remind the user that `/hookify-configure` can change state later.
