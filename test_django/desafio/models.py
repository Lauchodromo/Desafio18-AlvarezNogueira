from django.db import models

class Desafio(models.Model):
    name = models.CharField(max_length=40, null=True, blank=True)
    age = models.FloatField(null=True, blank=True)
    who_is = models.CharField(max_length=40, null=True, blank=True)
    birthday = models.DateField(null=True, blank=True)


