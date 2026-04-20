---
description: 📝 【文件定位】這是一個命令（Command）定義檔案。此命令的功能：Get help with the hookify system
---

Display comprehensive hookify documentation.

## Hook System Overview
> 🇹🇼 命令指示

Hookify creates rule files that integrate with Claude Code's hook system to prevent unwanted behaviors.

### Event Types
> 🇹🇼 命令指示

- `bash`: triggers on Bash tool use and matches command patterns
- `file`: triggers on Write/Edit tool use and matches file paths
- `stop`: triggers when a session ends
- `prompt`: triggers on user message submission and matches input patterns
- `all`: triggers on all events

### Rule File Format
> 🇹🇼 命令指示

Files are stored as `.claude/hookify.{name}.local.md`:

```yaml
---
name: descriptive-name
enabled: true
event: bash|file|stop|prompt|all
action: block|warn
pattern: "regex pattern to match"
---
Message to display when rule triggers.
Supports multiple lines.
```

### Commands
> 🇹🇼 命令指示

- `/hookify [description]` creates new rules and auto-analyzes the conversation when no description is given
- `/hookify-list` lists configured rules
- `/hookify-configure` toggles rules on or off

### Pattern Tips
> 🇹🇼 命令指示

- use regex syntax
- for `bash`, match against the full command string
- for `file`, match against the file path
- test patterns before deploying
