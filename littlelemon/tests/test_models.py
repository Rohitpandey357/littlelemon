from django.test import TestCase
from restaurant.models import Menu, Booking

class MenuTestCase(TestCase):
    def test_get_menu(self):
        menu = Menu.objects.create(title='IceCream', price=80, inventory=100)
        self.assertEqual(str(menu), "IceCream : 80")