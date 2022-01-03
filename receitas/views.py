from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import Receitas


# Create your views here.
def index(request):
    receitas = Receitas.objects.all()
    dados = {
        'receitas': receitas
    }

    return render(request, template_name='index.html', context=dados)


def receita(request,receita_id):
    receita = get_object_or_404(Receitas, pk=receita_id)

    receita_get = {
        'receita': receita
    }

    return render(request, template_name='receita.html', context=receita_get)
