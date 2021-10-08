# Generated by Django 3.2.7 on 2021-10-08 21:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Batch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reserve_value', models.DecimalField(decimal_places=2, max_digits=15)),
                ('value', models.DecimalField(decimal_places=2, max_digits=15)),
                ('fee', models.DecimalField(decimal_places=2, max_digits=15)),
                ('register_fee', models.DecimalField(decimal_places=2, max_digits=15)),
                ('payed', models.BooleanField()),
                ('sequential_number', models.CharField(max_length=50)),
                ('min_value', models.DecimalField(decimal_places=2, max_digits=15)),
                ('min_bid_increase_value', models.DecimalField(decimal_places=2, max_digits=15)),
                ('seller_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.user')),
            ],
        ),
    ]
