from django.urls import path
from . import views


urlpatterns = [
    path('buy/', views.BuyPageView.as_view(), name='buy'),
    path('charge/', views.charge, name='charge'),
    path('payment-success/', views.PaymentSuccess, name='payment-success'),
    path('payment-failed/', views.PaymentFailed, name='payment-failed'),
]
