from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from django.urls import reverse

# Create your tests here.
from .models import Item, Review

class ItemTests(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='reviewuser',
            email='reviewuser@email.com',
            password='testpass123'
        )

        self.item = Item.objects.create(
            label = 'jeans',
            price = '50.00',
        )

        self.review = Review.objects.create(
            item = self.item,
            author = self.user,
            review = 'An excellent review',
        )

    def test_item_listing(self):
        self.assertEqual(f'{self.item.label}', 'jeans')
        self.assertEqual(f'{self.item.price}', '50.00')

    def test_item_list_view(self):
        response = self.client.get(reverse('item_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'jeans')
        self.assertTemplateUsed(response, 'items/item_list.html')

    def test_item_detail_view(self):
        response = self.client.get(self.item.get_absolute_url())
        no_response = self.client.get('/items/12345/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'jeans')
        self.assertTemplateUsed(response, 'items/item_detail.html')
        self.assertContains(response, 'An excellent review')
