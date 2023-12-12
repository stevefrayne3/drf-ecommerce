
from rest_framework import viewsets, status
from rest_framework.response import Response


from . import models
from . import serializers

# Create your views here.


# BrandView
class BrandView(viewsets.ViewSet):
    """View all Brand"""

    brand = models.Brand.objects.all()

    # list all data
    def list(self ,request):
        serializer = serializers.BrandSerializer(self.brand, many=True)
        return Response(serializer.data ,status=status.HTTP_200_OK)
    

# CategoryView
class CategoryView(viewsets.ViewSet):
    """View all Category"""

    category = models.Category.objects.all()

    # list all data
    def list(self ,request):
        serializer = serializers.CategorySerializer(self.category, many=True)
        return Response(serializer.data ,status=status.HTTP_200_OK)
    

# CategoryView
class ProductView(viewsets.ViewSet):
    """View all Product"""

    product = models.Product.objects.all()

    # list all data
    def list(self ,request):
        serializer = serializers.ProductSerializer(self.product, many=True)
        return Response(serializer.data ,status=status.HTTP_200_OK)
