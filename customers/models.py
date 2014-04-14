from django.db import models
from django.core.urlresolvers import reverse
from django.utils.encoding import smart_text

class ContactInfo(models.Model):
	address = models.CharField(max_length=100)
	City = models.CharField(max_length=100)
	State = models.CharField(max_length=2)
	zip_code = models.IntegerField()
	country = models.CharField(max_length=100)
	phone_num = models.IntegerField(max_length=10)
	email = models.CharField(max_length=100)
#

class Feeder(models.Model):
	feeder_name = models.CharField(max_length=100)
	contact_info = models.ManyToManyField(ContactInfo)
	shift = models.CharField(max_length=30)

	def __unicode__(self):
		return self.feeder_name
	
class Boarder(models.Model):
	boarder_name = models.CharField(max_length=100)
	contact_info = ContactInfo #models.ManyToManyField(ContactInfo)
	#checks_paid = models.
	#liab_waivers = models.	
	def __unicode__(self):
	     return self.boarder_name
	def get_abosulte_url(self):
         return reverse('boarders.views.boarders_detail', kwargs={'pk': self.pk})

class Owner(models.Model):
	owner_name = models.CharField(max_length=100)
	contact_info = models.ManyToManyField(ContactInfo)
	vet_pref = models.TextField()
	farrier_pref = models.TextField()

	
class Task(models.Model):
    boarder = models.ForeignKey('Boarder')	