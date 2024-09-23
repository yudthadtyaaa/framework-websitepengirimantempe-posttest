"""
URL configuration for pengiriman_tempe project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('', views.home, name='index.html'),
    path('input_tempe/', views.input_tempe, name='input_tempe'),
    path('input_pesanan_tempe/', views.input_pesanan_tempe, name='input_pesanan_tempe'),
    path('input_pengiriman/', views.input_pengiriman, name='input_pengiriman'),
    path('input_pengiriman_produk/', views.input_pengiriman_produk, name='input_pengiriman_produk'),
]
