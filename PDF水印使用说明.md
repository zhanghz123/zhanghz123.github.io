# PDF批量添加水印工具使用说明

## 功能介绍
这个Python脚本可以批量给 `hub` 文件夹及其所有子文件夹中的PDF文件添加水印。

## 使用步骤

### 1. 安装Python
确保你的电脑已安装Python 3.7或更高版本。
- 检查是否安装：在命令行输入 `python --version`
- 如果未安装，访问 https://www.python.org/downloads/ 下载安装

### 2. 安装依赖包
在命令行中执行以下命令：

```bash
cd "D:\claude code\张老成的个人网站"
pip install -r requirements.txt
```

或者直接安装：
```bash
pip install pymupdf
```

### 3. 运行脚本
在命令行中执行：

```bash
cd "D:\claude code\张老成的个人网站"
python add_watermark.py
```

### 4. 按照提示操作
- 脚本会显示将要处理的PDF文件数量
- 输入 `y` 确认开始处理
- 等待处理完成

## 配置选项

你可以编辑 `add_watermark.py` 文件来修改以下选项：

| 选项 | 说明 | 默认值 |
|------|------|--------|
| `hub_folder` | 要处理的文件夹路径 | `D:\claude code\张老成的个人网站\hub` |
| `watermark_text` | 水印文字内容 | `张老成个人网站 · 内容仅供在线浏览` |
| `create_backup` | 是否创建备份文件 | `True` |

## 备份机制

- 脚本默认会为每个PDF文件创建备份（文件名后加 `.bak`）
- 处理完成后，原PDF文件会被添加水印
- 如需恢复，删除带水印的文件，将 `.bak` 文件重命名即可

## 水印效果

- 水印颜色：浅灰色
- 水印透明度：15%
- 水印旋转角度：25度
- 水印布局：每页多个水印平铺

## 注意事项

1. 处理大量PDF文件可能需要一些时间，请耐心等待
2. 建议先备份整个 `hub` 文件夹，以防意外
3. 处理后的PDF文件会覆盖原文件（除非修改配置）
4. 如遇到问题，可以使用 `.bak` 备份文件恢复

## 故障排除

**问题1：找不到PDF文件**
- 检查 `hub_folder` 路径是否正确
- 确保文件夹中有PDF文件

**问题2：处理失败**
- 确保PDF文件没有被其他程序打开
- 检查是否有足够的磁盘空间

**问题3：水印效果不明显**
- 编辑脚本中的 `watermark_opacity` 值（0-1之间，越大越深）
- 编辑脚本中的 `watermark_color` 调整颜色

## 恢复备份

如果需要恢复所有文件：

```bash
# 删除带水印的文件
del /s "*.pdf"

# 恢复备份文件
for /r %i in (*.bak) do ren "%i" "%~ni"
```

或在脚本中将 `create_backup` 设为 `False` 后重新运行
