from bottle import get, run

from demos import BootstrapStarterDemo


@get('/starter/')
def demo_starter():
    page = BootstrapStarterDemo()
    page.build()
    return page


if __name__ == '__main__':
    run(host='localhost', port=5050, debug=True)
