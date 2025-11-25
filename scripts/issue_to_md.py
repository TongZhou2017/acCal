import os
import json
import sys
from datetime import datetime


# 文件路径和文件名生成函数
def slugify(text):
    """将标题转换为文件名友好的slug"""
    import re
    import unicodedata
    
    # 转换为小写
    text = text.lower()
    
    # 处理中文字符：保留中文，转换为拼音或使用日期+标题前几个字符
    # 为了简化，我们使用日期+标题前10个字符的哈希值
    # 或者直接使用日期和标题的组合
    
    # 移除特殊字符，但保留中文、英文、数字、空格和连字符
    text = re.sub(r'[^\w\s-]', '', text)
    
    # 将多个空格/连字符替换为单个连字符
    text = re.sub(r'[\s_-]+', '-', text)
    
    # 移除首尾的连字符
    text = text.strip('-')
    
    # 如果结果为空（全是中文被移除），使用日期+标题前几个字符
    if not text or len(text) < 3:
        # 使用日期和标题的简单组合
        date_part = datetime.now().strftime('%Y%m%d')
        # 取标题的前几个字符（如果有的话）
        title_part = ''.join([c for c in text[:10] if c.isalnum()])[:10]
        text = f"{date_part}-{title_part}" if title_part else date_part
    
    # 限制文件名长度
    if len(text) > 100:
        text = text[:100]
    
    return text


def generate_markdown(issue_data_json):
    """将Issue数据转换为Hugo/Jekyll使用的Markdown文件"""
    
    # 解析 Issue 数据
    data = issue_data_json

    # 提取核心字段，并清理 tags
    tags_list = [tag.strip() for tag in data.get('tags', '').split(',') if tag.strip()]
    
    # 转换为 YAML Front Matter 格式
    front_matter = {
        "title": data['conf_name'],
        "discipline": data['discipline_group'],
        "location": data.get('location', 'TBD'),
        "date_start": data['date_start'],
        "date_end": data.get('date_end', data['date_start']), # 如果结束日期缺失，使用开始日期
        "deadline": data.get('deadline', 'N/A'),
        "url": data['url'],
        "tags": tags_list,
        "submitted_by": data.get('submitter_name', os.environ.get('ISSUE_AUTHOR', 'Community')), # 实际Action中会获取提交者
        "publishDate": datetime.now().isoformat(),
        "draft": True # 初始状态为草稿，等待人工审核
    }

    # 格式化 Front Matter
    yaml_fm = "---"
    for key, value in front_matter.items():
        if isinstance(value, list):
            yaml_fm += f"\n{key}: {json.dumps(value)}"
        else:
            yaml_fm += f"\n{key}: \"{value}\""
    yaml_fm += "\n---\n"
    
    # 文件主体内容（可为空或添加描述）
    content = f"\n\n请在审核时补充会议简介...\n"
    
    markdown_content = yaml_fm + content
    
    # 生成文件名：使用日期+标题的组合，确保唯一性和可读性
    date_str = data.get('date_start', datetime.now().strftime('%Y%m%d')).replace('-', '')
    title_slug = slugify(data['conf_name'])
    filename = f"{date_str}-{title_slug}" if title_slug else f"{date_str}-conference"
    
    # 写入文件到内容目录
    output_dir = "content"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    output_path = os.path.join(output_dir, f"{filename}.md")
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(markdown_content)
        
    print(f"成功生成文件: {output_path}")
    return output_path


# --- 模拟 Action 运行环境 ---
if __name__ == "__main__":
    # 在 GitHub Action 中，issue_data 会通过 ENV 或 STDIN 传递。
    # 这里我们用一个模拟的 JSON 字符串代替实际的 Issue 数据。
    
    # 检查是否在 GitHub Actions 环境中
    issue_data_env = os.environ.get('ISSUE_DATA')
    
    if issue_data_env:
        # 从环境变量读取 Issue 数据（GitHub Actions 环境）
        try:
            issue_data = json.loads(issue_data_env)
        except json.JSONDecodeError as e:
            print(f"解析 ISSUE_DATA 环境变量失败: {e}", file=sys.stderr)
            sys.exit(1)
    else:
        # 模拟 Issue 表单提交的数据 (本地测试用)
        issue_data = {
            "conf_name": "第六届全国进化生态学研讨会",
            "discipline_group": "🌿 生命科学 (Life Sciences)",
            "location": "上海·复旦大学",
            "date_start": "2026-04-10",
            "date_end": "2026-04-12",
            "deadline": "2026-02-15",
            "tags": "进化, 生态学, 植物学",
            "url": "http://www.evo-eco.cn/conf2026",
        }
        print("⚠️  未检测到 ISSUE_DATA 环境变量，使用模拟数据...")
    
    try:
        generate_markdown(issue_data)
        print("---")
        print("Python脚本运行成功，请在 'content/' 目录查看生成的 Markdown 文件。")
    except Exception as e:
        print(f"脚本运行失败: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc()
        sys.exit(1)

