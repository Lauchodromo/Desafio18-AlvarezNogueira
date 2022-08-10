
from turtle import title
from django.urls import path
from golem_gym.views import create_plan, list_plans, formulario, search_plans, informacion




urlpatterns=[
    path("create-plan/", create_plan, name="create_plan"),
    path("list-plans/", list_plans, name="list_plans"),
    path("formulario/", formulario, name="formulario" ),
    path("search-plans/", search_plans, name="search_plans"),
    path("informacion/", informacion, name="informacion")
]