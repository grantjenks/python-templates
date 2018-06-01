import templates

from .demos import StarterDemo

def test_build():
    assert templates.__build__ > 0

def test_starter():
    page = StarterDemo()
    assert 'Demo' in page.format()
