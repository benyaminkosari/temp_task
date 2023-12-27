from django.test import TestCase
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient
from django.contrib.auth.models import User

class RegisterLoginViewTests(TestCase):

    def setUp(self):
        self.client = APIClient()

    def test_register_view(self):
        user_data = {
            'username': 'testuser',
            'email': 'test@example.com',
            'password': 'testpassword',
        }
        response = self.client.post('/users/sign-up/', user_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(User.objects.filter(username='testuser').exists())
        user = User.objects.get(username='testuser')
        self.assertTrue(Token.objects.filter(user=user).exists())

    def test_login_view(self):
        test_user = User.objects.create_user(username='testuser', password='testpassword')
        login_data = {
            'username': 'testuser',
            'password': 'testpassword',
        }
        response = self.client.post('/users/login/', login_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('token',response.data['data'])
        token = response.data['data']['token']
        self.assertTrue(Token.objects.filter(key=token, user=test_user).exists())
