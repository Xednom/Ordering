from django.contrib import admin
from . models import Order, Inventory, UserProfile


admin.site.register(Order)
admin.site.register(Inventory)
admin.site.register(UserProfile)
