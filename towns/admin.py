from django.contrib import admin

# Register your models here.

from .models import *


class PlayerInline(admin.TabularInline):
	model = Player
	extra = 0

class TownSlotInline(admin.TabularInline):
	model = TownSlot
	fields = ("feature", "illustration", "owner", "on_sale")
	readonly_fields = fields
	extra = 0

class TownAdmin(admin.ModelAdmin):
	model = Town
	inlines = (PlayerInline, TownSlotInline, )
	list_display = ("name", "phase", "pk", "map_layout")
	prepopulated_fields = {"slug": ("name",)}

admin.site.register(Town, TownAdmin)



class PlayerAdmin(admin.ModelAdmin):
	model = Player
	list_display = ("user", "pk", "cash", "joined", "left")

admin.site.register(Player, PlayerAdmin)



class TownSlotAdmin(admin.ModelAdmin):
	model = TownSlot
	list_display = ("slot", "feature", "owner", "town", "illustration")

admin.site.register(TownSlot, TownSlotAdmin)



class BidAdmin(admin.ModelAdmin):
	model = Bid
	list_display = ("amount", "player", "town_slot")

admin.site.register(Bid, BidAdmin)