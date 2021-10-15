from django.db import models
from django.urls import reverse


class User(models.Model):
    name = models.CharField("Nome", max_length=200)
    cpf = models.CharField("CPF", max_length=11)
    email = models.CharField("E-mail", max_length=200)
    user_type = models.IntegerField("Tipo de usuário")
    password = models.CharField("Senha: ", max_length=15)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('users:user_edit', kwargs={'pk': self.pk})