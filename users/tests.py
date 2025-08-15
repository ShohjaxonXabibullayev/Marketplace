from django.test import TestCase
from django.urls import reverse
from .models import CustomUser
from django.contrib.auth import get_user


# Create your tests here.

class SignupTestCase(TestCase):
    def test_signup_view(self):
        response = self.client.post(
            reverse('users:signup'),
            data={
                'first_name': 'Shohjaxon',
                'username': 'shohjaxon',
                'email': 'aa@aa.aa',
                'password1': 'admin',
                'password2': 'admin',
            }
        )
        user = CustomUser.objects.get(username='shohjaxon')
        self.assertEqual(user.first_name, 'Shohjaxon')
        self.assertEqual(user.email, 'aa@aa.aa')
        self.assertTrue(user.check_password('admin'))

        second_response = self.client.get("/users/profile/akbarjon")
        self.assertEqual(second_response.status_code, 200)

        # login
        self.client.login(username='shohjaxon', password='admin')

        third_response = self.client.post(
            reverse('users:update'),
            data={
                'username': 'shohjaxon',
                'first_name': 'Shohjaxon2',
                'last_name': 'Xabibullayev',
                'email': 'aaa@aaa.aaa',
                'phone_number': '+998904505050',
                'tg_username': 'username',
            }
        )
        user = get_user(self.client)
        print(user.is_authenticated)
        self.assertEqual(third_response.status_code, 302)
        self.assertEqual(user.phone_number, '+998904505050')
        self.assertEqual(user.first_name, 'Shohjaxon2')
        self.assertNotEqual(user.first_name, 'Shohjaxon')


