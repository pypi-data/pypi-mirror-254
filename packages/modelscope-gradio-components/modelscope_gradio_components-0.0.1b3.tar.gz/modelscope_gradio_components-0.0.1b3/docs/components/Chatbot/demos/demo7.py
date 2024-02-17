import gradio as gr

import modelscope_gradio_components as mgr

conversation = [[
    None, f"""
custom tag:<custom-tag value="aaa"></custom-tag>
"""
]]

with gr.Blocks() as demo:
    chatbot = mgr.Chatbot(
        value=conversation,
        flushing=False,
        height=600,
        custom_components={
            # key 为标签名
            "custom-tag": {
                "props": ["value"],
                "template":
                "<button onclick='{onClick}'>{value}</button>",
                # js 接收一个 function
                "js":
                """
(props, cc, { el, onMount }) => {
    // onMount 会在 template 渲染完成后调用
    onMount(() => {
      // el 是当前自定义标签挂载的 container
      console.log(el)
    })
    // 可以返回一个对象，对象里的值会与 props 做并集最后渲染到模板中
    return {
      value: 'Click Me: ' + props.value,
      onClick: () => {
          alert('hello')
      }
    }
}"""
            }
        })

if __name__ == "__main__":
    demo.queue().launch()
