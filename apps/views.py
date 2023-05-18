# from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView, RetrieveAPIView, \
#     RetrieveUpdateAPIView, RetrieveUpdateDestroyAPIView, ListCreateAPIView
#
# from apps.models import New
# from apps.serializers import NewModelSerializer
#
#
# # CREATE
# class NewCreateAPIView(CreateAPIView):
#     serializer_class = NewModelSerializer
#
#
# # READ
# class NewListAPIView(ListAPIView):
#     queryset = New.objects.all()
#     serializer_class = NewModelSerializer
#
#
# # UPDATE
# class NewUpdateAPIView(UpdateAPIView):
#     queryset = New.objects.all()
#     serializer_class = NewModelSerializer
#
#
# # DELETE
# class NewDestroyAPIView(DestroyAPIView):
#     queryset = New.objects.all()
#     serializer_class = NewModelSerializer
#
#
# class NewRetrieveAPIView(RetrieveAPIView):
#     queryset = New.objects.all()
#     serializer_class = NewModelSerializer
#
#
# class NewRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
#     queryset = New.objects.all()
#     serializer_class = NewModelSerializer
#
#
# class NewListCreateAPIView(ListCreateAPIView):
#     queryset = New.objects.all()
#     serializer_class = NewModelSerializer
#
from rest_framework.decorators import action
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from apps.models import New
from apps.serializers import NewModelSerializer


class NewModelViewSet(ModelViewSet):
    queryset = New.objects.all()
    serializer_class = NewModelSerializer

    @action(methods=['GET'], detail=False, url_path='botirjonni-urli')
    def report(self, request, pk=None):
        return Response({'status': 'OK'})


class UserListAPIView(ListAPIView, GenericViewSet):
    queryset = New.objects.all()
    serializer_class = NewModelSerializer

    @action(methods=['GET'], detail=True, url_path='product', url_name='12321')
    def report(self, request, id=None):
        return Response({'status': id})
