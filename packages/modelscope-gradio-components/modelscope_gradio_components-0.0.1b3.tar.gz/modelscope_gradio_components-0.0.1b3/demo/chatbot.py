import gradio as gr
import modelscope_gradio_components as mgr
from modelscope_gradio_components.components.Chatbot.llm_thinking_presets import qwen
import time
import os


bot_msg1 = f"""
<场景描述>：你在古墓派的后山修炼内功，突然听到远处传来一阵异样的声音。你决定去查看一下。

调用工具：
Action: image_gen
Action Input: {{"text": "小龙女在古墓派后山修炼内功", "resolution": "1280*720"}}
Observation:
"""

bot_msg2 = f"""
<场景描述>：你在古墓派的后山修炼内功，突然听到远处传来一阵异样的声音。你决定去查看一下。

调用工具：
Action: image_gen
Action Input: {{"text": "小龙女在古墓派后山修炼内功", "resolution": "1280*720"}}
Observation: <result>![IMAGEGEN](https://dashscope-result-bj.oss-cn-beijing.aliyuncs.com/1d/f1/20231207/8d820c8d/463b323b-6209-4095-b1c3-f7c4dd337e6c-1.png?Expires=1702002840&OSSAccessKeyId=LTAI5tQZd8AEcZX6KZV4G8qL&Signature=zg6mIsIU3XDNrQxhwNWSt9QWTDI%3D)</result>
![小龙女在古墓派后山修炼内功](https://dashscope-result-bj.oss-cn-beijing.aliyuncs.com/1d/f1/20231207/8d820c8d/463b323b-6209-4095-b1c3-f7c4dd337e6c-1.png?Expires=1702002840&OSSAccessKeyId=LTAI5tQZd8AEcZX6KZV4G8qL&Signature=zg6mIsIU3XDNrQxhwNWSt9QWTDI%3D)

<选择>：
A: 继续修炼，不理睬那声音。
B: 走向声音的来源，查看发生了什么。
C: 召唤你的蜜蜂去调查情况。
D: 输入玩家的选择。

"""

conversation = [
    [None, {"text": "Hello I'm a chatbot", "flushing": False}],
]


def fn(input, chatbot):
    chatbot.append([input, None])
    yield chatbot
    time.sleep(3)
    chatbot[-1][1] = {"text": bot_msg1, "flushing": True}
    yield chatbot
    time.sleep(10)
    chatbot[-1][1] = {"text": bot_msg2, "flushing": True}
    yield chatbot


with gr.Blocks() as demo:
    chatbot = mgr.Chatbot(value=conversation, height=500, avatar_images=[os.path.join(os.path.dirname(__file__), 'avatar.jpeg'), os.path.join(
        os.path.dirname(__file__), 'avatar.jpeg')], llm_thinking_presets=[qwen()])
    input = gr.Textbox(label="Input")
    btn = gr.Button("Send")
    btn.click(fn=fn, inputs=[input, chatbot], outputs=[chatbot])

demo.queue().launch()
