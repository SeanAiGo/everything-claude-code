---
name: evolve
description: 📝 【文件定位】這是一個命令（Command）定義檔案。此命令的功能：Analyze instincts and suggest or generate evolved structures
command: true
---

# Evolve Command
> 🇹🇼 命令指示

## Implementation
> 🇹🇼 命令指示

Run the instinct CLI using the plugin root path:

```bash
python3 "${CLAUDE_PLUGIN_ROOT}/skills/continuous-learning-v2/scripts/instinct-cli.py" evolve [--generate]
```

Or if `CLAUDE_PLUGIN_ROOT` is not set (manual installation):

```bash
python3 ~/.claude/skills/continuous-learning-v2/scripts/instinct-cli.py evolve [--generate]
```

Analyzes instincts and clusters related ones into higher-level structures:
- **Commands**: When instincts describe user-invoked actions
- **Skills**: When instincts describe auto-triggered behaviors
- **Agents**: When instincts describe complex, multi-step processes

## Usage
> 🇹🇼 命令指示

```
/evolve                    # Analyze all instincts and suggest evolutions
/evolve --generate         # Also generate files under evolved/{skills,commands,agents}
```

## Evolution Rules
> 🇹🇼 命令指示

### → Command (User-Invoked)
> 🇹🇼 命令指示
When instincts describe actions a user would explicitly request:
- Multiple instincts about "when user asks to..."
- Instincts with triggers like "when creating a new X"
- Instincts that follow a repeatable sequence

Example:
- `new-table-step1`: "when adding a database table, create migration"
- `new-table-step2`: "when adding a database table, update schema"
- `new-table-step3`: "when adding a database table, regenerate types"

→ Creates: **new-table** command

### → Skill (Auto-Triggered)
> 🇹🇼 命令指示
When instincts describe behaviors that should happen automatically:
- Pattern-matching triggers
- Error handling responses
- Code style enforcement

Example:
- `prefer-functional`: "when writing functions, prefer functional style"
- `use-immutable`: "when modifying state, use immutable patterns"
- `avoid-classes`: "when designing modules, avoid class-based design"

→ Creates: `functional-patterns` skill

### → Agent (Needs Depth/Isolation)
> 🇹🇼 命令指示
When instincts describe complex, multi-step processes that benefit from isolation:
- Debugging workflows
- Refactoring sequences
- Research tasks

Example:
- `debug-step1`: "when debugging, first check logs"
- `debug-step2`: "when debugging, isolate the failing component"
- `debug-step3`: "when debugging, create minimal reproduction"
- `debug-step4`: "when debugging, verify fix with test"

→ Creates: **debugger** agent

## What to Do
> 🇹🇼 命令指示

1. Detect current project context
2. Read project + global instincts (project takes precedence on ID conflicts)
3. Group instincts by trigger/domain patterns
4. Identify:
   - Skill candidates (trigger clusters with 2+ instincts)
   - Command candidates (high-confidence workflow instincts)
   - Agent candidates (larger, high-confidence clusters)
5. Show promotion candidates (project -> global) when applicable
6. If `--generate` is passed, write files to:
   - Project scope: `~/.claude/homunculus/projects/<project-id>/evolved/`
   - Global fallback: `~/.claude/homunculus/evolved/`

## Output Format
> 🇹🇼 命令指示

```
============================================================
  EVOLVE ANALYSIS - 12 instincts
  Project: my-app (a1b2c3d4e5f6)
  Project-scoped: 8 | Global: 4
============================================================

High confidence instincts (>=80%): 5

## SKILL CANDIDATES
> 🇹🇼 命令指示
1. Cluster: "adding tests"
   Instincts: 3
   Avg confidence: 82%
   Domains: testing
   Scopes: project

## COMMAND CANDIDATES (2)
> 🇹🇼 命令指示
  /adding-tests
    From: test-first-workflow [project]
    Confidence: 84%

## AGENT CANDIDATES (1)
> 🇹🇼 命令指示
  adding-tests-agent
    Covers 3 instincts
    Avg confidence: 82%
```

## Flags
> 🇹🇼 命令指示

- `--generate`: Generate evolved files in addition to analysis output

## Generated File Format
> 🇹🇼 命令指示

### Command
> 🇹🇼 命令指示
```markdown
---
name: new-table
description: Create a new database table with migration, schema update, and type generation
command: /new-table
evolved_from:
  - new-table-migration
  - update-schema
  - regenerate-types
---

# New Table Command
> 🇹🇼 命令指示

[Generated content based on clustered instincts]

## Steps
> 🇹🇼 命令指示
1. ...
2. ...
```

### Skill
> 🇹🇼 命令指示
```markdown
---
name: functional-patterns
description: Enforce functional programming patterns
evolved_from:
  - prefer-functional
  - use-immutable
  - avoid-classes
---

# Functional Patterns Skill
> 🇹🇼 命令指示

[Generated content based on clustered instincts]
```

### Agent
> 🇹🇼 命令指示
```markdown
---
name: debugger
description: Systematic debugging agent
model: sonnet
evolved_from:
  - debug-check-logs
  - debug-isolate
  - debug-reproduce
---

# Debugger Agent
> 🇹🇼 命令指示

[Generated content based on clustered instincts]
```
