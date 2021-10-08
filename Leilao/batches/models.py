from django.db import models
from django.urls import reverse

from users.models import User

class Batch(models.Model):
    reserve_value = models.DecimalField(decimal_places=2, max_digits=15,)
    value = models.DecimalField(decimal_places=2, max_digits=15,)
    fee = models.DecimalField(decimal_places=2, max_digits=15,)
    register_fee = models.DecimalField(decimal_places=2, max_digits=15,)
    payed = models.BooleanField()
    sequential_number = models.CharField(max_length=50)
    min_value = models.DecimalField(decimal_places=2, max_digits=15,)
    min_bid_increase_value = models.DecimalField(decimal_places=2, max_digits=15,)
    seller_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    

    def __str__(self):
        return self.batch_id

    def get_absolute_url(self):
        return reverse('bid:bid_edit', kwargs={'pk': self.pk})