from django.contrib import admin
from django.utils import timezone

from .models import *


# Register your models here.

class CategoryProduct(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


class ProducthasimageTabularInline(admin.TabularInline):
    model = ProductHasImage


class ProductAdmin(admin.ModelAdmin):
    inlines = [ProducthasimageTabularInline]
    list_display = ('title', 'category', 'brand', 'pub_date')
    list_filter = ('category',)
    search_fields = ('title', 'category', 'pub_date',)
    prepopulated_fields = {'slug': ('title',)}
    list_per_page = 20
    action = ('set_product_to_published',)
    fields = (('title', 'slug'), 'category', 'description', 'brand', 'price')

    def days_since_creation(self, product):
        diff = timezone.now() - product.pub_date
        return diff.days

    days_since_creation.short_description = 'active days'

    def get_ordering(self, request):
        if request.user.is_superuser or request.user.is_staff:
            return 'title', '-pub_date'
        return 'title'

    def set_product_to_published(self, request, queryset):
        count = queryset.update(is_draft=False)
        self.message_user(request, "{} The selected message".format(count))

    set_product_to_published.short_description = 'action name'


class GalleryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Category, CategoryProduct)
admin.site.register(Product, ProductAdmin)
admin.site.register(Gallery, GalleryAdmin)
admin.site.register(SiteReview)
admin.site.register(BrandLogo)
