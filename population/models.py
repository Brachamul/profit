from django.db import models

from towns.models import *
from activities.models import *


class Resident(models.Model):
	town = models.ForeignKey(Town)
	number = models.PositiveSmallIntegerField()
	job = models.ForeignKey(Run, blank=True, null=True)
	savings = models.PositiveSmallIntegerField()

	def __str__(self):
		return self.number

@receiver(post_save, sender=Town) # When a Town is created, populate it with slots from the map layout.
def populate_town(sender, created, **kwargs):
	if created :
		town = kwargs.get('instance')
		number = 1
		for i in range(320) : # 5 per slot
			new_resident = Resident(town=town, savings=0, number=number)
			new_resident.save()
			number += 1