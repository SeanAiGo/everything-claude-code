---
name: skill-create
description: 📝 【文件定位】這是一個命令（Command）定義檔案。此命令的功能：Analyze local git history to extract coding patterns and generate SKILL.md files. Local version of the Skill Creator GitHub App.
allowed_tools: ["Bash", "Read", "Write", "Grep", "Glob"]
---

# /skill-create - Local Skill Generation
> 🇹🇼 命令指示

Analyze your repository's git history to extract coding patterns and generate SKILL.md files that teach Claude your team's practices.

## Usage
> 🇹🇼 命令指示

```bash
/skill-create                    # Analyze current repo
/skill-create --commits 100      # Analyze last 100 commits
/skill-create --output ./skills  # Custom output directory
/skill-create --instincts        # Also generate instincts for continuous-learning-v2
```

## What It Does
> 🇹🇼 命令指示

1. **Parses Git History** - Analyzes commits, file changes, and patterns
2. **Detects Patterns** - Identifies recurring workflows and conventions
3. **Generates SKILL.md** - Creates valid Claude Code skill files
4. **Optionally Creates Instincts** - For the continuous-learning-v2 system

## Analysis Steps
> 🇹🇼 命令指示

### Step 1: Gather Git Data
> 🇹🇼 命令指示

```bash
# Get recent commits with file changes
> 🇹🇼 命令指示
git log --oneline -n ${COMMITS:-200} --name-only --pretty=format:"%H|%s|%ad" --date=short

# Get commit frequency by file
> 🇹🇼 命令指示
git log --oneline -n 200 --name-only | grep -v "^$" | grep -v "^[a-f0-9]" | sort | uniq -c | sort -rn | head -20

# Get commit message patterns
> 🇹🇼 命令指示
git log --oneline -n 200 | cut -d' ' -f2- | head -50
```

### Step 2: Detect Patterns
> 🇹🇼 命令指示

Look for these pattern types:

| Pattern | Detection Method |
|---------|-----------------|
| **Commit conventions** | Regex on commit messages (feat:, fix:, chore:) |
| **File co-changes** | Files that always change together |
| **Workflow sequences** | Repeated file change patterns |
| **Architecture** | Folder structure and naming conventions |
| **Testing patterns** | Test file locations, naming, coverage |

### Step 3: Generate SKILL.md
> 🇹🇼 命令指示

Output format:

```markdown
---
name: {repo-name}-patterns
description: Coding patterns extracted from {repo-name}
version: 1.0.0
source: local-git-analysis
analyzed_commits: {count}
---

# {Repo Name} Patterns
> 🇹🇼 命令指示

## Commit Conventions
> 🇹🇼 命令指示
{detected commit message patterns}

## Code Architecture
> 🇹🇼 命令指示
{detected folder structure and organization}

## Workflows
> 🇹🇼 命令指示
{detected repeating file change patterns}

## Testing Patterns
> 🇹🇼 命令指示
{detected test conventions}
```

### Step 4: Generate Instincts (if --instincts)
> 🇹🇼 命令指示

For continuous-learning-v2 integration:

```yaml
---
id: {repo}-commit-convention
trigger: "when writing a commit message"
confidence: 0.8
domain: git
source: local-repo-analysis
---

# Use Conventional Commits
> 🇹🇼 命令指示

## Action
> 🇹🇼 命令指示
Prefix commits with: feat:, fix:, chore:, docs:, test:, refactor:

## Evidence
> 🇹🇼 命令指示
- Analyzed {n} commits
- {percentage}% follow conventional commit format
```

## Example Output
> 🇹🇼 命令指示

Running `/skill-create` on a TypeScript project might produce:

```markdown
---
name: my-app-patterns
description: Coding patterns from my-app repository
version: 1.0.0
source: local-git-analysis
analyzed_commits: 150
---

# My App Patterns
> 🇹🇼 命令指示

## Commit Conventions
> 🇹🇼 命令指示

This project uses **conventional commits**:
- `feat:` - New features
- `fix:` - Bug fixes
- `chore:` - Maintenance tasks
- `docs:` - Documentation updates

## Code Architecture
> 🇹🇼 命令指示

```
src/
├── components/     # React components (PascalCase.tsx)
├── hooks/          # Custom hooks (use*.ts)
├── utils/          # Utility functions
├── types/          # TypeScript type definitions
└── services/       # API and external services
```

## Workflows
> 🇹🇼 命令指示

### Adding a New Component
> 🇹🇼 命令指示
1. Create `src/components/ComponentName.tsx`
2. Add tests in `src/components/__tests__/ComponentName.test.tsx`
3. Export from `src/components/index.ts`

### Database Migration
> 🇹🇼 命令指示
1. Modify `src/db/schema.ts`
2. Run `pnpm db:generate`
3. Run `pnpm db:migrate`

## Testing Patterns
> 🇹🇼 命令指示

- Test files: `__tests__/` directories or `.test.ts` suffix
- Coverage target: 80%+
- Framework: Vitest
```

## GitHub App Integration
> 🇹🇼 命令指示

For advanced features (10k+ commits, team sharing, auto-PRs), use the [Skill Creator GitHub App](https://github.com/apps/skill-creator):

- Install: [github.com/apps/skill-creator](https://github.com/apps/skill-creator)
- Comment `/skill-creator analyze` on any issue
- Receives PR with generated skills

## Related Commands
> 🇹🇼 命令指示

- `/instinct-import` - Import generated instincts
- `/instinct-status` - View learned instincts
- `/evolve` - Cluster instincts into skills/agents

---

*Part of [Everything Claude Code](https://github.com/affaan-m/everything-claude-code)*
