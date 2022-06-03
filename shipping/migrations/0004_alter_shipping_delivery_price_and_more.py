# Generated by Django 4.0.4 on 2022-05-31 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shipping', '0003_alter_shipping_waybill_alter_shipping_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shipping',
            name='delivery_price',
            field=models.PositiveIntegerField(verbose_name='Цена доставки'),
        ),
        migrations.AlterField(
            model_name='shipping',
            name='purchase_price',
            field=models.PositiveIntegerField(verbose_name='Цена покупки'),
        ),
        migrations.AlterField(
            model_name='shipping',
            name='quantity',
            field=models.PositiveIntegerField(default=1, verbose_name='Количество'),
        ),
        migrations.AlterField(
            model_name='shipping',
            name='sales_price',
            field=models.PositiveIntegerField(verbose_name='Цена продажи'),
        ),
        migrations.AlterField(
            model_name='shipping',
            name='sales_tax',
            field=models.PositiveIntegerField(verbose_name='ТТН'),
        ),
    ]
