import re
import sys
from pathlib import Path


def remove_div_blocks(text: str) -> str:
    # 匹配单行或多行的 <div ...>...</div> 块
    pattern = r'<div\b[^>]*>.*?</div>'
    cleaned = re.sub(pattern, '', text, flags=re.DOTALL | re.IGNORECASE)
    # 清理可能产生的多余空行（超过2个连续空行压缩为1个）
    cleaned = re.sub(r'\n{3,}', '\n\n', cleaned)
    return cleaned


def process_directory(root_dir: str):
    root = Path(root_dir)
    md_files = list(root.rglob('*.md'))
    
    if not md_files:
        print("未找到任何 .md 文件")
        return

    for md_file in md_files:
        original = md_file.read_text(encoding='utf-8')
        cleaned = remove_div_blocks(original)
        
        if cleaned != original:
            md_file.write_text(cleaned, encoding='utf-8')
            print(f"✅ 已处理: {md_file}")
        else:
            print(f"⏭️  无需处理: {md_file}")

    print(f"\n完成，共扫描 {len(md_files)} 个文件")


if __name__ == '__main__':
    target = sys.argv[1] if len(sys.argv) > 1 else '.'
    process_directory(target)