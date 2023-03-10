from django.db import models


class Review(models.Model):
    CHOICE = (
        (True, 'Да'),
        (False, 'Нет'),
    )
    name = models.CharField('Имя', max_length=100)
    review = models.TextField('Отзыв')
    is_verified = models.BooleanField(
        'Проверен', choices=CHOICE, default=False)

    class Meta:
        verbose_name = 'отзыв'
        verbose_name_plural = 'отзывы'

    def __str__(self):
        is_verified = 'Проверен' if self.is_verified else 'Не проверен'
        return f'{is_verified} | {self.name} | {self.review}'
