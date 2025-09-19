# GitHub Actions 自动运行部署指南

## 🎯 功能介绍
- ✅ **每天自动运行1小时** - 定时访问医院网站
- ✅ **自动记录进度** - 记住访问到哪个网址
- ✅ **断点续传** - 下次从上次位置继续
- ✅ **循环访问** - 全部访问完后重新开始
- ✅ **完全免费** - GitHub Actions免费额度够用

## 📋 部署步骤（小白专用）

### 第一步：创建GitHub仓库
1. 打开 [GitHub官网](https://github.com/)
2. 点击右上角的 **"+"** → **"New repository"**
3. 仓库名称填写：`hospital-contact`（或其他你喜欢的名字）
4. 选择 **"Public"**（公开仓库）
5. 勾选 **"Add a README file"**
6. 点击 **"Create repository"**

### 第二步：上传程序文件
把我们准备好的文件上传到GitHub：

需要上传的文件：
- `api.txt` - 医院网址列表
- `github_daily_run.py` - 主要运行程序
- `requirements.txt` - 依赖包列表
- `.github/workflows/daily-run.yml` - GitHub Actions配置

#### 上传方法1：网页上传（推荐）
1. 进入你的仓库页面
2. 点击 **"Add file"** → **"Upload files"**
3. 拖拽文件到上传区域
4. 点击 **"Commit changes"**

#### 上传方法2：Git命令（高级用户）
```bash
git add .
git commit -m "添加医院联系程序"
git push origin main
```

### 第三步：配置GitHub Actions
1. 进入你的仓库
2. 点击 **"Actions"** 选项卡
3. 点击 **"set up a workflow yourself"**
4. 把 `.github/workflows/daily-run.yml` 文件内容复制进去
5. 点击 **"Start commit"**

### 第四步：修改配置（重要）

#### 修改手机号和姓名
打开 `github_daily_run.py` 文件，修改：
```python
TEL_NUMBER = '你的手机号'  # 改成你的手机号
TEL_NAME = '你的名字'      # 改成你的姓名
```

#### 修改运行时间（可选）
打开 `.github/workflows/daily-run.yml` 文件，修改：
```yaml
cron: '0 8 * * *'  # 现在是每天8点（UTC时间）
```

**时间对照表：**
- `0 8 * * *` = 北京时间下午4点
- `0 0 * * *` = 北京时间上午8点
- `0 16 * * *` = 北京时间凌晨0点

### 第五步：启动运行
1. 进入 **"Actions"** 页面
2. 点击 **"Run workflow"** 按钮
3. 选择 **"Run workflow"** 立即测试

## 📊 监控运行状态

### 查看运行日志
1. 进入 **"Actions"** 页面
2. 点击最新的workflow运行记录
3. 点击 **"build"** 查看详细日志

### 查看进度数据
运行完成后，在 **"Actions"** 页面下载：
- `progress-data` - 包含运行进度
- `run-logs` - 包含详细日志

## ⚙️ 工作原理

### 定时机制
- **每天早上自动启动**（可修改时间）
- **运行1小时后自动停止**
- **保存当前进度**
- **第二天继续从上次位置开始**

### 进度记录
- 自动记录处理到第几个网址
- 记录完成的循环次数
- 所有数据自动保存到GitHub

### 循环访问
- 第一次：从第1个网址开始
- 第二次：从上次结束位置继续
- 全部完成后：重新回到第1个开始

## 🔧 常见问题解决

### Q1: 运行失败了怎么办？
**A:** 查看Actions日志，常见问题：
- 依赖包安装失败 → 检查requirements.txt
- 网址访问失败 → 检查网络连接
- 超时错误 → 正常现象，1小时到了

### Q2: 如何修改运行时间？
**A:** 修改 `.github/workflows/daily-run.yml` 中的cron表达式

### Q3: 如何手动触发运行？
**A:** 进入Actions页面，点击 **"Run workflow"**

### Q4: 免费额度够用吗？
**A:** GitHub Actions每月2000分钟免费额度，我们的程序每天用60分钟，完全够用！

## 📱 手机查看方法

### 下载GitHub App
- **iOS**: App Store搜索"GitHub"
- **Android**: Google Play搜索"GitHub"

### 查看运行状态
1. 打开GitHub App
2. 进入你的仓库
3. 点击"Actions"查看运行状态

## 🎯 总结

**优点：**
- ✅ 完全免费
- ✅ 自动运行
- ✅ 手机监控
- ✅ 断点续传
- ✅ 循环访问

**限制：**
- ⚠️ 每天最多1小时（GitHub限制）
- ⚠️ 需要网络连接
- ⚠️ 不能访问需要验证码的网站

## 🚀 开始部署吧！

按照上面的步骤，一步一步来！
有问题随时问我！😊

**下一步：** 告诉我你创建好GitHub仓库了吗？我帮你检查配置！