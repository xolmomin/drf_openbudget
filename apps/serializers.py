from rest_framework.fields import CharField
from rest_framework.serializers import ModelSerializer

from apps.models import New


class NewModelSerializer(ModelSerializer):
    class Meta:
        model = New
        fields = ('id', 'title', 'image', 'description', 'created_at')
