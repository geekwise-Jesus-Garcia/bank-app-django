from django.contrib import admin
from .models import Bank,Account,Customer,Product

# Register your models here.
admin.site.register(Bank)
admin.site.register(Account)
admin.site.register(Customer)
admin.site.register(Product)