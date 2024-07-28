from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.views import View
from django.urls import reverse
from .models import Pergunta, Alternativa

class IndexView(View):
    def get(self, request, *args, **kwargs):
        enquetes = Pergunta.objects.order_by('-data_pub')[:10]
        contexto = {'pergunta_list': enquetes}
        return render(request, 'enquetes/index.html', contexto)

class DetalhesView(View):
    template = 'enquetes/pergunta_detail.html'

    def resposta(self, request, pergunta, error):
        contexto = {'pergunta': pergunta, 'error':error}
        return render(request, self.template, contexto)

    def get(self, request, *args, **kwargs):
        pergunta_id = kwargs['pk']
        pergunta = get_object_or_404(Pergunta, pk = pergunta_id)
        return self.resposta(request, pergunta, None)

    def post(self, request, *args, **kwargs):
        pergunta_id = kwargs['pk']
        pergunta = get_object_or_404(Pergunta, pk=pergunta_id)
        try:
            id_alternativa = request.POST['escolha']
            alt = pergunta.alternativa_set.get(pk=id_alternativa)
        except (KeyError, Alternativa.DoesNotExist):
            error = 'Você precisa selecionar uma alternativa.'
            return self.resposta(request, pergunta, error)
        else:
            alt.quant_votos += 1
            alt.save()
            return HttpResponseRedirect(reverse(
                'enquetes:resultado', args=(pergunta.id,)
            ))

class ResultadoView(View):
    def get(self, request, *args, **kwargs):
        pergunta_id = kwargs['pk']
        pergunta = get_object_or_404(Pergunta, pk = pergunta_id)
        contexto = {'pergunta': pergunta}
        return render(request, 'enquetes/resultado.html', contexto)


####
## Histórico de Versões
"""
--> View INDEX - Versão 1
def index(request):
    enquetes = Pergunta.objects.all()
    template = loader.get_template('enquetes/index.html')
    contexto = {'lista_enquetes': enquetes}
    return HttpResponse(template.render(contexto, request))

--> View INDEX - Versão 2
def index(request):
    enquetes = Pergunta.objects.order_by('-data_pub')[:10]
    contexto = {'lista_enquetes': enquetes}
    return render(request, 'enquetes/index.html', contexto)

--> View INDEX - Versão 3
class IndexView(generic.ListView):
    template_name = 'enquetes/index.html'
    def get_queryset(self):
        return Pergunta.objects.order_by('-data_pub')[:10]

--> View DETALHES - Versão 1
def detalhes(request, pergunta_id):
    resultado = 'DETALHES da enquete de número %s'
    return HttpResponse(resultado % pergunta_id)

--> View DETALHES - Versão 2
def detalhes(request, pergunta_id):
    pergunta = get_object_or_404(Pergunta, pk = pergunta_id)
    contexto = {'enquete': pergunta}
    return render(request, 'enquetes/detalhes.html', contexto)

--> View RESULTADO - Versão 1
class ResultadoView(generic.DetailView):
    model = Pergunta
    template_name = 'enquetes/resultado.html'


--> View VOTAÇÃO - Versão 1
def votacao(request, pergunta_id):
    pergunta = get_object_or_404(Pergunta, pk=pergunta_id)
    try:
        id_alternativa = request.POST['escolha']
        alt = pergunta.alternativa_set.get(pk=id_alternativa)
    except (KeyError, Alternativa.DoesNotExist):
        contexto = {
            'pergunta': pergunta,
            'error': 'Você precisa selecionar uma alternativa.'
        }
        return render(request, 'enquetes/pergunta_detail.html', contexto)
    else:
        alt.quant_votos += 1
        alt.save()
        return HttpResponseRedirect(reverse(
            'enquetes:resultado', args=(pergunta.id,)
        ))
"""