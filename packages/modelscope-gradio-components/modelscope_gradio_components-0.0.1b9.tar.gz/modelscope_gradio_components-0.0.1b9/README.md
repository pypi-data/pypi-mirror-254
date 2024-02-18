<h1>Modelscope Gradio Components</h1>

<p align="center">
    <br>
    <img src="https://modelscope.oss-cn-beijing.aliyuncs.com/modelscope.gif" width="400"/>
    <br>
<p>

<p align="center">
<a href="https://modelscope.cn/home">Modelscope Hub</a> ｜ <a href="https://modelscope.cn/studios/modelscope/modelscope_gradio_components/summary">Docs</a>
<br>
        <a href="README-zh_CN.md">中文</a>&nbsp ｜ &nbspEnglish
</p>

A components library for gradio.

![quickstart](./resources/sample.gif)

## Install

```sh
pip install modelscope_gradio_components
```

## Quickstart

```python
import time

import gradio as gr

import modelscope_gradio_components as mgr


def submit(_input, _chatbot):
    print('text：', _input.text)
    print('files: ', _input.files)
    _chatbot.append([_input, None])
    yield _chatbot
    time.sleep(1)
    _chatbot[-1][1] = [{
        "flushing": False,
        "text": 'bot1: ' + _input.text + '!'
    }, {
        "text": 'bot2: ' + _input.text + '!'
    }]
    yield {
        chatbot: _chatbot,
    }


with gr.Blocks() as demo:
    chatbot = mgr.Chatbot(height=400)

    input = mgr.MultimodalInput()
    input.submit(fn=submit, inputs=[input, chatbot], outputs=[chatbot])

demo.queue().launch()
```

![quickstart](./resources/quickstart.png)

## Development

Clone this repo locally:

```sh
git clone git@github.com:modelscope/modelscope-gradio-components.git
cd modelscope-gradio-components
# for backend
pip install -e '.'
# for frontend
npm install pnpm -g

pnpm install
pnpm build
```

Run demo!

```sh
gradio docs/app.py
```

or run a single demo like this:

```sh
gradio docs/components/Chatbot/demos/basic.py
```

## Component Docs

See [docs](https://modelscope.cn/studios/modelscope/modelscope_gradio_components/summary)
