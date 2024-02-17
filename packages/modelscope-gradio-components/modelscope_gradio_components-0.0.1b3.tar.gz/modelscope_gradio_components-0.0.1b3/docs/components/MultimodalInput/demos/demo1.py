import gradio as gr

import modelscope_gradio_components as mgr


def fn(value):
    # value 包含 text 与 files
    print(value.text, value.files)


with gr.Blocks() as demo:
    input = mgr.MultimodalInput()
    input.change(fn=fn, inputs=[input])

if __name__ == "__main__":
    demo.queue().launch()
