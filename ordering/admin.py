from django.contrib import admin
from . models import Order, Inventory, UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'address', 'barangay', 'city', 'province', 'phone')

    #def user_info(self, obj):
        #return obj.address

class OrderProfile(admin.ModelAdmin):
    list_display = ('shipment_provider', 'name_of_recipient', 'address', 'barangay', 'city', 'province', 'phone', 'quantity', 'order', 'special_instructions')

class InventoryProfile(admin.ModelAdmin):
    list_display = ('product_logo', 'product_name', 'stock_in', 'stock_out', 'balance', 'particulars')


admin.site.register(Order, OrderProfile)
admin.site.register(Inventory, InventoryProfile)
admin.site.register(UserProfile, UserProfileAdmin)
