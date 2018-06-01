import os.path

from ..html import HTMLTemplate

__dir__ = os.path.dirname(os.path.realpath(__file__))


class Bootstrap(HTMLTemplate):

    def head(self):
        self.charset_element()
        self.viewport_element()
        self.description_element()
        self.author_element()
        self.favicon_element()
        self.title_element()
        self.bootstrap_css_element()
        self.head_extra()

    def charset_element(self):
        self.put('<meta charset="')
        self.charset()
        self.put('">')

    def charset(self):
        self.put('utf-8')

    def viewport_element(self):
        self.put('<meta name="viewport" content="')
        self.viewport()
        self.put('">')

    def viewport(self):
        self.put('width=device-width, initial-scale=1, shrink-to-fit=no')

    def description_element(self):
        self.put('<meta name="description" content="')
        self.description()
        self.put('">')

    def description(self):
        pass

    def author_element(self):
        self.put('<meta name="author" content="')
        self.author()
        self.put('">')

    def author(self):
        pass

    def favicon_element(self):
        self.put('<link rel="icon" href="')
        self.favicon()
        self.put('">')

    def favicon(self):
        self.put('/favicon.ico')

    def title_element(self):
        with self.tag('title'):
            self.title()

    def title(self):
        self.put('Bootstrap Template')

    def bootstrap_css_element(self):
        with self.tag('style'):
            self._include('bootstrap.min.css')

    def _include(self, filename):
        with open(os.path.join(__dir__, filename)) as reader:
            text = reader.read()
        self.put(text)

    def head_extra(self):
        pass

    def body(self):
        self.nav_element()
        self.main_element()
        self.jquery_js_element()
        self.popper_js_element()
        self.bootstrap_js_element()

    def nav_element(self):
        pass

    def main_element(self):
        with self.tag('main', attrs={'role': 'main'}):
            self.main()

    def main(self):
        self.h1_element()

    def h1_element(self):
        with self.tag('h1'):
            self.h1()

    def h1(self):
        # pylint: disable=invalid-name
        self.put('Bootstrap Template')

    def jquery_js_element(self):
        with self.tag('script'):
            self._include('jquery-3.2.1.slim.min.js')

    def popper_js_element(self):
        with self.tag('script'):
            self._include('popper.min.js')

    def bootstrap_js_element(self):
        with self.tag('script'):
            self._include('bootstrap.min.js')
