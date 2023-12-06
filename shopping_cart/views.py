from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status 
from .models import Product,Cart,CartProduct
from .serializers import ProductSerializer, CartProductsSerializer
from django.shortcuts import get_object_or_404,redirect


@api_view(['POST'])
def add_products(request):
    product = ProductSerializer(data=request.data)
 
    #si no existe el producto se crea
    if Product.objects.filter(**request.data).exists():
        raise serializers.ValidationError('This data already exists')
 
    if product.is_valid():
        product.save()
        return Response(product.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
    

@api_view(['GET'])
def view_products(request):
    # compruebo los parametros de la URL
    if request.query_params:
        products = Product.objects.filter(**request.query_params.dict())
    else:
        products = Product.objects.order_by('date')
    # si algo falla lanzo un
    if products:
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)



@api_view(['POST'])
def update_products(request, pk):
    product = Product.objects.get(pk=pk)
    data = ProductSerializer(instance=product, data=request.data)
 
    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
@api_view(['DELETE'])
def delete_products(pk):
    products = get_object_or_404(Product, pk=pk)
    products.delete()
    return Response(status=status.HTTP_202_ACCEPTED)


def add_to_cart(request, product_id):
    product = Product.objects.filter(id=product_id)
   
    cart_product, created = CartProduct.objects.get_or_create(product)
    cart_product.quantity += 1
    cart_product.save()
    return redirect('cart:view_cart')

@api_view(['GET'])
def view_cart(request):
    
    if request.query_params:
        cart_products = cartProduct.objects.filter(**request.query_params.dict())
    else:
        products = Product.objects.order_by('id')
    if products:
        cart_products = cartProductSerializer(cart_products , many=True)
        return(cart_products.data)
    else:
        return redirect('cart:view_cart')
    
    
 

def remove_from_cart(request, product_id):
    cart_products = CartProducts.objects.get(id=product_id)
    cart_products.delete()
    return redirect('cart:view_cart')
 