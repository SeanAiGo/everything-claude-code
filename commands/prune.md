---
name: prune
description: 📝 【文件定位】這是一個命令（Command）定義檔案。此命令的功能：Delete pending instincts older than 30 days that were never promoted
command: true
---

# Prune Pending Instincts
> 🇹🇼 命令指示

Remove expired pending instincts that were auto-generated but never reviewed or promoted.

## Implementation
> 🇹🇼 命令指示

Run the instinct CLI using the plugin root path:

```bash
python3 "${CLAUDE_PLUGIN_ROOT}/skills/continuous-learning-v2/scripts/instinct-cli.py" prune
```

Or if `CLAUDE_PLUGIN_ROOT` is not set (manual installation):

```bash
python3 ~/.claude/skills/continuous-learning-v2/scripts/instinct-cli.py prune
```

## Usage
> 🇹🇼 命令指示

```
/prune                    # Delete instincts older than 30 days
/prune --max-age 60      # Custom age threshold (days)
/prune --dry-run         # Preview without deleting
```
