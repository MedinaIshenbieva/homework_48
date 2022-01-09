from django.db import models

# Create your models here.
CATEGORY_CHOICES = [('cosmetic', 'Косметика'), ('clothes', 'Одежда'), ('other', 'Разное')]


class ElShop(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, verbose_name="Наименование товара ")
    description = models.TextField(max_length=2000, null=True, blank=True, verbose_name="Описание товара")
    category = models.CharField(max_length=2000, null=False, blank=False, default='other', choices=CATEGORY_CHOICES,
                                verbose_name="Категория")
    remnant = models.IntegerField(verbose_name="Остаток")
    cost = models.DecimalField(max_digits=7, decimal_places=2, verbose_name="Стоимость")

    def __str__(self):
        return f"{self.pk}. {self.name}- {self.cost}$ {self.category}"

    class Meta:
        db_table = 'el_shop'
        verbose_name_plural = 'Электронный магазин'
