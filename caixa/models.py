from django.db import models
import datetime as dt
from django.utils import timezone

class ControleCaixa(models.Model):
    saida = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True,default=0)
    entrada = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True, default=0)
    data_fluxo = models.DateField(default=timezone.now)



# Create your models here.
