# ModelScope_Gradio_Components

## 开发准备

1. 先下载 gradio 4.x 版本，`pip install gradio`。
2. 关联本地依赖：`pip install -e '.'`，不然无法在本地开发识别包。
3. 使用 pnpm 下载依赖`pnpm install`
4. 运行 demo，`pnpm dev`

## 开发组件

### 如何新增组件

分别在`backend/modelscope_gradio_components/components`和`frontend`下新建组件目录，在`backend/modelscope_gradio_components/__init__.py`引入。

### 使用 React 组件

所有 React 组件都应该写在`packages/compiled`，并在下面的`components`目录内统一新增一个对应的 svelte 组件供外界导入。

## 打包

由于 gradio 没有对外暴露其打包配置，我们需要去本地的 gradio 源码中修改部分代码。

进入到本地的 gradio 源码目录，全局搜索`make_build`，会在`node/dev/files`下看到一个打包后的 js 文件，进入后找到这段代码:

```js
// ...
case 4:
      _d.trys.push([4, 6, , 7]);
      return [4 /*yield*/, build$1({
              root: source_dir,
              configFile: false,
              // 此处为要添加的代码
              define: {
                  'process.env.NODE_ENV': JSON.stringify('production'),
              },
              plugins: __spreadArray(__spreadArray([], plugins, true), [
                  make_gradio_plugin({ mode: "build", svelte_dir: svelte_dir })
              ], false),
              build: {
                  emptyOutDir: true,
                  outDir: join$3(template_dir, entry),
                  lib: {
                      entry: join$3(source_dir, path),
                      fileName: "index.js",
                      formats: ["es"]
                  },
                  minify: true,
                  rollupOptions: {
                      output: {
                          entryFileNames: function (chunkInfo) {
                              if (chunkInfo.isEntry) {
                                  return "index.js";
                              }
                              return "".concat(chunkInfo.name.toLocaleLowerCase(), ".js");
                          }
                      }
                  }
              }
          })];
//...
```

添加下面这段配置：

```js
define: {
    'process.env.NODE_ENV': JSON.stringify('production'),
},
```

然后执行`pnpm build`打包后就可以成功运行了。
