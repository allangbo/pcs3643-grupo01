from django.test import TestCase

# Create your tests here.

from catalog.models import Bid


class BidModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        """Set up non-modified objects used by all test methods."""
        Bid.objects.create(value=50.02)

    def test_value_label(self):
        bid = Bid.objects.get(id=1)
        field_label = bid._meta.get_field('value').verbose_name
        self.assertEquals(field_label, 'valor')

    def test_value_max_digits(self):
        bid = Bid.objects.get(id=1)
        max_digits = bid._meta.get_field('value').max_digits
        self.assertEquals(max_digits, 15)

    def test_value_decimal_places(self):
        bid = Bid.objects.get(id=1)
        decimal_places = bid._meta.get_field('value').decimal_places
        self.assertEquals(decimal_places, 2)

    def test_get_absolute_url(self):
        bid = Bid.objects.get(id=1)
        # This will also fail if the urlconf is not defined.
        self.assertEquals(bid.get_absolute_url(), '/bids/edit/1')