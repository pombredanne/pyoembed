import unittest

from pyoembed.parsers.xml_parser import XmlParser
from pyoembed.tests import get_fixture


class XmlParserTestCase(unittest.TestCase):

    def setUp(self):
        self.parser = XmlParser()
        self.maxDiff = None

    def test_content_supported(self):
        self.assertTrue(self.parser.content_supported('text/xml'))
        self.assertTrue(self.parser.content_supported('application/xml'))
        self.assertFalse(self.parser.content_supported('application/json'))

    def test_content_parse(self):
        content = get_fixture('sample-video.xml')
        rv = self.parser.content_parse(content)
        self.assertEqual(rv, {'provider_url': 'http://www.youtube.com/',
                              'author_name': 'Showlivre',
                              'title': u'Vespas Mandarinas em "Antes que '
                              u'voc\xea conte at\xe9 dez" no Est\xfadio '
                              u'Showlivre 2013',
                              'html': u'<iframe width="480" height="270" '
                              u'src="http://www.youtube.com/embed/2nLsvPBqeZ8'
                              u'?feature=oembed" frameborder="0" '
                              u'allowfullscreen></iframe>',
                              'thumbnail_width': 480,
                              'height': 270,
                              'width': 480,
                              'version': '1.0',
                              'author_url':
                              'http://www.youtube.com/user/showlivre',
                              'provider_name': 'YouTube',
                              'thumbnail_url': 'http://i1.ytimg.com/vi/'
                              '2nLsvPBqeZ8/hqdefault.jpg',
                              'type': 'video',
                              'thumbnail_height': 360})

    def test_content_parse_with_percent(self):
        content = get_fixture('sample-video-percent.xml')
        rv = self.parser.content_parse(content)
        self.assertEqual(rv, {'provider_url': 'http://www.youtube.com/',
                              'author_name': 'Showlivre',
                              'title': u'Vespas Mandarinas em "Antes que '
                              u'voc\xea conte at\xe9 dez" no Est\xfadio '
                              u'Showlivre 2013',
                              'html': u'<iframe width="100%" height="100%" '
                              u'src="http://www.youtube.com/embed/2nLsvPBqeZ8'
                              u'?feature=oembed" frameborder="0" '
                              u'allowfullscreen></iframe>',
                              'thumbnail_width': 480,
                              'height': '100%',
                              'width': '100%',
                              'version': '1.0',
                              'author_url':
                              'http://www.youtube.com/user/showlivre',
                              'provider_name': 'YouTube',
                              'thumbnail_url': 'http://i1.ytimg.com/vi/'
                              '2nLsvPBqeZ8/hqdefault.jpg',
                              'type': 'video',
                              'thumbnail_height': 360})
