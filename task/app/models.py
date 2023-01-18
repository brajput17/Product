from django.db import models

# Create your models here.


class Users(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField(max_length=254)
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=500)
    def __str__(self):
        return self.name

class Product(models.Model):
    name=models.CharField(max_length=50,blank=True, null=True)
    description=models.TextField()
    price=models.DecimalField(max_digits=50, decimal_places=2)

    def __str__(self):
        return self.name

