from django.test import TestCase
from django.urls import reverse

# Create your tests here.
from .models import Item

class ItemTests(TestCase):

    def setUp(self):
        self.item = Item.objects.create(
            label = 'jeans',
            price = '50.00',
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
