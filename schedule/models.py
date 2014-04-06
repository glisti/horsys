from django.db import models
from django.core.urlresolvers import reverse
from django.utils.encoding import smart_text
from django.utils import timezone
import datetime

# Create your models here.

class Log(models.Model):
	date = models.DateTimeField('date published')
	desc = models.CharField(max_length=100)
	details = models.CharField(max_length=1000)
	auth = models.CharField(max_length=100)
	horse = models.CharField(max_length=100)

	def is_today(self):
		return self.date >= timezone.now() - datetime.timedelta(days=1)

	def is_yesterday(self):
		return ( (self.date >= timezone.now() - datetime.timedelta(days=2)) and not (self.date >= timezone.now() - datetime.timedelta(days=1)))

	def __unicode__(self):
		return self.desc
	def get_absolute_url(self):
		return reverse('logs.views.log_detail', args=[str(self.id)])