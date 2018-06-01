from ..html import HTMLTemplate

class Bootstrap(HTMLTemplate):

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
