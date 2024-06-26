from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


from rest_framework.routers import DefaultRouter
from . views import UserViewSet

router = DefaultRouter()
router.register('users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('account/', include('accounts.urls')),
    path('category/', include('categories.urls')),
    path('product/', include('products.urls')),
    path('order/', include('order.urls')),
    path('card/', include('card.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
