from django.urls import path, include
from rest_framework.routers import DefaultRouter

from SiteSpace import views


router = DefaultRouter()
router.register('variants', views.VariantViewSet)
router.register('categories', views.CategoryViewSet)
router.register('products', views.ProductViewSet)

app_name = 'SiteSpace'

urlpatterns = [
    path('', include(router.urls))
]
