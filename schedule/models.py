from django.core.urlresolvers import reverse
from django.db import models

from core.models import HorsysBaseModel

class Shift(HorsysBaseModel):
	feeder_name   = models.CharField(max_length=100)
	turn_out       = models.BooleanField()
	refill_water  = models.BooleanField()
	feed_horses   = models.BooleanField()
	close_haytrap = models.BooleanField()
	open_haytrap  = models.BooleanField()
	clean_stalls  = models.BooleanField()
	tidy_barn     = models.BooleanField()
	lights_off    = models.BooleanField()

	def __unicode__(self):
		return self.feeder_name

	def is_today(self):
		return self.date >= date.today()

	def get_absolute_url(self):
		return reverse('shift_detail', kwargs={'pk': self.pk})

	def title(self):
		return self.feeder_name + "  " + self.date.isoformat()
