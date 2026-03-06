#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PDF批量添加水印脚本
功能：遍历指定文件夹及其子文件夹，为所有PDF文件添加水印
"""

import os
import sys
import fitz
import shutil
import tempfile
from pathlib import Path


def add_watermark_to_pdf(input_pdf_path, watermark_text="张老成个人网站 内容仅供在线浏览"):
    """
    给PDF文件添加水印

    Args:
        input_pdf_path: 输入PDF文件路径
        watermark_text: 水印文字内容
    """
    try:
        doc = fitz.open(input_pdf_path)

        for page in doc:
            rect = page.rect
            width = rect.width
            height = rect.height

            # 使用浅灰色
            color = (0.5, 0.5, 0.5)
            font_size = min(width, height) / 30

            # 添加多个水印，形成平铺效果
            rows = 6
            cols = 4
            for i in range(rows):
                for j in range(cols):
                    x = (width / cols) * j + width / 8
                    y = (height / rows) * i + height / 8
                    test_point = fitz.Point(x, y)
                    page.insert_text(test_point, watermark_text, fontsize=font_size, color=color)

        # 创建备份
        backup_path = str(input_pdf_path) + '.bak'
        if not os.path.exists(backup_path):
            shutil.copy2(input_pdf_path, backup_path)

        # 保存到临时文件（避免加密问题）
        with tempfile.NamedTemporaryFile(delete=False, suffix='.pdf') as tmp:
            tmp_path = tmp.name

        doc.save(tmp_path, deflate=True)
        doc.close()

        # 用临时文件替换原文件
        shutil.move(tmp_path, input_pdf_path)

        return True, os.path.basename(input_pdf_path)

    except Exception as e:
        return False, f'{os.path.basename(input_pdf_path)}: {str(e)}'


def batch_add_watermark(folder_path, watermark_text="张老成个人网站 内容仅供在线浏览"):
    """
    批量处理文件夹中的所有PDF文件

    Args:
        folder_path: 要处理的文件夹路径
        watermark_text: 水印文字内容
    """
    folder_path = Path(folder_path)

    if not folder_path.exists():
        print(f"错误: 文件夹不存在 - {folder_path}")
        return

    # 查找所有PDF文件
    pdf_files = sorted(list(folder_path.rglob("*.pdf")))

    if not pdf_files:
        print(f"在 {folder_path} 中没有找到PDF文件")
        return

    print(f"找到 {len(pdf_files)} 个PDF文件")
    print(f"水印文字: {watermark_text}")
    print("-" * 60)

    success_count = 0
    fail_count = 0

    for i, pdf_file in enumerate(pdf_files, 1):
        success, message = add_watermark_to_pdf(str(pdf_file), watermark_text)

        if success:
            success_count += 1
            print(f"[{i}/{len(pdf_files)}] OK - {message}")
        else:
            fail_count += 1
            print(f"[{i}/{len(pdf_files)}] FAIL - {message}")

    print("-" * 60)
    print(f"处理完成: 成功 {success_count} 个, 失败 {fail_count} 个")
    print(f"备份文件已创建，文件名为原文件名 + .bak")


def main():
    """主函数"""
    # 设置要处理的文件夹路径
    hub_folder = r"D:\claude code\张老成的个人网站\hub"

    # 水印文字（可修改）
    watermark_text = "张老成个人网站 内容仅供在线浏览"

    print("=" * 60)
    print("PDF批量添加水印工具")
    print("=" * 60)
    print(f"目标文件夹: {hub_folder}")
    print(f"水印文字: {watermark_text}")
    print("=" * 60)
    print()

    # 开始批量处理
    batch_add_watermark(hub_folder, watermark_text)


if __name__ == "__main__":
    main()
