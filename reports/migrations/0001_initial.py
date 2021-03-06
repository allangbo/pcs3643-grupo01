# Generated by Django 3.2.7 on 2021-11-05 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.BooleanField(default=False, verbose_name='Relatório de faturamento?')),
                ('start_date', models.DateField(verbose_name='Data de início')),
                ('end_date', models.DateField(verbose_name='Data de fim')),
            ],
        ),
    ]
