from django.contrib import admin

# Register your models here.

from .models import Item, Feature, RequiredMaterial, DevelopmentProject
from .forms import DevelopmentProjectInlineForm



class ItemAdmin(admin.ModelAdmin):
	model = Item
	list_display = ("name", "pk", "description")

admin.site.register(Item, ItemAdmin)




class DevelopmentProjectWas(admin.TabularInline):
	# For each feature, display development projects that can lead to it
	model = DevelopmentProject
	fk_name = 'was'
	form = DevelopmentProjectInlineForm
	extra = 0

class DevelopmentProjectBecomes(admin.TabularInline):
	# For each feature, display development projects that can improve it
	model = DevelopmentProject
	fk_name = 'becomes'
	form = DevelopmentProjectInlineForm
	extra = 0

class FeatureAdmin(admin.ModelAdmin):
	model = Feature
	list_display = ("name", "description")
	inlines = [DevelopmentProjectBecomes, DevelopmentProjectWas, ]
	prepopulated_fields = {"slug": ("name",)}

admin.site.register(Feature, FeatureAdmin)



class RequiredMaterialInline(admin.TabularInline):
	model = RequiredMaterial
	extra = 1

class DevelopmentProjectAdmin(admin.ModelAdmin):
	inlines = (RequiredMaterialInline,)
	list_display = ("development_project", "was", "becomes", "types_of_materials_needed")

admin.site.register(DevelopmentProject, DevelopmentProjectAdmin)