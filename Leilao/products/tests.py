from django.test import TestCase

# Create your tests here.

from models import Product


class ProductModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        """Set up non-modified objects used by all test methods."""
        Product.objects.create(name='Nome Teste')

    def test_name_label(self):
        product = Product.objects.get(id=1)
        field_label = product._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'Nome')

    def test_description_label(self):
        product = Product.objects.get(id=1)
        field_label = product._meta.get_field('description').verbose_name
        self.assertEquals(field_label, 'Descrição')

    def test_picture_label(self):
        product = Product.objects.get(id=1)
        field_label = product._meta.get_field('picture').verbose_name
        self.assertEquals(field_label, 'Foto')

    def test_name_max_length(self):
        product = Product.objects.get(id=1)
        max_length = product._meta.get_field('name').max_length
        self.assertEquals(max_length, 50)

    def test_description_max_length(self):
        product = Product.objects.get(id=1)
        max_length = product._meta.get_field('description').max_length
        self.assertEquals(max_length, 500)

    def test_picture_max_length(self):
        product = Product.objects.get(id=1)
        max_length = product._meta.get_field('picture').max_length
        self.assertEquals(max_length, 100)
        
    def test_get_absolute_url(self):
        product = Product.objects.get(id=1)
        # This will also fail if the urlconf is not defined.
        self.assertEquals(product.get_absolute_url(), '/products/edit/1')