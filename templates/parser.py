"""HTML Template Generator

Intended to parse HTML code and emit Python code compatible with Python
Templates.

TODO

- Change tag calls to pass void=True

Open Questions

1. How to merge the generic structure of parsed HTML with existing classes like
   HTMLTemplate? For example: the <head> and <body> tags should be merged.

2. How to identify common patterns between templates and refactor those common
   patterns into parent classes?

3. How to identify common patterns within a template and refactor to template
   class methods (possibly with different parameters)?

"""

import argparse
import bs4
import requests
from urllib.parse import urljoin


class HTMLTemplateGenerator:

    def __init__(self, url, name):
        self.url = url
        self.name = name
        self.indent = 0

    def put(self, value):
        print(f"{' ' * self.indent}{value}")

    def run(self):
        self.put(f'class {self.name}(HTMLTemplate):')
        self.indent += 4
        self.put('def run(self):')
        self.indent += 4
        resp = requests.get(self.url)
        soup = bs4.BeautifulSoup(resp.content, 'lxml')

        for element in soup.contents:
            self.visit(element)

    def visit(self, element):
        visit_name = 'visit_' + type(element).__name__.lower()
        visit_method = getattr(self, visit_name)
        visit_method(element)

    def visit_navigablestring(self, element):
        text = str(element)
        text = text.strip()

        if text:
            self.put(f'self.add({text!r})')

    def visit_comment(self, element):
        text = str(element)
        comment = f'<!--{text}-->'
        self.put(f'self.add({comment!r})')

    def visit_tag(self, element):
        attrs = getattr(element, 'attrs', {})

        for key, value in attrs.items():
            if isinstance(value, list) and len(value) == 1:
                value = value[0]

            if key == 'href':
                value = urljoin(self.url, value)
            elif key == 'src':
                value = urljoin(self.url, value)

            attrs[key] = value

        attrs_arg = f', attrs={attrs!r}' if attrs else ''

        if not element.contents:
            self.put(f'self.tag({element.name!r}{attrs_arg})')
        else:
            self.put(f'with self.tag({element.name!r}{attrs_arg}):')
            self.indent += 4

            for subelement in element.contents:
                self.visit(subelement)

            self.indent -= 4

    def visit_doctype(self, element):
        print(f"{' ' * self.indent}self.add('<!doctype {element}>')")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('url')
    parser.add_argument('name')
    args = parser.parse_args()
    generator = HTMLTemplateGenerator(args.url, args.name)
    generator.run()


if __name__ == '__main__':
    main()
