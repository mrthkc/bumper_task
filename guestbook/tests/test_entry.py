from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from guestbook.models import Entry, User


class EntryTests(APITestCase):
    test_user = None
    test_entry = None

    def setUp(self):
        self.test_user = User.objects.create(**{
            "name": "test user"
        })
        self.test_entry = Entry.objects.create(**{
            "user_id": self.test_user.pk,
            "subject": "test subject 1",
            "message": "test message 1",
        })

    def test_entry_list_success(self):
        """
        Test: Entry list
        """
        url = reverse('guestbook:entry-list')
        response = self.client.get(url, format='json')
        response_json = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response_json.get('count'), 1)
        self.assertEqual(Entry.objects.count(), 1)

    def test_create_entry_error_missing_subject(self):
        """
        Test: Create entry - missin subject
        """
        url = reverse('guestbook:entry-list')
        data = {
            "name": "test user tmp",
            # "subject": "test subject",
            "message": "test message",
        }
        response = self.client.post(url, data=data, format='json')
        response_json = response.json()
        self.assertEqual(list(response_json.keys())[0], 'subject')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_entry_error_missing_message(self):
        """
        Test: Create entry - missin message
        """
        url = reverse('guestbook:entry-list')
        data = {
            "name": "test user tmp",
            "subject": "test subject",
            # "message": "test message",
        }
        response = self.client.post(url, data=data, format='json')
        response_json = response.json()
        self.assertEqual(list(response_json.keys())[0], 'message')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_entry_success(self):
        """
        Test: Create entry success
        """
        url = reverse('guestbook:entry-list')
        data = {
            "name": "test user tmp",
            "subject": "test subject",
            "message": "test message",
        }
        response = self.client.post(url, data=data, format='json')
        response_json = response.json()
        self.assertEqual(response_json['name'], data['name'])
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
