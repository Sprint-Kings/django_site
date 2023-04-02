from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.base, name='base'),
    path('shop/', views.shop, name='shop'),
]