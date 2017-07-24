from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.core.urlresolvers import reverse

class Order(models.Model):

    QUANTITY_CHOICES = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        ('9', '9'),
        ('10', '10'),
    )

    ORDER_CHOICES = (
        ('Amfit Coffee', 'Amfit Coffee'),
        ('Algi Cleans', 'Algi Cleans'),
    )

    date = models.DateField(("Date"), default=datetime.now())
    shipment_provider = models.CharField(max_length=250)
    name_of_recipient = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    barangay = models.CharField(max_length=250)
    city = models.CharField(max_length=250)
    province = models.CharField(max_length=250)
    phone = models.CharField(max_length=13)
    quantity = models.CharField(max_length=6, choices=QUANTITY_CHOICES)
    order = models.CharField(max_length=250, choices=ORDER_CHOICES)
    special_instructions = models.CharField(max_length=250, default='')

    def get_absolute_url(self):
        return reverse('ordering:dropship_add', kwargs={'pk': self.pk })

    def __str__(self):
        return (
        self.date
        + ' - ' + self.shipment_provider
        + ' - ' + self.name_of_recipient
        + ' - ' + self.address
        + ' - ' + self.barangay
        + ' - ' + self.city
        + ' - ' + self.province
        + ' - ' + self.phone
        + ' - ' + self.quantity
        + ' - ' + self.order
        )

class OrderHistory(models.Model):
    user = models.ForeignKey(User)
    order = models.ForeignKey(Order)
    purchase_date = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('ordering:ordering_history', kwargs={'pk': self.pk })

    def __str__(self):
        return
        (
        self.user
        + ' - ' + self.order
        + ' - ' + self.purchase_date
        )

class Inventory(models.Model):
    date = models.DateField(("Date"), default=datetime.now())
    product_logo = models.ImageField(upload_to='product_image', blank=True)
    product_name = models.CharField(max_length=250)
    stock_in = models.CharField(max_length=250, default='')
    stock_out = models.CharField(max_length=250, default='')
    balance = models.CharField(max_length=250, default='')
    particulars = models.CharField(max_length=250)

    def get_absolute_url(self):
        return reverse('ordering:inventory_create', kwargs={'pk': self.pk })

    def __str__(self):
        return self.product_logo.name + ' - ' + self.product_name + ' - ' + ' - ' + self.stock_in + ' - ' + self.stock_out + ' - ' + self.balance + ' - ' + self.particulars

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    last_name = models.CharField(max_length=100, default='')
    first_name = models.CharField(max_length=100, default='')
    middle_name = models.CharField(max_length=100, default='')
    address = models.CharField(max_length=250, default='')
    barangay = models.CharField(max_length=100, default='')
    city = models.CharField(max_length=250, default='')
    province = models.CharField(max_length=100, default='')
    phone_number = models.IntegerField(default=0)

def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)
