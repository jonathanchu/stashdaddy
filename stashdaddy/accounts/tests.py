from django.test import TestCase
from django.test.client import Client

from .models import CustomUser as User


class ViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_MyView(self):
        User.objects.create_user('brad@pitt.com', 'mypassword')

        # use test client to perform login
        user = self.client.login(username='brad@pitt.com', password='mypassword')

        response = self.client.post('/accounts/profile/')
