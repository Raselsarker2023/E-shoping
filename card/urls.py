from django.urls import path, include
from . import views


from rest_framework.routers import DefaultRouter
router = DefaultRouter() 


router.register('list', views.CartViewset)
router.register('add', views.CartItemViewset)
router.register('wish', views.WishlistAPIView)


urlpatterns = [
    path('', include(router.urls)),
]