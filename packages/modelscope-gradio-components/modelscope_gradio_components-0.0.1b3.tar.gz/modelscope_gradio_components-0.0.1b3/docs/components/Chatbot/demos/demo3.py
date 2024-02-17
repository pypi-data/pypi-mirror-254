import os

import gradio as gr

import modelscope_gradio_components as mgr
from modelscope_gradio_components.components.Chatbot.llm_thinking_presets import \
  qwen


def resolve_assets(relative_path):
    return os.path.join(os.path.dirname(__file__), "../resources",
                        relative_path)


conversation = [
    [
        None, {
            "text": f"""
标签语法

:::llm-thinking
::llm-thinking-title[调用 tool]

```json
{{"text": "风和日丽", "resolution": "1024*1024"}}
```
:::

qwen preset

Action: image_gen
Action Input: {{"text": "风和日丽", "resolution": "1024*1024"}}
Observation: <result>![IMAGEGEN]({resolve_assets("screen.jpeg")})</result> 根据您的描述"风和日丽"，我生成了一张图片。![]({resolve_assets("screen.jpeg")})

Action: 「任意文本表示，将展示为思考链调用的名称」
Action Input: 「任意json or md 内容，将展示到调用过程的下拉框」
Observation: <result>「任意 md 内容，将作为完成调用的展示的下拉框内」</result>
""",
            "flushing": False
        }
    ],
]

with gr.Blocks() as demo:
    mgr.Chatbot(
        value=conversation,
        llm_thinking_presets=[qwen()],
        height=600,
    )

if __name__ == "__main__":
    demo.queue().launch()
