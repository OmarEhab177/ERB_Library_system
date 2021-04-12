from django.db import models
from django.db.models.enums import Choices

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=500, null=True, blank=True)

    # def __str__(self):
    #     return self.name

    def __str__(self):
        if self.name==None:
            return "ERROR-CUSTOMER NAME IS NULL"
        return self.name


class Book(models.Model):
    STATUS_CHOICES = [
        ('available', 'available'),
        ('rental', 'rental'),
        ('sold', 'sold'),
    ]

    title = models.CharField(max_length=250)
    author = models.CharField(max_length=250)
    photo_book = models.ImageField(upload_to='photos', null=True, blank=True)
    photo_author = models.ImageField(upload_to='photos', null=True, blank=True)
    pages = models.IntegerField(null=True, blank=True)
    price = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    rental_price_day = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    rental_period = models.IntegerField(null=True, blank=True)
    total_rental = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    active = models.BooleanField(default=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, null=True, blank=True)
    category = models.ForeignKey(Category,null=True, default='1' , on_delete=models.SET_DEFAULT)


    def __str__(self):
        display_name = self.title + " by " + self.author
        return display_name

    