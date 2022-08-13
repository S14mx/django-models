from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from snacks.models import Snack


class SnackTests(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="tester", email="tester@email.com", password="pass")
        self.snack = Snack.objects.create(
            name='cheetos', description="heavenly flavor", purchaser=self.user)

    def test_list_page_status_code(self):
        url = reverse("snack_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_detail_page_status_code(self):
        # url = reverse("snack_detail")
        response = self.client.get('http://127.0.0.1:8000/snacklist/1')
        self.assertEqual(response.status_code, 200)

    def test_list_page_template(self):
        url = reverse("snack_list")
        response = self.client.get(url)
        self.assertTemplateUsed(response, "snack_list.html")

    def test_detail_page_template(self):
        response = self.client.get('http://127.0.0.1:8000/snacklist/1')
        self.assertTemplateUsed(response, "snack_detail.html")

    def test_string_representation(self):
        self.assertEqual(str(self.snack), 'cheetos')

    def test_snack_name(self):
        self.assertEqual(f'{self.snack.name}', 'cheetos')

    def test_snack_description(self):
        self.assertEqual(f'{self.snack.description}', 'heavenly flavor')
