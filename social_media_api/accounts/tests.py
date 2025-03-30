from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import User

class UserTests(APITestCase):

    def setUp(self):
        self.user_data = {
            'username': 'testuser',
            'password': 'testpassword',
            'bio': 'This is a test user.',
            'profile_picture': None,  # Assuming a file upload is handled separately
        }
        self.user = User.objects.create_user(**self.user_data)

    def test_user_creation(self):
        response = self.client.post(reverse('user-register'), self.user_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 2)  # 1 from setUp and 1 from creation
        self.assertEqual(User.objects.get(username='testuser').bio, 'This is a test user.')

    def test_user_login(self):
        response = self.client.post(reverse('user-login'), {
            'username': 'testuser',
            'password': 'testpassword'
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_profile(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('user-profile', kwargs={'username': 'testuser'}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['bio'], 'This is a test user.')