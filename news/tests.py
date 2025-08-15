from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth import get_user_model
from .models import Article


class TestAPIViews(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user("test", "test@test.com", "testingpass")
        self.user.save()
        self.test_article = Article.objects.create(title="test article", author=self.user)
        self.client.login(username="test", password="testingpass")

    def test_article_list(self):
        url = reverse("api_article_list")
        response = self.client.get(url)
        data = response.data
        self.assertEqual(response.status_code, 200)
        self.assertGreater(len(data), 0)