from django.db import models


# Create your models here.

# Brand
class Brand(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name


# Category
class Category(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
   
    def __str__(self):
        return self.name
    

# Product
class Product(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, null=True,
                              related_name="Brand")
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, 
                              blank=True ,related_name="Category" 
    )

    name = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    avail_offline = models.BooleanField(default=False)

    def __str__(self):
        return self.name