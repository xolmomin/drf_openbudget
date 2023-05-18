from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.views import NewModelViewSet

# from apps.views import NewListAPIView, NewCreateAPIView, NewDestroyAPIView, NewUpdateAPIView, NewRetrieveAPIView, \
#     NewRetrieveUpdateDestroyAPIView, NewListCreateAPIView

router = DefaultRouter()
router.register('new', NewModelViewSet, 'new')

urlpatterns = [
    path('', include(router.urls)),
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
