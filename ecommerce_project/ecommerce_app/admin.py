from django.contrib import admin
from .models import Catagory,Product

# Register your models here.
class Catagory_admin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Catagory,Catagory_admin)

class Product_admin(admin.ModelAdmin):
    list_display = ('name','price','stock','availability','created','updated')
    list_editable = ('price','stock','availability')
    prepopulated_fields = {'slug': ('name',)}
    list_per_page = 20

admin.site.register(Product,Product_admin)