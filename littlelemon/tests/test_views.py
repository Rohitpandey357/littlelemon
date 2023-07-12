from django.test import TestCase
from restaurant.views import MenuItemsView
from restaurant.models import Menu

class MenuViewTestCase(TestCase):
    def setUp(self):
        menu = Menu.objects.create(title='IceCream', price=80, inventory=100)
        menu.save()
        menu = Menu.objects.create(title='Sandwich', price=15, inventory=50)
        menu.save()
        
    def test_getall(self):
        menu = Menu.objects.all()
        self.assertEqual(str(menu[0]), 'IceCream : 80.00')
        self.assertEqual(str(menu[1]), 'Sandwich : 15.00')