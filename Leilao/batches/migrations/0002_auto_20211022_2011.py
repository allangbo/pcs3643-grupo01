# Generated by Django 3.2.7 on 2021-10-22 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('batches', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='batch',
            name='fee',
            field=models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Taxa'),
        ),
        migrations.AlterField(
            model_name='batch',
            name='min_bid_increase_value',
            field=models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Aumento mínimo por lance'),
        ),
        migrations.AlterField(
            model_name='batch',
            name='min_value',
            field=models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Valor mínimo'),
        ),
        migrations.AlterField(
            model_name='batch',
            name='payed',
            field=models.BooleanField(verbose_name='Pago'),
        ),
        migrations.AlterField(
            model_name='batch',
            name='register_fee',
            field=models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Taxa de registro'),
        ),
        migrations.AlterField(
            model_name='batch',
            name='reserve_value',
            field=models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Reserva'),
        ),
        migrations.AlterField(
            model_name='batch',
            name='sequential_number',
            field=models.CharField(max_length=50, verbose_name='Número sequencial'),
        ),
        migrations.AlterField(
            model_name='batch',
            name='value',
            field=models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Valor'),
        ),
    ]
