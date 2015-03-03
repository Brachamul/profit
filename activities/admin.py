from django.contrib import admin

# Register your models here.

from .models import *

class RunAdmin(admin.ModelAdmin):
    model = Run

admin.site.register(Run, RunAdmin)