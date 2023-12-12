from django.urls import include, path
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('brand' ,views.BrandView ,basename='brand')
router.register('category' ,views.CategoryView ,basename='category')
router.register('product' ,views.ProductView ,basename='product')

urlpatterns = [
    path('' ,include(router.urls))
]