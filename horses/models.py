from django.core.urlresolvers import reverse
from django.db import models

FRONT_PASTURE = 'FRONT'
BACK_PASTURE  = 'BACK'
PONY_PASTURE  = 'PONY'
STALLS        = 'STALLS'
PLACEMENT_CHOICES = (
    (FRONT_PASTURE, 'Front Pasture'),
    (BACK_PASTURE, 'Back Pasture'),
    (PONY_PASTURE, 'Pony Pasture'),
    (STALLS, 'Stalls'),
)

class Horse(models.Model):
    name                    = models.CharField(max_length=100)
    # photo                   = models.ImageField([upload_to=None, height_field=None, width_field=None, max_length=100])
    description             = models.TextField()
    owner_name              = models.CharField(max_length=100)
    location                = models.CharField(max_length=6, choices=PLACEMENT_CHOICES,default=STALLS)
    feed                    = models.CharField(max_length=100)
    am_amount               = models.CharField(max_length=100)
    pm_amount               = models.CharField(max_length=100)
    beet_pulp               = models.CharField(max_length=30)
    rice_bran               = models.CharField(max_length=30)
    supplements             = models.CharField(max_length=100)
    hay                     = models.CharField(max_length=100)
    turnout                 = models.CharField(max_length=100)
    notes                   = models.TextField()
    blanketing_instructions = models.TextField()

    def __unicode__(self):
        return self.name

    def get_abosulte_url(self):
        return reverse('horses.views.horse_detail', kwargs={'pk': self.pk}) #args=[str(self.id)])

class MedicalRecord(models.Model):
    horse = models.ForeignKey('Horse')
    title = models.CharField(max_length=100)
    # form = models.FileField(upload_to='records')
