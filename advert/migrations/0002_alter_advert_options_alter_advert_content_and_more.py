# Generated by Django 4.0.4 on 2022-04-16 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advert', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='advert',
            options={'ordering': ['-created_at']},
        ),
        migrations.AlterField(
            model_name='advert',
            name='content',
            field=models.TextField(max_length=500, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='advert',
            name='title',
            field=models.CharField(max_length=150, verbose_name='Тема'),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=150, verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='name',
            field=models.CharField(max_length=150, verbose_name='Подкатегория'),
        ),
    ]
