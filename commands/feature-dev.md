---
description: 📝 【文件定位】這是一個命令（Command）定義檔案。此命令的功能：Guided feature development with codebase understanding and architecture focus
---

A structured feature-development workflow that emphasizes understanding existing code before writing new code.

## Phases
> 🇹🇼 命令指示

### 1. Discovery
> 🇹🇼 命令指示

- read the feature request carefully
- identify requirements, constraints, and acceptance criteria
- ask clarifying questions if the request is ambiguous

### 2. Codebase Exploration
> 🇹🇼 命令指示

- use `code-explorer` to analyze the relevant existing code
- trace execution paths and architecture layers
- understand integration points and conventions

### 3. Clarifying Questions
> 🇹🇼 命令指示

- present findings from exploration
- ask targeted design and edge-case questions
- wait for user response before proceeding

### 4. Architecture Design
> 🇹🇼 命令指示

- use `code-architect` to design the feature
- provide the implementation blueprint
- wait for approval before implementing

### 5. Implementation
> 🇹🇼 命令指示

- implement the feature following the approved design
- prefer TDD where appropriate
- keep commits small and focused

### 6. Quality Review
> 🇹🇼 命令指示

- use `code-reviewer` to review the implementation
- address critical and important issues
- verify test coverage

### 7. Summary
> 🇹🇼 命令指示

- summarize what was built
- list follow-up items or limitations
- provide testing instructions
