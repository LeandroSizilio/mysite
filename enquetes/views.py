from django.shortcuts import render
from django.http import HttpResponse
from .models import Pergunta

def index(request):
    return HttpResponse(
        'DSWeb 2024.1 - 3 Período <br/> Matrícula: 20231014040044 <br> Nome: Leandro Ramos Sizilio'
        )

def detalhes(request, pergunta_id):
    resultado = "Detalhes da enquete de número %s."
    return HttpResponse(resultado % pergunta_id)

def resultados(request, pergunta_id):
    resultado = "Resultados do enquete de número %s."
    return HttpResponse(resultado % pergunta_id)

def votacao(request, pergunta_id):
    resultado = "Votação da enquete de número %s."
    return HttpResponse(resultado % pergunta_id)

def teste(request):
    lista = Pergunta.Objects.all()
    resultado = '<br>'.join(p.texto for p in lista)
    return HttpResponse(resultado)