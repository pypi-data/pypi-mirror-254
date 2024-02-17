import os

import gradio as gr

import modelscope_gradio_components as mgr


def resolve_assets(relative_path):
    return os.path.join(os.path.dirname(__file__), "../resources",
                        relative_path)


conversation = [
    [
        None, {
            "text": f"""
图片

![image]({resolve_assets("bot.jpeg")})

<img src="{resolve_assets("user.jpeg")}" />

视频

<video src="{resolve_assets("dog.mp4")}"></video>

音频

<audio src="{resolve_assets("audio.wav")}"></audio>
""",
            "flushing": False
        }
    ],
]

with gr.Blocks() as demo:
    mgr.Chatbot(
        value=conversation,
        height=600,
    )

if __name__ == "__main__":
    demo.queue().launch()
