from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views
router = DefaultRouter() 

router.register('list', views.ProductModelAPIView)
router.register('review', views.ReviewAPIView, basename='review')


urlpatterns = [
    path('', include(router.urls)),
    path('detail/<int:pk>/', views.ProductDetailAPIView.as_view(), name='project-detail'),
]