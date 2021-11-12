from django.contrib.auth.models import User
from django.test import TestCase

from batches.models import Batch

# Create your tests here.

from .models import Auction
from .models import Bid


class AuctionModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        """Set up non-modified objects used by all test methods.""" 
        User.objects.create(username='username', email='email@com.br', password='senha')
        Batch.objects.create(reserve_value=20.32, value=20.00, seller= User.objects.latest('id'))
        Auction.objects.create(start_date='2021-10-14 15:20:51.388054', end_date='2021-10-20 15:20:51.388054', min_value=0.02, min_bid_increase_value=0.02, register_fee=0.01, auctioneer = User.objects.latest('id'), batch = Batch.objects.latest('id'))

    def test_start_date_label(self):
        auction = Auction.objects.latest('id')
        field_label = auction._meta.get_field('start_date').verbose_name
        self.assertEquals(field_label, 'Data de início')

    def test_end_date_label(self):
        auction = Auction.objects.latest('id')
        field_label = auction._meta.get_field('end_date').verbose_name
        self.assertEquals(field_label, 'Data de fim')

    def test_buy_fee_label(self):
        auction = Auction.objects.latest('id')
        field_label = auction._meta.get_field('buy_fee').verbose_name
        self.assertEquals(field_label, 'Taxa de Compra')

    def test_register_fee_label(self):
        auction = Auction.objects.latest('id')
        field_label = auction._meta.get_field('register_fee').verbose_name
        self.assertEquals(field_label, 'Taxa de Registro')

    def test_register_fee_paid_label(self):
        auction = Auction.objects.latest('id')
        field_label = auction._meta.get_field('register_fee_paid').verbose_name
        self.assertEquals(field_label, 'Taxa de Registro Paga')
    
    def test_buy_fee_paid_label(self):
        auction = Auction.objects.latest('id')
        field_label = auction._meta.get_field('buy_fee_paid').verbose_name
        self.assertEquals(field_label, 'Taxa da Compra Paga')

    def test_min_value_label(self):
        auction = Auction.objects.latest('id')
        field_label = auction._meta.get_field('min_value').verbose_name
        self.assertEquals(field_label, 'Valor mínimo')

    def test_min_bid_increase_value_label(self):
        auction = Auction.objects.latest('id')
        field_label = auction._meta.get_field('min_bid_increase_value').verbose_name
        self.assertEquals(field_label, 'Aumento mínimo por lance')

    def test_profit_label(self):
        auction = Auction.objects.latest('id')
        field_label = auction._meta.get_field('profit').verbose_name
        self.assertEquals(field_label, 'Lucro')

    def test_get_absolute_url(self):
        auction = Auction.objects.latest('id')
        # This will also fail if the urlconf is not defined.
        self.assertEquals(auction.get_absolute_url(), '/auctions/')

class BidModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        """Set up non-modified objects used by all test methods."""
        User.objects.create(username='username', email='email@com.br', password='senha')
        Batch.objects.create(reserve_value=20.32, value=20.00, seller= User.objects.latest('id'))
        Auction.objects.create(start_date='2021-10-14', end_date='2021-10-20', min_value=0.02, min_bid_increase_value=0.02, register_fee=0.01, auctioneer = User.objects.latest('id'), batch = Batch.objects.latest('id'))
        Bid.objects.create(value=50.02, auction = Auction.objects.latest('id'), buyer= User.objects.latest('id'))

    def test_value_label(self):
        bid = Bid.objects.latest('id')
        field_label = bid._meta.get_field('value').verbose_name
        self.assertEquals(field_label, 'Valor')

    def test_value_max_digits(self):
        bid = Bid.objects.latest('id')
        max_digits = bid._meta.get_field('value').max_digits
        self.assertEquals(max_digits, 15)

    def test_value_decimal_places(self):
        bid = Bid.objects.latest('id')
        decimal_places = bid._meta.get_field('value').decimal_places
        self.assertEquals(decimal_places, 2)

    def test_get_absolute_url(self):
        bid = Bid.objects.latest('id')
        # This will also fail if the urlconf is not defined.
        self.assertEquals(bid.get_absolute_url(), '/auctions/bid/list')