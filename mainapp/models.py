from django.db import models


class Categories(models.Model):
    name = models.CharField(max_length=100)


class SubCategories(models.Model):
    categories = models.ForeignKey(Categories, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)


class Tools(models.Model):
    subcatigories = models.ForeignKey(SubCategories, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    description = models.TextField('Описание')
    picture = models.ImageField(
        'Фото', upload_to=None, height_field=None, width_field=None, max_length=None)
    availability = models.BooleanField('Наличие', default=True)
