# Generated by Django 3.2.7 on 2021-11-19 18:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auctions', '0004_auto_20211119_1235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auction',
            name='buy_fee',
            field=models.DecimalField(decimal_places=2, max_digits=15, null=True, verbose_name='Taxa de Compra'),
        ),
        migrations.AlterField(
            model_name='auction',
            name='profit',
            field=models.DecimalField(decimal_places=2, max_digits=15, null=True, verbose_name='Lucro'),
        ),
        migrations.AlterField(
            model_name='auction',
            name='winner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='won_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='auction',
            name='winner_bid',
            field=models.DecimalField(decimal_places=2, max_digits=15, null=True, verbose_name='Lance Vencedor'),
        ),
        migrations.AlterField(
            model_name='auction',
            name='winner_bid_id',
            field=models.DecimalField(decimal_places=0, max_digits=30, null=True),
        ),
    ]
