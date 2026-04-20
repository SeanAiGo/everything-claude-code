---
name: instinct-status
description: 📝 【文件定位】這是一個命令（Command）定義檔案。此命令的功能：Show learned instincts (project + global) with confidence
command: true
---

# Instinct Status Command
> 🇹🇼 命令指示

Shows learned instincts for the current project plus global instincts, grouped by domain.

## Implementation
> 🇹🇼 命令指示

Run the instinct CLI using the plugin root path:

```bash
python3 "${CLAUDE_PLUGIN_ROOT}/skills/continuous-learning-v2/scripts/instinct-cli.py" status
```

Or if `CLAUDE_PLUGIN_ROOT` is not set (manual installation), use:

```bash
python3 ~/.claude/skills/continuous-learning-v2/scripts/instinct-cli.py status
```

## Usage
> 🇹🇼 命令指示

```
/instinct-status
```

## What to Do
> 🇹🇼 命令指示

1. Detect current project context (git remote/path hash)
2. Read project instincts from `~/.claude/homunculus/projects/<project-id>/instincts/`
3. Read global instincts from `~/.claude/homunculus/instincts/`
4. Merge with precedence rules (project overrides global when IDs collide)
5. Display grouped by domain with confidence bars and observation stats

## Output Format
> 🇹🇼 命令指示

```
============================================================
  INSTINCT STATUS - 12 total
============================================================

  Project: my-app (a1b2c3d4e5f6)
  Project instincts: 8
  Global instincts:  4

## PROJECT-SCOPED (my-app)
> 🇹🇼 命令指示
  ### WORKFLOW (3)
> 🇹🇼 命令指示
    ███████░░░  70%  grep-before-edit [project]
              trigger: when modifying code

## GLOBAL (apply to all projects)
> 🇹🇼 命令指示
  ### SECURITY (2)
> 🇹🇼 命令指示
    █████████░  85%  validate-user-input [global]
              trigger: when handling user input
```
