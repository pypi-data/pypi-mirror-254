# Chatbot

升级版的 gradio Chatbot。

- 支持前端匀速流式输出 message
- 支持输出多模态内容（音频、视频、语音、文件、文本）
- 支持多 agent 场景
- 支持自定义渲染组件，并与 Python 侧事件交互

## 如何使用

### 基本使用

<demo name="demo1"></demo>

### 多模态 & 支持本地文件的展示

<demo name="demo2"></demo>

### 支持思考链的展示

内置扩展了 llm-thinking 自定义标签语法

````text
:::llm-thinking
::llm-thinking-title[调用 image_gen]
```json
{
"text": "一幅描绘风和日丽的画，蓝天白云下，阳光照耀着绿色的草地，树木随风轻轻摇曳。",
"resolution": "1024\*1024"
}

```

:::

:::llm-thinking
::llm-thinking-title[完成调用]
![IMAGEGEN](https://dashscope-result-sh.oss-cn-shanghai.aliyuncs.com/1d/99/20231225/723609ee/2e652574-ca1b-43bd-bedc-f3b9fc840820-1.png?Expires=1703569465&OSSAccessKeyId=LTAI5tQZd8AEcZX6KZV4G8qL&Signature=Udhrrh2ocnebFh9OlnJ2EMNG0Ww%3D)
:::

````

同时针对千问等模型输入，支持下述格式的预设处理（会将下面的格式转换成上方 md 扩展的思考链形式）

```python
import modelscope_gradio_components as mgr
from modelscope_gradio_components.components.Chatbot.llm_thinking_presets import qwen

# 添加 qwen 解析预设
mgr.Chatbot(llm_thinking_presets=[qwen()])
```

```text
Action: image_gen
Action Input: {"text": "风和日丽", "resolution": "1024*1024"}
Observation: <result>![IMAGEGEN](https://dashscope-result-sh.oss-cn-shanghai.aliyuncs.com/1d/a2/20231213/723609ee/1926736d-7c6e-4d2f-b438-b7746b3d89f5-1.png?Expires=1702537773&OSSAccessKeyId=LTAI5tQZd8AEcZX6KZV4G8qL&Signature=H%2B0rIn6BMfE%2BOr1uPb7%2Br9G3%2B5w%3D)</result> 根据您的描述"风和日丽"，我生成了一张图片。![](https://dashscope-result-sh.oss-cn-shanghai.aliyuncs.com/1d/a2/20231213/723609ee/1926736d-7c6e-4d2f-b438-b7746b3d89f5-1.png?Expires=1702537773&OSSAccessKeyId=LTAI5tQZd8AEcZX6KZV4G8qL&Signature=H%2B0rIn6BMfE%2BOr1uPb7%2Br9G3%2B5w%3D)

Action: 「任意文本表示，将展示为思考链调用的名称」
Action Input: 「任意json or md 内容，将展示到调用过程的下拉框」
Observation: <result>「任意 md 内容，将作为完成调用的展示的下拉框内」</result>
```

<demo name="demo3"></demo>

### 控制打字机单句 message 开关

<demo name="demo4"></demo>

### 支持用户选择交互

在返回的内容中加入 `select-box` 标签，更多用法详见 <tab-link tab="custom_tags.md">内置自定义标签</tab-link>

<demo name="demo5"></demo>

### 自定义标签（高阶用法，需要了解前端知识）

<demo name="demo6"></demo>

#### 引入 js

<demo name="demo7"></demo>

template只能做简单的变量替换，如果想要引入更多自定义的行为，如条件判断、循环渲染等，请使用 js 控制 el 自行处理，下面是简单的示例：

<demo name="demo8">
<demo-suffix>
custom_select.js

```js
<file src="./resources/custom_components/custom_select.js" />
```

</demo-suffix>
</demo>

#### 与 Python 侧交互

在 js 中可以使用`cc.dispatch`触发 Python 侧监听的`custom`事件，以前面的custom_select.js为例，我们在前端调用了`cc.dispatch(options[i])`，则会向 Python 侧同时发送通知。

<demo name="demo9"></demo>

## API 及参数列表

以下 API 均为在原有 gradio Chatbot 外的额外拓展参数。

### value

接口定义：

```python
class FileMessage(GradioModel):
    file: FileData
    alt_text: Optional[str] = None


class MultimodalMessage(GradioModel):
    # 当前的 message 信息
    text: Optional[str] = None
    # 控制每一行 message 的头像显示，默认使用 Chatbot 自带的 avatar_images，传入 None 时不显示该行头像（包括 avatar_images 的头像）
    avatar: Optional[Union[FileData, str]] = ''
    # 控制每一行 message 的头像下方的名称显示
    name: Optional[str] = None
    # 是否开启打字机效果
    flushing: Optional[bool] = None
    # 需要单独展示的 files list，常用户辅助用户输入使用
    files: Optional[List[FileMessage]] = None

# value
class ChatbotData(GradioRootModel):
    root: List[Tuple[Optional[Union[MultimodalMessage, str]],
                      Optional[Union[MultimodalMessage, str]]]]
```

### props

| 属性                 | 类型                                                              | 默认值 | 描述                                                                                                                                                             |
| -------------------- | ----------------------------------------------------------------- | ------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| flushing             | bool                                                              | True   | 是否开启打字机效果。默认只有 bot 的 message 会开启，可以通过单独修改 message 的 flushing 属性精确控制每一条 message 的显示效果                                   |
| enable_base64        | bool                                                              | False  | 是否支持渲染的内容为 base64，因为直接渲染 base64 有安全问题，默认为 False。                                                                                      |
| avatar_images        | tuple\[str \| Path \| None \| dict, str \| Path \| None \| dict\] | None   | 拓展gr.Chatbot的参数值，除了接收 url 外还可以接收 dict，dict 可以传入avatar和name字段，name字段在渲染时会显示在头像下方。 当传入 dict 时，必须包含有avatar字段。 |
| flushing_speed       | int                                                               | 3      | 打字机速度，值为 1 - 10，值越大速度越快                                                                                                                          |
| llm_thinking_presets | list\[dict\]                                                      | \[\]   | llm 思考链路解析预设，可以将 llm 调用工具的输出格式转为固定的前端展示格式，需要从modelscope_gradio_components.Chatbot.llm_thinking_presets引入，目前支持：qwen   |
| custom_components    | dict\[str, CustomComponentDict\] CustomComponentDict 定义见下方   | None   | 支持用户定义自定义标签，并通过 js 控制标签渲染样式与触发 python 事件。                                                                                           |

**CustomComponent 定义如下**

```python
class CustomComponentDict(TypedDict):
    props: Optional[List[str]]
    template: Optional[str]
    js: Optional[str]
```

### 内置的自定义标签

见 <tab-link tab="custom_tags.md">内置自定义标签</tab-link>

### event listeners

| 事件                           | 描述                                                                                                                                                                                                                                      |
| ------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `mgr.Chatbot.flushed(fn, ···)` | 当打字机效果结束时触发。EventData 为：<br/> - index：当前 message 的 index tuple。<br/> - value：当前 message value。                                                                                                                     |
| `mgr.Chatbot.custom(fn, ···)`  | 自定义标签触发事件时触发，EventData 为：<br/> - index：前 message 的 index tuple。<br/> - tag：当前触发的标签。<br/> - tag_index：当前触发标签的 index，此 index 在 mesage 的 index tuple 基础上重新计算。<br/> - value：自定义传入的值。 |
