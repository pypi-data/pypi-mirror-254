from unittest import TestCase

from if_ import if_

d = {
    'i': 123,
    'n': None,
    'd': {'this': 456, 'that': False},
    'l': [1, 2, 3, True],
    'f': lambda x: x * 11,
    'T': True,
    'F': False,
}


class UnitTests(TestCase):

    def test_if_(self):
        assert if_(d)['i']._ == 123, 'Dict item works'
        assert if_(d)['d']['this']._ == 456, 'Chained dict item works'
        assert not if_(d)['d']['that'], 'Chained boolean dict item works'
        assert if_(d)['l'][1]._ == 2, 'Chained list item works'
        assert if_(d)['f'](4)._ == 44, 'Chained function call works'
        assert if_(d)['f'](4)._ > 40, 'Chained comparison works'

    def test_failed(self):
        assert if_(None).anything._ is None, 'Chain from None is None'
        assert if_(d).anything._ is None, 'Failed attribute in chain returns None'
        assert if_(d)['n']['anything']._ is None, 'Failed dict item in chain returns None'
        assert if_(d)['l'][5]._ is None, 'Failed list item in chain returns None'

    def test_if_without_underscore(self):
        assert if_(d)['T'], 'Chained True works without _'
        assert not if_(d)['F'], 'Chained False works without _'
        assert if_(d)['i'], 'Chained truthy works without _'
        assert not if_(d)['n'], 'Chained falsy works without _'
        assert not if_(d)['foo'], 'Bool of chained fail works without _'
        assert if_(d)['i'] == 123, 'Dict item works without _'
        assert if_(d)['foo'] != 123, 'Failed dict item works without _'
