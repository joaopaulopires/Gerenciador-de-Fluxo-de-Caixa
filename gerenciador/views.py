from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


'''from .models import ControleCaixa

def login(request):
    return HttpResponse('Área de Login')
def resumoFinanceiro(request):
    return render(request, 'resumo_financeiro.html')'''

