from templates import bootstrap

class BootstrapStarterDemo(bootstrap.Starter):

    def title(self):
        self.put('Starter Template / Bootstrap / Templates')

    def heading_content(self):
        self.title_content()

    def content(self):
        with self.tag('p'):
            self.put('Demo of the Bootstrap Starter Template.')
