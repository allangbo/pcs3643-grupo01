# Generated by Django 3.2.7 on 2021-11-02 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_product_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.CharField(blank=True, default='', max_length=500, null=True, verbose_name='Descrição'),
        ),
    ]