from django.urls import path
from .views import controleCaixa, resumoFinanceiro

urlpatterns = [
    path('controle-caixa/', controleCaixa),
    path('resumo-financeiro/', resumoFinanceiro),
]