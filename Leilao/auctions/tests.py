from django.test import TestCase

# Create your tests here.

from auction.models import Auction


class AuctionModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        """Set up non-modified objects used by all test methods.""" 
        Auction.objects.create(start_date='14/10/2021', end_date='20/10/2021')

    def test_start_date_label(self):
        auction = Auction.objects.get(id=1)
        field_label = auction._meta.get_field('start_date').verbose_name
        self.assertEquals(field_label, 'Data de início')

    def test_end_date_label(self):
        auction = Auction.objects.get(id=1)
        field_label = auction._meta.get_field('end_date').verbose_name
        self.assertEquals(field_label, 'Data de fim')

    def test_profit_label(self):
        auction = Auction.objects.get(id=1)
        field_label = auction._meta.get_field('profit').verbose_name
        self.assertEquals(field_label, 'Lucro')

    def test_get_absolute_url(self):
        auction = Auction.objects.get(id=1)
        # This will also fail if the urlconf is not defined.
        self.assertEquals(auction.get_absolute_url(), '/auctions/edit/1')