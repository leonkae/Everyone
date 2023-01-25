from django.contrib import admin
from .models import Item, Order, OrderItem

# Register your models here.
class ItemAdmin(admin.ModelAdmin):
    prepopulated_fields ={'slug': ('title')}
    list_display =[
        'title',
        'price',
        'discount_price'
    ]
    
    
admin.site.register(Item)
admin.site.register(Order)
admin.site.register(OrderItem)   