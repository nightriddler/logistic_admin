# Generated by Django 4.0.5 on 2022-06-03 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shipping', '0008_alter_shipping_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shipping',
            name='date',
            field=models.DateField(blank=True, null=True, verbose_name='Дата'),
        ),
    ]
