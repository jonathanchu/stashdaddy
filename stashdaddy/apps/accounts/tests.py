from django.test import TestCase
from django.test.client import Client
from django.contrib.auth.models import User

class ViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_MyView(self):
        User.objects.create_user('bradpitt', 'brad@pitt.com', 'mypassword')

        # use test client to perform login
        user = self.client.login(username='bradpitt', password='mypassword')

        response = self.client.post('/accounts/profile/')
