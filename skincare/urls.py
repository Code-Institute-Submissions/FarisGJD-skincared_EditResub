from django.urls import path
from . import views

urlpatterns = [
    path('all_products/', views.all_products, name='all_products'),
    path('brands/', views.all_brands, name='brands'),
    path('skin_type', views.skin_type, name='skin_type'),
    path('skin_concern', views.skin_concern, name='skin_concern'),
    path('<slug:slug>/', views.full_brands, name='full_brands'),
    path('<product_id>/', views.product_details, name='product_details'),
]
