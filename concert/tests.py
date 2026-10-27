from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from unittest.mock import patch
from .models import Concert, ConcertAttending

class ApplicationTests(TestCase):
    def setUp(self):
        self.concert = Concert.objects.create(concert_name='Test Concert', city='Almaty', duration=2)

    def test_anonymous_cannot_rsvp(self):
        self.assertRedirects(self.client.get(reverse('concerts')), reverse('login'))

    def test_signup_login_and_attendance(self):
        response = self.client.post(reverse('signup'), {'username': 'testfan', 'password': 'testpass123'})
        self.assertRedirects(response, reverse('index'))
        self.assertTrue(User.objects.get(username='testfan').check_password('testpass123'))
        self.assertEqual(self.client.get(reverse('concerts')).status_code, 200)
        response = self.client.post(reverse('concert_attendee'), {'concert_id': self.concert.id, 'attendee_choice': 'Attending'})
        self.assertRedirects(response, reverse('concerts'))
        self.assertEqual(ConcertAttending.objects.get().attending, 'Attending')
        self.assertEqual(self.client.post(reverse('concert_attendee'), {'concert_id': self.concert.id, 'attendee_choice': 'invalid'}).status_code, 400)
        self.client.get(reverse('logout'))
        self.assertRedirects(self.client.post(reverse('login'), {'username': 'testfan', 'password': 'testpass123'}), reverse('index'))

    @patch('concert.views.req.get')
    def test_microservice_data_is_rendered(self, get):
        get.return_value.json.return_value = [{'id': 1, 'title': 'A song', 'lyrics': 'Lyrics'}]
        self.assertContains(self.client.get(reverse('songs')), 'A song')
        get.return_value.json.return_value = [{'id': 1, 'pic_url': 'https://example.com/image.png', 'event_city': 'Almaty'}]
        self.assertContains(self.client.get(reverse('photos')), 'Almaty')

    @patch('concert.views.req.get')
    def test_service_outage_returns_503(self, get):
        import requests
        get.side_effect = requests.ConnectionError('offline')
        self.assertEqual(self.client.get(reverse('songs')).status_code, 503)

# Create your tests here.
