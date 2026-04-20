---
name: promote
description: 📝 【文件定位】這是一個命令（Command）定義檔案。此命令的功能：Promote project-scoped instincts to global scope
command: true
---

# Promote Command
> 🇹🇼 命令指示

Promote instincts from project scope to global scope in continuous-learning-v2.

## Implementation
> 🇹🇼 命令指示

Run the instinct CLI using the plugin root path:

```bash
python3 "${CLAUDE_PLUGIN_ROOT}/skills/continuous-learning-v2/scripts/instinct-cli.py" promote [instinct-id] [--force] [--dry-run]
```

Or if `CLAUDE_PLUGIN_ROOT` is not set (manual installation):

```bash
python3 ~/.claude/skills/continuous-learning-v2/scripts/instinct-cli.py promote [instinct-id] [--force] [--dry-run]
```

## Usage
> 🇹🇼 命令指示

```bash
/promote                      # Auto-detect promotion candidates
/promote --dry-run            # Preview auto-promotion candidates
/promote --force              # Promote all qualified candidates without prompt
/promote grep-before-edit     # Promote one specific instinct from current project
```

## What to Do
> 🇹🇼 命令指示

1. Detect current project
2. If `instinct-id` is provided, promote only that instinct (if present in current project)
3. Otherwise, find cross-project candidates that:
   - Appear in at least 2 projects
   - Meet confidence threshold
4. Write promoted instincts to `~/.claude/homunculus/instincts/personal/` with `scope: global`
