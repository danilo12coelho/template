from django.urls import path
from core import views
from core.views import index
urlpatterns = [
    path('', index, name='index'),
    path('base/', views.base, name='casa'),
    path('register/', views.register, name='register'),
    path('forgot-password/', views.forgot, name='tables'),
    path('404/', views.erro, name='404'),
    path('base/', views.base, name='base'),
    path('blank/', views.blanck, name='blanck'),
    path('tables/', views.tables, name='tables'),
]
