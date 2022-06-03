from django.db import models


class Shipping(models.Model):
    waybill_choice = (("1", "Да"), ("0", "Нет"))

    date = models.DateField(
        null=True,
        blank=True,
        verbose_name="Дата",
    )
    supplier = models.CharField(blank=True, max_length=250, verbose_name="Поставщик")
    factory = models.CharField(blank=True, max_length=250, verbose_name="Завод")
    order = models.CharField(blank=True, max_length=250, verbose_name="Приказ")
    seller = models.CharField(blank=True, max_length=250, verbose_name="Продавец")
    buyer = models.CharField(blank=True, max_length=250, verbose_name="Покупатель")
    waybill = models.CharField(
        max_length=250,
        verbose_name="Накладная",
        choices=waybill_choice,
        default="0",
    )
    sales_tax = models.CharField(blank=True, max_length=250, verbose_name="ТТН")
    product = models.CharField(blank=True, max_length=250, verbose_name="Продукция")
    quantity = models.PositiveIntegerField(
        blank=True, verbose_name="Количество", default=1
    )
    purchase_price = models.PositiveIntegerField(
        blank=True, verbose_name="Цена покупки", default="5000"
    )
    sales_price = models.PositiveIntegerField(
        blank=True, verbose_name="Цена продажи", default="0"
    )
    delivery_price = models.PositiveIntegerField(
        blank=True, verbose_name="Цена доставки", default="0"
    )
    driver = models.CharField(blank=True, max_length=250, verbose_name="Водитель")
    address = models.CharField(blank=True, max_length=250, verbose_name="Адрес")
    dispatcher = models.CharField(blank=True, max_length=250, verbose_name="Диспетчер")
    comment = models.CharField(blank=True, max_length=250, verbose_name="Комментарий")

    class Meta:
        db_table = "Таблица отгрузок"
        verbose_name = "Отгрузку"
        verbose_name_plural = "Отгрузки"
        ordering = ["-id"]

    def __str__(self):
        return f"{self.date} {self.buyer} {self.driver} {self.address}"
