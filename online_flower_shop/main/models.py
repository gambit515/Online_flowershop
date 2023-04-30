from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User, Group
from django.db.models.signals import post_save
from django.dispatch import receiver

from online_flower_shop import settings

default_group = Group.objects.get(name=settings.DEFAULT_GROUP_NAME)

class Product(models.Model):
    Tittle = models.CharField('Название товара', blank=True, max_length=100)
    Text = models.TextField('Текст товара', blank=True, max_length=1500)
    Photo = models.ImageField('Фотография товара', blank=True, upload_to="photo/%Y/%m/%d/")
    Price = models.IntegerField('Цена товара', blank=True,)
    SubCat = models.ForeignKey('SubCategory', on_delete=models.CASCADE, blank=True, verbose_name="Категория товара")

    def get_absolute_url(self):
       return reverse('product', kwargs = {'product_id': self.pk})

    def __str__(self):
        return self.Tittle

    class Meta:
        verbose_name = "Товары"
        verbose_name_plural = "Товары"
        ordering = ['Tittle','SubCat','Price']


class Order(models.Model):
    Order_User = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, verbose_name="Заказчик")
    Order_Prod = models.ForeignKey('Product', on_delete=models.CASCADE, blank=True, verbose_name="Заказанный товар")
    Quantity = models.IntegerField('Количество', blank=True,)
    Status = models.CharField('Статус', blank=True, max_length=50)

    def get_absolute_url(self):
       return reverse('order', kwargs = {'order_id': self.pk})

    def __str__(self):
        return self.Order_User

    class Meta:
        verbose_name = "Заказы"
        verbose_name_plural = "Заказы"
        ordering = ['Order_User']


class Category(models.Model):
    Tittle = models.CharField('Название категории', blank=True, max_length=100)

    def get_absolute_url(self):
       return reverse('cat', kwargs = {'cat_id': self.pk})

    def __str__(self):
        return self.Tittle

    class Meta:
        verbose_name = "Категории"
        verbose_name_plural = "Категории"
        ordering = ['Tittle']


class SubCategory(models.Model):
    Tittle = models.CharField('Название подкатегории', blank=True, max_length=100)
    Cat = models.ForeignKey('Category', on_delete=models.CASCADE, blank=True, verbose_name="Основная категория")

    def get_absolute_url(self):
       return reverse('subcat', kwargs = {'subcat_id': self.pk})

    def __str__(self):
        return self.Tittle

    class Meta:
        verbose_name = "Подкатегории"
        verbose_name_plural = "Подкатегории"
        ordering = ['Tittle']


class Comment(models.Model):
    Order_User = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, verbose_name="Комментатор")
    Order_Prod = models.ForeignKey('Product', on_delete=models.CASCADE, blank=True, verbose_name="Комментируемый товар")
    Tittle = models.CharField('Название категории', blank=True, max_length=100)
    Text = models.TextField('Текст комментария', blank=True, max_length=1500)
    Date_Of_Change = models.DateField('Дата изменения', blank=True,)
    Rating = models.IntegerField('Рейтинг', blank=True,)

    def get_absolute_url(self):
        return reverse('comment', kwargs={'comment_id': self.pk})

    def __str__(self):
        return self.Tittle

    class Meta:
        verbose_name = "Комментарии"
        verbose_name_plural = "Комментарии"
        ordering = ['Tittle','Order_User','Order_Prod','Date_Of_Change','Rating']


class Profile(models.Model):
    Prof_User = models.OneToOneField(User,on_delete=models.CASCADE, blank=True, verbose_name="Пользователь")
    Patronymic = models.CharField('Отчество', blank=True, max_length=150,null=True)
    Photo = models.ImageField('Аватар', blank=True, upload_to="avatar/%Y/%m/%d/",null=True)

    #@receiver(post_save, sender=User)
    #def create_user_profile(sender, instance, created, **kwargs):
    #    if created:
    #        Profile.objects.create(user=instance)

    #@receiver(post_save, sender=User)
    #def save_user_profile(sender, instance, **kwargs):
    #    instance.profile.save()

    def get_absolute_url(self):
        return reverse('profile', kwargs={'profile_id': self.pk})

    def __str__(self):
        return self.Prof_User

    class Meta:
        verbose_name = "Доп информация о пользователе"
        verbose_name_plural = "Доп информация о пользователе"
        ordering = ['Prof_User']