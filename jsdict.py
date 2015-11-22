# coding:utf-8


class JsDict(dict):
    def __getitem__(self, item):
        return self.get(item)

    def __repr__(self):
        return '<jsDict ' + dict.__repr__(self) + '>'

    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__
    __getattr__ = __getitem__


if __name__ == '__main__':
    d = JsDict({'a': 1, 'b': 2})
    print(d.a)
    print(d.c)
    print(d['c'])
    print(d.b)
    d.c = 3
    print(d.c)
    print(d['c'])
