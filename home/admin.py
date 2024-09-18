from django.contrib import admin

from .models import *

# Register your models here.

class ProductVariantInlines(admin.TabularInline) :
    model = Variants
    extra = 2

# @admin_thumbnails.thumbnail('image')
class ImageInlines(admin.TabularInline):
    model = Images
    extra = 2

class CategoryAdmin(admin.ModelAdmin) :
    list_display = ('name' , 'sub_cat','create' , 'update')
    prepopulated_fields = {
        'slug': ('name' ,)
    }


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name' , 'create' , 'update' , 'amount' , 'available' , 'unit_price' , 'discount' , 'total_price']
    list_editable = ('amount' ,)
    inlines = [ProductVariantInlines , ImageInlines]


class CommentAdmin(admin.ModelAdmin):
    list_display = ['user' , 'create' , 'rate']




admin.site.register(Category , CategoryAdmin)
admin.site.register(Product , ProductAdmin)
admin.site.register(Variants)
admin.site.register(Size)
admin.site.register(Color)
admin.site.register(Comment , CommentAdmin)