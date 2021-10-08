from django.db import models
from django.urls import reverse


class User(models.Model):
    name = models.CharField(max_length=200)
    cpf = models.CharField(max_length=11)
    email = models.CharField(max_length=200)
    user_type = models.IntegerField()
    password = models.CharField(max_length=15)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('users:user_edit', kwargs={'pk': self.pk})