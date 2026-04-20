---
description: 📝 【文件定位】這是一個命令（Command）定義檔案。此命令的功能：Configure your preferred package manager (npm/pnpm/yarn/bun)
disable-model-invocation: true
---

# Package Manager Setup
> 🇹🇼 命令指示

Configure your preferred package manager for this project or globally.

## Usage
> 🇹🇼 命令指示

```bash
# Detect current package manager
> 🇹🇼 命令指示
node scripts/setup-package-manager.js --detect

# Set global preference
> 🇹🇼 命令指示
node scripts/setup-package-manager.js --global pnpm

# Set project preference
> 🇹🇼 命令指示
node scripts/setup-package-manager.js --project bun

# List available package managers
> 🇹🇼 命令指示
node scripts/setup-package-manager.js --list
```

## Detection Priority
> 🇹🇼 命令指示

When determining which package manager to use, the following order is checked:

1. **Environment variable**: `CLAUDE_PACKAGE_MANAGER`
2. **Project config**: `.claude/package-manager.json`
3. **package.json**: `packageManager` field
4. **Lock file**: Presence of package-lock.json, yarn.lock, pnpm-lock.yaml, or bun.lockb
5. **Global config**: `~/.claude/package-manager.json`
6. **Fallback**: First available package manager (pnpm > bun > yarn > npm)

## Configuration Files
> 🇹🇼 命令指示

### Global Configuration
> 🇹🇼 命令指示
```json
// ~/.claude/package-manager.json
{
  "packageManager": "pnpm"
}
```

### Project Configuration
> 🇹🇼 命令指示
```json
// .claude/package-manager.json
{
  "packageManager": "bun"
}
```

### package.json
> 🇹🇼 命令指示
```json
{
  "packageManager": "pnpm@8.6.0"
}
```

## Environment Variable
> 🇹🇼 命令指示

Set `CLAUDE_PACKAGE_MANAGER` to override all other detection methods:

```bash
# Windows (PowerShell)
> 🇹🇼 命令指示
$env:CLAUDE_PACKAGE_MANAGER = "pnpm"

# macOS/Linux
> 🇹🇼 命令指示
export CLAUDE_PACKAGE_MANAGER=pnpm
```

## Run the Detection
> 🇹🇼 命令指示

To see current package manager detection results, run:

```bash
node scripts/setup-package-manager.js --detect
```
