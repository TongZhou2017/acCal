#!/usr/bin/env python3
"""
生成详细的 PR Body，包含信息摘要表格和完整内容
"""
import os
import json
import sys
from datetime import datetime
import re

def parse_date(date_str):
    """解析日期字符串"""
    if not date_str or date_str.strip() == '':
        return None, None
    date_str = date_str.strip()
    # 处理格式：2025年12月10-13日
    match = re.search(r'(\d{4})年(\d{1,2})月(\d{1,2})(?:-(\d{1,2}))?日?', date_str)
    if match:
        year = match.group(1)
        month = match.group(2).zfill(2)
        day_start = match.group(3).zfill(2)
        day_end = match.group(4).zfill(2) if match.group(4) else None
        start_date = f"{year}-{month}-{day_start}"
        end_date = f"{year}-{month}-{day_end}" if day_end else None
        return start_date, end_date
    return date_str, None

def validate_url(url):
    """验证 URL 格式"""
    if not url:
        return False, "URL 为空"
    url = url.strip()
    if url.startswith(('http://', 'https://')):
        return True, "格式正确"
    return False, "URL 应以 http:// 或 https:// 开头"

def check_completeness(data):
    """检查数据完整性"""
    required_fields = {
        'conf_name': '会议名称',
        'discipline_group': '一级学科分类',
        'date_start': '会议时间',
        'url': '官方网址'
    }
    
    missing = []
    for field, name in required_fields.items():
        value = data.get(field, '').strip()
        if not value:
            missing.append(name)
    
    return len(missing) == 0, missing

def format_field_value(value, max_length=100):
    """格式化字段值，限制长度"""
    if not value:
        return "*(未填写)*"
    value_str = str(value).strip()
    if len(value_str) > max_length:
        return value_str[:max_length] + "..."
    return value_str

