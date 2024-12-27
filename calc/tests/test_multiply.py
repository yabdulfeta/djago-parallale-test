from rest_framework.test import APITestCase
from django.urls import reverse

class MultiplyTests(APITestCase):
    def test_multiplication(self):
        url = reverse('multiply')
        data = {'operand1': 10, 'operand2': 5}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['result'], 50)

    def test_multiplication_zero(self):
        url = reverse('multiply')
        data = {'operand1': 10, 'operand2': 0}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['result'], 0)