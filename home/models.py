from django.db import models

class Fashion(models.Model):

    phonenumber = models.IntegerField(blank=True, null=True, default=3)
    delivery= models.CharField(max_length=30, blank=True, null=True)
    category = models.CharField(max_length=30, blank=True, null=True)


def __str__(self):
    return self.id


class Product(models.Model):
    name= models.CharField(max_length=30, blank=False, null=False)
    price = models.FloatField(blank=False, null=False)
    image =  models.ImageField(upload_to="images", blank=False, null=False)


def __str__(self):
    return str(self.name)



