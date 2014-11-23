from django.contrib import admin

# Register your models here.

from .models import *
from .forms import *

class ResidentAdmin(admin.ModelAdmin):
    model = Resident
    list_display = ("town", "number", "job", "savings")

admin.site.register(Resident, ResidentAdmin)