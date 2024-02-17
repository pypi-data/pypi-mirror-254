import json

import gradio as gr

import modelscope_gradio_components as mgr

options = [{"label": "A", "value": "a"}, "b", "c"]


def fn(data: gr.EventData):
    custom_data = data._data
    if (custom_data["tag"] == "select-box"):
        print(custom_data["value"])  # 用户选择的值，与 options 中的 value 对应


with gr.Blocks() as demo:
    md = mgr.Markdown(
        f"<select-box options='{json.dumps(options)}' select-once></select-box>"
    )
    md.custom(fn=fn)

if __name__ == "__main__":
    demo.queue().launch()
