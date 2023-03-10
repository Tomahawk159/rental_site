from http import HTTPStatus

from django.test import TestCase
from django.urls import reverse

from review.models import Review


class ReviewTestCase(TestCase):
    def setUp(self):
        self.data = {
            'name': 'John',
            'review': 'Good service!!!',
        }
        self.path = reverse('review:reviews')

    def test_review_get(self):
        response = self.client.get(self.path)

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(
            response.context_data['title'], 'Аренда инструмента - Отзывы')
        self.assertTemplateUsed(response, 'review/review_list.html')

    def test_review_post(self):
        response = self.client.post(self.path, self.data)
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertRedirects(response, reverse('review:reviews'))
        self.assertTrue(Review.objects.filter(name=self.data['name']).exists())
