from django.db import models


class Category(models.Model):
    name = models.CharField('Наименование', max_length=100)
    picture = models.ImageField(
        'Фото', upload_to='Images', height_field=None, width_field=None, max_length=None)

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    categories = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField('Наименование', max_length=100)
    picture = models.ImageField(
        'Фото', upload_to='Images', height_field=None, width_field=None, max_length=None)

    def __str__(self):
        return self.name


class Tool(models.Model):
    subcategories = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    name = models.CharField('Наименование', max_length=150)
    description = models.TextField('Описание')
    picture = models.ImageField(
        'Фото', upload_to='Images', height_field=None, width_field=None, max_length=None)
    availability = models.BooleanField('Наличие', default=True)

    def __str__(self):
        return self.name
