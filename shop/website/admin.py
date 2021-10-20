from django.contrib import admin
from .models import items,Category,Cart
# Register your models here.
admin.site.register(items)
admin.site.register(Category)
admin.site.register(Cart)