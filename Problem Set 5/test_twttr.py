from twttr import shorten


def test_shorten_alpha():
    assert shorten("twitter") == "twttr"

def test_shorten_nums():
    assert shorten("123twitter") == "123twttr"

def test_shorten_etc():
    assert shorten("!@#$%^&*()QWeRtYUIOp") == "!@#$%^&*()QWRtYp"

def test_shorten_nothing():
    assert shorten("") == ""
