from django.db import models

class Fashion(models.Model):

    phonenumber = models.IntegerField(blank=False, null=False, default=3)
    delivery= models.CharField(max_length=30, blank=False, null=False)
    category = models.CharField(max_length=30, blank=False, null=False)


def __str__(self):
    return self.id


