from django.contrib import admin

# Register your models here.

from .models import Town, Player, TownSlot, StoredItems


class PlayerInline(admin.TabularInline):
	model = Player
	extra = 0

class TownSlotInline(admin.TabularInline):
	model = TownSlot
	fields = ("feature", "owner")
	readonly_fields = fields
	extra = 0

class TownAdmin(admin.ModelAdmin):
	model = Town
	inlines = (PlayerInline, TownSlotInline, )
	list_display = ("name", "pk", "map_layout")
	prepopulated_fields = {"slug": ("name",)}

admin.site.register(Town, TownAdmin)



class PlayerAdmin(admin.ModelAdmin):
	model = Player
	list_display = ("user", "pk", "cash", "joined", "left")

admin.site.register(Player, PlayerAdmin)