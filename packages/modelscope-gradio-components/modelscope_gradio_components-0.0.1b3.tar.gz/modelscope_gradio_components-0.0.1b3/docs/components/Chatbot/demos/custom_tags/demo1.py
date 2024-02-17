import json
import os

import gradio as gr

import modelscope_gradio_components as mgr

options = [{"label": "A", "value": "a"}, "b", "c"]

conversation = [[
    None,
    f"""Single Select: <select-box options='{json.dumps(options)}' select-once></select-box>

Multiple Select：<select-box type="checkbox" options='{json.dumps(options)}' select-once submit-text="Submit"></select-box>

Vertical Direction：

<select-box direction="vertical" type="checkbox" options='{json.dumps(options)}' select-once submit-text="Submit"></select-box>
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
