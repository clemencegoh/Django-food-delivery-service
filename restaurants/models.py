from django.db import models

# Create your models here.



class Restaurants(models.Model):
    name = models.CharField(max_length=255)


class Orders(models.Model):
    number_of_items = models.IntegerField()
    created_date = models.DateTimeField()
    restaurant = models.ForeignKey(Restaurants, on_delete=models.CASCADE)
