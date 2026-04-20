---
description: 📝 【文件定位】這是一個命令（Command）定義檔案。此命令的功能：Create comprehensive feature implementation plan with codebase analysis and pattern extraction
argument-hint: <feature description | path/to/prd.md>
---

> Adapted from PRPs-agentic-eng by Wirasm. Part of the PRP workflow series.

# PRP Plan
> 🇹🇼 命令指示

Create a detailed, self-contained implementation plan that captures all codebase patterns, conventions, and context needed to implement a feature in a single pass.

**Core Philosophy**: A great plan contains everything needed to implement without asking further questions. Every pattern, every convention, every gotcha — captured once, referenced throughout.

**Golden Rule**: If you would need to search the codebase during implementation, capture that knowledge NOW in the plan.

---

## Phase 0 — DETECT
> 🇹🇼 命令指示

Determine input type from `$ARGUMENTS`:

| Input Pattern | Detection | Action |
|---|---|---|
| Path ending in `.prd.md` | File path to PRD | Parse PRD, find next pending phase |
| Path to `.md` with "Implementation Phases" | PRD-like document | Parse phases, find next pending |
| Path to any other file | Reference file | Read file for context, treat as free-form |
| Free-form text | Feature description | Proceed directly to Phase 1 |
| Empty / blank | No input | Ask user what feature to plan |

### PRD Parsing (when input is a PRD)
> 🇹🇼 命令指示

1. Read the PRD file with `cat "$PRD_PATH"`
2. Parse the **Implementation Phases** section
3. Find phases by status:
   - Look for `pending` phases
   - Check dependency chains (a phase may depend on prior phases being `complete`)
   - Select the **next eligible pending phase**
4. Extract from the selected phase:
   - Phase name and description
   - Acceptance criteria
   - Dependencies on prior phases
   - Any scope notes or constraints
5. Use the phase description as the feature to plan

If no pending phases remain, report that all phases are complete.

---

## Phase 1 — PARSE
> 🇹🇼 命令指示

Extract and clarify the feature requirements.

### Feature Understanding
> 🇹🇼 命令指示

From the input (PRD phase or free-form description), identify:

- **What** is being built (concrete deliverable)
- **Why** it matters (user value)
- **Who** uses it (target user/system)
- **Where** it fits (which part of the codebase)

### User Story
> 🇹🇼 命令指示

Format as:
```
As a [type of user],
I want [capability],
So that [benefit].
```

### Complexity Assessment
> 🇹🇼 命令指示

| Level | Indicators | Typical Scope |
|---|---|---|
| **Small** | Single file, isolated change, no new dependencies | 1-3 files, <100 lines |
| **Medium** | Multiple files, follows existing patterns, minor new concepts | 3-10 files, 100-500 lines |
| **Large** | Cross-cutting concerns, new patterns, external integrations | 10+ files, 500+ lines |
| **XL** | Architectural changes, new subsystems, migration needed | 20+ files, consider splitting |

### Ambiguity Gate
> 🇹🇼 命令指示

If any of these are unclear, **STOP and ask the user** before proceeding:

- The core deliverable is vague
- Success criteria are undefined
- There are multiple valid interpretations
- Technical approach has major unknowns

Do NOT guess. Ask. A plan built on assumptions fails during implementation.

---

## Phase 2 — EXPLORE
> 🇹🇼 命令指示

Gather deep codebase intelligence. Search the codebase directly for each category below.

### Codebase Search (8 Categories)
> 🇹🇼 命令指示

For each category, search using grep, find, and file reading:

1. **Similar Implementations** — Find existing features that resemble the planned one. Look for analogous patterns, endpoints, components, or modules.

2. **Naming Conventions** — Identify how files, functions, variables, classes, and exports are named in the relevant area of the codebase.

3. **Error Handling** — Find how errors are caught, propagated, logged, and returned to users in similar code paths.

4. **Logging Patterns** — Identify what gets logged, at what level, and in what format.

5. **Type Definitions** — Find relevant types, interfaces, schemas, and how they're organized.

