from rest_framework.test import APITestCase
from django.urls import reverse

class AddTests(APITestCase):
    def test_addition(self):
        url = reverse('add')
        data = {'operand1': 10, 'operand2': 5}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['result'], 15)

    def test_addition_negative(self):
        url = reverse('add')
        data = {'operand1': -10, 'operand2': 5}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['result'], -5)