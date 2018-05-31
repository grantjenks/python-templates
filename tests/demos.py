from themes import bootstrap

class BootstrapStarterDemo(bootstrap.Starter):

    def title_content(self):
        self.put('Starter Template / Bootstrap / Themes')

    def heading_content(self):
        self.title_content()

    def content(self):
        with self.tag('p'):
            self.put('Demo of the Bootstrap Starter template in Python Themes.')
