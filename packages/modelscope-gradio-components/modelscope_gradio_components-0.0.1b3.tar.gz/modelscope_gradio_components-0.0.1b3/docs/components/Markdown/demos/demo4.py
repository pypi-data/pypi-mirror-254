import gradio as gr

import modelscope_gradio_components as mgr

with gr.Blocks() as demo:
    mgr.Markdown(
        f"""
custom tag:<custom-tag value="aaa"></custom-tag>
""",
        custom_components={
            # key 为标签名
            "custom-tag": {
                # 自定义标签允许接收的值，可在调用标签时由用户传入
                "props": ["value"],
                # 实际渲染时的 template, 可以使用 {} 将用户传入的 props 替换。
                "template": "<div>{value}</div>"
            }
        })

if __name__ == "__main__":
    demo.queue().launch()
