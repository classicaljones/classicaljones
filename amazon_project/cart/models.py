from django.db import models

# Create your models here.
class Product(models.Model):
    image = models.ImageField()
    name = models.CharField(max_length=70)
    star = models.ImageField()
    rating = models.IntegerField()
    price = models.FloatField()

    def __str__(self) -> str:
        return self.name