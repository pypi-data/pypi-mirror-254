import os
import time

import gradio as gr

import modelscope_gradio_components as mgr
from modelscope_gradio_components.components.Chatbot.llm_thinking_presets import \
  qwen

bot_msg1 = f"""
开始测试
```js
import React from 'react';
console.log(React)
```

It is a very cute dog <a href='http://www.modelscope.cn'>ModelScope</a>

:::llm-thinking


::llm-thinking-title[llm thinking title]

查看 pdf

::file{{title="facechain.pdf" src="{os.path.join(os.path.dirname(__file__), 'facechain.pdf')}" viewable=true}}

222

![通义千问](https://wanx.alicdn.com/wanx/0/upload//327f0b0610ec41f5b7cfd610125d9382_0.png?x-oss-process=image/watermark,image_d2FueC93YXRlcm1hcmsvcWlhbndlbl93YXRlcm1hcmsucG5n,t_80,g_se,x_30,y_30/format,webp)

<audio id="audio" controls preload="none"><source id=wav src="https://modelscope.cn/api/v1/studio/modelscope/AgentFabric-pre/gradio/file=/tmp/gradio/f77deeceb81de710ed182989a5df50c4ebc9925a/1f762a65-fc7e-4777-9a33-cd7eea92b045.wav"></audio>

## hello
<video src="http://dmshared.oss-cn-hangzhou.aliyuncs.com/ljp/maas/sot_demo_resource_video_20230712/dog.mp4?OSSAccessKeyId=LTAI5tC7NViXtQKpxFUpxd3a&Expires=1725148237&Signature=6E3L2vccyZUNgK842JIgAop81Vk%3D" controls />

:::

:flushing-end

<video src="http://dmshared.oss-cn-hangzhou.aliyuncs.com/ljp/maas/sot_demo_resource_video_20230712/dog.mp4?OSSAccessKeyId=LTAI5tC7NViXtQKpxFUpxd3a&Expires=1725148237&Signature=6E3L2vccyZUNgK842JIgAop81Vk%3D" controls ></video>

# Hello

111

# Hello

111
"""

conversation = [
    [
        None, {
            "avatar": os.path.join(os.path.dirname(__file__), 'repo.jpeg'),
            "text":
            f"""Hello I'm a chatbot<audio src="xx"></audio><select-box item-width="auto"  value="a" options='["aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "b", {{"imgSrc":"{os.path.join(os.path.dirname(__file__), 'avatar.jpeg')}", "label": "Content", "value": "c"}}]' shape="card" select-once  equal-height></select-box>

            <select-box  type='checkbox' columns="2" value='["b"]' options='["a", "b", "c", "e", "f", "g", "h"]' ></select-box>


            <custom-toggle></custom-toggle>

            <custom-select options='[\"a\", \"b\", \"c\"]' ></custom-select>
            """,
            "flushing": False,
            "files": [os.path.join(os.path.dirname(__file__), 'avatar.jpeg')]
        }
    ],
]


def fn(input, chatbot):
    chatbot.append([input, None])
    yield mgr.MultimodalInput(upload_button_props=dict(variant="primary"),
                              value=None), chatbot
    time.sleep(1)
    chatbot[-1][1] = {"text": bot_msg1, "flushing": True}
    yield {
        user_chatbot: chatbot,
    }
    time.sleep(10)
    yield {
        user_chatbot: chatbot,
    }


def clear():
    return None


def flushed():
    return mgr.MultimodalInput(interactive=True)


def custom(data: gr.EventData):
    print('custom', data._data)


with open(
        os.path.join(os.path.dirname(__file__),
                     './custom_components/custom-select/index.js'), 'r') as f:
    custom_select_js = f.read()

with open(
        os.path.join(os.path.dirname(__file__),
                     './custom_components/custom-toggle/index.js'), 'r') as f:
    custom_toggle_js = f.read()

