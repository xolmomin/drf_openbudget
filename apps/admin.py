from django.contrib import admin

from apps.models import UseFulInfo


@admin.register(UseFulInfo)
class UseFulInfoAdmin(admin.ModelAdmin):
    pass
