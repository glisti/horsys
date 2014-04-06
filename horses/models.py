from django.core.urlresolvers import reverse
from django.utils.encoding import smart_text
from django.db import models

colors = [
    'bay','gray','white','chestnut','black','dun','buckskin','palomino',
    'perlino','cremello','roan','champagne'
]

class Horse(models.Model):
    name     = models.CharField(max_length=100)
    nickname = models.CharField(max_length=100)
    age      = models.IntegerField()
    weight   = models.DecimalField(max_digits=6,decimal_places=2)
    feet     = models.IntegerField()
    inches   = models.IntegerField()
    color    = models.CharField(max_length=100)
    breed    = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name

    def height(self):
        return smart_text('%s ft, %s in') % (self.feet,self.inches)

    def get_abosulte_url(self):
        return reverse('horses.views.horse_detail', args=[str(self.id)])

class Placement(models.Model):
    front_pasture = models.TextField()
    back_pasture = models.TextField()
    pony_pasture = models.TextField()
    stalls = models.TextField()

class Feedings(models.Model):
	FRONT_PASTURE = 'FRONT'
	BACK_PASTURE = 'BACK'
	PONY_PASTURE = 'PONY'
	STALLS = 'STALLS'
	PLACEMENT_CHOICES= (
		(FRONT_PASTURE, 'Front Pasture'),
		(BACK_PASTURE, 'Back Pasture'),
		(PONY_PASTURE, 'Pony Pasture'),
		(STALLS, 'Stalls'),
	)
	horse_name = models.CharField(max_length=100)
	location = models.CharField(max_length=6, choices=PLACEMENT_CHOICES, default=STALLS)
	feed = models.CharField(max_length=100)
	f_am = models.CharField(max_length=100)
	f_pm = models.CharField(max_length=100)
	beet_pulp = models.CharField(max_length=30)
	rice_bran = models.CharField(max_length=30)
	supplements = models.CharField(max_length=100)
	hay = models.CharField(max_length=100)
	turnout = models.CharField(max_length=100)
	owner_name = models.CharField(max_length=100)
	notes = models.TextField()

class Blanketing(models.Model):
	horse_name = models.CharField(max_length=100)
	instructions = models.TextField()

