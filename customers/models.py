from django.core.urlresolvers import reverse
from django.db import models

from core.models import HorsysBaseModel

# Create your models here.


class ContactInfo(models.Model):
	boarder_name = models.ForeignKey('Boarders', null = True)
	owner_name = models.ForeignKey('Owners', null = True)
	address   = models.CharField(max_length=100)
	City      = models.CharField(max_length=100)
	State     = models.CharField(max_length=2)
	zip_code  = models.IntegerField()
	country   = models.CharField(max_length=100)
	phone_num = models.IntegerField(max_length=10)
	email     = models.EmailField(max_length=75)
	def get_absolute_url(self):
		return reverse('boarder_detail', kwargs={'pk': self.pk})

	

class Owners(models.Model):
	owner = models.CharField(max_length=100)
	#contact_info = models.OneToOneField(ContactInfo)
	vet_pref = models.TextField()
	farrier_pref = models.TextField()

	def __unicode__(self): 	
		return self.owner 
	def get_abosulte_url(self): 
            return reverse('customers.views.owner_detail', kwargs={'pk': self.pk}) #args=[str(self.id)])
	

class Boarders(models.Model):
	boarder = models.CharField(max_length=100)
	#contact_info = models.OneToOneField(ContactInfo)
	#checks_paid = models.FileField(upload_to='customers/checks')
	#liab_waivers  = models.FileField(upload_to='customers/waivers')
	#boarder_agreements = models.FileField(upload_to='customers/agreements')
	def __unicode__(self): 
		return self.boarder

	def get_abosulte_url(self): 
            return reverse('customers.views.boarder_detail', kwargs={'pk': self.pk}) #args=[str(self.id)])
 
# ====================================================================
# Boarder Documents
# ====================================================================
class ChecksPaid(HorsysBaseModel):
    boarder_name    = models.ForeignKey('Boarders')
    title    = models.CharField(max_length=100)
    form     = models.FileField(upload_to='customers/checks')
    # added by

    def get_absolute_url(self):
        return reverse('boarder_detail', kwargs={'pk': self.pk})

class LiabilityWaiver(HorsysBaseModel):
    boarder_name    = models.ForeignKey('Boarders')
    title    = models.CharField(max_length=100)
    form     = models.FileField(upload_to='customers/waivers')
    # added by

    def get_absolute_url(self):
        return reverse('boarder_detail', kwargs={'pk': self.pk})

class BoarderAgreement(HorsysBaseModel):
    boarder_name    = models.ForeignKey('Boarders')
    title    = models.CharField(max_length=100)
    form     = models.FileField(upload_to='customers/agreements')
    # added by

    def get_absolute_url(self):
        return reverse('boarder_detail', kwargs={'pk': self.pk})

