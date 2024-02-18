"""注册器"""


class Register(object):

    def __init__(self) -> None:
        self._module_dict = {}

    def register(self, name=''):
        def inner(cls_or_func):
            key = name if name else cls_or_func.__name__
            self._module_dict.setdefault(key, cls_or_func)
            return cls_or_func

        return inner

    def run(self, name: str, *, params: dict):
        return self(name)(**params)

    def __call__(self, name: str):
        cls_or_func = self._module_dict.get(name)
        if cls_or_func is None:
            raise KeyError(f'Class or Function {name} not found in registry!')

        return cls_or_func

    def __repr__(self) -> str:
        string = self.__class__.__name__ + ':' + str(list(self._module_dict.keys()))

        return string


ENGINES = Register()
