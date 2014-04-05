from django.db import models
from django.core.urlresolvers import reverse
from django.utils.encoding import smart_text
from django.utils import timezone
import datetime

# Create your models here.

class Log(models.Model):
	date = models.CharField(max_length=100)
	desc = models.CharField(max_length=100)
	details = models.CharField(max_length=1000)
	auth = models.CharField(max_length=100)

	def __unicode__(self):
		return self.desc
	def get_absolute_url(self):
		return reverse('logs.views.log_detail', args=[str(self.id)])