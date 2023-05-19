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
        'sold',
        
      
    )

    list_display_links = ("id",)
    
    search_fields = ("id",)
    list_editable = (
        "price",
        "sold",
        "category",
        "name",
       
    )


admin.site.register(Product, ProductAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        
      
    )
admin.site.register(Category, CategoryAdmin)
admin.site.register(Images)
admin.site.register(Order)
admin.site.register(Shopping)
