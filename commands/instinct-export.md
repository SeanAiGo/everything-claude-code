---
name: instinct-export
description: 📝 【文件定位】這是一個命令（Command）定義檔案。此命令的功能：Export instincts from project/global scope to a file
command: /instinct-export
---

# Instinct Export Command
> 🇹🇼 命令指示

Exports instincts to a shareable format. Perfect for:
- Sharing with teammates
- Transferring to a new machine
- Contributing to project conventions

## Usage
> 🇹🇼 命令指示

```
/instinct-export                           # Export all personal instincts
/instinct-export --domain testing          # Export only testing instincts
/instinct-export --min-confidence 0.7      # Only export high-confidence instincts
/instinct-export --output team-instincts.yaml
/instinct-export --scope project --output project-instincts.yaml
```

## What to Do
> 🇹🇼 命令指示

1. Detect current project context
2. Load instincts by selected scope:
   - `project`: current project only
   - `global`: global only
   - `all`: project + global merged (default)
3. Apply filters (`--domain`, `--min-confidence`)
4. Write YAML-style export to file (or stdout if no output path provided)

## Output Format
> 🇹🇼 命令指示

Creates a YAML file:

```yaml
# Instincts Export
> 🇹🇼 命令指示
# Generated: 2025-01-22
> 🇹🇼 命令指示
# Source: personal
> 🇹🇼 命令指示
# Count: 12 instincts
> 🇹🇼 命令指示

---
id: prefer-functional-style
trigger: "when writing new functions"
confidence: 0.8
domain: code-style
source: session-observation
scope: project
project_id: a1b2c3d4e5f6
project_name: my-app
---

# Prefer Functional Style
> 🇹🇼 命令指示

## Action
> 🇹🇼 命令指示
Use functional patterns over classes.
```

## Flags
> 🇹🇼 命令指示

- `--domain <name>`: Export only specified domain
- `--min-confidence <n>`: Minimum confidence threshold
- `--output <file>`: Output file path (prints to stdout when omitted)
- `--scope <project|global|all>`: Export scope (default: `all`)
