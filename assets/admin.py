from django.contrib import admin

# Register your models here.

from .models import *
from .forms import *



class IllustrationAdmin(admin.ModelAdmin):
	model = Illustration

admin.site.register(Illustration, IllustrationAdmin)



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
	list_display = ("name", "id", "description")
	inlines = [DevelopmentProjectBecomes, DevelopmentProjectWas, ]
	prepopulated_fields = {"slug": ("name",)}

admin.site.register(Feature, FeatureAdmin)


class DevelopmentProjectRequiredMaterialInline(admin.TabularInline):
	model = DevelopmentProjectRequiredMaterial
	extra = 1

class DevelopmentProjectAdmin(admin.ModelAdmin):
	inlines = (DevelopmentProjectRequiredMaterialInline,)
	list_display = ("id", "development_project", "was", "becomes", "types_of_materials_needed")

admin.site.register(DevelopmentProject, DevelopmentProjectAdmin)


class UpgradeRequiredMaterialInline(admin.TabularInline):
	model = UpgradeRequiredMaterial
	extra = 1

class UpgradeAdmin(admin.ModelAdmin):
	inlines = (UpgradeRequiredMaterialInline,)
	list_display = ("name", "types_of_materials_needed")

admin.site.register(Upgrade, UpgradeAdmin)