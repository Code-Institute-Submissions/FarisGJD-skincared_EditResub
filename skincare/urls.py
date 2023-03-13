from django.urls import path
from . import views

urlpatterns = [
    path('all_products/', views.all_products, name='all_products'),
    path('brands/', views.all_brands, name='brands'),
    path('skin_type', views.skin_type, name='skin_type'),
    path('skin_concern', views.skin_concern, name='skin_concern'),
    path('<slug:slug>', views.full_brands, name='full_brands'),
    path('<int:product_id>/', views.product_details, name='product_details'),
    path('add/', views.add_product, name='add_product'),
    path('edit/<int:product_id>/', views.edit_product, name='edit_product'),
    path('delete/<int:product_id>/', views.delete_product, name='delete_product'),
]
