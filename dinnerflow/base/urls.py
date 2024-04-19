from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('scan/', views.scan, name='scan'),
    path('qrcode/', views.qr_code, name='qrcode'),
]