with gr.Blocks() as demo:
    c2 = mgr.Markdown(f"""

Hello I'm a chatbot<audio src="xx"></audio><select-box item-width="auto"  value="a" options='["aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "b", {{"imgSrc":"{os.path.join(os.path.dirname(__file__), 'avatar.jpeg')}", "label": "Content", "value": "c"}}]' shape="card" select-once  equal-height></select-box>

<select-box  type='checkbox' columns="2" value='["b"]' options='["a", "b", "c", "e", "f", "g", "h"]' ></select-box>


<custom-toggle></custom-toggle>

<custom-select options='[\"a\", \"b\", \"c\"]' ></custom-select>

222`h2`22

# `h1`
## `你好`
### h3
#### h4
##### h4
###### h4

$$
math
$$

Given a **formula** below:
$$
s = ut + \\frac{1}{2}at^{2}
$$
$$
L = \\frac{1}{2} \\pi v^2 S C_L
$$
$$
\\int_0^1 x^2 dx
$$

开始测试
```js
import React from 'react';
console.log(React)
```

It is a very cute dog <a href='http://www.modelscope.cn'>ModelScope</a>

:::llm-thinking


::llm-thinking-title[llm thinking title]

查看 pdf

::file{{title="facechain.pdf" src="{os.path.join(os.path.dirname(__file__), 'facechain.pdf')}" viewable=true}}

222

![通义千问](https://wanx.alicdn.com/wanx/0/upload//327f0b0610ec41f5b7cfd610125d9382_0.png?x-oss-process=image/watermark,image_d2FueC93YXRlcm1hcmsvcWlhbndlbl93YXRlcm1hcmsucG5n,t_80,g_se,x_30,y_30/format,webp)

<audio id="audio" controls preload="none"><source id=wav src="https://modelscope.cn/api/v1/studio/modelscope/AgentFabric-pre/gradio/file=/tmp/gradio/f77deeceb81de710ed182989a5df50c4ebc9925a/1f762a65-fc7e-4777-9a33-cd7eea92b045.wav"></audio>

### hello

<video src="{os.path.join(os.path.dirname(__file__), 'dog.mp4')}" controls />

:::

:flushing-end

<video src="http://dmshared.oss-cn-hangzhou.aliyuncs.com/ljp/maas/sot_demo_resource_video_20230712/dog.mp4?OSSAccessKeyId=LTAI5tC7NViXtQKpxFUpxd3a&Expires=1725148237&Signature=6E3L2vccyZUNgK842JIgAop81Vk%3D" controls ></video>

# Hello

111

# Hello

111
""",
                      header_links=True)
    user_chatbot = mgr.Chatbot(value=conversation,
                               show_copy_button=True,
                               flushing_speed=5,
                               height=500,
                               bubble_full_width=True,
                               likeable=True,
                               show_share_button=True,
                               enable_base64=True,
                               avatar_image_align='top',
                               avatar_images=[
                                   {
                                       "avatar":
                                       os.path.join(os.path.dirname(__file__),
                                                    'avatar.jpeg'),
                                       "name":
                                       "aaasdasdasdas"
                                   },
                                   {
                                       "avatar":
                                       os.path.join(os.path.dirname(__file__),
                                                    'avatar.jpeg'),
                                       "name":
                                       "bbbccccggsd"
                                   },
                               ],
                               custom_components={
                                   "custom-select": {
                                       "props": ["options"],
                                       "js": custom_select_js,
                                   },
                                   "custom-toggle": {
                                       "js": custom_toggle_js,
                                   }
                               },
                               llm_thinking_presets=[qwen()])
    input = mgr.MultimodalInput(sources=["upload", "microphone", "webcam"])
    gr.on(triggers=[input.submit],
          fn=fn,
          inputs=[input, user_chatbot],
          outputs=[input, user_chatbot])
    user_chatbot.flushed(fn=flushed, outputs=[input])
    user_chatbot.custom(fn=custom)
    gr.Examples(
        [{
            "text": "hello",
            "files": [os.path.join(os.path.dirname(__file__), 'avatar.jpeg')]
        }, "hello2"],
        inputs=[input])
    gr.Examples([[
        """
开始测试
```js
import React from 'react';
console.log(React)
```

It is a very cute dog <a href='http://www.modelscope.cn'>ModelScope</a>

:::llm-thinking


::llm-thinking-title[llm thinking title]

查看 pdf

::file{{title="facechain.pdf" src="{os.path.join(os.path.dirname(__file__), 'facechain.pdf')}" viewable=true}}

222

![通义千问](https://wanx.alicdn.com/wanx/0/upload//327f0b0610ec41f5b7cfd610125d9382_0.png?x-oss-process=image/watermark,image_d2FueC93YXRlcm1hcmsvcWlhbndlbl93YXRlcm1hcmsucG5n,t_80,g_se,x_30,y_30/format,webp)

<audio id="audio" controls preload="none"><source id=wav src="https://modelscope.cn/api/v1/studio/modelscope/AgentFabric-pre/gradio/file=/tmp/gradio/f77deeceb81de710ed182989a5df50c4ebc9925a/1f762a65-fc7e-4777-9a33-cd7eea92b045.wav"></audio>

## hello

:::
    """
    ]],
                inputs=[c2])

demo.queue().launch(debug=True)
