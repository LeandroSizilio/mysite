from django.urls import path
from . import views

app_name = 'enquetes'
urlpatterns = [
    # URL "/enquetes/" --> lista geral das enqquetes
    path('', views.IndexView.as_view(), name='index'),
    # URL "/enquetes/55/" --> detalhes da enquete com "id" 55
    path(
        '<int:pk>/',
        views.DetalhesView.as_view(), name='detalhes'
    ),
    # URL "/enquetes/77/resultado/ --> resultado da enquete 77
    path(
        '<int:pk>/resultado/',
        views.ResultadoView.as_view(), name='resultado'
    ),
]