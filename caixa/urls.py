from django.urls import path
from .views import controleCaixa, resumoFinanceiro, home

urlpatterns = [
    path('', home),
    path('controle-caixa/', controleCaixa),
    path('resumo-financeiro/', resumoFinanceiro),
]