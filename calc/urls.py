"""locus URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path,include

from . import views

urlpatterns = [
    path('',views.home,name='home'),
     path('market.html', views.market,name='market'),
     path('home.html', views.home,name='home'),
     path('search', views.search,name='search'),
     path('technical_screener.html', views.technical_screener,name='technical_screener'),
     path('fundamental_screener.html', views.fundamental_screener,name='fundamental_screener'),
     path('fundamental_screener_search', views.fundamental_screener_search,name='fundamental_screener_search'),
    path('comparator.html', views.comparator,name='comparator'),
    path('forecast.html', views.forecast,name='forecast'),
    path('forecast_search', views.forecast_search,name='forecast_search'),
    path('forecast_applied', views.forecast_applied,name='forecast_applied'),

    
    path('comparator_comp1_search', views.comparator_comp1_search,name='comparator_comp1_search'),
    path('technical_screener_search', views.technical_screener_search,name='technical_screener_search'),

    path('table1.html', views.comparator_comp1_search,name='table1'),
    path('login.html', views.login,name='login'),
    path('login_user', views.login_user,name='login-user'),
    path('register.html',views.signup,name='register'),
    path('signup_user',views.signup_user,name='signup-user'),
    path('forecast_search', views.forecast_search,name='forecast_search'),
    path('dashboard.html', views.dashboard,name='dashboard'),
    #path('pages/tables/basic-table.html', views.table,name='table'),
    path('watchlist.html', views.watchlist,name='watchlist'),
    path('portfolio.html', views.portfolio,name='portfolio'),





]
