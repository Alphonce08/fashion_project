from django.contrib import admin
from .models import Fashion,Product

# class FashionAdmin(admin.ModelAdmini):
#     pass


admin.site.register(Fashion)
admin.site.register(Product)
