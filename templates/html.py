from abc import ABCMeta, abstractmethod

from .base import Template

class HTMLTemplate(Template, metaclass=ABCMeta):
    HTML_LANG = 'en'

    def build(self):
        self.doctype()
        self.html_element()

    def doctype(self):
        self.put('<!doctype html>')

    def html_element(self):
        with self.tag('html', {'lang': self.HTML_LANG}):
            self.head_element()
            self.body_element()

    def head_element(self):
        with self.tag('head'):
            self.head()

    @abstractmethod
    def head(self):
        pass

    def body_element(self):
        with self.tag('body'):
            self.body()

    @abstractmethod
    def body(self):
        pass
