from django.contrib import admin
from . models import Order, Inventory, Product, UserProfile


admin.site.register(Order)
admin.site.register(Inventory)
admin.site.register(Product)
admin.site.register(UserProfile)
