
from rest_framework import serializers
from . import models



# Brand
class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Brand
        fields = "__all__"


# Category
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = "__all__"
        

# Product
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Product
        fields = "__all__"
