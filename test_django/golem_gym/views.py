from multiprocessing import context
from turtle import title
from django.shortcuts import redirect, render
from golem_gym.models import Plans
from golem_gym.forms import Formulario_plans
from golem_gym.models import Blog

def create_plan(request):
    
    if request.method == "POST":
       form = Formulario_plans(request.POST)
       if form.is_valid():
        Plans.objects.create(
            title = form.cleaned_data["title"],
            price = form.cleaned_data["price"],
            description = form.cleaned_data["description"]
        )
        return redirect(list_plans)
    
    elif request.method == "GET":
        form = Formulario_plans()
        context = {"form":form}    
    return render(request, "plans/training_plan.html", context=context)

def list_plans(request):
    plans = Plans.objects.all()
    context= {
        "plans":plans
    }
    return render(request, "plans/list_plans.html", context=context)   

def formulario(request):
    print(request.method)
    if request.method == "POST":
        print(request.POST)
    return render(request, "plans/formulario.html", context={})

def search_plans(request):
    search = request.GET["search"]
    plans = Plans.objects.filter(title__icontains=search)
    context = {"plans":plans} 
    return render(request, "plans/search_plans.html", context=context)   


def informacion(request):
    info_lautaro = Blog.objects.create(name = "Lautaro", age = 27, description= "Soy profesor de Educacion Fisica, instructor de musculacion y profesor de calistenia" )
    context= {
        "info_lautaro": info_lautaro
    }
    return render(request, "Info/info_lautaro.html", context=context)    