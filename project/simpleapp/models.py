# from django.db import models
# from django.core.validators import MinValueValidator
#
# # Товар нашей витрины
# class Product(models.Model):
#     name = models.CharField( # models - единствинный и точный источник информации в ваших данныхю ОН содержит основные поля и поведения данных, которые вы храните. Обычно каждая модель сопостовляеться с одной таблицей базы данных
#                              # CharField ???
#         max_length=50, # Длина 50 символов
#         unique=True, # Название товаров не должно повторяться
#     )
#
#     description = models.TextField() # TextField ???
#
#     quantity = models.IntegerField( # IntegerField ???
#         validators=[MinValueValidator(0)],
#     )
#
#     # Поле категории будет ссылаться на модель категории
#     category = models.ForeignKey(
#         to='Category',
#         on_delete=models.CASCADE,
#         related_name='products' # Все продукты в категории будут доступны через поле products
#     )
#
#     price = models.FloatField(
#         validators=[MinValueValidator(0.0)],
#     )
#
#     def __str__(self):
#         return f'{self.name.title()}:{self.description[:20]}'
#
# # Категория, которой будет привязывать товар
# class Category(models.Model):
#     # Название категории тоже не должны повторяться
#     name = models.CharField(max_length=100, unique=True)
#
#     def __str__(self):
#         return self.name.title()
#

from django.db import models
from django.core.validators import MinValueValidator


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name.title()


class Product(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField()
    quantity = models.IntegerField(validators=[MinValueValidator(0)])
    price = models.FloatField(validators=[MinValueValidator(0.0)])

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='products'
    )

    def __str__(self):
        return f'{self.name.title()}:{self.description[:20]}'