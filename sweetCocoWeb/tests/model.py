from django.test import TestCase
from model_bakery import baker
from decimal import *
from sweetCocoWeb.models import Order, Product, OrderItem
from sweetCocoWeb.generator import string_generator, decimal_generator, dateTime_generator
# Create your tests here.
class TestProductModel(TestCase): 
    def test_product_creation(self):
        for i in range(0, 5):
            name = string_generator()
            description = string_generator()
            price = decimal_generator()
            url = string_generator()

            product = Product.objects.create(
                name=name, 
                description=description, 
                url=url,
                price=price
            )

            print('---------------------------------- Run test creating Product ----------------------------------') 
            # Test creation Product
            self.assertIsInstance(product, Product)
            print('Object successful created') 
            self.assertEqual(product.name, name, msg='Name is correct')
            self.assertEqual(product.description, description, msg='Description is correct')
            self.assertEqual(product.price, price, msg='Price is correct')
            self.assertEqual(product.url, url, msg='Url is correct')
            print('All fields are correct') 
            # Test if the created object is saved in the database
            try:
                saved_product = Product.objects.get(id=product.id)
                print('---------------------------------- Run test saved Product ----------------------------------')
                self.assertEqual(product.name, saved_product.name, msg='Name is correct. Saved')
                self.assertEqual(product.description, saved_product.description, msg='Description is correct. Saved')
                self.assertEqual(product.price, saved_product.price, msg='Price is correct. Saved')
                self.assertEqual(product.url, saved_product.url, msg='Url is correct. Saved')
                print('Correctly saved.')
                print('---------------------------------- Finish test Product ----------------------------------')
            except Product.DoesNotExist:
                self.fail("Product was not saved in the database.")

    

