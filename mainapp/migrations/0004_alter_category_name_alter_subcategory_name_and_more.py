# Generated by Django 4.1.5 on 2023-02-01 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_tool'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Наименование'),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Наименование'),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='picture',
            field=models.ImageField(upload_to='Images', verbose_name='Фото'),
        ),
        migrations.AlterField(
            model_name='tool',
            name='name',
            field=models.CharField(max_length=150, verbose_name='Наименование'),
        ),
        migrations.AlterField(
            model_name='tool',
            name='picture',
            field=models.ImageField(upload_to='Images', verbose_name='Фото'),
        ),
    ]