from django.test import TestCase

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import User

class UserAPITestCase(APITestCase):

    def setUp(self):
        self.user1 = User.objects.create(username='user1', first_name='First', last_name='User', email='user1@example.com')
        self.user1.set_password('password1')
        self.user1.save()

        self.user2 = User.objects.create(username='user2', first_name='Second', last_name='User', email='user2@example.com')
        self.user2.set_password('password2')
        self.user2.save()

    def test_create_user(self):
        url = reverse('user_api_app:user-create')
        data = {
            'username': 'newuser',
            'first_name': 'New',
            'last_name': 'User',
            'email': 'newuser@example.com',
            'password': 'newpassword'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 3)
        self.assertEqual(User.objects.get(username='newuser').email, 'newuser@example.com')

    def test_retrieve_user_by_name(self):
        url = reverse('user_api_app:user-detail-by-name')
        response = self.client.get(url, {'username': 'user1'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['username'], 'user1')

    def test_retrieve_user_by_id(self):
        url = reverse('user_api_app:user-detail-by-id', kwargs={'pk': self.user1.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['username'], 'user1')

    def test_update_user_by_name(self):
        url = reverse('user_api_app:user-update-by-name')
        data = {'username': 'updateduser1'}
        response = self.client.put(url, data, format='json', QUERY_STRING='old_name=user1')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(User.objects.get(pk=self.user1.pk).username, 'updateduser1')

    def test_update_user_by_id(self):
        url = reverse('user_api_app:user-update-by-id', kwargs={'pk': self.user2.pk})
        data = {'username': 'updateduser2'}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(User.objects.get(pk=self.user2.pk).username, 'updateduser2')


       

    def test_delete_user_by_id(self):
        url = reverse('user_api_app:user-delete-by-id', kwargs={'pk': self.user2.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(User.objects.count(), 1)
 

# N/B: To test for delete_user_by_name database should contain the user you're trying to delete else it will throw error
    def test_delete_user_by_name(self):
        url = reverse('user_api_app:user-delete-by-name')
        response = self.client.delete(f"{url}?username=user1")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(User.objects.count(), 1)

    
