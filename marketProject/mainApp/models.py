from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return f'{self.name}'


class Product(models.Model):
    name = models.CharField(max_length=40)
    price = models.FloatField()
    count_on_stock = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.category}: {self.name} - {self.price}'

    def get_absolute_url(self):
        return f'{self.pk}'


class Client(models.Model):
    name = models.CharField(max_length=40)
    order = models.ManyToManyField(Product, null=True)

    def __str__(self):
        return f'{self.name} - {self.order}'
