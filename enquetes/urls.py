from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('<int:pergunta_id>/', views.detalhes, name='detalhes'),

    path('<int:pergunta_id>/resultado/', views.resultados, name='resultado'),

    path('<int:pergunta_id>/votacao/', views.votacao, name='votacao'),

    path('teste/', views.teste, name='Teste'),

]