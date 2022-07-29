from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render


def familia(request):
    context = {
        "lista": ["Debora", "Nogueira", "50"]
     }
    return render(request, "familia.html", context=context)    