from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=75)
    image = models.ImageField()
    star = models.ImageField()
    rating = models.IntegerField()
    price = models.FloatField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

