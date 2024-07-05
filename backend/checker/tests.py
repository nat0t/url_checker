from mixer.backend.django import mixer
from rest_framework.reverse import reverse
from rest_framework.test import APIClient, APITestCase

from checker.models import Link


class LinkTest(APITestCase):
    @classmethod
    def setUp(cls):
        cls.user = mixer.blend('accounts.CustomUser')
        cls.link = mixer.blend('checker.Link')
        cls.client = APIClient()

    def test_instance(self):
        self.assertIsInstance(self.link, Link)

    def test_not_authenticated(self):
        url = reverse('checker:checker-list')
        response = self.client.get(url)
        assert response.status_code == 403

    def test_authenticated(self):
        self.client.force_authenticate(user=self.user)
        url = reverse('checker:checker-list')
        response = self.client.get(url)
        assert response.status_code == 200

    def test_create_links(self):
        self.client.force_authenticate(user=self.user)
        url = reverse('checker:checker-list')
        response = self.client.post(
            url,
            {
                'links': [
                    {'url': self.link.url},
                    {'url': self.link.url},
                ],
            }
        )
        assert response.status_code == 201

    def test_delete_link(self):
        self.client.force_authenticate(user=self.link.user)
        response = self.client.delete(f'http://127.0.0.1/api/checker/{self.link.id}/')
        assert response.status_code == 204
