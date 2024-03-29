# Generated by Django 4.1.7 on 2023-04-30 16:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_profile_patronymic_alter_profile_photo_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='Cat',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='main.category', verbose_name='Категория товара'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='SubCat',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='main.subcategory', verbose_name='Подкатегория товара'),
        ),
    ]
