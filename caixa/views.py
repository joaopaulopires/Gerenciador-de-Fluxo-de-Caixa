'''from django.shortcuts import render
from django.http import HttpResponse'''


from django.shortcuts import render
from .models import ControleCaixa
import datetime as dt

def calculadora():
    listaSaida = []

    'Cálculo do dia'
    dia = ControleCaixa.objects.filter(data_fluxo=dt.datetime.now())
    totDia = 0
    for entradas in dia:
        totDia = totDia +entradas.saida

    'Cálculo da Semana'
    semana = ControleCaixa.objects.filter(data_fluxo__gt=(dt.datetime.now() - dt.timedelta(days=7)))
    totSemana = 0
    for entradas in semana:
        totSemana = totSemana + entradas.saida

    'Cálculo do Mês'
    mes = ControleCaixa.objects.filter(data_fluxo__gt=(dt.datetime.now() - dt.timedelta(days=30)))
    totMes = 0
    for entradas in mes:
        totMes = totMes +entradas.saida

    listaSaida.append(totDia)
    listaSaida.append(totSemana)
    listaSaida.append(totMes)

    return listaSaida


def resumoFinanceiro(request):
    lista = calculadora()
    return render(request, 'resumo_financeiro.html', {'saidas': lista})


def controleCaixa(request):
    totEntrada = ControleCaixa.objects.all().order_by('data_fluxo')
    return render(request, 'controle_caixa.html', {'totEntrada': totEntrada})











'''def resumoFinanceiro(request):
    return render(request, 'resumo_financeiro.html')'''

'''soma = ()(dt.datetime.now() - dt.timedelta(days=7)
   soma = ControleCaixa.objects.data_fluxo()
   sete = ControleCaixa.objects.data_fluxo()
   for semana in sete:semana = ControleCaixa.objects.filter((dt.datetime.now() - dt.timedelta(days=7))
       totSemana = totSemana + semana
   soma''''''
   totEntrada = ControleCaixa.objects.filter(entrada__gt=0)
   semana = (dt.datetime.now() - dt.timedelta(days=7))
   mes = (dt.datetime.now() - dt.timedelta(days=30))
   ano = (dt.datetime.now() - dt.timedelta(days=356))
   print(listaSaida)
   for entradas in totEntrada:
       soma = soma + entradas.entrada
   print(listaSaida)'''''