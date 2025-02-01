from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from guestbook.models import Entry, User


class EntryTests(APITestCase):
    test_user_1 = None
    test_user_2 = None

    test_user_1_message_count = 3
    test_user_2_message_count = 2

    def setUp(self):
        self.test_user_1 = User.objects.create(**{
            "name": "test user 1"
        })
        self.test_user_2 = User.objects.create(**{
            "name": "test user 2"
        })
        for i in range(0, self.test_user_1_message_count):
            self.test_entry = Entry.objects.create(**{
                "user_id": self.test_user_1.pk,
                "subject": "test subject {i}",
                "message": "test message {i}",
            })

        for i in range(0, self.test_user_2_message_count):
            self.test_entry = Entry.objects.create(**{
                "user_id": self.test_user_2.pk,
                "subject": "test subject {i}",
                "message": "test message {i}",
            })

    def test_user_list_success(self):
        """
        Test: User list
        """
        url = reverse('guestbook:user-list')
        response = self.client.get(url, format='json')
        response_json = response.json()
        users = response_json.get('users')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response_json.get('users')), 2)
        for us in users:
            if us['message_count'] == self.test_user_2_message_count:
                self.assertEqual(us['username'], 'test user 2')
            else:
                self.assertEqual(us['username'], 'test user 1')
