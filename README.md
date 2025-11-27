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
* **托管：** GitHub Pages

## 📅 时间范围筛选

网站支持按时间范围筛选会议：
- 在筛选面板中设置开始日期和结束日期
- 系统会筛选出在指定时间范围内召开的会议
- 时间范围筛选与学科领域、状态筛选等功能可同时使用