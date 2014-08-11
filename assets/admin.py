from django.contrib import admin

# Register your models here.

from .models import Item, Building, RequiredMaterial


class ItemAdmin(admin.ModelAdmin):
	model = Item

admin.site.register(Item, ItemAdmin)


#	class BuildingAdmin(admin.ModelAdmin):
#		model = Building

class RequiredMaterialInline(admin.TabularInline):
	model = RequiredMaterial
	extra = 1

class BuildingAdmin(admin.ModelAdmin):
	inlines = (RequiredMaterialInline,)

admin.site.register(Building, BuildingAdmin)