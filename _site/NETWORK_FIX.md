# 网络问题解决方案

## 问题
如果遇到 `bundle install` 时网络超时，可以使用国内镜像源。

## 解决方案

### 使用 Ruby China 镜像（推荐）

```bash
# 配置镜像源
bundle config mirror.https://rubygems.org https://gems.ruby-china.com

# 然后重新安装
bundle install
```

### 或者使用淘宝镜像

```bash
# 配置淘宝镜像
bundle config mirror.https://rubygems.org https://ruby.taobao.org

# 然后重新安装
bundle install
```

### 恢复默认源（如果需要）

```bash
bundle config --delete mirror.https://rubygems.org
```

## 当前状态

✅ 已配置 Ruby China 镜像源
✅ 依赖安装成功
✅ Jekyll 服务器已启动

访问：`http://localhost:4000/acCal/`

