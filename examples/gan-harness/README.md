---
description: 📝 【文件定位】這是一個範例（Example）檔案，提供實際應用的參考。
---
# GAN-Style Harness Examples
> 🇹🇼 說明與指示

Examples showing how to use the Generator-Evaluator harness for different project types.

## Quick Start

```bash
# Full-stack web app (uses all three agents)
> 🇹🇼 說明與指示
./scripts/gan-harness.sh "Build a project management app with Kanban boards and team collaboration"

# Frontend design (skip planner, focus on design iterations)
> 🇹🇼 說明與指示
GAN_SKIP_PLANNER=true ./scripts/gan-harness.sh "Create a stunning landing page for a crypto portfolio tracker"

# API-only (no browser testing needed)
> 🇹🇼 說明與指示
GAN_EVAL_MODE=code-only ./scripts/gan-harness.sh "Build a REST API for a recipe sharing platform with search and ratings"

# Tight budget (fewer iterations, lower threshold)
> 🇹🇼 說明與指示
GAN_MAX_ITERATIONS=5 GAN_PASS_THRESHOLD=6.5 ./scripts/gan-harness.sh "Build a todo app with categories and due dates"
```

## Example: Using the Command

```bash
# In Claude Code interactive mode:
> 🇹🇼 說明與指示
/project:gan-build "Build a music streaming dashboard with playlists, visualizer, and social features"

# With options:
> 🇹🇼 說明與指示
/project:gan-build "Build a recipe sharing platform" --max-iterations 10 --pass-threshold 7.5 --eval-mode screenshot
```

## Example: Manual Three-Agent Run

For maximum control, run each agent separately:

```bash
# Step 1: Plan (produces spec.md)
> 🇹🇼 說明與指示
claude -p --model opus "$(cat agents/gan-planner.md)

Your brief: 'Build a retro game maker with sprite editor and level designer'

Write the full spec to gan-harness/spec.md and eval rubric to gan-harness/eval-rubric.md."

# Step 2: Generate (iteration 1)
> 🇹🇼 說明與指示
claude -p --model opus "$(cat agents/gan-generator.md)

Iteration 1. Read gan-harness/spec.md. Build the initial application.
Start dev server on port 3000. Commit as iteration-001."

# Step 3: Evaluate (iteration 1)
> 🇹🇼 說明與指示
claude -p --model opus "$(cat agents/gan-evaluator.md)

Iteration 1. Read gan-harness/eval-rubric.md.
Test http://localhost:3000. Write feedback to gan-harness/feedback/feedback-001.md.
Be ruthlessly strict."

# Step 4: Generate (iteration 2 — reads feedback)
> 🇹🇼 說明與指示
claude -p --model opus "$(cat agents/gan-generator.md)

Iteration 2. Read gan-harness/feedback/feedback-001.md FIRST.
Address every issue. Then read gan-harness/spec.md for remaining features.
Commit as iteration-002."

# Repeat steps 3-4 until satisfied
> 🇹🇼 說明與指示
```

## Example: Custom Evaluation Criteria

For non-visual projects (APIs, CLIs, libraries), customize the rubric:

```bash
mkdir -p gan-harness
cat > gan-harness/eval-rubric.md << 'EOF'
# API Evaluation Rubric
> 🇹🇼 說明與指示

### Correctness (weight: 0.4)
- Do all endpoints return expected data?
- Are edge cases handled (empty inputs, large payloads)?
- Do error responses have proper status codes?

### Performance (weight: 0.2)
- Response times under 100ms for simple queries?
- Database queries optimized (no N+1)?
- Pagination implemented for list endpoints?

### Security (weight: 0.2)
- Input validation on all endpoints?
- SQL injection prevention?
- Rate limiting implemented?
- Authentication properly enforced?

### Documentation (weight: 0.2)
- OpenAPI spec generated?
- All endpoints documented?
- Example requests/responses provided?
EOF

GAN_SKIP_PLANNER=true GAN_EVAL_MODE=code-only ./scripts/gan-harness.sh "Build a REST API for task management"
```

## Project Types and Recommended Settings

| Project Type | Eval Mode | Iterations | Threshold | Est. Cost |
|-------------|-----------|------------|-----------|-----------|
| Full-stack web app | playwright | 10-15 | 7.0 | $100-200 |
| Landing page | screenshot | 5-8 | 7.5 | $30-60 |
| REST API | code-only | 5-8 | 7.0 | $30-60 |
| CLI tool | code-only | 3-5 | 6.5 | $15-30 |
| Data dashboard | playwright | 8-12 | 7.0 | $60-120 |
| Game | playwright | 10-15 | 7.0 | $100-200 |

## Understanding the Output

After each run, check:

1. **`gan-harness/build-report.md`** — Final summary with score progression
2. **`gan-harness/feedback/`** — All evaluation feedback (useful for understanding quality evolution)
3. **`gan-harness/spec.md`** — The full spec (useful if you want to continue manually)
4. **Score progression** — Should show steady improvement. Plateaus indicate the model has hit its ceiling.

## Tips

1. **Start with a clear brief** — "Build X with Y and Z" beats "make something cool"
2. **Don't go below 5 iterations** — The first 2-3 iterations are usually below threshold
3. **Use `playwright` mode for UI projects** — Screenshot-only misses interaction bugs
4. **Review feedback files** — Even if the final score passes, the feedback contains valuable insights
5. **Iterate on the spec** — If results are disappointing, improve `spec.md` and run again with `--skip-planner`
