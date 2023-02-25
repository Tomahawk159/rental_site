from django.db import models


class Category(models.Model):
    name = models.CharField('Наименование', max_length=100)
    picture = models.ImageField(
        'Фото', upload_to='category_image', height_field=None, width_field=None, max_length=None)

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField('Наименование', max_length=100)
    picture = models.ImageField(
        'Фото', upload_to='subcategory_image', height_field=None, width_field=None, max_length=None)

    class Meta:
        verbose_name = 'подкатегория'
        verbose_name_plural = 'подкатегории'

    def __str__(self):
        return f'{self.name} | {self.category}'


class Tool(models.Model):
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    name = models.CharField('Наименование', max_length=150)
    description = models.TextField('Описание')
    price = models.DecimalField(default=0, max_digits=8, decimal_places=0)
    picture = models.ImageField(
        'Фото', upload_to='tool_image', height_field=None, width_field=None, max_length=None)
    availability = models.BooleanField('Наличие', default=True)

    class Meta:
        verbose_name = 'инструмент'
        verbose_name_plural = 'инструменты'

    def __str__(self):
        return f'{self.name} | {self.subcategory}'
