from djongo import models

# Create your models here.

class Crop(models.Model):
    title = models.CharField(max_length=100)
    vendor = models.CharField(max_length=100)
    price = models.CharField(max_length=5)
    #discount = models.CharField(max_length=4)


    def __str__(self):
        return self.title