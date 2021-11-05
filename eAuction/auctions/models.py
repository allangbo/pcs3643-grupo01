from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import DecimalField
from django.db.models.fields.related import ForeignKey
from django.urls import reverse

from django.contrib.auth.models import User

from batches.models import Batch


class Auction(models.Model):
    start_date = models.DateField("Data de início")
    end_date = models.DateField("Data de fim")
    batch = models.OneToOneField(Batch, on_delete=models.CASCADE)    
    auctioneer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='auctioned_by')
    winner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='won_by', null=True)
    winner_bid = models.DecimalField("Lance Vencedor", decimal_places=2, max_digits=15, null=True)
    winner_bid_id = DecimalField(decimal_places=0, max_digits=30, null=True)
    min_value = models.DecimalField("Valor mínimo", decimal_places=2, max_digits=15)    
    min_bid_increase_value = models.DecimalField("Aumento mínimo por lance", decimal_places=2, max_digits=15)
    register_fee = models.DecimalField("Taxa de Registro", decimal_places=2, max_digits=15)   
    buy_fee = models.DecimalField("Taxa de Compra", decimal_places=2, max_digits=15, null=True)
    register_fee_paid = models.BooleanField("Taxa de Registro Paga", default=False)
    buy_fee_paid = models.BooleanField("Taxa da Compra Paga", default=False)
    

    def __str__(self):
        return str(self.id)

    def get_absolute_url(self):
        return reverse("auctions:auction_list")

class Bid(models.Model):
    value = models.DecimalField("Valor", decimal_places=2, max_digits=15)
    auction = models.ForeignKey(Auction, on_delete=models.CASCADE)
    buyer = models.ForeignKey(User, on_delete=models.CASCADE)
    datetime = models.DateTimeField("Data e Horário", null=True)

    def __str__(self):
        return str(self.id)

    def get_absolute_url(self):
        return reverse("auctions:auction_list")