from django.urls import path, include
from . import views

urlpatterns = [
    path('login/', views.login),
    path('register/', views.register),
    path('test/', views.TestAuth.as_view()),
    path('testno/', views.TestNoAuth.as_view()),
    path('', views.failure),
]