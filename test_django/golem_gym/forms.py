from django import forms

class Formulario_plans(forms.Form):
    title = forms.CharField(max_length=40)
    description = forms.CharField(max_length=200)
    price = forms.FloatField()