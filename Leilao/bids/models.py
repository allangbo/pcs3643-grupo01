from django.db import models
from django.urls import reverse

from users.models import User
from auctions.models import Auction


class Bid(models.Model):
    value = models.DecimalField(decimal_places=2, max_digits=15,)
    auction_id = models.ForeignKey(Auction, on_delete=models.CASCADE, null=True)
    buyer_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.buyer_id

    def get_absolute_url(self):
        return reverse('bid:bid_edit', kwargs={'pk': self.pk})