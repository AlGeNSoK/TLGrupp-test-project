from django.db import models


class Company(models.Model):
    """
        Модель компании
    """
    name = models.CharField(max_length=100, verbose_name='название')
    catchPhrase = models.CharField(max_length=100)
    bs = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Geo(models.Model):
    """
        Модель местоположения
    """
    lat = models.CharField(max_length=100, verbose_name='широта')
    lng = models.CharField(max_length=100, verbose_name='долгота')


class Address(models.Model):
    """
        Модель адреса
    """
    street = models.CharField(max_length=100, verbose_name='улица')
    suite = models.CharField(max_length=100, verbose_name='корпус')
    city = models.CharField(max_length=100, verbose_name='город')
    zipcode = models.CharField(max_length=100, verbose_name='почтовый индекс')
    geo = models.ForeignKey(Geo, related_name='address', on_delete=models.CASCADE, verbose_name='местоположение')


class User(models.Model):
    """
        Модель пользователя
    """
    name = models.CharField(max_length=100, verbose_name='имя')
    username = models.CharField(max_length=100, verbose_name='имя пользователя')
    email = models.EmailField(max_length=100, verbose_name='электронная почта')
    address = models.ForeignKey(Address, related_name='user', on_delete=models.CASCADE, verbose_name='адрес')
    phone = models.CharField(max_length=100, verbose_name='телефон')
    website = models.URLField(verbose_name='сайт')
    company = models.ForeignKey(Company, related_name='user', on_delete=models.CASCADE, verbose_name='компания')

    def __str__(self):
        return self.name


class Post(models.Model):
    """
        Модель поста
    """
    title = models.CharField(max_length=100, verbose_name='заголовок')
    body = models.TextField(verbose_name='текст')
    userId = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE, verbose_name='пользователь')

    def __str__(self):
        return self.title
