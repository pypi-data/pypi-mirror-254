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

conversation = [[
    None, f"""
custom tag: <custom-select options='{json.dumps(options)}'></custom-select>
"""
]]

with gr.Blocks() as demo:
    chatbot = mgr.Chatbot(value=conversation,
                          flushing=False,
                          height=600,
                          custom_components={
                              "custom-select": {
                                  "props": ["options"],
                                  "js": custom_select_js,
                              }
                          })

if __name__ == "__main__":
    demo.queue().launch()
