from django.db import models
from django.urls import reverse

from batches.models import Batch


class Product(models.Model):
    name = models.CharField("Nome", max_length=50, default="")
    description = models.CharField("Descrição", max_length=500, null=True)
    picture = models.CharField("Foto", max_length=100, null=True)
    batch = models.ForeignKey(Batch, on_delete=models.CASCADE, default='1')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('products:product_edit', kwargs={'pk': self.pk})