def generate_pr_body(issue_data_json, issue_number, issue_author, issue_url):
    """生成详细的 PR Body"""
    data = issue_data_json
    
    # 字段映射
    field_mapping = {
        '1_': 'conf_name',
        '2_': 'edition',
        '3_': 'discipline_group',
        '4_': 'tags',
        '5_': 'location',
        '6__yyyymmdd': 'date_start',
        '7__yyyymmdd': 'deadline',
        '8___': 'url',
        '9_': 'description',
    }
    
    mapped_data = {}
    for parser_key, standard_key in field_mapping.items():
        if parser_key in data:
            mapped_data[standard_key] = data[parser_key]
    
    # 兼容旧格式
    for key in ['conf_name', 'edition', 'discipline_group', 'tags', 'location', 
                 'date_start', 'deadline', 'url', 'description']:
        if key in data and key not in mapped_data:
            mapped_data[key] = data[key]
    
    # 提取字段值
    conf_name = mapped_data.get('conf_name', '').strip()
    edition = mapped_data.get('edition', '').strip()
    discipline = mapped_data.get('discipline_group', '').strip()
    tags = mapped_data.get('tags', '').strip()
    location = mapped_data.get('location', '').strip()
    date_start_raw = mapped_data.get('date_start', '').strip()
    deadline_raw = mapped_data.get('deadline', '').strip()
    url = mapped_data.get('url', '').strip()
    description = mapped_data.get('description', '').strip()
    
    # 解析日期
    date_start, date_end = parse_date(date_start_raw)
    deadline, _ = parse_date(deadline_raw)
    
    # 验证完整性
    is_complete, missing_fields = check_completeness(mapped_data)
    
    # 验证 URL
    url_valid, url_message = validate_url(url)
    
    # 生成 PR Body
    body = f"""## 📋 会议信息摘要

| 项目 | 状态 | 内容 |
|------|------|------|
| **会议名称** | {'✅' if conf_name else '❌'} | {format_field_value(conf_name)} |
| **届数** | {'✅' if edition else '⚠️ 可选'} | {format_field_value(edition) if edition else '*(未填写)*'} |
| **学科分类** | {'✅' if discipline else '❌'} | {format_field_value(discipline)} |
| **细分标签** | {'✅' if tags else '❌'} | {format_field_value(tags)} |
| **会议地点** | {'✅' if location else '⚠️ 可选'} | {format_field_value(location) if location else '*(未填写)*'} |
| **会议时间** | {'✅' if date_start else '❌'} | {format_field_value(date_start_raw)} |
| **截止日期** | {'✅' if deadline else '⚠️ 可选'} | {format_field_value(deadline_raw) if deadline_raw else '*(未填写)*'} |
| **官方网址** | {'✅' if url_valid else '❌'} | {format_field_value(url, 80)} |
| **会议简介** | {'✅' if description else '⚠️ 可选'} | {format_field_value(description, 200) if description else '*(未填写)*'} |

### 📊 完整性检查

"""
    
    if is_complete:
        body += "✅ **所有必需字段已填写**\n\n"
    else:
        body += f"❌ **缺少必需字段**: {', '.join(missing_fields)}\n\n"
    
    if url_valid:
        body += "✅ **URL 格式正确**\n\n"
    else:
        body += f"❌ **URL 格式错误**: {url_message}\n\n"
    
    # 日期格式检查
    if date_start and re.match(r'^\d{4}-\d{2}-\d{2}$', date_start):
        body += "✅ **日期格式正确**\n\n"
    elif date_start_raw:
        body += f"⚠️ **日期格式**: {date_start_raw} (已自动解析为 {date_start})\n\n"
    
    body += f"""---

## 📝 完整信息详情

### 基本信息

- **会议名称**: {conf_name if conf_name else '*(未填写)*'}
- **届数**: {edition if edition else '*(未填写)*'}
- **学科分类**: {discipline if discipline else '*(未填写)*'}
- **细分标签**: {tags if tags else '*(未填写)*'}
- **会议地点**: {location if location else '*(未填写)*'}

### 时间信息

- **会议时间**: {date_start_raw if date_start_raw else '*(未填写)*'}
  - 解析后开始日期: {date_start if date_start else '*(无法解析)*'}
  - 解析后结束日期: {date_end if date_end else date_start if date_start else '*(无法解析)*'}
- **截止日期**: {deadline_raw if deadline_raw else '*(未填写)*'}
  - 解析后日期: {deadline if deadline else '*(无法解析)*'}

### 链接信息

- **官方网址**: {url if url else '*(未填写)*'}
  - URL 验证: {'✅ 通过' if url_valid else f'❌ {url_message}'}

### 会议简介

{description if description else '*(未填写)*'}

---

## 🔗 相关信息

- **来源 Issue**: [#{issue_number}]({issue_url})
- **提交者**: @{issue_author}
- **生成时间**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

---

## ⚠️ 审核提示

1. **URL 验证**: 请确认官方网址是否为官方信息源，拒绝第三方中介链接
2. **会议真实性**: 请验证会议是否为合法学术会议，拒绝掠夺性会议
3. **信息准确性**: 请核对日期、地点等信息是否准确
4. **格式检查**: 确认生成的 Markdown 文件格式正确
5. **⚠️ 重要**: 合并前请将会议文件的 `draft: true` 改为 `draft: false`，否则会议不会在网站上显示

### 📝 如何发布会议

合并 PR 后，需要手动编辑会议文件，将 `draft: true` 改为 `draft: false`：

```yaml
draft: false  # 改为 false 后会议才会在网站上显示
```

或者，如果审核通过，可以在合并 PR 时直接修改文件中的 `draft` 字段。

**此 PR 由 Issue #{issue_number} 自动生成，合并后将自动关闭该 Issue。**
"""
    
    return body

if __name__ == "__main__":
    issue_data_env = os.environ.get('ISSUE_DATA')
    issue_number = os.environ.get('ISSUE_NUMBER', '')
    issue_author = os.environ.get('ISSUE_AUTHOR', '')
    issue_url = os.environ.get('ISSUE_URL', f'https://github.com/{os.environ.get("GITHUB_REPOSITORY", "")}/issues/{issue_number}')
    
    if issue_data_env:
        try:
            issue_data = json.loads(issue_data_env)
            pr_body = generate_pr_body(issue_data, issue_number, issue_author, issue_url)
            
            # 使用包含 Issue 号的唯一文件名，避免并发写入冲突
            if issue_number:
                pr_body_file = f'pr_body_issue_{issue_number}.txt'
            else:
                # 如果没有 Issue 号，使用时间戳作为唯一标识
                timestamp = datetime.now().strftime('%Y%m%d_%H%M%S_%f')
                pr_body_file = f'pr_body_{timestamp}.txt'
            
            # 输出到文件，供工作流使用
            with open(pr_body_file, 'w', encoding='utf-8') as f:
                f.write(pr_body)
            
            # 同时输出文件名到标准输出，供工作流读取
            print(f"PR_BODY_FILE={pr_body_file}")
            print("✅ PR Body 生成成功")
            print("=" * 50)
            print(pr_body)
        except Exception as e:
            print(f"❌ 生成 PR Body 失败: {e}", file=sys.stderr)
            sys.exit(1)
    else:
        print("⚠️  未检测到 ISSUE_DATA 环境变量", file=sys.stderr)
        sys.exit(1)

