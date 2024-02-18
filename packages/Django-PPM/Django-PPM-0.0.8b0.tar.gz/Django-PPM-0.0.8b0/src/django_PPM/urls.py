from django.urls import path,include

from . import views

urlpatterns = [
    path('', views.packages, name='index'),
    path('<str:package_name>/', views.packages_details, name='index'),
]
