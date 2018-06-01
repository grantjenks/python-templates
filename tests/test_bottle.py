from bottle import get, run

from demos import StarterDemo


@get('/starter/')
def starter_demo():
    page = StarterDemo()
    return page.format()


if __name__ == '__main__':
    run(host='localhost', port=5050, reloader=True, debug=True)
