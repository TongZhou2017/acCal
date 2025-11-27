# Issue 提交工作流程说明

## 📋 概述

当有人通过 GitHub Issue 提交会议信息时，系统会自动执行以下流程：

1. **Issue 创建** → 用户填写 Issue 模板提交会议信息
2. **自动触发** → GitHub Actions 工作流自动运行
3. **解析数据** → 解析 Issue 内容为结构化 JSON
4. **生成文件** → Python 脚本生成 Markdown 文件到 `_conferences/` 目录
5. **创建 PR** → 自动创建 Pull Request 等待审核
6. **人工审核** → 维护者检查并合并 PR
7. **网站更新** → Jekyll 自动构建并更新网站

## 🔧 已配置的文件

### 1. Issue 模板
- **位置**: `.github/ISSUE_TEMPLATE/conference_submission.yml`
- **功能**: 定义会议提交表单的结构和字段

### 2. GitHub Actions 工作流
- **位置**: `.github/workflows/process_issue.yml`
- **触发条件**: 当有新的 Issue 被创建时
- **功能**: 
  - 解析 Issue 内容
  - 运行 Python 脚本生成 Markdown
  - 自动创建 Pull Request

### 3. Python 转换脚本
- **位置**: `scripts/issue_to_md.py`
- **功能**: 将 Issue 数据转换为 Jekyll 格式的 Markdown 文件

## 🚀 使用步骤

### 对于提交者（用户）

1. 访问: https://github.com/TongZhou2017/acCal/issues/new
2. 选择模板: "📅 提交会议信息 (Submit Conference)"
3. 填写表单:
   - 会议名称
   - 学科分类
   - 标签
   - 地点
   - 开始日期
   - 截止日期（可选）
   - 官方网址
4. 提交 Issue

### 对于维护者（你）

1. **等待自动 PR**: 当 Issue 提交后，GitHub Actions 会自动创建 PR
2. **审核 PR 内容**:
   - 检查生成的 Markdown 文件格式是否正确
   - 验证会议信息的准确性
   - 确认 URL 是官方来源
   - 检查是否为掠夺性会议
3. **合并 PR**: 如果审核通过，合并 PR
4. **关闭 Issue**: PR 合并后会自动关闭关联的 Issue（如果 PR 中包含了 `Closes #<issue_number>`）

## 🔍 测试你的 Issue

你已经创建了测试 Issue #1，现在可以：

1. **手动触发工作流**（如果 Actions 没有自动运行）:
   - 前往 GitHub 仓库的 Actions 标签页
   - 查看是否有工作流运行
   - 如果没有，可以手动重新运行

2. **本地测试脚本**:
   ```bash
   cd /Users/zhoutong/Documents/GitHub/acCal
   python scripts/issue_to_md.py
   ```
   这会使用模拟数据生成一个测试文件。

3. **检查生成的文件**:
   - 查看 `_conferences/` 目录
   - 确认文件格式正确

## ⚠️ 注意事项

1. **首次运行**: GitHub Actions 工作流需要仓库有 Actions 权限，确保已启用
2. **权限设置**: 确保 `GITHUB_TOKEN` 有创建 PR 的权限（默认应该已配置）
3. **文件冲突**: 如果同一日期和标题的会议已存在，文件名可能会冲突
4. **审核流程**: 所有生成的会议已自动设置为 `draft: false`，合并 PR 后即可在网站上显示

## 🐛 故障排除

### 工作流没有自动运行
- 检查 `.github/workflows/process_issue.yml` 文件是否存在
- 确认文件语法正确（YAML 格式）
- 查看 Actions 标签页的错误信息

### 脚本解析失败
- 检查 Issue 是否使用了正确的模板
- 确认 Issue body 包含必要的字段
- 查看工作流日志中的错误信息

### PR 创建失败
- 检查 `GITHUB_TOKEN` 权限
- 确认分支名称没有冲突
- 查看工作流日志

## 📝 下一步

1. ✅ Issue 模板已创建
2. ✅ GitHub Actions 工作流已配置
3. ✅ Python 脚本已就绪
4. ⏳ 等待测试 Issue 触发工作流
5. ⏳ 审核并合并自动生成的 PR

现在你可以：
- 提交你的测试 Issue 到 GitHub（如果还没有）
- 或者等待其他人提交新的 Issue
- 系统会自动处理并创建 PR 供你审核

