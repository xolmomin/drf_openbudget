from rest_framework.fields import CharField, ImageField, FileField
from rest_framework.serializers import ModelSerializer, ListSerializer

from apps.models import New, UseFulInfo, ResponsiblePerson, Region, District, Product


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


class DistrictModelSerializer(ModelSerializer):
    class Meta:
        model = District
        exclude = ('id', 'region')

    def to_representation(self, instance: District):
        _repr = super().to_representation(instance)
        _repr['full_name'] = instance.responsibleperson.full_name
        _repr['phone'] = instance.responsibleperson.phone
        return _repr


class DistrictResponsiblePersonModelSerializer(ModelSerializer):
    districts = DistrictModelSerializer(many=True, required=False)

    class Meta:
        model = Region
        exclude = ('id',)


class ResponsiblePersonModelSerializer(ModelSerializer):
    class Meta:
        model = ResponsiblePerson
        fields = ('id', 'full_name', 'phone', 'district')


class ProductModelSerializer(ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'
