
from django.contrib import admin
from django.urls import path, include
from test_django.views import familia
from desafio.views import mi_familia, list_familia
from golem_gym.views import create_plan

urlpatterns = [
    path('admin/', admin.site.urls),
    path("familia/", familia, name="familia"),
    path("mi_familia/", mi_familia, name="mi_familia"),
    path("list_familia/", list_familia, name="list_familia"),
    path("golem_gym/", include("golem_gym.urls"))
]
