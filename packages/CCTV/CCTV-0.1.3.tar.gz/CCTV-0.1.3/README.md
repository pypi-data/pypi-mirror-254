
# CCTV (Convert to Convenient Tree View) [dog]

版本：0.1.3

这是一个数据转树状图的模块，能够将字典、列表、元组粗略地构成树状图。

## 函数解释

### tree
将字典、列表、元组转换为树状图。
- indent：用于排版计数，无需手动设置
- valued：是否显示字典的值（0.1.1版本新增）

### visual
细化树状图

### colorize
在树状图的基础上给节点上色，需要tree的参数为真且终端支持ANSI。
注意：colorize函数中用来处理颜色的注释已被弃用。

## 函数变更
- 0.1.2版本：删除了成堆烦人的注释，使用join替代重复新建字符串，修复了不支持ANSI终端传入color=0时的错误转义字符'\033[0m'。
- 0.1.3版本：重构了函数，并且用链式替换优化了正则表达式。

## 注意事项
- colorize函数在0.1.3版本中做出了部分改动，不再需要使用正则表达式，而是直接进行链式替换。

## 示例

```python
from CCTV import colorize, visual, tree
data={'test': {1,1,4,5,1,4}}
print('data')
print(colorize(visual(tree(data, color=1, valued=1))))
```

请注意以上示例仅供参考，具体设置根据实际需要进行调整。

祝使用愉快！
