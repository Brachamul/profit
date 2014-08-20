from django.contrib import admin

# Register your models here.

from .models import MapLayout, Slot



class SlotInline(admin.TabularInline):
	model = Slot
	extra = 0

class MapLayoutAdmin(admin.ModelAdmin):
	model = MapLayout
	inlines = (SlotInline,)
	list_display = ("name", "description")

admin.site.register(MapLayout, MapLayoutAdmin)



class SlotAdmin(admin.ModelAdmin):
	model = Slot
	list_display = ("map_layout", "number", "latitude", "longitude", "starting_feature")

admin.site.register(Slot, SlotAdmin)