6. **Test Patterns** — Find how similar features are tested. Note test file locations, naming, setup/teardown patterns, and assertion styles.

7. **Configuration** — Find relevant config files, environment variables, and feature flags.

8. **Dependencies** — Identify packages, imports, and internal modules used by similar features.

### Codebase Analysis (5 Traces)
> 🇹🇼 命令指示

Read relevant files to trace:

1. **Entry Points** — How does a request/action enter the system and reach the area you're modifying?
2. **Data Flow** — How does data move through the relevant code paths?
3. **State Changes** — What state is modified and where?
4. **Contracts** — What interfaces, APIs, or protocols must be honored?
5. **Patterns** — What architectural patterns are used (repository, service, controller, etc.)?

### Unified Discovery Table
> 🇹🇼 命令指示

Compile findings into a single reference:

| Category | File:Lines | Pattern | Key Snippet |
|---|---|---|---|
| Naming | `src/services/userService.ts:1-5` | camelCase services, PascalCase types | `export class UserService` |
| Error | `src/middleware/errorHandler.ts:10-25` | Custom AppError class | `throw new AppError(...)` |
| ... | ... | ... | ... |

---

## Phase 3 — RESEARCH
> 🇹🇼 命令指示

If the feature involves external libraries, APIs, or unfamiliar technology:

1. Search the web for official documentation
2. Find usage examples and best practices
> 🇹🇼 範例
3. Identify version-specific gotchas

Format each finding as:

```
KEY_INSIGHT: [what you learned]
APPLIES_TO: [which part of the plan this affects]
GOTCHA: [any warnings or version-specific issues]
```

If the feature uses only well-understood internal patterns, skip this phase and note: "No external research needed — feature uses established internal patterns."

---

## Phase 4 — DESIGN
> 🇹🇼 命令指示

### UX Transformation (if applicable)
> 🇹🇼 命令指示

Document the before/after user experience:

**Before:**
```
┌─────────────────────────────┐
│  [Current user experience]  │
│  Show the current flow,     │
│  what the user sees/does    │
└─────────────────────────────┘
```

**After:**
```
┌─────────────────────────────┐
│  [New user experience]      │
│  Show the improved flow,    │
│  what changes for the user  │
└─────────────────────────────┘
```

### Interaction Changes
> 🇹🇼 命令指示

| Touchpoint | Before | After | Notes |
|---|---|---|---|
| ... | ... | ... | ... |

If the feature is purely backend/internal with no UX change, note: "Internal change — no user-facing UX transformation."

---

## Phase 5 — ARCHITECT
> 🇹🇼 命令指示

### Strategic Design
> 🇹🇼 命令指示

Define the implementation approach:

- **Approach**: High-level strategy (e.g., "Add new service layer following existing repository pattern")
- **Alternatives Considered**: What other approaches were evaluated and why they were rejected
- **Scope**: Concrete boundaries of what WILL be built
- **NOT Building**: Explicit list of what is OUT OF SCOPE (prevents scope creep during implementation)

---

## Phase 6 — GENERATE
> 🇹🇼 命令指示

Write the full plan document using the template below. Save to `.claude/PRPs/plans/{kebab-case-feature-name}.plan.md`.

Create the directory if it doesn't exist:
```bash
mkdir -p .claude/PRPs/plans
```

### Plan Template
> 🇹🇼 命令指示

````markdown
# Plan: [Feature Name]
> 🇹🇼 命令指示

## Summary
> 🇹🇼 命令指示
[2-3 sentence overview]

## User Story
> 🇹🇼 命令指示
As a [user], I want [capability], so that [benefit].

## Problem → Solution
> 🇹🇼 命令指示
[Current state] → [Desired state]

## Metadata
> 🇹🇼 命令指示
- **Complexity**: [Small | Medium | Large | XL]
- **Source PRD**: [path or "N/A"]
- **PRD Phase**: [phase name or "N/A"]
- **Estimated Files**: [count]

---

## UX Design
> 🇹🇼 命令指示

### Before
> 🇹🇼 命令指示
[ASCII diagram or "N/A — internal change"]

