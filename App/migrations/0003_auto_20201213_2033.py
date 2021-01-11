# Generated by Django 3.1.4 on 2020-12-13 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0002_material'),
    ]

    operations = [
        migrations.AddField(
            model_name='material',
            name='category',
            field=models.ManyToManyField(to='App.Category', verbose_name='دسته بندی '),
        ),
        migrations.AddField(
            model_name='material',
            name='product',
            field=models.ManyToManyField(to='App.Product', verbose_name='محصول '),
        ),
        migrations.AddField(
            model_name='material',
            name='supplier',
            field=models.ManyToManyField(to='App.Supplier', verbose_name='تامین کنند '),
        ),
    ]
