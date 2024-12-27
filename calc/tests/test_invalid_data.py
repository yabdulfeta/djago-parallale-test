from rest_framework.test import APITestCase
from django.urls import reverse

class InvalidDataTests(APITestCase):
    def test_invalid_data(self):
        url = reverse('add')
        data = {'operand1': 'a', 'operand2': 5}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 400)

        url = reverse('subtract')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 400)

        url = reverse('multiply')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 400)

        url = reverse('divide')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 400)