### After
> 🇹🇼 命令指示
[ASCII diagram or "N/A — internal change"]

### Interaction Changes
> 🇹🇼 命令指示
| Touchpoint | Before | After | Notes |
|---|---|---|---|

---

## Mandatory Reading
> 🇹🇼 命令指示

Files that MUST be read before implementing:

| Priority | File | Lines | Why |
|---|---|---|---|
| P0 (critical) | `path/to/file` | 1-50 | Core pattern to follow |
| P1 (important) | `path/to/file` | 10-30 | Related types |
| P2 (reference) | `path/to/file` | all | Similar implementation |

## External Documentation
> 🇹🇼 命令指示

| Topic | Source | Key Takeaway |
|---|---|---|
| ... | ... | ... |

---

## Patterns to Mirror
> 🇹🇼 命令指示

Code patterns discovered in the codebase. Follow these exactly.

### NAMING_CONVENTION
> 🇹🇼 命令指示
// SOURCE: [file:lines]
[actual code snippet showing the naming pattern]

### ERROR_HANDLING
> 🇹🇼 命令指示
// SOURCE: [file:lines]
[actual code snippet showing error handling]

### LOGGING_PATTERN
> 🇹🇼 命令指示
// SOURCE: [file:lines]
[actual code snippet showing logging]

### REPOSITORY_PATTERN
> 🇹🇼 命令指示
// SOURCE: [file:lines]
[actual code snippet showing data access]

### SERVICE_PATTERN
> 🇹🇼 命令指示
// SOURCE: [file:lines]
[actual code snippet showing service layer]

### TEST_STRUCTURE
> 🇹🇼 命令指示
// SOURCE: [file:lines]
[actual code snippet showing test setup]

---

## Files to Change
> 🇹🇼 命令指示

| File | Action | Justification |
|---|---|---|
| `path/to/file.ts` | CREATE | New service for feature |
| `path/to/existing.ts` | UPDATE | Add new method |

## NOT Building
> 🇹🇼 命令指示

- [Explicit item 1 that is out of scope]
- [Explicit item 2 that is out of scope]

---

## Step-by-Step Tasks
> 🇹🇼 命令指示

### Task 1: [Name]
> 🇹🇼 命令指示
- **ACTION**: [What to do]
- **IMPLEMENT**: [Specific code/logic to write]
- **MIRROR**: [Pattern from Patterns to Mirror section to follow]
- **IMPORTS**: [Required imports]
- **GOTCHA**: [Known pitfall to avoid]
- **VALIDATE**: [How to verify this task is correct]

### Task 2: [Name]
> 🇹🇼 命令指示
- **ACTION**: ...
- **IMPLEMENT**: ...
- **MIRROR**: ...
- **IMPORTS**: ...
- **GOTCHA**: ...
- **VALIDATE**: ...

[Continue for all tasks...]

---

## Testing Strategy
> 🇹🇼 命令指示

### Unit Tests
> 🇹🇼 命令指示

| Test | Input | Expected Output | Edge Case? |
|---|---|---|---|
| ... | ... | ... | ... |

### Edge Cases Checklist
> 🇹🇼 命令指示
- [ ] Empty input
- [ ] Maximum size input
- [ ] Invalid types
- [ ] Concurrent access
- [ ] Network failure (if applicable)
- [ ] Permission denied

---

## Validation Commands
> 🇹🇼 命令指示

### Static Analysis
> 🇹🇼 命令指示
```bash
# Run type checker
> 🇹🇼 命令指示
[project-specific type check command]
```
EXPECT: Zero type errors

### Unit Tests
> 🇹🇼 命令指示
```bash
# Run tests for affected area
> 🇹🇼 命令指示
[project-specific test command]
```
EXPECT: All tests pass

### Full Test Suite
> 🇹🇼 命令指示
```bash
# Run complete test suite
> 🇹🇼 命令指示
[project-specific full test command]
```
EXPECT: No regressions

### Database Validation (if applicable)
> 🇹🇼 命令指示
```bash
# Verify schema/migrations
> 🇹🇼 命令指示
[project-specific db command]
```
EXPECT: Schema up to date

