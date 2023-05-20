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
from django.db.models import F
from django.shortcuts import redirect
from rest_framework.decorators import action
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from apps.models import New, UseFulInfo
from apps.serializers import NewListModelSerializer, NewDetailModelSerializer, UseFulInfoListModelSerializer


class BaseAPIView(GenericAPIView):
    serializer_class = NewListModelSerializer

    def get(self, request, *args, **kwargs):
        return Response({'msg': 'hello world'})


class UseFulModelVUseFulInfo(ModelViewSet):
    queryset = UseFulInfo.objects.all()
    serializer_class = UseFulInfoListModelSerializer

    @action(methods=['GET'], detail=False)
    def counter(self, request, pk=None):
        if file_id := request.GET.get('file_id'):
            UseFulInfo.objects.filter(id=file_id).update(number_download=F('number_download') + 1)
            return Response()
        return Response('Not Found', status=404)


class NewModelViewSet(ModelViewSet):
    queryset = New.objects.all()
    serializer_class = NewListModelSerializer

    def retrieve(self, request, *args, **kwargs):
        self.get_queryset()
        instance = self.get_object()
        instance.view_count += 1
        instance.save()
        serializer = NewDetailModelSerializer(instance)
        return Response(serializer.data)

    # def get_serializer_class(self):
    #     if self.action == 'retrieve':
    #         return NewDetailModelSerializer
    #     return NewListModelSerializer

    # @action(methods=['GET'], detail=False, url_path='botirjonni-urli')
    # def report(self, request, pk=None):
    #     return Response({'status': 'OK'})
    #

# class UserListAPIView(ListAPIView, GenericViewSet):
#     queryset = New.objects.all()
#     serializer_class = NewModelSerializer
#
#     def list(self, request, *args, **kwargs):
#         '''
#         nimadir yozamiz
#         user likni olish uchun
#         :param request:
#         :param args:
#         :param kwargs:
#         :return:
#         '''
#         return super().list(request, *args, **kwargs)
#
#     @action(methods=['GET'], detail=True, url_path='product', url_name='12321')
#     def report(self, request, id=None):
#         return Response({'status': id})
