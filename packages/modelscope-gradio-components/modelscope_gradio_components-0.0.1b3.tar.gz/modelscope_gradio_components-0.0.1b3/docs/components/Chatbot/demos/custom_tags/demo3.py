import json
import os

import gradio as gr

import modelscope_gradio_components as mgr

# card 支持额外传入 imgSrc 属性作为样式封面
options = [{
    "label":
    "A",
    "imgSrc":
    os.path.join(os.path.dirname(__file__), '../../resources/screen.jpeg'),
    "value":
    "a"
}, "b", "c", "d"]
# 填入 item-width="auto"
conversation = [[
    None, f"""
<select-box shape="card" direction="vertical" options='{json.dumps(options)}' select-once item-width="auto"></select-box>
"""
]]

with gr.Blocks() as demo:
    chatbot = mgr.Chatbot(
        value=conversation,
        flushing=False,
        height=600,
    )

if __name__ == "__main__":
    demo.queue().launch()