### Browser Validation (if applicable)
> 🇹🇼 命令指示
```bash
# Start dev server and verify
> 🇹🇼 命令指示
[project-specific dev server command]
```
EXPECT: Feature works as designed

### Manual Validation
> 🇹🇼 命令指示
- [ ] [Step-by-step manual verification checklist]

---

## Acceptance Criteria
> 🇹🇼 命令指示
- [ ] All tasks completed
- [ ] All validation commands pass
- [ ] Tests written and passing
- [ ] No type errors
- [ ] No lint errors
- [ ] Matches UX design (if applicable)

## Completion Checklist
> 🇹🇼 命令指示
- [ ] Code follows discovered patterns
- [ ] Error handling matches codebase style
- [ ] Logging follows codebase conventions
- [ ] Tests follow test patterns
- [ ] No hardcoded values
- [ ] Documentation updated (if needed)
- [ ] No unnecessary scope additions
- [ ] Self-contained — no questions needed during implementation

## Risks
> 🇹🇼 命令指示
| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| ... | ... | ... | ... |

## Notes
> 🇹🇼 命令指示
[Any additional context, decisions, or observations]
```

---

## Output
> 🇹🇼 命令指示

### Save the Plan
> 🇹🇼 命令指示

Write the generated plan to:
```
.claude/PRPs/plans/{kebab-case-feature-name}.plan.md
```

### Update PRD (if input was a PRD)
> 🇹🇼 命令指示

If this plan was generated from a PRD phase:
1. Update the phase status from `pending` to `in-progress`
2. Add the plan file path as a reference in the phase

### Report to User
> 🇹🇼 命令指示

```
## Plan Created
> 🇹🇼 命令指示

- **File**: .claude/PRPs/plans/{kebab-case-feature-name}.plan.md
- **Source PRD**: [path or "N/A"]
- **Phase**: [phase name or "standalone"]
- **Complexity**: [level]
- **Scope**: [N files, M tasks]
- **Key Patterns**: [top 3 discovered patterns]
- **External Research**: [topics researched or "none needed"]
- **Risks**: [top risk or "none identified"]
- **Confidence Score**: [1-10] — likelihood of single-pass implementation

> Next step: Run `/prp-implement .claude/PRPs/plans/{name}.plan.md` to execute this plan.
```

---

## Verification
> 🇹🇼 命令指示

Before finalizing, verify the plan against these checklists:

### Context Completeness
> 🇹🇼 命令指示
- [ ] All relevant files discovered and documented
- [ ] Naming conventions captured with examples
> 🇹🇼 範例
- [ ] Error handling patterns documented
- [ ] Test patterns identified
- [ ] Dependencies listed

### Implementation Readiness
> 🇹🇼 命令指示
- [ ] Every task has ACTION, IMPLEMENT, MIRROR, and VALIDATE
- [ ] No task requires additional codebase searching
- [ ] Import paths are specified
- [ ] GOTCHAs documented where applicable

### Pattern Faithfulness
> 🇹🇼 命令指示
- [ ] Code snippets are actual codebase examples (not invented)
> 🇹🇼 範例
- [ ] SOURCE references point to real files and line numbers
- [ ] Patterns cover naming, errors, logging, data access, and tests
- [ ] New code will be indistinguishable from existing code

### Validation Coverage
> 🇹🇼 命令指示
- [ ] Static analysis commands specified
- [ ] Test commands specified
- [ ] Build verification included

### UX Clarity
> 🇹🇼 命令指示
- [ ] Before/after states documented (or marked N/A)
- [ ] Interaction changes listed
- [ ] Edge cases for UX identified

### No Prior Knowledge Test
> 🇹🇼 命令指示
A developer unfamiliar with this codebase should be able to implement the feature using ONLY this plan, without searching the codebase or asking questions. If not, add the missing context.

---

## Next Steps
> 🇹🇼 命令指示

- Run `/prp-implement <plan-path>` to execute this plan
- Run `/plan` for quick conversational planning without artifacts
- Run `/prp-prd` to create a PRD first if scope is unclear
````
