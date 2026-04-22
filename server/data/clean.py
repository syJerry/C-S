#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re


def clean_newlines_simple(input_file, output_file=None):
    """
    简化版：处理单个文件
    """
    # 读取文件
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # 使用正则表达式处理
    # 将奇数个连续的换行符替换为\n\n
    # 这里使用了一个技巧：将两个\n替换为特殊字符，然后删除所有单个\n，最后恢复
    result = re.sub(r'\n{3,}', lambda m: '\n\n' + '\n' * ((len(m.group()) - 2) % 2), content)
    result = result.replace('\n\n', 'TEMP_DOUBLE_NEWLINE')
    result = result.replace('\n', '')
    result = result.replace('TEMP_DOUBLE_NEWLINE', '\n\n')

    # 写入文件
    if output_file is None:
        output_file = input_file

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(result)

    print(f"处理完成！结果已保存到: {output_file}")


# 使用示例
if __name__ == "__main__":
    # 直接调用
    clean_newlines_simple("blog_clean.txt", "blog_clean_1.txt")

    # 或者覆盖原文件
    # clean_newlines_simple("input.txt")