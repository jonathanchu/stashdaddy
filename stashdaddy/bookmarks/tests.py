from django.test import TestCase


class BookmarksViewsTestCase(TestCase):
    def test_bookmarks(self):
        """
        Tests that the experts view returns HTTP 200
        """
        resp = self.client.get('/bookmarks/')
        self.assertEqual(resp.status_code, 200)
