from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse


class AdminSiteTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.admin_user = get_user_model().object.create_superuser('admin@mail.com', 'adminpass')
        self.client.force_login(self.admin_user)
        self.user = get_user_model() \
            .object \
            .create_user(email='mail@com', password='password', name='full user name')

    def test_user_listed(self):
        """test that user are listed on userpage"""
        url = reverse('admin:core_user_changelist')
        res = self.client.get(url)
        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)

    def test_user_change_page(self):
        """test that user edit page work"""
        url = reverse('admin:core_user_change', args=[self.user.id])
        res = self.client.get(url)
        self.assertEquals(res.status_code, 200)

    def test_create_user_page(self):
        """test that user page is created"""
        url = reverse('admin:core_user_add')
        res = self.client.get(url)
        self.assertEquals(res.status_code, 200)
