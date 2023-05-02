# Generated by Django 4.1.7 on 2023-05-02 18:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0003_product_cat_alter_product_subcat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='Order_Prod',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.product', verbose_name='Заказанный товар'),
        ),
        migrations.AlterField(
            model_name='order',
            name='Order_User',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Заказчик'),
        ),
        migrations.AlterField(
            model_name='order',
            name='Quantity',
            field=models.IntegerField(blank=True, null=True, verbose_name='Количество'),
        ),
        migrations.AlterField(
            model_name='order',
            name='Status',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Статус'),
        ),
    ]
