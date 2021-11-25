from django import forms
from django.db import models
from django.urls import reverse

from django.contrib.auth.models import User

from products.models import Product

class Batch(models.Model):
    description = models.CharField("Descrição", max_length=500, null=True, blank=True)
    reserve_value = models.DecimalField("Valor de Reserva", decimal_places=2, max_digits=15)
    seller = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Vendedor")
    products = models.ManyToManyField(Product, verbose_name="Produtos")
    
    def __str__(self):
        return self.description

    def get_absolute_url(self):
        return reverse("batches:batch_list")
