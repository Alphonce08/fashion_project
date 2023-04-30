from django.db import models

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
    name= models.CharField(max_length=30, blank=False, null=False)
    price = models.FloatField(blank=False, null=False)
    image =  models.ImageField(upload_to="images", blank=False, null=False)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,blank=True, null=True)
    description = models.TextField(max_length=220, blank=True, default=None)
    publish = models.DateField(auto_now=False, auto_now_add=True)
    #avatar = models.ImageField(upload_to='avatars', default=Category)
    

    def __str__(self):
        return str(self.name)



