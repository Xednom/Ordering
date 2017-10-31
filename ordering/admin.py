from django.contrib import admin
from . models import Order, Product, Inventory, UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'address', 'barangay', 'city', 'province', 'phone')


class OrderProfile(admin.ModelAdmin):
    list_display = ('shipment_provider', 'last_name', 'first_name', 'middle_name', 'address', 'barangay', 'city_and_municipality', 'province', 'phone', 'quantity', 'order', 'status', 'special_instructions')


class InventoryProfile(admin.ModelAdmin):
    list_display = ('product', 'stock_in', 'stock_out', 'balance', 'particulars')


fields = ('image_tag',)
readonly_fields = ('image_tag',)

admin.site.site_header = "TCL BackOffice"
admin.site.register(Order, OrderProfile)
admin.site.register(Inventory, InventoryProfile)
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Product)
