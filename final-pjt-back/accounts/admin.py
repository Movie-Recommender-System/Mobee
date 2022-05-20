from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Item, PurchaseList

admin.site.register(User, UserAdmin)
admin.site.register(Item)
admin.site.register(PurchaseList)
# Register your models here.
