# 邮件模板说明

本目录包含 acCal 邮件订阅系统使用的所有邮件模板。

## 模板列表

1. **subscription_confirmation.html** - 订阅确认邮件
   - 当用户成功订阅时发送
   - 包含订阅信息确认和说明

2. **conference_reminder.html** - 会议提醒邮件
   - 在会议开始前按用户设置的天数发送
   - 包含会议详细信息

3. **new_conference_notification.html** - 新会议通知邮件
   - 当有新会议添加到日历中时发送给订阅了相关学科的用户
   - 包含会议基本信息和快速操作链接

4. **deadline_reminder.html** - 截稿提醒邮件
   - 在摘要截稿日期前7天发送
   - 突出显示截稿日期，提醒用户及时提交

## 模板变量

所有模板支持以下变量（使用双大括号语法）：

- `{{EMAIL}}` - 用户邮箱地址
- `{{CONFERENCE_TITLE}}` - 会议标题
- `{{CONFERENCE_URL}}` - 会议详情页面URL
- `{{LOCATION}}` - 会议地点
- `{{DATE_START}}` - 会议开始日期
- `{{DATE_END}}` - 会议结束日期
- `{{DEADLINE}}` - 摘要截稿日期
- `{{DISCIPLINE}}` - 学科领域
- `{{DESCRIPTION}}` - 会议简介
- `{{TAGS}}` - 会议标签（数组）
- `{{DAYS_UNTIL}}` - 距离目标日期的天数
- `{{DISCIPLINES}}` - 用户订阅的学科列表
- `{{DEFAULT_REMINDER_DAYS}}` - 默认提醒天数
- `{{SITE_URL}}` - 网站URL
- `{{OFFICIAL_URL}}` - 会议官方网站URL
- `{{UNSUBSCRIBE_URL}}` - 取消订阅链接
- `{{MANAGE_SUBSCRIPTION_URL}}` - 管理订阅设置链接
- `{{MANAGE_REMINDERS_URL}}` - 管理提醒设置链接

## 使用说明

这些模板需要在后端邮件发送系统中使用。建议使用以下方式之一：

1. **GitHub Actions + SendGrid/Mailgun** - 自动化邮件发送
2. **第三方服务** - 如 Mailchimp, SendGrid 等
3. **自建邮件服务** - 使用 Python/Node.js 等脚本处理

## 模板定制

所有模板使用内联CSS样式，确保在各种邮件客户端中正确显示。如需修改样式，请确保：

1. 保持内联样式
2. 测试在不同邮件客户端中的显示效果
3. 确保移动端响应式设计

## 注意事项

- 所有链接应使用绝对URL
- 取消订阅链接必须包含唯一标识符
- 建议添加纯文本版本（.txt）以提高兼容性
- 遵循反垃圾邮件最佳实践（SPF, DKIM, DMARC）

