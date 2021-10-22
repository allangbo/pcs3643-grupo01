# Generated by Django 3.2.7 on 2021-10-22 20:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20211022_2059'),
        ('auctions', '0007_auto_20211022_2051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auction',
            name='auctioneer_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='auctioned_by', to='users.user'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='auction',
            name='end_date',
            field=models.DateField(default='01/01/01', verbose_name='Data de fim'),
        ),
        migrations.AlterField(
            model_name='auction',
            name='profit',
            field=models.DecimalField(decimal_places=2, default=0.01, max_digits=15, null=True, verbose_name='Lucro'),
        ),
        migrations.AlterField(
            model_name='auction',
            name='start_date',
            field=models.DateField(default='01/01/01', verbose_name='Data de início'),
        ),
        migrations.AlterField(
            model_name='auction',
            name='winner_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='won_by', to='users.user'),
            preserve_default=False,
        ),
    ]
