from templates.bootstrap import Starter


class StarterDemo(Starter):

    def title(self):
        self.put('Demo / Starter / Bootstrap / Templates')

    h1 = title
