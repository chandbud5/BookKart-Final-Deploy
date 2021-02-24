from django.contrib import admin
from .models import product, book
# Register your models here.
admin.site.register(book)
admin.site.register(product)