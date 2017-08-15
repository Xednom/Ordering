from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.core.urlresolvers import reverse

class Order(models.Model):

    ORDER_CHOICES = (
        ('Amfit Coffee', 'Amfit Coffee'),
        ('Algi Cleans', 'Algi Cleans'),
    )

    SHIPMENT_CHOICES = (
        ('LBC','LBC'),
        ('GO','GO'),
        ('JRS Express','JRS Express'),
        ('Zen','Zen'),
        ('Philpost','Philpost'),
        ('EMS','EMS'),
        ('Fedex','Fedex'),
        ('DHL','DHL'),
    )

    date = models.DateField(("Date"), default=datetime.now())
    shipment_provider = models.CharField(max_length=100, choices=SHIPMENT_CHOICES)
    last_name = models.CharField(max_length=250)
    first_name = models.CharField(max_length=250)
    middle_name = models.CharField(max_length=250)
    address = models.TextField(max_length=250)
    barangay = models.CharField(max_length=250)
    city_and_municipality = models.CharField(max_length=250)
    zip_code = models.IntegerField(default=0)
    province = models.CharField(max_length=250)
    phone = models.CharField(max_length=13)
    quantity = models.IntegerField(default=0)
    order = models.CharField(max_length=250, choices=ORDER_CHOICES)
    special_instructions = models.CharField(max_length=250, default='')


    def get_absolute_url(self):
        return reverse('ordering:dropship_add', kwargs={'pk': self.pk })

    def __str__(self):
        return (
        self.shipment_provider
        + ' - ' + self.last_name
        + ' - ' + self.first_name
        + ' - ' + self.middle_name
        + ' - ' + self.address
        + ' - ' + self.barangay
        + ' - ' + self.city_and_municipality
        + ' - ' + self.province
        + ' - ' + self.phone
        + ' - ' + self.quantity
        + ' - ' + self.order
        + ' - ' + self.special_instructions
        )

    class meta:
        ordering = ('order')

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    address = models.CharField(max_length=250, default='')
    barangay = models.CharField(max_length=100, default='')
    city = models.CharField(max_length=250, default='')
    province = models.CharField(max_length=100, default='')
    phone = models.IntegerField(default=0)
    image = models.ImageField(upload_to='profile_image', blank=True)

    def __str__(self):
        return self.user.username + ' - ' + self.address + ' - ' + self.barangay + ' - ' + self.city + ' - ' + self.province

def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)

class OrderHistory(models.Model):
    user = models.ForeignKey(UserProfile)
    order = models.ManyToManyField(Order)
    purchase_date = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('ordering:ordering_history', kwargs={'pk': self.pk })

    def __str__(self):
        return
        (
        self.user
        + ' - ' + self.order
        )

    class meta:
        ordering = ('user')

class Inventory(models.Model):
    date = models.DateField(("Date"), default=datetime.now())
    product_logo = models.ImageField(upload_to='product_image', blank=True)
    product_name = models.CharField(max_length=250)
    stock_in = models.IntegerField(max_length=6)
    stock_out = models.IntegerField(max_length=6)
    balance = models.IntegerField(max_length=6)
    particulars = models.CharField(max_length=250)

    def get_absolute_url(self):
        return reverse('ordering:inventory_create', kwargs={'pk': self.pk })

    def __str__(self):
        return self.product_logo.name + ' - ' + self.product_name + ' - ' + ' - ' + self.stock_in + ' - ' + self.stock_out + ' - ' + self.balance + ' - ' + self.particulars

    def total_balance(self):
        return self.balance - self.stock_out

class Publication(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):              # __unicode__ on Python 2
        return self.title

    class Meta:
        ordering = ('title',)

class Article(models.Model):
    headline = models.CharField(max_length=100)
    publications = models.ManyToManyField(Publication)

    def __str__(self):              # __unicode__ on Python 2
        return self.headline

    class Meta:
        ordering = ('headline',)
