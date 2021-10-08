from django.db import models
from django.urls import reverse

from users.models import User


class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    picture = models.CharField(max_length=50)
    batch_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.batch_id

    def get_absolute_url(self):
        return reverse('auction:auction_edit', kwargs={'pk': self.pk})