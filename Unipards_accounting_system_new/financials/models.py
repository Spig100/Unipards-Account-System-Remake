from django.db import models

# Create your models here.

class Money(models.Model):
    amount = models.DecimalField(max_digits = 10, decimal_place = 2)
    date = models.DateFile()
    category = models.CharField(max_length=255)
    description = models.TextField()
    
