from django.db import models

from assets.models import Feature

# Create your models here.


def map_storage_folder(map_layout_name):
		return 'maps/%s' % (map_layout_name)

class MapLayout(models.Model):
	name = models.CharField(max_length=255)
	description = models.TextField(max_length=255)
	image = models.ImageField(upload_to='maps')

	def __str__(self):
		return self.name



class Slot(models.Model):
	# A feature is what occupies a slot, it can be a man-made constuct or natural terrain.
	map_layout = models.ForeignKey(MapLayout)
	number = models.PositiveSmallIntegerField()
	latitude = models.PositiveSmallIntegerField()
	longitude = models.PositiveSmallIntegerField()
	starting_feature = models.ForeignKey(Feature)

	def __str__(self):
		return ("Map %s, slot %s : %s" % (str(self.map_layout), str(self.number), str(self.starting_feature)))
