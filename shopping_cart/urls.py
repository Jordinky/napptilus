from django.urls import path
from . import views
 
urlpatterns = [
    path('create/', views.add_products, name='add-items'),
    path('all/', views.view_products, name='view_products'),
    path('update/<int:pk>/', views.update_products, name='update-items'),
    path('product/<int:pk>/delete/', views.delete_products, name='delete-items'),
    path('cart/', views.view_cart, name='view_cart'),
    path('add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove/<int:pk>/', views.remove_from_cart, name='remove_from_cart'),
]
