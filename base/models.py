from pickle import APPEND
from django.db import models

# creating a boxes for the dash board


class ProductName(models.Model):
    product_name = models.CharField(max_length=20)
    description = models.CharField(max_length=50)

    def __str__(self):
        return self.product_name


class Picture(models.Model):
    picture = models.ImageField(upload_to='pictures', default='')

    def __str__(self):
        return self.picture


class Product(models.Model):
    product_name = models.ForeignKey(ProductName, on_delete=models.CASCADE)
    quantity = models.FloatField()
    product_price = models.FloatField()
    picture = models.ForeignKey(Picture, on_delete=models.CASCADE)

    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product_name
