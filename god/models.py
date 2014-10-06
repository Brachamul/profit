from django.db import models
from assets.models import Feature
import os

# Create your models here.



class MapLayout(models.Model):
	name = models.CharField(max_length=255, unique=True)
	description = models.TextField(max_length=255)
	slug = models.SlugField(max_length=255, unique=True)
	

	def upload_details(instance, filename):
		path = "maps/" # Upload location
		format = instance.slug + '.png' # Filename
		return os.path.join(path, format)

	image = models.ImageField(upload_to=upload_details)

	def __str__(self):
		return self.name



class Slot(models.Model):
	map_layout = models.ForeignKey(MapLayout)
	number = models.PositiveSmallIntegerField(null=True, blank=True) # Let it be null to make input easier
	longitude = models.PositiveSmallIntegerField()
	latitude = models.PositiveSmallIntegerField()
	starting_feature = models.ForeignKey(Feature, default=1)

	def __str__(self):
		return ("%s" % str(self.number))
