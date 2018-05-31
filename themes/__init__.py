"""Themes -- Python templating library with themes included.

:copyright: (c) 2018 by Grant Jenks.
:license: Apache 2.0, see LICENSE for more details.

"""

from abc import ABCMeta, abstractmethod

class Template(metaclass=ABCMeta):

    def __init__(self):
        self._parts = []

    def put(self, part):
        self._parts.append(part)

    @abstractmethod
    def build(self):
        pass

    def tag(self, name, attrs={}):
        return Tag(self, name, attrs)

    def __iter__(self):
        yield from self._parts

    def __str__(self):
        return ''.join(self._parts)


class Tag:
    def __init__(self, template, name, attrs):
        self.template = template
        self.name = name
        self.attrs = attrs

    def __enter__(self):
        extra = ''
        attrs = self.attrs
        if attrs:
            items = attrs.items()
            pairs = ' '.join(f'{key}="{value}"' for key, value in items)
            extra = ' ' + pairs
        self.template.put(f'<{self.name}{extra}>')

    def __exit__(self, exc_type, exc_inst, exc_tb):
        self.template.put(f'</{self.name}>')


__title__ = 'themes'
__version__ = '0.0.1'
__build__ = 0x000001
__author__ = 'Grant Jenks'
__license__ = 'Apache 2.0'
__copyright__ = '2018, Grant Jenks'
