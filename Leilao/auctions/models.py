from django.db import models
from django.urls import reverse

from batches.models import Batch
from users.models import User


class Auction(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    batch_id = models.ForeignKey(Batch, on_delete=models.CASCADE, null=True)
    profit = models.DecimalField(decimal_places=2, max_digits=15, null=True)
    auctioneer_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name="Auctioneer")
    winner_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name="Winner")

    def __str__(self):
        return self.batch_id

    def get_absolute_url(self):
        return reverse('auction:auction_edit', kwargs={'pk': self.pk})