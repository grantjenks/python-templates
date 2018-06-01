from .base import Template


class HTMLTemplate(Template):
    HTML_LANG = 'en'

    def run(self):
        self.doctype()
        self.html_element()

    def doctype(self):
        self.put('<!doctype html>')

    def html_element(self):
        with self.tag('html', {'lang': self.HTML_LANG}):
            self.head_element()
            self.body_element()

    def tag(self, name, attrs=None):
        return Tag(self, name, attrs or {})

    def head_element(self):
        with self.tag('head'):
            self.head()

    def head(self):
        pass

    def body_element(self):
        with self.tag('body'):
            self.body()

    def body(self):
        pass


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
