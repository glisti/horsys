from django.core.urlresolvers import reverse
from django.db import models

# Create your models here.


class ContactInfo(models.Model):
	address = models.CharField(max_length=100)
	City = models.CharField(max_length=100)
	State = models.CharField(max_length=2)
	zip_code = models.IntegerField()
	country = models.CharField(max_length=100)
	phone_num = models.IntegerField(max_length=10)
	email = models.EmailField(max_length=75)

	

class Owners(models.Model):
	owner = models.CharField(max_length=100)
	contact_info = models.OneToOneField(ContactInfo)
	vet_pref = models.TextField()
	farrier_pref = models.TextField()

	def __unicode__(self): 	
		return self.owner 
	def get_abosulte_url(self): 
            return reverse('customers.views.owner_detail', kwargs={'pk': self.pk}) #args=[str(self.id)])
	

class Boarders(models.Model):
	boarder = models.CharField(max_length=100)
	checks_paid = models.CharField(max_length=100)
	contact_info = models.OneToOneField(ContactInfo)
	liab_waivers = models.CharField(max_length=100)

	def __unicode__(self): 
		return self.boarder

	def get_abosulte_url(self): 
            return reverse('customers.views.boarder_detail', kwargs={'pk': self.pk}) #args=[str(self.id)])
 
