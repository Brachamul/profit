from django.db import models
from django.core.exceptions import ValidationError
import os

# Create your models here.



class Item(models.Model):
	name = models.CharField(max_length=255)
	description = models.TextField(max_length=255)
#	illustration = models.ImageField(upload_to=)

	def __str__(self):
		return self.name



class Feature(models.Model):
	# A feature is what occupies a slot, it can be a man-made constuct or natural terrain.
	name = models.CharField(max_length=255)
	description = models.TextField(max_length=255, blank=True)
	shape = models.CharField(max_length=255, blank=True, default='30,0,61,15,31,31,0,16') # Coordinates of the HTML map polygon
	slug = models.SlugField() # Used to name image folder and as a css class for rendering

	def upload_details(instance, filename):
		path = "features/" # Upload location
		format = instance.slug + '.png' # Filename
		return os.path.join(path, format)

	illustration = models.ImageField(upload_to=upload_details, blank=True)

	def __str__(self):
		return self.name



class DevelopmentProject(models.Model):
	# Development projects can be applied to features in order to improve them.
	was = models.ForeignKey(Feature, related_name='Project Source')
	becomes = models.ForeignKey(Feature, related_name='Project Result')
	required_materials = models.ManyToManyField(Item, through='RequiredMaterial')
#	illustration = models.ImageField(upload_to=)

	def development_project(self):
		return ("[%s] ⇒ [%s]" % (str(self.was), str(self.becomes)))

	def types_of_materials_needed(self):
		return ",\n".join([r.name for r in self.materials_needed.all()])



def validate_material_quantity(value):
	if value % 10 != 0:
		raise ValidationError('Please input a multiple of 10.')

class RequiredMaterial(models.Model):
	development_project = models.ForeignKey(DevelopmentProject)
	item = models.ForeignKey(Item)
	quantity = models.PositiveSmallIntegerField(default=0, validators=[validate_material_quantity], blank=True)

	def __str__(self):
		quantity_of_items = str(self.item) + ', ' + str(self.quantity)
		return quantity_of_items

