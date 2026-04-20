---
description: 📝 【文件定位】這是一個規則（Rule）定義檔案。此規則的範疇與目的：規範開發時應遵循的準則與最佳實踐。
---
# Git 工作流
> 🇹🇼 規則說明與指示

## 提交消息格式
```
<类型>: <描述>

<可选正文>
```

类型：feat, fix, refactor, docs, test, chore, perf, ci

注意：通过 ~/.claude/settings.json 全局禁用归属。

## Pull Request 工作流

创建 PR 时：
1. 分析完整提交历史（不仅是最新提交）
2. 使用 `git diff [base-branch]...HEAD` 查看所有更改
3. 起草全面的 PR 摘要
4. 包含带有 TODO 的测试计划
5. 如果是新分支，使用 `-u` 标志推送

> 对于 git 操作之前的完整开发流程（规划、TDD、代码审查），
> 参见 [development-workflow.md](./development-workflow.md)。
