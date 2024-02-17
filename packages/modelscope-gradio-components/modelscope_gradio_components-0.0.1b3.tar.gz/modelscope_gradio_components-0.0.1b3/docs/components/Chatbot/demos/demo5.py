import json

import gradio as gr

import modelscope_gradio_components as mgr

# label 为对用户展示值，value 为实际选择值
options = [{"label": "A", "value": "a"}, "b", "c"]

conversation = [[
    None, f"""
Single Select: <select-box options='{json.dumps(options)}' select-once></select-box>

Multiple Select：<select-box type="checkbox" options='{json.dumps(options)}' select-once submit-text="Submit"></select-box>

Vertical Direction：

<select-box direction="vertical" type="checkbox" options='{json.dumps(options)}' select-once submit-text="Submit"></select-box>

Card Shape:

<select-box shape="card" options='{json.dumps(options)}' select-once equal-height></select-box>


<select-box shape="card" columns="2" options='{json.dumps(options)}' select-once  equal-height></select-box>


<select-box shape="card" direction="vertical" options='{json.dumps(options)}' select-once  equal-height></select-box>
"""
]]


# 必须使用 gr.EventData 显示标注
def fn(data: gr.EventData):
    print(data._data)


with gr.Blocks() as demo:
    chatbot = mgr.Chatbot(
        value=conversation,
        flushing=False,
        height=600,
    )
    # 所有自定义标签都会触发 custom 事件
    chatbot.custom(fn=fn)

if __name__ == "__main__":
    demo.queue().launch()
