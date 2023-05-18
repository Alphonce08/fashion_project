from django.db import models
from django.contrib.auth.models import User


class TimeStamp(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    
    class Meta:
        abstract = True
       

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
        
class Images(models.Model):
    ''' Images class to hold general images to be used anywhere in the product'''
    images = models.ImageField(upload_to="media")
    titr = models.CharField(max_length=200)
    create = models.DateField(auto_now_add=True)
    update = models.DateField(auto_now=True)

    class Meta:
        def __str__(self):
            return self(self.titr)
            
            
class Product(TimeStamp):#inherit TimeStamp class
    '''This represent an instance of a product to be sold in the market/platform'''
    
    name= models.CharField(max_length=30, blank=False, null=False)
    price = models.FloatField(blank=False, null=False)
    image =  models.ImageField(upload_to="images", blank=True, null=True)#image to be displayed for the product
    description = models.TextField(max_length=220, blank=True)
    
    sold  = models.BooleanField(default=False, blank=True, null=True)
    
    other_image = models.ForeignKey(Images,on_delete=models.CASCADE,blank=True, null=True)#other images that can be displayed along the main image
    category = models.ForeignKey(Category,on_delete=models.CASCADE,blank=True, null=True)
  

    def __str__(self):
        return str(self.name)


class Shopping(TimeStamp):#inherit TimeStamp class
    '''
    Create an instance of shopping by a buyer
    A single order can have many products and can be assosiated to aa registered user
    '''

    user =models.ForeignKey(User,on_delete=models.CASCADE,blank=True, null=True)
  
  
    def __str__(self):
        return str(self.id)    
        
class Order(TimeStamp):#inherit TimeStamp class
    '''
    Create an instance of order by a buyer
    A single order can have many order
    '''

    shopping = models.ForeignKey(Shopping,on_delete=models.CASCADE,blank=True, null=True)

    def __str__(self):
        return str(self.shopping)   
