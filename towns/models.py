from django.db import models

from maps.models import Slot, MapLayout
from assets.models import Feature, Item
from django.contrib.auth.models import User

from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.



class Town(models.Model):
	name = models.CharField(max_length=255, unique=True)
	slug = models.SlugField(max_length=255, unique=True)
	map_layout = models.ForeignKey(MapLayout)
	founded = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.name


@receiver(post_save, sender=Town)
def slotify_town(sender, **kwargs):
	town = kwargs.get('instance')
	map_layout = town.map_layout
	slot_map = Slot.objects.filter(map_layout=map_layout)
	for master_slot in slot_map :
		new_slot = TownSlot(
			town = town,
			slot = master_slot,
			feature = master_slot.starting_feature
			)
		new_slot.save()


class Player(models.Model):
	town = models.ForeignKey(Town)
	user = models.ForeignKey(User)
	cash = models.PositiveIntegerField(default=10000)
	joined = models.DateTimeField(auto_now_add=True) # States when the user joined a town
	left = models.DateTimeField(blank=True, null=True)

	def __str__(self):
		return self.user.username



class TownSlot(models.Model):
	town = models.ForeignKey(Town)
	slot = models.ForeignKey(Slot) # Finds the coordinates and starting feature of this Slot
	owner = models.ForeignKey(Player, null=True, default=None)
	feature = models.ForeignKey(Feature)
	stored_items = models.ManyToManyField(Item, through='StoredItems')

	def __str__(self):
		return 'Slot #%d | %d - %d' % (self.slot.number, self.slot.latitude, self.slot.longitude)

class StoredItems(models.Model):
	town_slot = models.ForeignKey(TownSlot)
	item = models.ForeignKey(Item)
	quantity = models.PositiveSmallIntegerField()

	def __str__(self):
		quantity_of_items = str(self.item) + ', ' + str(self.quantity)
		return quantity_of_items