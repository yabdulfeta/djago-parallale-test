from rest_framework.test import APITestCase
from django.urls import reverse

class SubtractTests(APITestCase):
    def test_subtraction(self):
        url = reverse('subtract')
        data = {'operand1': 10, 'operand2': 5}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['result'], 5)

    def test_subtraction_negative(self):
        url = reverse('subtract')
        data = {'operand1': 5, 'operand2': 10}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['result'], -5)