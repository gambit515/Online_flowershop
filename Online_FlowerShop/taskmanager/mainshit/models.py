from django.db import models

# Create your models here.
class Flowers(models.Model):
    idflower = models.IntegerField('Id Товара')
    title = models.CharField('Название', max_length=50)
    price = models.IntegerField('Цена Товара')
    notes = models.TextField('Описание')
    picture = models.ImageField('Фото',upload_to='images/')
    def __str__(self):
        return self.title