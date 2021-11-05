from django.contrib.auth.models import User
from django.test import TestCase

# Create your tests here.

from .models import Product


class ProductModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        """Set up non-modified objects used by all test methods.""" 
        # batch=Batch.objects.latest('id')
        User.objects.create(username='username', email='email@com.br', password='senha')
        Product.objects.create(name='Nome Teste', seller= User.objects.all().latest('id'))

    def test_name_label(self):
        product = Product.objects.latest('id')
        field_label = product._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'Nome')

    def test_description_label(self):
        product = Product.objects.latest('id')
        field_label = product._meta.get_field('description').verbose_name
        self.assertEquals(field_label, 'Descrição')

    def test_picture_label(self):
        product = Product.objects.latest('id')
        field_label = product._meta.get_field('picture').verbose_name
        self.assertEquals(field_label, 'Url da foto')

    def test_name_max_length(self):
        product = Product.objects.latest('id')
        max_length = product._meta.get_field('name').max_length
        self.assertEquals(max_length, 50)

    def test_description_max_length(self):
        product = Product.objects.latest('id')
        max_length = product._meta.get_field('description').max_length
        self.assertEquals(max_length, 500)

    def test_picture_max_length(self):
        product = Product.objects.latest('id')
        max_length = product._meta.get_field('picture').max_length
        self.assertEquals(max_length, 100)
        
    def test_get_absolute_url(self):
        product = Product.objects.latest('id')
        # This will also fail if the urlconf is not defined.
        self.assertEquals(product.get_absolute_url(), '/products/')