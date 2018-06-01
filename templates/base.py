from abc import ABCMeta, abstractmethod


class Template(metaclass=ABCMeta):

    def __init__(self):
        self._parts = []

    def put(self, value):
        self._parts.append(value)

    def format(self, **kwargs):
        delete = object()
        originals = {}
        for key in kwargs:
            if hasattr(self, key):
                originals[key] = getattr(self, key)
            else:
                originals[key] = delete
        try:
            for key, value in kwargs.items():
                setattr(self, key, value)
            self._parts.clear()
            self.run()
            return ''.join(self._parts)
        finally:
            for key, value in originals.items():
                if value is delete:
                    delattr(self, key)
                else:
                    setattr(self, key, value)

    @abstractmethod
    def run(self):
        pass


class ChainDict(dict):

    def __init__(self, *maps):
        # pylint: disable=super-init-not-called
        self._maps = maps

    def __missing__(self, key):
        for mapping in self._maps:
            try:
                return mapping[key]
            except KeyError:
                pass
        raise KeyError(key)
