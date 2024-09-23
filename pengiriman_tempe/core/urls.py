from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='index.html'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('input_tempe/', views.input_tempe, name='input_tempe'),
    path('input_pesanan_tempe/', views.input_pesanan_tempe, name='input_pesanan_tempe'),
    path('input_pengiriman/', views.input_pengiriman, name='input_pengiriman'),
    path('input_pengiriman_produk/', views.input_pengiriman_produk, name='input_pengiriman_produk'),
]
