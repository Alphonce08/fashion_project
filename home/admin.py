from django.contrib import admin
from .models import *#Fashion,Product,Category,Images,Order

# class FashionAdmin(admin.ModelAdmini):
#     pass


admin.site.register(Fashion)
#admin.site.register(Product)

class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "price",
        "image",
        "category",
      
    )

    list_display_links = ("id",)


admin.site.register(Product, ProductAdmin)


admin.site.register(Category)
admin.site.register(Images)
admin.site.register(Order)
admin.site.register(Shopping)
