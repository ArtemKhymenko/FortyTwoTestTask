from django.test import TestCase
from django.core.urlresolvers import reverse


class HelloUrlsTest(TestCase):

    def test_index_url(self):
        url = reverse('index')
        self.assertEqual(url, '/')
