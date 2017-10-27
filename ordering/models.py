from django.db import models
from datetime import datetime

from django.contrib.auth.models import User


class Product(models.Model):
    product_name = models.CharField(max_length=250)
    date_created = models.DateTimeField()

    def __str__(self):
        return self.product_name


class Inventory(models.Model):
    date = models.DateField(("Date"), default=datetime.now)
    product = models.ForeignKey(Product)
    product_logo = models.ImageField(upload_to='product_image', blank=True)
    stock_in = models.IntegerField()
    stock_out = models.IntegerField()
    balance = models.IntegerField()
    particulars = models.CharField(max_length=250)

    def __str__(self):
        template = '{0.product} {0.product_logo} {0.stock_in} {0.stock_out} {0.balance} {0.particulars}'
        return template.format(self)

    def total_balance(self):
        return self.balance - self.stock_out

    def image_tag(self):
        return u'<img src="%s" />' % self.product_logo.url_125x125
    image_tag.short_description = 'Image'
    image_tag.allow_tags = True


class Order(models.Model):

    SHIPMENT_CHOICES = (
        ('LBC', 'LBC'),
        ('GO', 'GO'),
        ('JRS Express', 'JRS Express'),
        ('Zen', 'Zen'),
        ('Philpost', 'Philpost'),
        ('EMS', 'EMS'),
        ('Fedex', 'Fedex'),
        ('DHL', 'DHL'),
    )

    date = models.DateField(("Date"), default=datetime.now)
    shipment_provider = models.CharField(max_length=100, choices=SHIPMENT_CHOICES)
    last_name = models.CharField(max_length=250,)
    first_name = models.CharField(max_length=250)
    middle_name = models.CharField(max_length=250)
    address = models.TextField(max_length=250)
    barangay = models.CharField(max_length=250)
    city_and_municipality = models.CharField(max_length=250)
    zip_code = models.IntegerField(default=0)
    province = models.CharField(max_length=250)
    phone = models.CharField(max_length=13)
    quantity = models.IntegerField(default=0)
    order = models.ForeignKey(Product)
    special_instructions = models.CharField(max_length=250, default='')

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
        )


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


class OrderHistory(models.Model):
    user = models.ForeignKey(User)
    shipment_provider = models.CharField(max_length=100)
    last_name = models.CharField(max_length=250, )
    first_name = models.CharField(max_length=250)
    middle_name = models.CharField(max_length=250)
    address = models.TextField(max_length=250)
    barangay = models.CharField(max_length=250)
    city_and_municipality = models.CharField(max_length=250)
    zip_code = models.IntegerField(default=0)
    province = models.CharField(max_length=250)
    phone = models.CharField(max_length=13)
    quantity = models.IntegerField(default=0)
    order = models.ForeignKey(Product)
    special_instructions = models.CharField(max_length=250, default='')
    purchase_date = models.DateTimeField(auto_now_add=True)
