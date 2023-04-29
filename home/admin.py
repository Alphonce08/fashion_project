from django.contrib import admin
from .models import Fashion,Product,Category

# class FashionAdmin(admin.ModelAdmini):
#     pass


admin.site.register(Fashion)
admin.site.register(Product)
admin.site.register(Category)