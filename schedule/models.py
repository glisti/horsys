from django.core.urlresolvers import reverse
from django.db import models

from core.models import HorsysBaseModel

TIME_CHOICES = (
	('AM', 'AM'),
	('PM', 'PM'),
)

class Shift(HorsysBaseModel):
	feeder_name   = models.CharField(max_length=100)
	time_of_day   = models.CharField(max_length=2,choices=TIME_CHOICES,default='AM')
	turn_out      = models.BooleanField(default=False)
	refill_water  = models.BooleanField(default=False)
	feed_horses   = models.BooleanField(default=False)
	close_haytrap = models.BooleanField(default=False)
	open_haytrap  = models.BooleanField(default=False)
	clean_stalls  = models.BooleanField(default=False)
	tidy_barn     = models.BooleanField(default=False)
	lights_off    = models.BooleanField(default=False)

	def get_absolute_url(self):
		return reverse('shift_detail', kwargs={'time': self.time_of_day,'pk': self.pk})
