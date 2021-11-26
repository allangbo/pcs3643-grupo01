from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import DecimalField
from django.db.models.fields.related import ForeignKey
from django.urls import reverse

from django.contrib.auth.models import User
from django.utils import timezone

from batches.models import Batch


class Auction(models.Model):
    class StateType(models.TextChoices):
        NOT_STARTED = 'Não iniciado'
        RUNNING = 'Ocorrendo'
        FINISHED = 'Finalizado'
        INVALID = 'Não atingiu o valor de reserva'
        CANCELED = 'Cancelado'

    state = models.CharField("Tipo de relatório",
        max_length=50,
        choices=StateType.choices,
        default=StateType.NOT_STARTED,
    )
    start_date = models.DateTimeField("Data de início")
    end_date = models.DateTimeField("Data de fim")
    start_date = models.DateTimeField("Data de início")
    end_date = models.DateTimeField("Data de fim")
    batch = models.OneToOneField(Batch, verbose_name="Lote", on_delete=models.CASCADE)    
    auctioneer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='auctioned_by')
    winner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='won_by', null=True)
    winner_bid = models.DecimalField("Lance Vencedor", decimal_places=2, max_digits=15, null=True)
    winner_bid_id = DecimalField(decimal_places=0, max_digits=30, null=True)
    min_value = models.DecimalField("Valor inicial", decimal_places=2, max_digits=15)    
    min_bid_increase_value = models.DecimalField("Aumento mínimo por lance", decimal_places=2, max_digits=15)
    register_fee = models.DecimalField("Taxa de Registro", decimal_places=2, max_digits=15)   
    buy_fee = models.DecimalField("Taxa de Compra", decimal_places=2, max_digits=15, null=True)
    register_fee_paid = models.BooleanField("Taxa de Registro Paga", default=False)
    buy_fee_paid = models.BooleanField("Taxa da Compra Paga", default=False)
    profit = models.DecimalField("Lucro", decimal_places=2, max_digits=15, null=True)


    def __str__(self):
        return str(self.id)

    def get_absolute_url(self):
        return reverse("auctions:auction_list")

    def get_start_date(self):
        return self.start_date

    def update_state(self):
        if self.state != self.StateType.CANCELED:
            now = timezone.now()
            if now >= self.end_date and self.winner_bid >= self.batch.reserve_value:
                self.state = self.StateType.FINISHED
            elif now < self.end_date:
                if now >= self.start_date:
                    self.state = self.StateType.RUNNING
                else:
                    self.state = self.StateType.NOT_STARTED
            else:
                self.state = self.StateType.INVALID
        self.save()

class Bid(models.Model):
    value = models.DecimalField("Valor", decimal_places=2, max_digits=15)
    auction = models.ForeignKey(Auction, on_delete=models.CASCADE)
    buyer = models.ForeignKey(User, on_delete=models.CASCADE)
    datetime = models.DateTimeField("Data e Horário", null=True)

    def __str__(self):
        return str(self.id)

    def get_absolute_url(self):
        return reverse("auctions:bid_list")