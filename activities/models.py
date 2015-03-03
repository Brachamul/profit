from django.db import models

from assets.models import *
from towns.models import *

class Run(models.Model):
	
	town_slot = models.ForeignKey(TownSlot)
	date_created = models.DateTimeField(auto_now_add=True)
	completed = models.BooleanField(default=False)
	date_completed = models.DateTimeField(blank=True, null=True)

	# A run can be either one of the following things :
	is_development = models.ForeignKey(DevelopmentProject, blank=True, null=True)
	is_upgrade = models.ForeignKey(Upgrade, blank=True, null=True)
	is_production = models.ForeignKey(Production, blank=True, null=True)
#	is_service = models.ForeignKey(Service, blank=True, null=True)
#	is_boost = models.ForeignKey(Boost, blank=True, null=True)

#	pay = models.PositiveSmallIntegerField()
	is_recurrent = models.BooleanField(default=False) # Does it automatically repeat itself ?
	remaining_cycles = models.PositiveSmallIntegerField(default=1) # Does it have a defined runtime ?