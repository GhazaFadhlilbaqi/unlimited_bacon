from django.db import models

from django.db import models

# Create your models here.
class UnlimitedBacon(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField()
    stock = models.IntegerField()
    