import os
import re
from typing import Callable

from gradio import processing_utils, utils
from gradio.components import Component


def process_html_links(html: str, transformer: Callable):
    # 匹配HTML字符串中的src属性值
    src_regex = re.compile(r'src=["\'](.*?)["\']')
    img_src_regex = re.compile(r'"imgSrc": *"(.*?)"')

    def replace_src(type):

        def replace(match):
            # 获取src属性值
            src = match.group(1)
            # 用回调函数处理src属性值，并获取新的URL地址
            new_url = transformer(src) if transformer else src
            if (type == "src"):
                # 返回新的替换后的字符串
                return f'src="{new_url}"'
            elif (type == "imgSrc"):
                return f'"imgSrc": "{new_url}"'

        return replace

    # 使用re.sub替换HTML字符串中的src属性值
    html = src_regex.sub(replace_src("src"), html)
    html = img_src_regex.sub(replace_src("imgSrc"), html)
    return html


def process_markdown_links(markdown: str, transformer: Callable):
    # 正则表达式用于匹配 Markdown 链接
    link_pattern = r"\[(.*?)\]\((.*?)\)"
    file_pattern = r":file\[(.*?)\]"

    def replace_link(match):
        # 获取链接文本和链接地址
        text = match.group(1)
        url = match.group(2)

        # 调用回调函数处理链接并返回新的链接地址
        new_url = transformer(url) if transformer else url

        # 构造新的 Markdown 链接
        new_link = f"[{text}]({new_url})"

        return new_link

    def replace_file(match):
        # 获取链接文本和链接地址
        url = match.group(1)

        # 调用回调函数处理链接并返回新的链接地址
        new_url = transformer(url) if transformer else url

        # 构造新的 Markdown 链接
        new_link = f"::file[{new_url}]"

        return new_link

    # 使用正则表达式替换链接
    new_markdown = re.sub(link_pattern, replace_link, markdown)
    new_markdown = re.sub(file_pattern, replace_file, new_markdown)

    return new_markdown


def process_links(text: str, block: Component):

    def links_transformer(src: str):
        if (src.startswith("http") or src.startswith("https")):
            return src

        file_path = str(utils.abspath(src))
        if (not os.path.exists(file_path)):
            return src
        return f"/file={processing_utils.move_resource_to_block_cache(file_path, block)}"

    return process_html_links(process_markdown_links(text, links_transformer),
                              links_transformer)
