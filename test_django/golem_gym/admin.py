from django.contrib import admin
from golem_gym.models import Plans

@admin.register(Plans)
class Plans_admin(admin.ModelAdmin):
    list_display = ["title", "price", "description"]
