from django.contrib.auth.models import User
from django.test import TestCase

# Create your tests here.

from .models import Batch
class BatchModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        """Set up non-modified objects used by all test methods."""
        User.objects.create(username='username', email='email@com.br', password='senha')
        Batch.objects.create(reserve_value=20.32, value=20.00, seller= User.objects.latest('id'))

    def test_reserve_value_label(self):
        batch = Batch.objects.latest('id')
        field_label = batch._meta.get_field('reserve_value').verbose_name
        self.assertEquals(field_label, 'Valor de Reserva')

    def test_value_label(self):
        batch = Batch.objects.latest('id')
        field_label = batch._meta.get_field('value').verbose_name
        self.assertEquals(field_label, 'Valor')

    def test_get_absolute_url(self):
        batch = Batch.objects.latest('id')
        # This will also fail if the urlconf is not defined.
        self.assertEquals(batch.get_absolute_url(), '/batches/')  