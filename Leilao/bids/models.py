from django.db import models
from django.urls import reverse

from users.models import User


class Bid(models.Model):
    value = models.DecimalField(decimal_places=2, max_digits=15,)
    buyer_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.batch_id

    def get_absolute_url(self):
        return reverse('bid:bid_edit', kwargs={'pk': self.pk})