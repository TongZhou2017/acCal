# acCal: 学术会议日历 (Academic Conference Calendar)

## 🎯 项目目标
acCal 致力于解决国内学术会议信息分散、鱼龙混杂的痛点。我们提供一个开源、可订阅、且经过人工审核的纯净会议日历，帮助科研人员更高效地规划学术日程。

## 🛡️ 质量保证
本网站 **严格拒绝** 任何高价收费培训班和疑似掠夺性会议（Predatory Conferences）。所有信息均通过社区提交和维护者审核。

## 💡 如何贡献（提交新会议）
我们采用 **GitHub Issue 驱动** 的自动化流程：

1.  点击 [提交会议链接](https://github.com/TongZhou2017/acCal/issues/new?assignees=&labels=pending-review&projects=&template=conference_submission.yml&title=%5B会议%5D%3A)。
2.  填写结构化表单（YAML 格式）。
3.  提交后，GitHub Actions (通过 `issue_to_md.py` 脚本) 会自动生成一个 Pull Request。
4.  维护者审核通过后，数据将自动合并并更新网站。

## ⚙️ 技术栈
* **内容管理：** GitHub Issues
* **自动化：** GitHub Actions + Python
* **前端：** Jekyll + Tailwind CSS
* **地图服务：** 高德地图（有审图号：GS(2023)2650号）
* **托管：** GitHub Pages

## 🗺️ 地图功能配置

网站支持地图视图功能，可以在地图上查看会议位置。要启用此功能，需要配置高德地图API密钥：

### ⚠️ 安全提示

**请勿将API密钥直接提交到GitHub！** 这会导致密钥泄露，可能被他人滥用。

### 安全配置步骤

1. **申请高德地图API密钥**
   - 访问 [高德开放平台](https://console.amap.com/)
   - 注册/登录账号
   - 创建应用并获取Web服务API密钥

2. **配置密钥（使用GitHub Secrets）**
   
   **生产环境（GitHub Pages）：**
   
   1. 前往仓库设置：`Settings` → `Secrets and variables` → `Actions`
   2. 点击 `New repository secret`
   3. 名称填写：`AMAP_KEY`
   4. 值填写：您的高德地图API密钥
   5. 点击 `Add secret`
   
   GitHub Actions会自动在构建时读取该Secret并创建临时配置文件。
   **密钥不会出现在代码中，最安全！**
   
   **本地开发（可选）：**
   
   如需在本地预览地图功能，可创建本地配置文件：
   ```bash
   # 1. 复制配置文件示例
   cp _config.local.yml.example _config.local.yml
   
   # 2. 编辑 _config.local.yml，填入您的API密钥
   # 注意：_config.local.yml 已添加到 .gitignore，不会被提交到GitHub
   
   # 3. 本地运行Jekyll时，需要指定配置文件：
   bundle exec jekyll serve --config _config.yml,_config.local.yml
   ```
   
   ⚠️ **注意**：本地配置文件仅用于开发测试，不要提交到GitHub！

3. **设置API密钥安全限制（重要！）**
   
   在高德地图控制台中设置HTTP Referer白名单：
   - 登录 [高德开放平台控制台](https://console.amap.com/)
   - 进入您的应用设置
   - 在"安全设置"中添加HTTP Referer白名单：
     - `https://yourusername.github.io/*`（GitHub Pages域名）
     - `http://localhost:*`（本地开发）
   - 这样可以限制API密钥只能在指定域名下使用

4. **功能说明**
   - 地图视图使用高德地图Web API（审图号：GS(2023)2650号）
   - 支持地址自动解析和标记点显示
   - 点击标记点可查看会议详情
   - 地图会自动调整视野以显示所有会议位置

## 📅 时间范围筛选

网站支持按时间范围筛选会议：
- 在筛选面板中设置开始日期和结束日期
- 系统会筛选出在指定时间范围内召开的会议
- 时间范围筛选与学科领域、状态筛选等功能可同时使用