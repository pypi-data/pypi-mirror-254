# libnotems

Notems操作库。
示例
```
from libnotems import Notems

notems = Notems()
# 获取 https://note.ms/1 的笔记内容
n = notems.get_note("1")
print(n)
# 修改 https://note.ms/1 的笔记内容为“blabla”
notems.post_note("1","blabla")
```
#### 使用代理
```
notems = Notems(proxy="http://127.0.0.1:8080")
```
#### 自定义Notems域名（例如搭载[NotePaper](https://github.com/rHanbowChic/NotePaper)的其他服务器）
```
notems = Notems(host="https://note.ms.example.com")
```
