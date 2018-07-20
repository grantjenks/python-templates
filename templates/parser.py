"""HTML Template Generator

Intended to parse HTML code and emit Python code compatible with Python
Templates.

TODO

- support doctype
- support comments
- join attrs values that are a list of strings

Open Questions

1. How to merge the generic structure of parsed HTML with existing classes like
   HTMLTemplate? For example: the <head> and <body> tags should be merged.

2. How to identify common patterns between templates and refactor those common
   patterns into parent classes?

"""

import argparse
import bs4
import requests


class HTMLTemplateGenerator:

    def __init__(self, url, name):
        self.url = url
        self.name = name
        self.indent = 8

    def run(self):
        resp = requests.get(self.url)
        soup = bs4.BeautifulSoup(resp.content, 'lxml')
        print(f'class {self.name}(HTMLTemplate):')
        print('    def run(self):')
        for element in soup.contents:
            self.visit(element)

    def visit(self, element):
        if isinstance(element, bs4.Doctype):
            print(f"{' ' * self.indent}self.add('?doctype?')")
        elif isinstance(element, bs4.Tag):
            space = ' ' * self.indent
            children = list(getattr(element, 'contents', []))
            name = getattr(element, 'name', '')
            attrs = getattr(element, 'attrs', {})

            if not children:
                print(f'{space}self.tag({name!r}, attrs={attrs!r})')
                return

            print(f'{space}with self.tag({name!r}, attrs={attrs!r}):')
            self.indent += 4
            for subelement in children:
                self.visit(subelement)
            self.indent -= 4
        elif isinstance(element, bs4.NavigableString):
            text = str(element)
            text = text.strip()
            if text:
                print(f"{' ' * self.indent}self.add('{element}')")
        else:
            print('type:', type(element))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('url')
    parser.add_argument('name')
    args = parser.parse_args()
    generator = HTMLTemplateGenerator(args.url, args.name)
    generator.run()


if __name__ == '__main__':
    main()
