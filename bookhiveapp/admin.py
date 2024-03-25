from django.contrib import admin
from .models import Catagories,Brand,FilterPrice,Product,Contact,OrderItem,Order
# Register your models here.
admin.site.register(Catagories)
admin.site.register(Brand)
admin.site.register(FilterPrice)
admin.site.register(Product)
admin.site.register(Contact)
admin.site.register(Order)
admin.site.register(OrderItem)
