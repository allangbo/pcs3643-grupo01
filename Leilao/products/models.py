from django.db import models
from django.urls import reverse

from batches.models import Batch


class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    picture = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('products:product_edit', kwargs={'pk': self.pk})