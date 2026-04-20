---
name: projects
description: 📝 【文件定位】這是一個命令（Command）定義檔案。此命令的功能：List known projects and their instinct statistics
command: true
---

# Projects Command
> 🇹🇼 命令指示

List project registry entries and per-project instinct/observation counts for continuous-learning-v2.

## Implementation
> 🇹🇼 命令指示

Run the instinct CLI using the plugin root path:

```bash
python3 "${CLAUDE_PLUGIN_ROOT}/skills/continuous-learning-v2/scripts/instinct-cli.py" projects
```

Or if `CLAUDE_PLUGIN_ROOT` is not set (manual installation):

```bash
python3 ~/.claude/skills/continuous-learning-v2/scripts/instinct-cli.py projects
```

## Usage
> 🇹🇼 命令指示

```bash
/projects
```

## What to Do
> 🇹🇼 命令指示

1. Read `~/.claude/homunculus/projects.json`
2. For each project, display:
   - Project name, id, root, remote
   - Personal and inherited instinct counts
   - Observation event count
   - Last seen timestamp
3. Also display global instinct totals
