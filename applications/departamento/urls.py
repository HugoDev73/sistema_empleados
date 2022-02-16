from django.contrib import admin
from django.urls import path

from . import views

app_name = "departamento_app"

urlpatterns = [
    path('departamentos/', views.DepartamentoListView.as_view(), name='departamentos'),
    path('new-departamento/', views.NewDepartamentoView.as_view(), name='nuevo_departamento'),
]
