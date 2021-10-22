from django.db import models
from django.urls import reverse

from batches.models import Batch
from users.models import User


class Auction(models.Model):
    start_date = models.DateField("Data de início", default='01/01/01')
    end_date = models.DateField("Data de fim", default='01/01/01')
    batch_id = models.OneToOneField(Batch, on_delete=models.CASCADE)
    profit = models.DecimalField("Lucro", decimal_places=2, max_digits=15, null=True)
    auctioneer_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='auctioned_by')
    winner_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='won_by')

    def __str__(self):
        return self.batch_id

    def get_absolute_url(self):
        return reverse('auction:auction_edit', kwargs={'pk': self.pk})