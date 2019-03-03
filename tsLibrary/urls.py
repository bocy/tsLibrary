"""tsLibrary URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from tsLib import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.index),
    path("index/", views.index),
    path("login/", views.login),
    path("logout/", views.logout),
    path("borrowed_list/", views.borrowed_list),
    path("borrow_history/", views.borrow_history),
    path("book_list/", views.book_list),
    path(r'borrow_book/<int:book_id>/', views.borrow_book),
    path(r'return_book/<int:borrow_id>/', views.return_book),

]
