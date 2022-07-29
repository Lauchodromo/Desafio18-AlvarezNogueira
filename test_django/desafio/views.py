from django.shortcuts import render
from desafio.models import Desafio

def mi_familia(request):
    Famliar_1 = Desafio.objects.create(name = "Thiago", age = 19, birthday= "2002-9-3" )
    context= {
        "mi_familia": mi_familia
    }
    return render(request, "mi_familia.html", context=context)

def list_familia(request):
    familiares = Desafio.objects.all()
    context= {
        "familiares":familiares
    }
    return render(request, "list_familia.html", context=context)    