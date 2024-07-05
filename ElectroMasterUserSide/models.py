from django.db import models

# Create your models here.

class ContactDB(models.Model):
    First_Name = models.CharField(max_length=100,null=True,blank=True)
    Last_Name = models.CharField(max_length=100,null=True,blank=True)
    Email = models.EmailField(max_length=100,null=True,blank=True)
    Address = models.CharField(max_length=100,null=True,blank=True)
    City = models.CharField(max_length=100,null=True,blank=True)
    Country = models.CharField(max_length=100,null=True,blank=True)
    Pin_Code = models.IntegerField(null=True,blank=True)
    Mobile_Number = models.IntegerField(null=True,blank=True)


class LoginDB(models.Model):
    User_Name = models.CharField(max_length=100,null=True,blank=True)
    Pass_Word = models.CharField(max_length=100,null=True,blank=True)
    Email = models.EmailField(max_length=100,null=True,blank=True)
    Address = models.EmailField(max_length=100,null=True,blank=True)


class CartDB(models.Model):
    USer_NAme = models.CharField(max_length=100,null=True,blank=True)
    PRoduct_NAme = models.CharField(max_length=100,null=True,blank=True)
    DEscription = models.CharField(max_length=100,null=True,blank=True)
    QUantity = models.IntegerField(null=True,blank=True)
    TOtal_PRice = models.IntegerField(null=True,blank=True)