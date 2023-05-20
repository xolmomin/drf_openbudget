from rest_framework.fields import CharField
from rest_framework.serializers import ModelSerializer

from apps.models import New, UseFulInfo


class NewListModelSerializer(ModelSerializer):
    class Meta:
        model = New
        fields = ('id', 'title', 'view_count', 'created_at')


class UseFulInfoListModelSerializer(ModelSerializer):
    class Meta:
        model = UseFulInfo
        fields = ('id', 'image', 'number_download', 'title', 'file')


class NewDetailModelSerializer(ModelSerializer):
    class Meta:
        model = New
        fields = ('id', 'title', 'view_count', 'description', 'created_at')
