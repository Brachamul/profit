from django.db import models
from django.utils.encoding import smart_text
from django.core.exceptions import ValidationError

# Create your models here.



class Item(models.Model):
	name = models.CharField(max_length=255)

	def __str__(self):
		return self.name



class Building(models.Model):
	name = models.CharField(max_length=255)
	description = models.TextField(max_length=255)
	materials = models.ManyToManyField(Item, through='RequiredMaterial')
	low_tech = models.BooleanField()
#	illustration = models.ImageField(upload_to=)

	def __str__(self):
		return self.name



def validate_material_quantity(value):
	if value % 10 != 0:
		raise ValidationError('Please input a multiple of 10.')

class RequiredMaterial(models.Model):
	building = models.ForeignKey(Building)
	item = models.ForeignKey(Item)
	quantity = models.PositiveSmallIntegerField(default=0, validators=[validate_material_quantity])
