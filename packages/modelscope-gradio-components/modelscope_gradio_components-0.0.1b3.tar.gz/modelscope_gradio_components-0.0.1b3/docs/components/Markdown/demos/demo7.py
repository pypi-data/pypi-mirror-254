import json
import os

import gradio as gr

import modelscope_gradio_components as mgr

options = ["a", "b", "c"]


def resolve_assets(relative_path):
    return os.path.join(os.path.dirname(__file__), "../resources",
                        relative_path)


with open(resolve_assets("./custom_components/custom_select.js"), 'r') as f:
    custom_select_js = f.read()


# 注意一定要显示指明类型，gradio 使用 ioc 机制注入值
def fn(data: gr.EventData):
    # custom {'index': [0, 1], 'tag': 'custom-select', 'tag_index': 0, 'value': 'option A'}
    print("custom value", data._data)


with gr.Blocks() as demo:
    md = mgr.Markdown(value=f"""
custom tag: <custom-select options='{json.dumps(options)}'></custom-select>
""",
                      custom_components={
                          "custom-select": {
                              "props": ["options"],
                              "js": custom_select_js,
                          }
                      })
    md.custom(fn=fn)

if __name__ == "__main__":
    demo.queue().launch()
