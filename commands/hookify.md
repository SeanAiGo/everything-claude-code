---
description: 📝 【文件定位】這是一個命令（Command）定義檔案。此命令的功能：Create hooks to prevent unwanted behaviors from conversation analysis or explicit instructions
---

Create hook rules to prevent unwanted Claude Code behaviors by analyzing conversation patterns or explicit user instructions.

## Usage
> 🇹🇼 命令指示

`/hookify [description of behavior to prevent]`

If no arguments are provided, analyze the current conversation to find behaviors worth preventing.

## Workflow
> 🇹🇼 命令指示

### Step 1: Gather Behavior Info
> 🇹🇼 命令指示

- With arguments: parse the user's description of the unwanted behavior
- Without arguments: use the `conversation-analyzer` agent to find:
  - explicit corrections
  - frustrated reactions to repeated mistakes
  - reverted changes
  - repeated similar issues

### Step 2: Present Findings
> 🇹🇼 命令指示

Show the user:

- behavior description
- proposed event type
- proposed pattern or matcher
- proposed action

### Step 3: Generate Rule Files
> 🇹🇼 命令指示

For each approved rule, create a file at `.claude/hookify.{name}.local.md`:

```yaml
---
name: rule-name
enabled: true
event: bash|file|stop|prompt|all
action: block|warn
pattern: "regex pattern"
---
Message shown when rule triggers.
```

### Step 4: Confirm
> 🇹🇼 命令指示

Report created rules and how to manage them with `/hookify-list` and `/hookify-configure`.
