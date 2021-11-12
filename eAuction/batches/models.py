from django import forms
from django.db import models
from django.urls import reverse

from django.contrib.auth.models import User

from products.models import Product

class Batch(models.Model):
    description = models.CharField("Descrição", max_length=500, null=True, blank=True)
    value = models.DecimalField("Valor", decimal_places=2, max_digits=15)
    reserve_value = models.DecimalField("Valor de Reserva", decimal_places=2, max_digits=15)
    seller = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    
    def __str__(self):
        return self.description

    def get_absolute_url(self):
        return reverse("batches:batch_list")
