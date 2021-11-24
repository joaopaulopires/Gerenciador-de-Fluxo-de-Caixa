'''from django.shortcuts import render
from django.http import HttpResponse'''


from django.shortcuts import render, redirect
from .models import ControleCaixa
from .form import FieldsApp
import datetime as dt


def calculadoraEntrada():
    resumoEntradas = {}

    'Cálculo do dia'
    dia = ControleCaixa.objects.filter(data_fluxo=dt.datetime.now())
    totDia = 0
    for entradas in dia:
        totDia = totDia + entradas.entrada

    'Cálculo da Semana'
    semana = ControleCaixa.objects.filter(data_fluxo__gt=(dt.datetime.now() - dt.timedelta(days=7)))
    totSemana = 0
    for entradas in semana:
        totSemana = totSemana + entradas.entrada

    'Cálculo do Mês'
    mes = ControleCaixa.objects.filter(data_fluxo__gt=(dt.datetime.now() - dt.timedelta(days=30)))
    totMes = 0
    for entradas in mes:
        totMes = totMes + entradas.entrada


    resumoEntradas['entrada_dia'] = totDia
    resumoEntradas['entrada_semana'] = totSemana
    resumoEntradas['entrada_mes'] = totMes

    return resumoEntradas


def calculadoraSaida():
    resumoSaidas = {}

    'Cálculo do dia'
    dia = ControleCaixa.objects.filter(data_fluxo=dt.datetime.now())
    totDia = 0
    for saidas in dia:
        totDia = totDia + saidas.saida

    'Cálculo da Semana'
    semana = ControleCaixa.objects.filter(data_fluxo__gt=(dt.datetime.now() - dt.timedelta(days=7)))
    totSemana = 0
    for saidas in semana:
        totSemana = totSemana + saidas.saida

    'Cálculo do Mês'
    mes = ControleCaixa.objects.filter(data_fluxo__gt=(dt.datetime.now() - dt.timedelta(days=30)))
    totMes = 0
    for saidas in mes:
        totMes = totMes + saidas.saida

    resumoSaidas['saida_dia'] = totDia
    resumoSaidas['saida_semana'] = totSemana
    resumoSaidas['saida_mes'] = totMes

    return resumoSaidas


def calculadora():
    listaResumofinanc= {}

    listaSaida = calculadoraSaida()
    listaResumofinanc.update(listaSaida)
    listaEntrada = calculadoraEntrada()
    listaResumofinanc.update(listaEntrada)

    listaResumofinanc['consolidado_dia'] = listaResumofinanc['entrada_dia'] - listaResumofinanc['saida_dia']
    listaResumofinanc['consolidado_semana'] = listaResumofinanc['entrada_semana'] - listaResumofinanc['saida_semana']
    listaResumofinanc['consolidado_mes'] = listaResumofinanc['entrada_mes'] - listaResumofinanc['saida_mes']

    return listaResumofinanc


def resumoFinanceiro(request):
    lista = calculadora()
    return render(request, 'resumo_financeiro.html', {'resumoFinanc': lista})

def controleCaixa(request):
    form = FieldsApp(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('http://127.0.0.1:8000/login/controle-caixa/')
    return render(request, 'controle_caixa.html', {'form': form})

def home(request):
    return render(request, 'home.html')


''' /// '''''

















