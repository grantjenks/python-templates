# import os.path

from ..base import HTMLTemplate

# __dir__ = os.path.dirname(os.path.realpath(__file__))


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
        self.put('''
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
        ''')
        # with self.tag('style'):
        #     self._include('bootstrap.min.css')

    # def _include(self, filename):
    #     with open(os.path.join(__dir__, filename)) as reader:
    #         text = reader.read()
    #     self.put(text)

    def head_extra(self):
        pass

    def body(self):
        self.nav_element()
        self.main_element()
        self.footer_element()
        self.jquery_js_element()
        self.popper_js_element()
        self.bootstrap_js_element()

    def nav_element(self):
        self.put('''
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
        ''')

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

    def footer_element(self):
        pass

    def jquery_js_element(self):
        self.put('''
<script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
        ''')
        # with self.tag('script'):
        #     self._include('jquery-3.2.1.slim.min.js')

    def popper_js_element(self):
        self.put('''
<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
        ''')
        # with self.tag('script'):
        #     self._include('popper.min.js')

    def bootstrap_js_element(self):
        self.put('''
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
        ''')
        # with self.tag('script'):
        #     self._include('bootstrap.min.js')
