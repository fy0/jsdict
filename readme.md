# jsdict

JavaScript-style Dict.

Tested on py2.7/py3.4

```python
from jsdict import JsDict

d = JsDict({'a': 1, 'b': 2})

print(d.a)
>>>> 1

print(d.c)
>>>> None

d.c = 3
print(d.c)
>>>> 3
```
