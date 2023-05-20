from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.views import NewModelViewSet, BaseAPIView, UseFulModelVUseFulInfo, ResponsePersonModelViewSet, \
    ProductListCreateAPIView

# from apps.views import NewListAPIView, NewCreateAPIView, NewDestroyAPIView, NewUpdateAPIView, NewRetrieveAPIView, \
#     NewRetrieveUpdateDestroyAPIView, NewListCreateAPIView

router = DefaultRouter()
router.register('use', UseFulModelVUseFulInfo, 'use')
router.register('new', NewModelViewSet, 'new')

router.register('response-person', ResponsePersonModelViewSet, 'response-person')
# router.register('district', DistrictModelViewSet, 'district')


urlpatterns = [
    path('', include(router.urls)),
    path('base', BaseAPIView.as_view()),
    path('product', ProductListCreateAPIView.as_view()),

    # path('news', NewListCreateAPIView.as_view()),
    # path('UserListAPIView', NewListCreateAPIView.as_view()),

    # path('news', NewListAPIView.as_view()),
    # path('news', NewCreateAPIView.as_view()),
    # path('news/<int:pk>', NewDestroyAPIView.as_view()),

    # path('news/<int:pk>', NewRetrieveUpdateDestroyAPIView.as_view()),

    # path('news/<int:pk>', NewUpdateAPIView.as_view()),
    # path('news/<int:pk>', NewRetrieveAPIView.as_view()),
]

'''
news   - GET  - list
news   - POST - create
news/nimadir   - POST - create

news/1 - GET  - detail
news/1 - DELETE  - delete
news/1 - PATCH/PUT  - update

user/
user/product

'''
