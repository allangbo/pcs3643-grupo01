from django.db import models
from django.urls import reverse


class Seller(models.Model):
    name = models.CharField(max_length=200)
    cpf = models.CharField(max_length=11)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('sellers:seller_edit', kwargs={'pk': self.pk})