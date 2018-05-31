import os.path as op
from .. import Template

class Starter(Template):

    def build(self):
        self.put('''
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <meta name="description" content="">
    <meta name="author" content="">
        ''')
        self.link_favicon()
        self.title()
        self.css_bootstrap()
        self.css_extra()
        self.put('''
  </head>
  <body>
    <nav class="navbar navbar-expand-md navbar-dark bg-dark fixed-top">
      <a class="navbar-brand" href="#">Navbar</a>
      <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarsExampleDefault" aria-controls="navbarsExampleDefault" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarsExampleDefault">
        <ul class="navbar-nav mr-auto">
          <li class="nav-item active">
            <a class="nav-link" href="#">Home <span class="sr-only">(current)</span></a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#">Link</a>
          </li>
          <li class="nav-item">
            <a class="nav-link disabled" href="#">Disabled</a>
          </li>
          <li class="nav-item dropdown">
            <a class="nav-link dropdown-toggle" href="http://example.com" id="dropdown01" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">Dropdown</a>
            <div class="dropdown-menu" aria-labelledby="dropdown01">
              <a class="dropdown-item" href="#">Action</a>
              <a class="dropdown-item" href="#">Another action</a>
              <a class="dropdown-item" href="#">Something else here</a>
            </div>
          </li>
        </ul>
        <form class="form-inline my-2 my-lg-0">
          <input class="form-control mr-sm-2" type="text" placeholder="Search" aria-label="Search">
          <button class="btn btn-outline-success my-2 my-sm-0" type="submit">Search</button>
        </form>
      </div>
    </nav>
    <main role="main" class="container">
      <div class="starter-template">
        ''')
        self.heading()
        self.lead()
        self.content()
        self.put('''
      </div>
    </main><!-- /.container -->
    <!-- Bootstrap core JavaScript
    ================================================== -->
    <!-- Placed at the end of the document so the pages load faster -->
        ''')
        self.script_jquery()
        self.script_popper()
        self.script_bootstrap()
        self.put('''
  </body>
</html>
        ''')

    def link_favicon(self):
        self.put('<link rel="icon" href="/favicon.ico">')

    def title(self):
        with self.tag('title'):
            self.title_content()

    def title_content(self):
        self.put('Starter Template for Bootstrap')

    def css_bootstrap(self):
        filename = 'bootstrap.min.css'
        path = op.join(op.dirname(op.realpath(__file__)), filename)
        with self.tag('style'):
            with open(path) as reader:
                text = reader.read()
            self.put(text)

    def css_extra(self):
        with self.tag('style'):
            self.put('''
body {
  padding-top: 5rem;
}
.starter-template {
  padding: 3rem 1.5rem;
  text-align: center;
}
            ''')

    def script_jquery(self):
        filename = 'jquery-3.2.1.slim.min.js'
        path = op.join(op.dirname(op.realpath(__file__)), filename)
        with self.tag('script'):
            with open(path) as reader:
                text = reader.read()
            self.put(text)

    def script_popper(self):
        path = op.join(op.dirname(op.realpath(__file__)), 'popper.min.js')
        with self.tag('script'):
            with open(path) as reader:
                text = reader.read()
            self.put(text)

    def script_bootstrap(self):
        path = op.join(op.dirname(op.realpath(__file__)), 'bootstrap.min.js')
        with self.tag('script'):
            with open(path) as reader:
                text = reader.read()
            self.put(text)

    def heading(self):
        with self.tag('h1'):
            self.heading_content()

    def heading_content(self):
        self.put('Bootstrap starter template')

    def lead(self):
        with self.tag('p', attrs={'class': 'lead'}):
            self.lead_content()

    def lead_content(self):
        self.put('''
Use this document as a way to quickly start any new project.<br> All you get
is this text and a mostly barebones HTML document.
        ''')

    def content(self):
        pass
