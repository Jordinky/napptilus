from django.urls import path
from . import views
 
urlpatterns = [
    path('create/', views.add_items, name='add-items'),
    path('all/', views.view_items, name='view_products'),
    path('update/<int:pk>/', views.update_items, name='update-items'),
    path('product/<int:pk>/delete/', views.delete_items, name='delete-items'),
    path('cart/', views.view_cart, name='view_cart'),
    path('add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove/<int:pk>/', views.remove_from_cart, name='remove_from_cart'),
]
