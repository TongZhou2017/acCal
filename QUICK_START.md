# 快速开始指南

## 问题：Bundle 权限错误

如果遇到 bundle cache 权限问题，请按以下步骤操作：

### 步骤 1：修复权限

在终端运行以下命令（需要输入密码）：

```bash
sudo chown -R $(whoami):staff ~/.bundle/cache/
```

### 步骤 2：安装依赖

```bash
cd /Users/zhoutong/Documents/GitHub/acCal
bundle install
```

### 步骤 3：启动本地服务器

```bash
bundle exec jekyll serve
```

访问：`http://localhost:4000/acCal/`

---

## 或者：直接部署到 GitHub Pages

如果本地环境有问题，可以直接推送到 GitHub，让 GitHub Pages 自动构建：

```bash
cd /Users/zhoutong/Documents/GitHub/acCal
git add .
git commit -m "feat: 实现现代化深色主题设计"
git push origin main
```

等待几分钟后访问：`https://tongzhou2017.github.io/acCal/`

---

## 当前项目状态

✅ 已完成：
- 现代化深色主题设计
- Tailwind CSS 集成
- 响应式布局
- 搜索和筛选功能
- 3 个示例会议数据

📝 下一步：
- 修复本地环境权限问题（如需要本地测试）
- 或直接推送到 GitHub 部署

