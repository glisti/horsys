from django.core.urlresolvers import reverse
from django.db import models
import time
from datetime import date, datetime, timedelta
from core.models import HorsysBaseModel
import time
from datetime import date, datetime, timedelta
from django.contrib.admin.widgets import AdminDateWidget
from django.contrib.auth.models import User


TIME_CHOICES = (
	('AM', 'AM'),
	('PM', 'PM'),
)

class Shift(HorsysBaseModel):
	time_of_day   = models.CharField(max_length=2,choices=TIME_CHOICES,default='AM')
	turn_out      = models.BooleanField(default=False)
	refill_water  = models.BooleanField(default=False)
	feed_horses   = models.BooleanField(default=False)
	close_haytrap = models.BooleanField(default=False)
	open_haytrap  = models.BooleanField(default=False)
	clean_stalls  = models.BooleanField(default=False)
	tidy_barn     = models.BooleanField(default=False)
	lights_off    = models.BooleanField(default=False)
	clock_in = models.DateTimeField()
	clock_out = models.DateTimeField()
	user = models.ForeignKey(User)

	def __unicode__(self):
		return self.feeder_name

	def is_today(self):
		return self.date >= date.today()

	def get_absolute_url(self):
		return reverse('shift_detail', kwargs={'pk': self.pk})

	def title(self):
		return self.date.isoformat()
	
	def total_hours(self):
		diff = self.clock_out - self.clock_in
		return round(float(diff.seconds)/float(3600),2)

