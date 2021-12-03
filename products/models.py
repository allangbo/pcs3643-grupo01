from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Product(models.Model):
    name = models.CharField("Nome", max_length=50)
    description = models.CharField("Descrição", max_length=500, null=True, blank=True)
    picture = models.ImageField("Figura", upload_to='images/', null=True, blank=True)
    seller = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    @property
    def picture_url(self):
        if self.picture and hasattr(self.picture, 'url'):
            return self.picture.url

    def get_absolute_url(self):
        return reverse("products:product_list")
