from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Money(models.Model):
    amount = models.DecimalField(max_digits = 10, decimal_place = 2)
    date = models.DateFile()
    category = models.CharField(max_length=255)
    description = models.TextField()
    is_income = models.BooleanField(default = False)
    user = models.ForeignKey(User, on_delete = models.CASCADE, null = False)

    def __str__(self):
        return f'{self.user.username} - {self.amount} on {self.date}'
    
class Part(models.Model):
    name = models.CharField(max_length = 255)
    category = models.CharField(max_length = 255)
    quantity = models.PositiveIntegerField()
    status = models.CharField(max_length = 50, choices = [('I', 'In stock'), ('O', 'Out of stock')])

    def __str__(self):
        return f'{self.category} - {self.name} ({self.status})'
    

