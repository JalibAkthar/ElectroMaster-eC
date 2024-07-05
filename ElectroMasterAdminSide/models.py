from django.db import models

# Create your models here.

class CategoryDB(models.Model):
    Category_Name = models.CharField(max_length=100,null=True,blank=True)
    Description = models.CharField(max_length=100,null=True,blank=True)
    Category_Image = models.ImageField(upload_to="Images",null=True,blank=True)


class ProductDB(models.Model):
    Category_name = models.CharField(max_length=100,null=True,blank=True)
    Product_Name = models.CharField(max_length=100,null=True,blank=True)
    Descriptio_n = models.CharField(max_length=100,null=True,blank=True)
    Price = models.IntegerField(null=True,blank=True)
    Product_Image = models.ImageField(upload_to="Images2",null=True,blank=True)
