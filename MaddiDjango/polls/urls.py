from django.urls import path

from . import views

urlpatterns = [
    path('kenn/', views.kenn),
    path('language/', views.language),
    path('system/', views.system),
    path('IDE/', views.IDE),
    path('', views.default)
]