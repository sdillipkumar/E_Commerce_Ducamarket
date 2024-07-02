from django.contrib import admin
from webapp.models import *
# Register your models here.
class Product_images(admin.TabularInline):
    model = Product_Image

class Addition_Information(admin.TabularInline):
    model = Additional_Information

class Product_Admin(admin.ModelAdmin):
    inlines = (Product_images,Addition_Information)
    list_display = ['product_name','price','Categories','section']
    list_editable = ['Categories','section']

admin.site.register(Section)
admin.site.register(Product,Product_Admin)
admin.site.register(Product_Image)
admin.site.register(Additional_Information)

admin.site.register(slider)
admin.site.register(Banner_area)
admin.site.register(Main_Category)
admin.site.register(Category)
admin.site.register(Subcategory)


