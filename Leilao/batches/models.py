from django.db import models
from django.urls import reverse


from users.models import User

class Batch(models.Model):
    reserve_value = models.DecimalField("Reserva", decimal_places=2, max_digits=15, default=0.01)
    value = models.DecimalField("Valor", decimal_places=2, max_digits=15, default=0.01)
    fee = models.DecimalField("Taxa", decimal_places=2, max_digits=15, default=0.01)
    register_fee = models.DecimalField("Taxa de registro", decimal_places=2, max_digits=15, default=0.01)
    paid = models.BooleanField("Pago", default=False)
    sequential_number = models.CharField("Número sequencial", max_length=50, default="")
    min_value = models.DecimalField("Valor mínimo", decimal_places=2, max_digits=15, default=0.01)
    min_bid_increase_value = models.DecimalField("Aumento mínimo por lance", decimal_places=2, max_digits=15, default=0.01)
    seller_id = models.ForeignKey(User, on_delete=models.CASCADE)    

    def __str__(self):
        return self.sequential_number

    def get_absolute_url(self):
        return reverse('bids:bid_edit', kwargs={'pk': self.pk})