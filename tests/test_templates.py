import templates

from .demos import BootstrapStarterDemo

def test_build():
    assert templates.__build__ > 0

def test_starter():
    page = BootstrapStarterDemo()
    page.build()
