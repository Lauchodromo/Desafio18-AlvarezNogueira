
from django.contrib import admin
from django.urls import path
from test_django.views import familia
from desafio.views import mi_familia, list_familia
urlpatterns = [
    path('admin/', admin.site.urls),
    path("familia/", familia, name="familia"),
    path("mi_familia/", mi_familia, name="mi_familia"),
    path("list_familia/", list_familia, name="list_familia")

]
