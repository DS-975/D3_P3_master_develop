# Как я создавал это проект
#
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#
# Сoздаём виртуальное окружение
python -m venv venv
#
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#
# Активируем виртуальное окружение
.\venv\Scripts\activate
#
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#
# Устанавливаем библиотеки из requirements.txt (Django)
pip install -r requirements.txt
#
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Создание админки 21 - 65 < - ☻☻☻CREATESUREPUSER☻☻☻
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Создал новый Django-проект
django-admin startproject project
#
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#
# Переходим в папку project
cd .\project
#
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# 
# Создал приложение simpleapp
python manage.py startapp simpleapp
#
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#
# Запуски сервера
python manage.py runserver
#
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#
# Создаём новые миграции
python manage.py makemigrations
#
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#
# Применяем миграции
python manage.py migrate
#
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#
# Создаём админку 
#
python manage.py createsuperuser
#
# Username: admin
# Password: admin
#
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#

# Запуски сервера
python manage.py runserver
#
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#
# Установил приложение Flatpages | Документация - > https://docs.djangoproject.com/en/3.1/ref/contrib/flatpages/
#
# В project/project/settings.py -> INSTALLED_APPS | 41 'django.contrib.sites', # <- Для работы приложения Flatpages
#                                                 | 42 'django.contrib.flatpages', # <- Для работы приложения Flatpages
#
# В project/project/settings.py -> MIDDLEWARE | 54 | 'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware', # <- Для работы приложения Flatpages
#
# В project/project/settings.py -> | 57 SITE_ID = 1 # <- Для работы приложения Flatpages
#
# В project/project/urls.py -> | include | 18 | from django.urls import path, include
#
# В project/project/urls.py -> | 22 | path('pages/', include('django.contrib.flatpages.urls')),
#
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#
# B project/simpleapp/models.py -> |  1 | from django.db import models
#                                  |  2 | from django.core.validators import MinValueValidator
#                                  |  3 |
#                                  |  4 |
#                                  |  5 | # Товар для нашей витрины
#                                  |  6 | class Product(models.Model):
#                                  |  7 |    name = models.CharField(
#                                  |  8 |    max_length=50,
#                                  |  9 |    unique=True, # названия товаров не должны повторяться
#                                  | 10 |    )
#                                  | 11 |    description = models.TextField()
#                                  | 12 |    quantity = models.IntegerField(
#                                  | 13 |    validators=[MinValueValidator(0)],
#                                  | 14 |    )
#                                  | 15 |    # поле категории будет ссылаться на модель категории
#                                  | 16 |    category = models.ForeignKey(
#                                  | 17 |        to='Category',
#                                  | 18 |        on_delete=models.CASCADE,
#                                  | 19 |        related_name='products', # все продукты в категории будут доступны через поле products
#                                  | 20 |    )
#                                  | 21 |    price = models.FloatField(
#                                  | 22 |        validators=[MinValueValidator(0.0)],
#                                  | 23 |    )
#                                  | 24 |
#                                  | 25 |    def __str__(self):
#                                  | 26 |        return f'{self.name.title()}: {self.description[:20]}'
#                                  | 27 |
#                                  | 28 |
#                                  | 29 | # Категория, к которой будет привязываться товар
#                                  | 30 | class Category(models.Model):
#                                  | 31 |     # названия категорий тоже не должны повторяться
#                                  | 32 |     name = models.CharField(max_length=100, unique=True)
#                                  | 33 |
#                                  | 34 |     def __str__(self):
#                                  | 35 |         return self.name.title()
#
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#
# B project/simpleapp/admin.py -> | 1 | from django.contrib import admin
#                                 | 2 | from .models import Category, Product
#                                 | 3 |
#                                 | 4 |
#                                 | 5 | admin.site.register(Category)
#                                 | 6 | admin.site.register(Product)
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#
# B project/simpleapp/views.py -> |  1 | # Импортируем класс, который говорит нам о том,
#                                 |  2 | # что в этом представлении мы будем выводить список объектов из БД
#                                 |  3 | from django.views.generic import ListView
#                                 |  4 | from .models import Product
#                                 |  5 |
#                                 |  6 |
#                                 |  7 | class ProductsList(ListView):
#                                 |  8 |     # Указываем модель, объекты которой мы будем выводить
#                                 |  9 |     model = Product
#                                 | 10 |     # Поле, которое будет использоваться для сортировки объектов
#                                 | 11 |     ordering = 'name'
#                                 | 12 |     # Указываем имя шаблона, в котором будут все инструкции о том,
#                                 | 13 |     # как именно пользователю должны быть показаны наши объекты
#                                 | 14 |     template_name = 'products.html'
#                                 | 15 |     # Это имя списка, в котором будут лежать все объекты.
#                                 | 16 |     # Его надо указать, чтобы обратиться к списку объектов в html-шаблоне.
#                                 | 17 |     context_object_name = 'products'
#
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#
# B project/simpleapp -> New -> File -> urls.py
#
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#
# B project/simpleapp/urls.py -> |  1 | from django.urls import path
#                                |  2 | # Импортируем созданное нами представление
#                                |  3 | from .views import ProductsList
#                                |  4 |
#                                |  5 |
#                                |  6 | urlpatterns = [
#                                |  7 |    # path — означает путь.
#                                |  8 |    # В данном случае путь ко всем товарам у нас останется пустым,
#                                |  9 |    # чуть позже станет ясно почему.
#                                | 10 |    # Т.к. наше объявленное представление является классом,
#                                | 11 |    # а Django ожидает функцию, нам надо представить этот класс в виде view.
#                                | 12 |    # Для этого вызываем метод as_view.
#                                | 13 |    path('', ProductsList.as_view()),
#                                | 13 | ]
#
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#
# B project/project/urls.py -> |  1 | from django.contrib import admin
#                              |  2 | from django.urls import path, include
#                              |  3 |
#                              |  4 | urlpatterns = [
#                              |  5 |    path('admin/', admin.site.urls),
#                              |  6 |    path('pages/', include('django.contrib.flatpages.urls')),
#                              |  7 |    # Делаем так, чтобы все адреса из нашего приложения (simpleapp/urls.py)
#                              |  8 |    # подключались к главному приложению с префиксом products/.
#                              |  9 |    path('products/', include('simpleapp.urls')),
#                              | 10 ] ]
#
#
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#
# B projec/templates -> New -> File -> products.html
#
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#
# B projec/templates/products.html -> |  1 | <!--  наследуемся от шаблона default.html, который мы создавали для flatpages -->
#                                     |  2 | {% extends 'flatpages/default.html' %}
#                                     |  3 |
#                                     |  4 | <!-- Название у нас будет products -->
#                                     |  5 | {% block title %}
#                                     |  6 | Products
#                                     |  7 | {% endblock title %}
#                                     |  8 |
#                                     |  9 | <!-- В контенте на странице мы выводим все товары -->
#                                     | 10 | {% block content %}
#                                     | 11 | <h1>Все товары</h1>
#                                     | 12 | {{ products }}
#                                     | 13 | {% endblock content %}
#
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#
#
# Напомним, что скачать шаблон и статические файлы можно по ссылке.
# После скачивания нужно создать папку static
# и добавить в нее файлы styles.css
# по пути project/static/css/styles.css
# и index.html в project/static/index.html.
# В templates/flatpages/default.html должен быть
# базовый HTML темплейт.
# Вспомнить, что и как нужно настроить, вы можете в модуле D1.
#
# B projec -> New -> File -> static/css/styles.css
#
# B project/static  -> New -> File -> index.html
#
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#



# Запускаем окно командной строки
python manage.py shell

from newapp.models import *