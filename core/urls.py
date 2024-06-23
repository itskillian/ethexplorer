from django.urls import path

from . import views

app_name = 'core'
urlpatterns = [
    path('', views.index, name='index'),
    path('address/<str:address>', views.address, name='address'),
    path('error/', views.error, name='error'),
]
