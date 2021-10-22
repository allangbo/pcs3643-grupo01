from django.test import TestCase

# Create your tests here.

from models import Batch


class BatchModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        """Set up non-modified objects used by all test methods."""
        Batch.objects.create(reserve_value=20.32, value=20.00, fee=0.23, register_fee=0.14, paid=False, sequential_number=1, min_value=22.34, min_bid_increase_value=25.00)

    def test_name_label(self):
        batch = Batch.objects.get(id=1)
        field_label = batch._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'Nome')

    def test_reserve_value_label(self):
        batch = Batch.objects.get(id=1)
        field_label = batch._meta.get_field('reserve_value').verbose_name
        self.assertEquals(field_label, 'Reserva')

    def test_value_label(self):
        batch = Batch.objects.get(id=1)
        field_label = batch._meta.get_field('value').verbose_name
        self.assertEquals(field_label, 'Valor')

    def test_fee_label(self):
        batch = Batch.objects.get(id=1)
        field_label = batch._meta.get_field('fee').verbose_name
        self.assertEquals(field_label, 'Taxa')

    def test_register_fee_label(self):
        batch = Batch.objects.get(id=1)
        field_label = batch._meta.get_field('register_fee').verbose_name
        self.assertEquals(field_label, 'Taxa de registro')

    def test_paid_label(self):
        batch = Batch.objects.get(id=1)
        field_label = batch._meta.get_field('paid').verbose_name
        self.assertEquals(field_label, 'Pago')

    def test_sequential_number_label(self):
        batch = Batch.objects.get(id=1)
        field_label = batch._meta.get_field('sequential_number').verbose_name
        self.assertEquals(field_label, 'Número sequencial')

    def test_min_value_label(self):
        batch = Batch.objects.get(id=1)
        field_label = batch._meta.get_field('min_value').verbose_name
        self.assertEquals(field_label, 'Valor mínimo')
    
    def test_min_bid_increase_value_label(self):
        batch = Batch.objects.get(id=1)
        field_label = batch._meta.get_field('min_bid_increase_value').verbose_name
        self.assertEquals(field_label, 'Aumento mínimo por lance')

    def test_get_absolute_url(self):
        batch = Batch.objects.get(id=1)
        # This will also fail if the urlconf is not defined.
        self.assertEquals(batch.get_absolute_url(), '/batches/edit/1')  