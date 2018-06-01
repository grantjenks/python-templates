import templates

def test_build():
    assert templates.__build__ > 0

def test_htmltemplate():
    doc = templates.HTMLTemplate()
    assert 'html' in doc.format()

def test_bootstrap_bootstrap():
    doc = templates.bootstrap.Bootstrap()
    assert 'Bootstrap' in doc.format()

def test_bootstrap_starter():
    doc = templates.bootstrap.Starter()
    assert 'Starter' in doc.format()

def test_bootstrap_jumbotron():
    doc = templates.bootstrap.Jumbotron()
    assert 'Jumbotron' in doc.format()
