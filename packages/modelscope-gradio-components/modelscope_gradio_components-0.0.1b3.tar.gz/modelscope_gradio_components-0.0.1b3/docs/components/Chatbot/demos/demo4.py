import time

import gradio as gr

import modelscope_gradio_components as mgr


def submit(_chatbot):
    _chatbot.append(["test user", "test bot"])  # 此时只有 bot 会开启打字机效果
    yield _chatbot
    time.sleep(2)
    _chatbot.append(["test user", {
        "text": "test bot",
        "flushing": False
    }])  # 两者都没有打字机效果
    yield _chatbot
    time.sleep(2)
    _chatbot.append([{
        "text": "test user",
        "flushing": True
    }, {
        "text": "test bot",
        "flushing": False
    }])  # user 会开启打字机效果
    yield _chatbot


with gr.Blocks() as demo:
    chatbot = mgr.Chatbot(height=600, )
    button = gr.Button("Submit")
    button.click(fn=submit, inputs=[chatbot], outputs=[chatbot])

if __name__ == "__main__":
    demo.queue().launch()
