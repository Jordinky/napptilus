from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status 
from .models import Product,Cart,CartItem
from .serializers import ProductSerializer, CartItemsSerializer
from django.shortcuts import get_object_or_404,redirect


@api_view(['POST'])
def add_items(request):
    item = ProductSerializer(data=request.data)
 
    # validating for already existing data
    if Product.objects.filter(**request.data).exists():
        raise serializers.ValidationError('This data already exists')
 
    if item.is_valid():
        item.save()
        return Response(item.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
    

@api_view(['GET'])
def view_items(request):
    # checking for the parameters from the URL
    if request.query_params:
        items = Product.objects.filter(**request.query_params.dict())
        print(items)
    else:
        items = Product.objects.order_by('date')
        print(items)
    # if there is something in items else raise error
    if items:
        serializer = ProductSerializer(items, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)



@api_view(['POST'])
def update_items(request, pk):
    item = Product.objects.get(pk=pk)
    data = ProductSerializer(instance=item, data=request.data)
 
    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
@api_view(['DELETE'])
def delete_items(pk):
    item = get_object_or_404(Product, pk=pk)
    item.delete()
    return Response(status=status.HTTP_202_ACCEPTED)


def add_to_cart(request, product_id):
    product = Product.objects.filter(id=product_id)
   
    cart_item, created = CartItem.objects.get_or_create(product)
    cart_item.quantity += 1
    cart_item.save()
    return redirect('cart:view_cart')

@api_view(['GET'])
def view_cart(request):
    
    if request.query_params:
        cart_items = CartItem.objects.filter(**request.query_params.dict())
    else:
        items = Product.objects.order_by('id')
    if items:
        cart_products = CartItemsSerializer(cart_items , many=True)
        return(cart_products.data)
    else:
        return redirect('cart:view_cart')
    
    
 

def remove_from_cart(request, item_id):
    cart_item = CartItem.objects.get(id=item_id)
    cart_item.delete()
    return redirect('cart:view_cart')
 