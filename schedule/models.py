from django.db import models
from django.core.urlresolvers import reverse
from django.utils.encoding import smart_text
from django.utils import timezone
import datetime
from datetime import date

# Create your models here.

class Log(models.Model):
	desc = models.CharField(max_length=100)
	injuries = models.TextField()
	beh_changes = models.TextField()
	horse_name = models.CharField(max_length=100)
	tasks = models.TextField()
	feed_change = models.TextField()
	comments = models.TextField()
	date = models.DateField()
	auth = models.CharField(max_length=100)

	def is_today(self):
		return self.date >= date.today()

	def is_yesterday(self):
		t = date.today()
		n = abs(t - self.date)
		return n.days is 1

	def __unicode__(self):
		return self.desc
	def get_absolute_url(self):
		return reverse('logs.views.log_detail', args=[str(self.id)])


class ShiftAM(models.Model):
	feeder_name = models.CharField(max_length=100)
	date = models.DateField()
	turnout = models.BooleanField()
	close_haytrap = models.BooleanField()
	clean_stalls = models.BooleanField()
	tidy_barn = models.BooleanField()
	clean_area = models.BooleanField()

	def __unicode__(self):
		return self.feeder_name
	def is_today(self):
		return self.date >= date.today()
	def get_absolute_url(self):
		return reverse('shiftAM.views.shift_detail', args=[str(self.id)])
	def title(self):
		return self.feeder_name + "  " + self.date.isoformat()


class ShiftPM(models.Model):
	feeder_name = models.CharField(max_length=100)
	date = models.DateField()
	turnout = models.BooleanField()
	open_haytrap = models.BooleanField()
	tidy_barn = models.BooleanField()
	clean_area = models.BooleanField()
	lights_off = models.BooleanField()
	def __unicode__(self):
		return self.feeder_name
	def is_today(self):
		return self.date >= date.today()
	def get_absolute_url(self):
		return reverse('shiftPM.views.shift_detail', args=[str(self.id)])
	def title(self):
		return self.feeder_name + "  " + self.date.isoformat()