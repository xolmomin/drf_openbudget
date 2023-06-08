from django.contrib.auth.models import User
from rest_framework.permissions import BasePermission, DjangoModelPermissions, IsAuthenticated


class CustomDjangoModelPermissions(DjangoModelPermissions):
    perms_map = {
        'GET': ['%(app_label)s.view_%(model_name)s', '%(app_label)s.view_is_premium'],
        'OPTIONS': ['%(app_label)s.view_%(model_name)s'],
        'HEAD': ['%(app_label)s.view_%(model_name)s'],
        'POST': ['%(app_label)s.add_%(model_name)s'],
        'PUT': ['%(app_label)s.change_%(model_name)s'],
        'PATCH': ['%(app_label)s.change_%(model_name)s'],
        'DELETE': ['%(app_label)s.delete_%(model_name)s'],
    }

# dict

#
# class IsPremiumNew(CustomDjangoModelPermissions):
#
#     def has_permission(self, request, view):
#         return request.user.has_perm('apps.view_is_premium')
