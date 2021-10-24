from django.db import models

class ControleCaixa(models.Model):
    saida = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    entrada = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    data_fluxo = models.DateField()


# Create your models here.
