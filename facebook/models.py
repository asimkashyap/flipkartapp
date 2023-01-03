
from unittest.util import _MAX_LENGTH
from django.db import models
import datetime


class Registration (models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    AGE = models.IntegerField()


def __str__(self):
    return self.first_name


class Signup(models.Model):
    first_name = models.CharField(max_length=20, null=True)
    last_name = models.CharField(max_length=20, null=True)
    email = models.CharField(max_length=200, null=True, unique=True)
    password = models.CharField(max_length=200, null=True)
    mobile = models.BigIntegerField((""))
    gender = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.first_name


class Category(models.Model):
    name=models.CharField (max_length=200,null=True)
    cat_image=models.ImageField(upload_to='upload/category/')

def __str__(self):
    return self.name

class Product(models.Model):
    pro_name=models.CharField(max_length=300,null=True) 
    price=models.IntegerField()  
    desc=models.TextField(max_length=300,null=True)
    pro_image=models.ImageField( upload_to='upload/product/')
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.pro_name

class Order(models.Model):
    address =models.TextField(max_length=300,null=True)
    mobile_no =models.BigIntegerField()  
    product= models.ForeignKey(Product,on_delete =models.CASCADE) 
    customer=models.ForeignKey(Signup,on_delete =models.CASCADE)  
    quantity=models.IntegerField()  
    price= models.IntegerField() 
    date=models.DateTimeField(default=datetime.datetime.now() )
    status=models.BooleanField(default=False)
   
    def __str__(self):
        return self.customer.first_name
    


    