from django.contrib import admin
from .models import Victims

@admin.register(Victims)
class VictimsAdmin (admin.ModelAdmin):
    list_display = ['id', 'username', 'password', 'created_at']
    class Meta:
        model = Victims