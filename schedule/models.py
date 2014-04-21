from django.core.urlresolvers import reverse
from django.db import models

from core.models import HorsysBaseModel
import time
from datetime import date, datetime, timedelta
from django.contrib.admin.widgets import AdminDateWidget

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

	def __unicode__(self):
		return self.feeder_name

	def is_today(self):
		return self.date >= date.today()

	def get_absolute_url(self):
		return reverse('shift_detail', kwargs={'pk': self.pk})

	def title(self):
		return self.date.isoformat()

class Clock(models.Model):
	AM_SHIFT = 'AM'
	PM_SHIFT = 'PM'
	SHIFT_CHOICES = (
		(AM_SHIFT, 'Morning Shift'),
		(PM_SHIFT, 'Evening Shift'),

		)
	feeder_name = models.CharField(max_length=100)
	shift_type = models.CharField(max_length=2,
								  choices=SHIFT_CHOICES,
								  default=AM_SHIFT)
	date = models.DateField()
	log_in = models.TimeField()
	log_out = models.TimeField()
	def __unicode__(self):
		return self.feeder_name
	
	def is_today(self):
		return self.date >= date.today()	
	def get_absolute_url(self):
		return reverse('clock_detail', kwargs={'pk': self.pk})	

	def title(self):
		return self.date.toordinal()	
