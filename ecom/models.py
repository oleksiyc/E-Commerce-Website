from __future__ import unicode_literals

from django.db import models

class Item(models.Model):
    article_id = models.CharField(max_length=200, primary_key=True)
    name = models.CharField(max_length=200)
    price = models.PositiveIntegerField()
    picture_link = models.CharField(max_length=200)
    sold = models.BooleanField()
    quantity = models.PositiveIntegerField(default=10)

class Basket(models.Model):
    total = models.DecimalField(max_digits=100, decimal_places=2, default=0.00)
    
class BasketItem(models.Model):
    basket = models.ForeignKey(Basket, null=True, blank=True)
    product = models.ForeignKey(Item)
    quantity = models.IntegerField(default=1)
    line_total = models.DecimalField(default=10.99, max_digits=1000, decimal_places=2)

class User(models.Model):
    firstname = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    username = models.CharField(max_length=16, primary_key=True)
    password = models.CharField(max_length=16)
    email = models.EmailField()
    phone = models.PositiveIntegerField()
    address = models.CharField(max_length=80)
    city = models.CharField(max_length=200)
    postcode = models.CharField(max_length=8)
    dob = models.DateField('dob')
    basket = models.OneToOneField(Basket)






