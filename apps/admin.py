from django.contrib import admin
from parler.admin import TranslatableAdmin

from apps.models import UseFulInfo, Product, Category


@admin.register(UseFulInfo)
class UseFulInfoAdmin(admin.ModelAdmin):
    pass


@admin.register(Product)
class ProductTranslatableAdmin(TranslatableAdmin):
    pass


@admin.register(Category)
class CategoryTranslatableAdmin(TranslatableAdmin):
    pass
