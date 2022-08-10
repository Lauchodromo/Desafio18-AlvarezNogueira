from tabnanny import verbose
from django.db import models

class Plans(models.Model):
    title = models.CharField(max_length=40)
    description = models.CharField(max_length=200) 
    price = models.FloatField(null=True, blank=True)
    period = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Plan"
        verbose_name_plural = "Plans"

class Blog(models.Model):
    name = models.CharField(max_length=40)
    age = models.FloatField(null=True, blank=True)
    description = models.CharField(max_length=1000)

