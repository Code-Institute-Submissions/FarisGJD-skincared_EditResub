from django.urls import path
from . import views

urlpatterns = [
    path('brands/', views.all_brands, name='brands'),
    path('<slug:slug>/', views.full_brands, name='full_brands'),
]
