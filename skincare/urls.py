from django.urls import path
from . import views

urlpatterns = [
    path('brands/', views.all_brands, name='brands'),
    path('<slug:slug>/', views.full_brands, name='full_brands'),
    path('skin_type', views.skin_type, name='skin_type'),
    path('skin_concern', views.skin_concern, name='skin_concern'),
]
