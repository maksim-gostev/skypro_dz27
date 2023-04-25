from django.db import models

class Categories(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Ads(models.Model):
    name = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    price = models.FloatField()
    description = models.TextField()
    address = models.CharField(max_length=200)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'