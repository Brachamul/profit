from django.contrib import admin

# Register your models here.

from .models import Item, Feature, RequiredMaterial, DevelopmentProject
from .forms import DevelopmentProjectFormSet


class ItemAdmin(admin.ModelAdmin):
	model = Item
	list_display = ("name", "description")

admin.site.register(Item, ItemAdmin)



class DevelopmentProjectBecomes(admin.StackedInline):
	# For each feature, display development projects that can lead to it
    model = DevelopmentProject
    fk_name = 'becomes'
    formset = DevelopmentProjectFormSet
    extra = 0

class FeatureAdmin(admin.ModelAdmin):
	model = Feature
	list_display = ("name", "description")
	inlines = [DevelopmentProjectBecomes, ]

admin.site.register(Feature, FeatureAdmin)



class RequiredMaterialInline(admin.TabularInline):
	model = RequiredMaterial
	extra = 1

class DevelopmentProjectAdmin(admin.ModelAdmin):
	inlines = (RequiredMaterialInline,)
	list_display = ("development_project", "was", "becomes", "types_of_materials_needed")

admin.site.register(DevelopmentProject, DevelopmentProjectAdmin)