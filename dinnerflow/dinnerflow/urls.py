"""
URL configuration for dinnerflow project.

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
from django.urls import path
from django.urls import include
from accounts import views as accounts_views


urlpatterns = [
    path('', include('base.urls')),
    path('', include('payment.urls')),
    path('menu/', include('menu.urls')),
    path('admin/', admin.site.urls),
    path('register/', accounts_views.register, name="register"),
    path('profile/', accounts_views.profile, name="profile"),
    #path('login/', accounts_views.login, name="login"),
    path('logout/', accounts_views.logout, name="logout"),
    path('accounts/profile/', accounts_views.home, name="home"),
    path('pass_dinner/', accounts_views.pass_diner_to_someone, name="pass_dinner"),
    path('', include('django.contrib.auth.urls')),
    path('', include('paypal.standard.ipn.urls')),
]