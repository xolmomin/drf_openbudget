from rest_framework.fields import CharField
from rest_framework.serializers import ModelSerializer

from apps.models import New


class NewListModelSerializer(ModelSerializer):
    class Meta:
        model = New
        fields = ('id', 'title', 'view_count', 'created_at')


class NewDetailModelSerializer(ModelSerializer):
    class Meta:
        model = New
        fields = ('id', 'title', 'view_count', 'description', 'created_at')
