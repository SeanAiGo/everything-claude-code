---
description: 📝 【文件定位】這是一個命令（Command）定義檔案。此命令的功能：Legacy slash-entry shim for dmux-workflows and autonomous-agent-harness. Prefer the skills directly.
---

# Orchestrate Command (Legacy Shim)
> 🇹🇼 命令指示

Use this only if you still invoke `/orchestrate`. The maintained orchestration guidance lives in `skills/dmux-workflows/SKILL.md` and `skills/autonomous-agent-harness/SKILL.md`.

## Canonical Surface
> 🇹🇼 命令指示

- Prefer `dmux-workflows` for parallel panes, worktrees, and multi-agent splits.
- Prefer `autonomous-agent-harness` for longer-running loops, governance, scheduling, and control-plane style execution.
- Keep this file only as a compatibility entry point.

## Arguments
> 🇹🇼 命令指示

`$ARGUMENTS`

## Delegation
> 🇹🇼 命令指示

Apply the orchestration skills instead of maintaining a second workflow spec here.
- Start with `dmux-workflows` for split/parallel execution.
- Pull in `autonomous-agent-harness` when the user is really asking for persistent loops, governance, or operator-layer behavior.
- Keep handoffs structured, but let the skills define the maintained sequencing rules.
Security Reviewer: [summary]

### FILES CHANGED
> 🇹🇼 命令指示

[List all files modified]

### TEST RESULTS
> 🇹🇼 命令指示

[Test pass/fail summary]

### SECURITY STATUS
> 🇹🇼 命令指示

[Security findings]

### RECOMMENDATION
> 🇹🇼 命令指示

[SHIP / NEEDS WORK / BLOCKED]
```

## Parallel Execution
> 🇹🇼 命令指示

For independent checks, run agents in parallel:

```markdown
### Parallel Phase
> 🇹🇼 命令指示
Run simultaneously:
- code-reviewer (quality)
- security-reviewer (security)
- architect (design)

### Merge Results
> 🇹🇼 命令指示
Combine outputs into single report
```

For external tmux-pane workers with separate git worktrees, use `node scripts/orchestrate-worktrees.js plan.json --execute`. The built-in orchestration pattern stays in-process; the helper is for long-running or cross-harness sessions.

When workers need to see dirty or untracked local files from the main checkout, add `seedPaths` to the plan file. ECC overlays only those selected paths into each worker worktree after `git worktree add`, which keeps the branch isolated while still exposing in-flight local scripts, plans, or docs.

```json
{
  "sessionName": "workflow-e2e",
  "seedPaths": [
    "scripts/orchestrate-worktrees.js",
    "scripts/lib/tmux-worktree-orchestrator.js",
    ".claude/plan/workflow-e2e-test.json"
  ],
  "workers": [
    { "name": "docs", "task": "Update orchestration docs." }
  ]
}
```

To export a control-plane snapshot for a live tmux/worktree session, run:

```bash
node scripts/orchestration-status.js .claude/plan/workflow-visual-proof.json
```

The snapshot includes session activity, tmux pane metadata, worker states, objectives, seeded overlays, and recent handoff summaries in JSON form.

## Operator Command-Center Handoff
> 🇹🇼 命令指示

When the workflow spans multiple sessions, worktrees, or tmux panes, append a control-plane block to the final handoff:

```markdown
CONTROL PLANE
-------------
Sessions:
- active session ID or alias
- branch + worktree path for each active worker
- tmux pane or detached session name when applicable

Diffs:
- git status summary
- git diff --stat for touched files
- merge/conflict risk notes

Approvals:
- pending user approvals
- blocked steps awaiting confirmation

Telemetry:
- last activity timestamp or idle signal
- estimated token or cost drift
- policy events raised by hooks or reviewers
```

This keeps planner, implementer, reviewer, and loop workers legible from the operator surface.

## Workflow Arguments
> 🇹🇼 命令指示

$ARGUMENTS:
- `feature <description>` - Full feature workflow
- `bugfix <description>` - Bug fix workflow
- `refactor <description>` - Refactoring workflow
- `security <description>` - Security review workflow
- `custom <agents> <description>` - Custom agent sequence

## Custom Workflow Example
> 🇹🇼 命令指示

```
/orchestrate custom "architect,tdd-guide,code-reviewer" "Redesign caching layer"
```

## Tips
> 🇹🇼 命令指示

1. **Start with planner** for complex features
2. **Always include code-reviewer** before merge
3. **Use security-reviewer** for auth/payment/PII
4. **Keep handoffs concise** - focus on what next agent needs
5. **Run verification** between agents if needed
