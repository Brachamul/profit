from django.db import models
from django.core.exceptions import ValidationError
import os



class Illustration(models.Model):
	name = models.CharField(max_length=255, unique=True)
	image = models.ImageField(upload_to="illustrations")

	def __str__(self):
		return self.name


class Item(models.Model):
	name = models.CharField(max_length=255, unique=True)
	description = models.TextField(max_length=1000)

	def __str__(self):
		return self.name


class Feature(models.Model):
	# A feature is what occupies a slot, it can be a man-made constuct or natural terrain.
	name = models.CharField(max_length=255, unique=True)
	description = models.TextField(max_length=1000, blank=True)
#	shape = models.CharField(max_length=255, blank=True, default='30,0,61,15,31,31,0,16') # Coordinates of the HTML map polygon
	slug = models.SlugField(max_length=255, unique=True) # Used to name image folder and as a css class for rendering
	min_price = models.PositiveSmallIntegerField(blank=True, null=True)
	base_illustration = models.ForeignKey(Illustration, default=1)
	def __str__(self):
		return self.name



### Upgrade Runs


class Upgrade(models.Model):
	# Features can typically have several upgrades
	feature = models.ForeignKey(Feature)
	name = models.CharField(max_length=255, unique=True)
	description = models.TextField(max_length=1000, blank=True)
	required_materials = models.ManyToManyField(Item, through='UpgradeRequiredMaterial')
	illustration = models.ForeignKey(Illustration, null=True)

	def __str__(self):
		return str(self.feature) + ' ' + str(self.name)

	def types_of_materials_needed(self):
		return ",\n".join([r.name for r in self.required_materials.all()])


class UpgradeRequiredMaterial(models.Model):
	upgrade = models.ForeignKey(Upgrade)
	item = models.ForeignKey(Item)
	quantity = models.PositiveSmallIntegerField(default=0, blank=True)

	def __str__(self):
		quantity_of_items = str(self.item) + ', ' + str(self.quantity)
		return quantity_of_items



### Development Runs


class DevelopmentProject(models.Model):
	# Development projects can be applied to features in order to improve them.
	was = models.ForeignKey(Feature, related_name='Project Source')
	becomes = models.ForeignKey(Feature, related_name='Project Result')
	required_materials = models.ManyToManyField(Item, through='DevelopmentProjectRequiredMaterial')
	illustration = models.ForeignKey(Illustration, null=True)
	required_amount_of_workers = models.PositiveSmallIntegerField(default=4)

	def development_project(self):
		return ("[%s] ⇒ [%s]" % (str(self.was), str(self.becomes)))

	def types_of_materials_needed(self):
		return ",\n".join([r.name for r in self.required_materials.all()])


class DevelopmentProjectRequiredMaterial(models.Model):
	development_project = models.ForeignKey(DevelopmentProject)
	item = models.ForeignKey(Item)
	quantity = models.PositiveSmallIntegerField(default=0, blank=True)

	def __str__(self):
		quantity_of_items = str(self.item) + ', ' + str(self.quantity)
		return quantity_of_items



### Production Runs


class Production(models.Model):
	# Production is an activity which outputs items
	feature = models.ManyToManyField(Feature)
	name = models.CharField(max_length=255, unique=True)
	description = models.TextField(max_length=1000, blank=True)
	output = models.ManyToManyField(Item, through='ProductionOutput')
	workers = models.PositiveSmallIntegerField(default=0, blank=True, null=True)
	illustration = models.ForeignKey(Illustration, null=True)

	def __str__(self):
		return self.name

	def production_output(self):
		return ",\n".join([output.name for output in self.output.all()])


class ProductionOutput(models.Model):
	production = models.ForeignKey(Production)
	item = models.ForeignKey(Item)
	quantity = models.PositiveSmallIntegerField(default=0, blank=True)

	def __str__(self):
		quantity_of_items = str(self.item) + ', ' + str(self.quantity)
		return quantity_of_items




def validate_material_quantity(value):
	if value % 10 != 0:
		raise ValidationError('Please input a multiple of 10.')