# 故障排除指南

## Bundle 权限问题

如果遇到 bundle cache 权限问题，可以尝试以下解决方案：

### 方案 1：修复权限（推荐）

```bash
# 修复 bundle cache 目录权限
sudo chown -R $(whoami):staff ~/.bundle/cache/

# 然后重新运行
bundle install
```

### 方案 2：使用本地 bundle 路径

```bash
# 配置使用项目本地路径
bundle config set --local path 'vendor/bundle'

# 安装依赖
bundle install

# 运行 Jekyll（使用 bundle exec）
bundle exec jekyll serve
```

### 方案 3：跳过本地测试，直接部署

如果本地环境有问题，可以直接推送到 GitHub，让 GitHub Pages 自动构建：

```bash
git add .
git commit -m "feat: 实现现代化深色主题设计"
git push origin main
```

然后访问：`https://tongzhou2017.github.io/acCal/`

### 方案 4：使用 Docker（如果已安装 Docker）

```bash
# 使用官方 Jekyll Docker 镜像
docker run --rm \
  --volume="$PWD:/srv/jekyll" \
  --volume="$PWD/vendor/bundle:/usr/local/bundle" \
  -p 4000:4000 \
  -it jekyll/jekyll:latest \
  jekyll serve
```

## RubyGems 版本警告

如果看到 RubyGems 版本警告，可以忽略（不影响功能），或者：

```bash
# 更新 RubyGems（可能需要 sudo）
gem update --system
```

## 其他问题

如果遇到其他问题，请检查：
1. Ruby 版本是否符合要求（Jekyll 通常需要 Ruby 2.5+）
2. 是否已安装 Bundler：`gem install bundler`
3. 网络连接是否正常（需要访问 rubygems.org）

