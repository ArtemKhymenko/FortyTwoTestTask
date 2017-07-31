from django.test import TestCase
from django.core.urlresolvers import reverse


class HelloViewsTestCase(TestCase):

    def test_home(self):
        """
        test if http response from index url is OK.
        test that right template is used
        """
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
