from django.db import models
from datetime import datetime
class Fashion(models.Model):

    phonenumber = models.IntegerField(blank=True, null=True, default=3)
    delivery= models.CharField(max_length=30, blank=True, null=True)
    category = models.CharField(max_length=30, blank=True, null=True)


def __str__(self):
    return self.id

class Category(models.Model):
    name= models.CharField(max_length=30, blank=False, null=False)

    class Meta:
        verbose_name_plural = "Categories"
    
    def __str__(self):
        return str(self.name)

class Product(models.Model):
    name= models.CharField(max_length=30, blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    image =  models.ImageField(upload_to="images", blank=True, null=True)
    category = models.ImageField(upload_to="images", blank=True, null=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,blank=True, null=True)
    #avatar = models.ImageField(upload_to='avatars', default=Category)
    

    def __str__(self):
        return str(self.name)



