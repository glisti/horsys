from django.core.urlresolvers import reverse
from django.db import models

import os

from core.models import HorsysBaseModel

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

def photo_path(instance, file):
    ext = file.split('.')[-1]
    filename = "%s.%s" % (instance.name)
    return os.path.join('horses/photos',filename)

class Horse(HorsysBaseModel):
    name                    = models.CharField(max_length=25, unique=True)
    photo                   = models.ImageField(upload_to='horses/photos', blank=True)
    description             = models.TextField()
    owner_name              = models.CharField(max_length=25)
    location                = models.CharField(max_length=6, choices=PLACEMENT_CHOICES,default=STALLS)
    feed                    = models.CharField(max_length=35, blank=True)
    am_amount               = models.CharField(max_length=35, blank=True)
    pm_amount               = models.CharField(max_length=35, blank=True)
    beet_pulp               = models.CharField(max_length=35, blank=True)
    rice_bran               = models.CharField(max_length=35, blank=True)
    supplements             = models.CharField(max_length=35, blank=True)
    hay                     = models.CharField(max_length=35, blank=True)
    turnout                 = models.CharField(max_length=35, blank=True)
    blanketing_instructions = models.TextField(blank=True)

    def get_absolute_url(self):
        return reverse('horse_detail', kwargs={'pk': self.pk})

    def __unicode__(self):
        return self.name


class MedicalRecord(HorsysBaseModel):
    horse    = models.ForeignKey('Horse')
    title    = models.CharField(max_length=100)
    form     = models.FileField(upload_to='horses/records')
    # added by

    def get_absolute_url(self):
        return reverse('medicalrecord_detail', kwargs={'pk': self.pk})


class Task(HorsysBaseModel):
    horse     = models.ForeignKey('Horse')
    task      = models.TextField()
    program   = models.CharField(max_length=100)
    completed = models.BooleanField(default=False)
    # appointmenttime?
    # added by

    def get_absolute_url(self):
        return reverse('task_detail', kwargs={'pk': self.pk})


class Log(HorsysBaseModel):
    horse            = models.ForeignKey('Horse')
    injuries         = models.TextField(max_length=100,blank=True)
    behavior_changes = models.TextField(max_length=100,blank=True)
    feed_changes     = models.TextField(max_length=100,blank=True)
    comments         = models.TextField(max_length=100,blank=True)
    # added by