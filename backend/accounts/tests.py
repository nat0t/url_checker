from mixer.backend.django import mixer
from rest_framework.reverse import reverse
from rest_framework.test import APIClient, APITestCase


class UserTest(APITestCase):
    @classmethod
    def setUp(cls):
        cls.user = mixer.blend('accounts.CustomUser')
        cls.client = APIClient()

    def test_not_authenticated(self):
        url = reverse('users:users-list')
        response = self.client.get(url)
        assert response.status_code == 403

    def test_authenticated(self):
        self.client.force_authenticate(user=self.user)
        url = reverse('users:users-list')
        response = self.client.get(url)
        assert response.status_code == 200

    def test_create_user(self):
        self.client.force_authenticate(user=self.user)
        url = reverse('users:users-list')
        response = self.client.post(
            url,
            {'username': 'username', 'email': 'example@local.local'},
        )
        assert response.status_code == 201

    def test_delete_user(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.delete(f'http://127.0.0.1/api/users/{self.user.id}/')
        assert response.status_code == 204
