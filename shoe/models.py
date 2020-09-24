from django.db import models
from manufacturer.models import Manufacturer

# Create your models here.

class ShoeType(models.Model):
    style = models.CharField(max_length=140)

    def __str__(self):
        return self.style

class ShoeColor(models.Model):
    color_name = models.CharField(max_length=140)

    def __str__(self):
        return self.color_name

class Shoe(models.Model):
    size = models.IntegerField()
    brand_name = models.CharField(max_length=200)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    color = models.ForeignKey(ShoeColor, on_delete=models.CASCADE)
    material = models.CharField(max_length=200)
    shoe_type = models.ForeignKey(ShoeType, on_delete=models.CASCADE)
    fasten_type = models.CharField(max_length=200)

    def __str__(self):
        return self.brand_name