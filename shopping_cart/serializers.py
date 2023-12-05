from django.db.models import fields
from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('name','date','img_url','price','initial_stock','actual_stock','description','primary_color','secondary_color','brand','size')



