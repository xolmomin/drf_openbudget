from django.contrib import admin
from parler.admin import TranslatableAdmin

from apps.models import Category, Product, UseFulInfo


@admin.register(UseFulInfo)
class UseFulInfoAdmin(admin.ModelAdmin):
    pass


@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):

    def get_queryset(self, request):
        query_set = super().get_queryset(request)
        if request.user.is_superuser:
            return query_set
        return query_set.filter(owner=request.user)
    #
    # def get_queryset(self, request):
    #     query_set = Product.objects.all()
    #     if request.user.is_superuser:
    #         return query_set
    #     return query_set.filter(owner=request.user)
    #
    # def get_queryset(self, request):
    #     query_set = super().get_queryset(request)
    #     if request.user.is_superuser:
    #         return query_set
    #     return request.user.product_set.all()
    #


@admin.register(Category)
class CategoryModelAdmin(admin.ModelAdmin):
    pass
