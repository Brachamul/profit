from django.contrib import admin
from django.forms.models import inlineformset_factory

# Register your models here.

from .models import Item, Feature, RequiredMaterial, DevelopmentProject


class ItemAdmin(admin.ModelAdmin):
	model = Item

admin.site.register(Item, ItemAdmin)



class FeatureAdmin(admin.ModelAdmin):
	model = Feature
#	DevelopmentProjectFormSet = inlineformset_factory(Feature,DevelopmentProject)

admin.site.register(Feature, FeatureAdmin)



class RequiredMaterialInline(admin.TabularInline):
	model = RequiredMaterial
	extra = 1

class DevelopmentProjectAdmin(admin.ModelAdmin):
	inlines = (RequiredMaterialInline,)
	list_display = ("development_project", "was", "becomes", "types_of_materials_needed")

admin.site.register(DevelopmentProject, DevelopmentProjectAdmin)