from django.db import models


class Hobby(models.Model):
    """Класс увлечения.
    Информация о каждом будет на главной странице
    и на тематической странице
    """

    # название
    title = models.CharField(max_length=100)
    # описание
    content = models.TextField(null=True, blank=True)

    # фото
    # Поначалу, можно обойтись лишь css, далее можно подумать о создании
    # отдельного поля модели
