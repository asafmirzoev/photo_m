import uuid

from django.db import models


class Image(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    image = models.ImageField('Изображение', upload_to='%Y/%m/%d/')
    location = models.CharField('Локация', max_length=255, null=True, blank=True)
    description = models.CharField('Описание', max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'


class Person(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField('Имя', max_length=255)
    image = models.ForeignKey(Image, verbose_name='Изображение', on_delete=models.CASCADE, related_name='persons')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Человек'
        verbose_name_plural = 'Люди'

